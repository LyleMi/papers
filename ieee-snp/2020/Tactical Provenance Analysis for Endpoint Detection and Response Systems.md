# title: Tactical Provenance Analysis for
Endpoint Detection and Response Systems

# Abstract

EDR 通过对系统事件的监控，提供了精密的入侵检测观测方案。
但是，当前的EDR系统仍然有多个挑战没有解决：

- EDR 生成了大量的误报
- 处理大量的 EDR 报告需要非常多的人力
- 考虑到处理日志的成本，有的关键日志可能在发现威胁时已经被删除了

这篇文章提出了一个 Tactical Provenance Graphs (TPGs) 的概念。

# Introduction

经典的商业级的面向APT的解决方案是 Endpoint Detection and Response (EDR) 。
EDR 通过基于专家经验的 Tactics, Techniques, and Procedures (TTPs) 来刻画底层的攻击事件。MITRE 的 ATT&CK 矩阵就是最知名的公开 TTPs knowledge base。

EDR 要面临的第一个问题是设计之初就是为了发现，而不是准确率。TTPs 倾向于把所有潜在的攻击行为都描述出来。

## Contributions

- 提出了一个 tactical provenance graphs (TPGs) 处理 EDR 的方案
- 提出了一个基于 TPG 的威胁评分方案
- 提出了一个可以降低日志存储的方案
- 将原型系统 RapSheet 集成进了赛门铁克的 EDR 工具

# Related Work

## 数据溯源 Data Provenance

Windows ETW
Linux Audit

## MITRE ATT&CK and EDR tools

MITRE ATT&CK 矩阵提供了常见的攻击技战术。
EDR 则基于 ATT&CK 矩阵 实现了安全方案，致力于：

- 检测潜在的安全事件
- 日志处理与管理
- 汇总并发现安全事件
- 提供解决方案

EDR 的挑战：

- 误报
- 巨大的上下文
- 相对短时间的数据存储无法处理长时间跨度的攻击

# System Overview

## 威胁建模

考虑企业环境有上千的设备面临攻击者。
攻击者攻击的手法是慢而低的。不容易引起注意。
时间跨度通常持续数个月。
同样，我们考虑APT攻击通常会带来巨大的损失。

假设：
- EDR在所有的终端上收集信息
- 当时收集到的信息是准确没有被修改的

## 目标

- 多阶段攻击的解释
- 攻击报警
- 长时间日志保存
- 方法相对通用
- 入侵程度低，不用对操作系统做修改
- 可扩展

## 方法

原型系统被称为 RapSheet。
使用规则去匹配系统日志里面符合 MITRE ATT&CK 的行为。
当含报警信息的溯源图构建完成的时候，生成一张 TGP（tactical provenance graph）来展示。
首先确定 initial infection point (IIP)，而后根据 IIP 前溯。最后输出威胁程度的评分。

威胁评分的核心思路是根据时序将威胁信息综合起来，基于杀伤链进行评估。

# 系统设计

## 日志收集

系统在 Linux 上使用 Linux Audit 框架，在 Windows 上使用 ETW 。
另外系统也收集了Windows 的 ALPC (Asynchronous Local Procedure
Call) 做为补充。

## 规则匹配

RapSheet 基于 ATT&CK 矩阵做了规则引擎，可以通过加入 TTP 比较方便的扩展。

## 数据溯源数据库

获取到的数据库在解析后加入图结构的数据库。
为了减小存储的负担，作者也引入了之前工作中的一项技术：causality-preserved reduction 。
对于相同的向量，只保存最新的时间戳。

## 战略溯源分析 (Tactical Provenance Analysis)

# 威胁评分

# 图数据缩减

常规的EDR通常使用FIFO的策略来删除日志，但是这样并不完善。
本文基于图数据库，优先删除和报警无关联的节点。

# EVALUATION

本文在评估部分考虑了四个因素：

- RapSheet 在触发报警的能力
- RapSheet 的效率
- RapSheet 在减小日志存储的能力
- RapSheet 在面对真实攻击的表现

# 相关工作

Holmes[43] 是比较早期的工作，提供了数据溯源与威胁评分。但是该工具依赖于全量日志，同时支持TTP的数目较少。
另外为了减少误报，Holmes将部分常见操作加入到了白名单中，容易被投毒攻击。

# 讨论与缺点

## 跨机器分析

本文在实现和讨论时仅关注了单机的情况。

## 在线分析

本文面对实时分析仍有一些缺陷，放到以后处理。

## 绕过

非TTP覆盖的情况，可能识别不够及时。

## APT实验的仿真度有限

## 部分低位的危险会被忽略


