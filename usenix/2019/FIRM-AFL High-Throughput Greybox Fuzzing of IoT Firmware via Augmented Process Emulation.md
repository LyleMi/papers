# Abstract

# Introduction

## Challenges in IoT firmware fuzzing

- 不能像正常Binary一样直接执行

# 2. Background and Motivation

## 2.1 Fuzzing

## 2.2 QEMU

## 2.3 Testing IoT Firmware

## 2.4 Motivations

文章发现相对全系统仿真，在用户模式下可以很大程度下加速程序执行

有三个瓶颈造成了执行速度的问题

### Memory address translation

在全系统仿真中，QEMU使用了软件MMU来做地址转换

### Dynamic code translation

在全系统仿真中，block chaining将基本块限制在同一个物理页
导致translator比用户模式调用得更频繁

### Syscall emulation

# 3. Augmented Process Emulation

## 3.1 Overview

## 3.2 Memory Mapping

## 3.3 System Call Redirection

# 4. Firm-AFL Design and Implementation

## 4.1 Workflow of AFL

## 4.2 AFL with Augmented Process Emulation

文章在实现的时候倾向于保留AFL的完整性的同时让AFL支持测试IoT固件镜像。
文章使用augmented process emluation替换了QEMU的用户模式。

*Bootstrapping*

文章使用Firmadyne来正确仿真镜像，并集成DECAF以集成使用VMI的能力。
通过这种方式，文章可以找到目标程序起始或终止的时间。

*Forking*

AFL默认使用main函数作为fork的入口点
文章中hook了网络相关的系统调用，并把网络相关的系统调用作为fork的入口点。
正常的AFL Fork出一个进程，而文章需要fork出一个新的虚拟机实例，但是复制一个虚拟机实例的成本过高。
文章考虑使用创建快照的方式，在每次执行完毕后恢复快照。
但是在创建快照时，读写仍然是一个消耗资源的操作，因此文章基于写时复制技术创建了一个快照机制。

*Feeding input*

输入基于对系统调用的hook加入。

*Collecting coverage information*

覆盖率的收集同样基于用户模式的AFL QEMU。

# 5. Evaluation

- Transparency: firm-afl可以无感的让程序执行吗
- High Efficiency: 执行速度
- Effectiveness of optimization：优化的技巧是不是解决了瓶颈
- Effectiveness in vulnerability discovery：发现漏洞的能力

*Experiments setup*

使用了3个数据集

第一个数据集来自 nbench / lmbench 用于测试仿真的正确性
第二个数据集来自 不同厂商的IoT设备
第三个数据集是存在1 day漏洞的HTTP/uPnP服务

## 5.1 Transparency

## 5.2 Efficiency

```
公开的代码中没有bench的实验代码
nbench 是 CPU 的测试，在这里的overhead有多少作用存疑
select tcp有159%的overhead 测的大部分都是网络协议
```

*Fuzzing throughput*

- baseline: TriforceAFL

```
TriforceAFL 本意是Fuzz内核，用TriforceAFL作为baseline是否合适？
```

## 5.3 Effectiveness of Optimization

在2.4 文章提到全系统仿真三个主要的性能瓶颈

文章把执行时间分为五个模块：

- 用户执行时间
- 内存同步时间
- 代码翻译时间
- syscall 执行时间
- syscall 转发时间
- 镜像时间

## 5.4 Vulnerability Discovery

### Data collection

文章基于Firmadyne的数据库开始
然后基于exploit-db等数据库获取exp数据

### Experiment setup

文章集中在HTTP / uPnP 服务上
基于 -x 提供字典
为每个服务都提供了普通的service request来作为初始化种子

实验环境为 40-core Intel Xeon(R) E5-2687W(v3) 3.10GHz CPU and 125GB of RAM
为了保证实验的统计学意义 每个实验都跑了10个实例 并行24小时

实验数据用的是afl的plot_data

### Evaluation results

文章计算发现第一次crash的时间来作为评判标准

找到了两个 0day 漏洞

## 6. Discussion

Limitation on supported CPU architectures

Limitation on supported IoT firmware

## ?

- 文章以AFL为基础，但是在实验中并没有涉及覆盖率
- 文章提到基于Firmadyne的仿真都可以，但是在公开的代码中几乎每个程序都需要大量的手工操作
- 文章在实验部分使用了unique crash来作为衡量的指标，但是afl的unique crash计算方式并不合适
- afl-fuzz-full 等程序只给出了可执行文件
