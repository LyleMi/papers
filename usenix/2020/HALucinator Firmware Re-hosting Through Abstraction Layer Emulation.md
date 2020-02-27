title: Title
authors: authors
organizations: organizations
keywords: keywords

# Abstract

逆向硬件困难。
在开发时会抽象，Hardware Abstraction Layers，HAL。
提供了一个re-hosting的方案。
High-Level Emulation – HLE
把硬件层从软件层解耦
在firmware的样本里面通过二进制分析找到系统函数的位置
然后对这些函数做一个通用的实现 最后提供给全系统仿真的仿真器

然后基于这个想法做了一个原型系统 HALucinator
让虚拟设备可以比较好的跑起来

1. 为存在的函数提供了扩展
2. 解释了re-hosting的流程 通过简单的handler 和 peripheral model (外围模型)
3. 利用 HLE 做安全研究 用到了AFL上 发现了多个漏洞

# Introduction

嵌入式设对当今生活特别重要：交通、通信、智能家居，甚至宠物玩具都由嵌入式系统控制。然而，审计固件是一个非常消耗时间，每个设备都要付出代价。

模拟执行，QEMU只支持30个不到的ARM设备。

## Contributions

1. 通过HAL层的抽象，可以在没有硬件依赖的基础上，仿真二进制固件
2. 优化修改了一个匹配的技术，更好的定位函数
3. 提出了HALucinator，一个更高层级的仿真系统
4. 基于这种方法

# 2. Motivation

CPU很复杂，然后引入了HAL。
微结构体系的厂商开发了HAL来给开发者用。
HAL给一系列的微体系结构控制提供了接口。一个HAL可以覆盖很多机器。
例如STMicroelectronic的STM32Cube 就覆盖了 Cortex-M 系列

QEMU在实际跑的时候，在遇到不支持的外设的时候就会hang住

## 2.1 Emulating Hardware and Peripherals

要实现 re-hosting 固件，需要执行环境
即使是最低级的CPU 也有完整的 on-chip peripherals
包括 计时器 / bus controllers / 网络 / 输出

代码在CPU上是通过这些特性执行的
Memory-Mapped I/O (MMIO)
具体的MMIO是根据设备有所不同的，但是在芯片的手册中有涉及

## 2.2 The Firmware Stack

系统的库
mBed OS[39] FreeRTOS[30] Contiki[25]
可以选择不同程度的抽象 但是实际执行的代码越多 找到漏洞的可能性就越大
最底层的函数肯定最复杂 有大量的函数 定义了特定的语义 也和硬件特性有复杂的交互 例如中断和DMA

这篇文章决定在HAL层做这件事情

## 2.3 High-Level Emulation

首先，这篇文章减少了模拟执行层面需要付出的努力
HAL的机制很大程度上简化了理解硬件细节的难度
handlers不用实现底层的MMIO 只需要实现HAL就可以了
把参数传给HAL 把返回值传回给固件

最后 实现了一定的精度控制 对于一些不重要的执行
只是使用低精度的模拟 返回代表成功的状态即可

# 3. Desgin

要完成这个设计 需要

1. 找到HAL库的位置
2. 为HAL函数提供高层次的替代
3. 启用外部

HAL做了一个比较模块化的设计来实现 多类型的硬件和分析状况

## 3.1 Prerequisites

1. 需要获取完整的固件

Architecture
Compile toolchain
Libraries
HALs
OS library
Middleware
Generic memory layout
Flash
RAM

## 3.2 LibMatch

闭源的 大部分函数是优化过的
不一定会遵守调用约定

是HAL函数的CFG+IR的数据库

用几种手段

- Statistical Comparison
    - Basic Blocks
    - CFG
    - Function Calls
- Basic Block Comparison
    - IR
- Contextual Matching
    - Caller / Callee

问题在于 编译器 编译参数 都可能带来不同

## 3.3 High-level Emulation

### Handlers

把替代HAL函数的代码称为Handler
是手动写的

### Peripheral Models

少部分的交互逻辑
每一个外设 都有 发送数据 接收数据 触发中断

### I/O Server

外设的接口通过 I/O Server 来暴露

### Peripheral Accesses Outside a HAL

还有一种情况是 设备绕过了HAL 直接访问
这里把所有的read都返回0 所有的write都无视 然后回报给用户

## 3.4 Fuzzing with HALucinator

### Fuzzed Input

需要专家经验 写输入怎么进去

### Termination

硬件没有结束，需要发送信号

### Non-determinism

把rand() / time() 还有一些设备特定的输出固定下来
方便测试

### Timers

不用时钟很多中断会出问题，如果用真实时钟，有的结果可能不能复现
这里写了时钟

### Crash Detection

用ASAN来检测

### Input Generation

覆盖率反馈

# 4. Implementation

用angr得IR / cfg

Avatar²来做全系统实现

HALucinator 需要的输入

- 内存布局
- 和handler关联的函数列表
- libmatch找到的函数列表

# 5. Evaluation

选了16个样例来做实验，包括串口通信、文件系统、网络

## 5.1 Library Identification in Binaries

Overall,
LibMatch without context matching averaged over the 16
applications matches 74.5% of the library functions, and
LibMatch with context matching increases this to an average
of 87.4%. Thus, nearly all of the HAL and middleware
libraries are accurately located within the binary.

## 5.2 Scaling of High-Level Emulation

## 5.3 Interactive Emulation Comparison

用QEMU Avatar²来做对比

unique basic blocks => BB
external behavior correct => EBC

## 5.4 Fuzzing with HALucinator


# Links

https://github.com/avatartwo/avatar2
https://github.com/ucsb-seclab/hal-fuzz
https://github.com/embedded-sec/halucinator
https://www.usenix.org/conference/usenixsecurity20/presentation/clements
https://www.st.com/content/ccc/resource/technical/document/user_manual/2f/71/ba/b8/75/54/47/cf/DM00105879.pdf/files/DM00105879.pdf/jcr:content/translations/en.DM00105879.pdf

# Related Work

# Methodology

# Evaluation

# Limitation

# Bibliography

# Summary

# Strength

# Weakness

# Comment
