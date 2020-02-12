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

# Related Work

# Methodology

# Evaluation

# Limitation

# Bibliography

# Summary

# Strength

# Weakness

# Comment
