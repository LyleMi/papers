Designing New Operating Primitives to Improve Fuzzing Performance

Wen Xu

## Abstract

shorten the execution time of each itera- tion

three new operating primitives specialized for fuzzing that solve these performance bottlenecks and achieve scalable performance on multi-core machines

speed up AFL and LibFuzzer by 6.1 to 28.9× and 1.1 to 735.7×

*scalability*

## Introduction

ClusterFuzz

OSSFuzz

commodity OSes with manycore architectures that are readily available today

fork() is designed to duplicate any running process. In the context of fuzzing, a large portion of operations in fork() is repeated but has the same effects, as the target process never changes.

propose 

1) snapshot(), a new system call which clones a new instance of the target application in an efficient and scalable manner; 

2) dual file system service, which makes fuzzers operate test cases on a memory file system (e.g., tmpfs) for performance and scalability and meanwhile ensures capacity and durability by a disk file system (e.g., ext4); 

3) shared in-memory test case log, which helps fuzzers share test case execution information in a scalable and collaborative way.

 the following contributions:

We identify and analyze three prominent performance bottlenecks that stem in large-scale fuzzing and they are caused by the intensive use of existing operating primitives that are only better for the general purpose use

We design and implement three new fuzzing specific operating primitives that can improve the performance and scalability for the state-of-the-art fuzzers in a multi-core machine

We apply and evaluate our proposed operating primitives to AFL and LibFuzzer. By leveraging our proposed primitives, AFL has at most 7.7×, 25.9×, and 28.9× improvement on the number of executions per second on 30, 60, and 120 cores, respectively. Meanwhile, LibFuzzer can speed up by at most 170.5×, 134.9×, and 735.7× on 30, 60, and 120 cores respectively

## BACKGROUND AND MOTIVATION

### 2.3 Perils to Scalable Fuzzing

#### Cloning a target application

there are two problems with the fork() system call. First, an OS repeatedly performs redundant operations in fork() that are neither used nor necessary for executing a target application during the fuzzing loop. Second, concurrent spawning of processes by using the fork() system call is not scalable because of various contentions (e.g., spinlocks) and standard requirements (e.g., PID should be assigned in an incremental order in POSIX). These operations are required for a general-purpose fork() in an OS, but significantly deter the scalability of fuzzing. For example, fork() needs to update the reverse mapping of a physical page for swapping under memory contention, which is a well-known scalability bottleneck in the current Linux kernel [8, 9, 11]. Moreover, fork() stresses the global memory allocator for allocating various metadata required for a new task, needs to set up security and auditing information, and has to add the task to the scheduler queue, which are all known to be non-scalable with increasing core count. Hence, none of the above operations are necessary and important for the purpose of fuzzing.

#### Creating a mutated test case

Typical file system operations that fuzzers rely on are, namely, open/creat (for generating the mutated test case), write (for flushing interesting test cases), and read (for loading test cases) of small files in each fuzzing loop, importantly in parallel. Two benchmarks in FxMark [32] can be used to explain in detail the scalability of the fuzzer: MWCL (i.e., creating a file in a private directory) and DWOL (i.e., writing a small file in a private directory). More specifically, the process of creating and writing small files heavily modifies the file system metadata (e.g., allocating inode for file creating and disk blocks for file writing), which is a critical section in most file system implementations, and not scalable

#### Syncing test cases each other

Scanning directories at the syncing phase is not scalable for the following reasons: First, the number of direc- tory enumeration operations to discover new, unsynced test cases increases non-linearly with more fuzzers, which results in a longer syncing phase. For instance, each fuzzer will take O(f ×t),where f isthenumberoffuzzersandt isthenumberof test cases in a test case directory. Second, directory enumeration severely interferes with creating a new test case because a direc- tory write operation (i.e., creating a file) and a read operation (i.e., enumerating files) cannot be performed concurrently

## 3. OPERATING PRIMITIVES

### 3.1 Snapshot System Call

```c
int snapshot(unsigned long cmd, unsigned long callback, struct iovec *shared_addr);
```

cmd is either BEG_SNAPSHOT for snapshotting or END_SNAPSHOT for reverting. 

It even has better performance than pthread_create() because it does not need to allocate and free thread stack, which is required for pthread_create(). The unnecessary operations in fork() and pthread_create() eventually incur costly TLB shoot- downs, scheduler invocations, memory allocations, auditing, and security related modifications 

#### 3.1.1 Before Fuzzing: Process Snapshotting


• Virtual Memory Area (VMA). snapshot() iterates the vir- tual memory areas (i.e., vmas) of the process and temporarily stores the start and end address of every vma.
• Page. snapshot() maintains a set of pages that belong to a writable vma because it is possible that the target application may modify these writable pages, which the kernel should revert to the original state when the application terminates. To track these writable pages and maintain their original memory status, we use the copy-on-write (CoW) technique. We change the permission of writable pages to read-only by updating their corresponding page table entries (PTE) and flushing TLB to maintain the consistency. Thus, any write on these pages incurs a page fault, which the page-fault handler captures and handles. Our approach includes an optimization: We do not change the permission of mapped writable virtual address for which the kernel is yet to allocate a physical page because memory access on those pages will always incur a page fault.
• brk. A process’s brk defines the end of its data segment, which indicates the valid range of its heap region in Linux. Thus it influences the results of heap allocations during the execution of the process. snapshot() saves the brk value of the current process.
• File descriptor. At the end of a snapshotted process, the kernel closes file descriptors that are opened after snapshot but revert the status of file descriptors that were already opened before snapshot. snapshot() saves the status of open file descriptors by checking the file descriptor table and bitmap

#### 3.1.2 During Fuzzing: Demanding Page Copy

#### 3.1.3 After Fuzzing: Snapshot Recovering

• Recovering copied pages. snapshot() recovers the pages that have a modified copy of the original one; it also deallocates the allocated physical memory, reverts corresponding PTE, and flushes the corresponding TLB entries.
• Adjusting memory layout. snapshot() iterates the VMAs of the target process again and unmaps all of the newly mapped virtual memory areas.
• Recovering brk. The brk value of a process affects the heap allocations and it is restored to the saved brk value.
• Closing opened file descriptors. By comparing the current file descriptor bitmap with the one saved before the past fuzzing run, snapshot() determines the opened file descriptors and closes them.

### 3.2 Dual File System Service

## 优点

- 找的点很合适
- 功底很深

# Related Work

# Method

# Evaluation

# Limitation

# Reference
