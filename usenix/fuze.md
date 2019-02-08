# Abstract

一般认漏洞的时候会要求有exploit，但是手工构造exploit需要大量的精力和时间，于是这篇文章尝试考虑自动化的生成exploit。其中UAF又是较难构造的。

这篇文章构造了一个名为FUZE的工具，基于符号执行等方式来自动化的构造内核UAF Exploit的攻击载荷。

为了更好的解释FUZE的想法，基于一个二进制分析框架和Kernel Fuzzer实现了FUZE。

# Introduction

UAF是内存破坏漏洞的一种类型，可能会造成权限提升、信息泄漏等问题。

FUZE以一个会导致Kernel Painc的Case作为起点，辅助完整exploit。

FUZE并不是想自动化的完成整个过程，而是这些过程：

首先，找到UAF利用需要的sys call。

第二，找到需要计算的数据。

第三，帮助找到exploit的时间片。

最后，绕过防护机制。

总的来说，这篇论文完成了以下的工作：

+ 设计了FUZE，一个内核UAF漏洞 exploitation framework
+ 实现了FUZE
+ 基于FUZE完成了15个demo

# 2. Background and Challenge

一般来说，完成exploit需要如下的步骤。

1. 对废弃指针用到的sys call过程有足够的了解。

## 2.2 Challenge of Crafting Working Exploits

# 3. Overview

