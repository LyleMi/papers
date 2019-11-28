# 1. Introduction

自从1990年以来，Fuzzing。

用于渗透测试。

# 2. Systemization, Taxonomy And Test Programs

## 2.1 Fuzzing & Fuzz Test

*Definition 2.1 Fuzzing* 
*Definition 2.2 Fuzz Tesing* 
*Definition 2.3 Fuzzer* 
*Definition 2.4 Fuzz Campaign* 
*Definition 2.5 Bug Oracle* 判断一个输入是否触发了bug 
*Definition 2.6 Fuzz Configuration* 

## 2.2 Paper Selection Criteria

主要是从4个主要的安全期刊和3个主要的软工期刊选

- ACM CCS
- IEEE S&P
- NDSS
- USENIX Security

- ACM FSE
- ACM ASE
- ACM ICSE

## 2.3 Fuzz Testing Algorithm

- Preprocess
- Schedule
- InputGen
- InputEval
- ConfUpdate
- Continue

## 2.4 Taxonomy of Fuzzers

### 2.4.1 Black-box Fuzzer

又被叫做IO-Driven / Data-Driven测试。
大部分的传统测试都是在这块。

### 2.4.2 White-box Fuzzer

DSE（Dynamice Symbolic Execution）由Godefroid在2007年提出。
污点分析。

### 2.4.3 Grey-box Fuzzer

不用对程序获得完整的信息。
做轻量级的静态分析。

# 3. Preprocess

## 3.1 Instrumentation

动态程序

- DynInst
- DynamoRIO
- Pin
- Valgrind
- QEMU

### 3.1.1 Execution Feedback

### 3.1.2 In-Memory Fuzzing

内存级别的Fuzz
主要是在Fuzz大程序的时候
做一个snapshot
再测试的时候就载入 去掉不必要的操作

### 3.1.3 Thread Scheduling

## 3.2 Seed Selection

语料期望用的minimal size和大小 完成max的效果

## 3.3 Seed Trimming

## 3.4 Preparing a Driver Application

不能直接fuzz的时候 考虑用其他方式fuzz

# 4. Scheduling

策略决定下一个case跑什么

## 4.1 The Fuzz Configuration Scheduling (FCS) Problem

## 4.2 Black-box FCS Algorithms

考虑 success rate (#bugs / #runs)

## 4.3 Grey-box FCS Algorithms

# 5. INPUT GENERATION

## 5.1 Model-Based (Generation-based) Fuzzers

### 5.1.1 Predefined Model

### 5.1.2 Inference Model

## 5.2 Model-less (Mutation-based) Fuzzers

### 5.2.1 Bit Flipping

### 5.2.2 Arithmetic Mutation

### 5.2.3 Block-based Mutation

### 5.2.4 Dictionary-based Mutation

## 5.3 White-box Fuzzers

### 5.3.1 Dynamic Symbolic Execution

### 5.3.2 Guided Fuzzing

### 5.3.3 PUT Mutation

checksum 绕不过去怎么办
patch掉

# 6. Input Evaluation

## 6.1 Execution Optimizations

## 6.2 Bug Oracles

### Memory and Type Safety

### Address Sanitizer

SoftBound / CETS

### Undefined Behaviors

### Input Validation

### Semantic Difference

## 6.3 Triage

### 6.3.1 Deduplication

case重复的情况 有几种

- 栈回溯 然后算hash 重复
- 覆盖率重复
- 语义重复

### 6.3.2 Prioritization and Exploitability

### 6.3.3 Test case minimization

# 7. Configuration Updating

## 7.1 Evolutionary Seed Pool Update

## 7.2 Maintaining a Minset

# 8. Concluding Remarks


