# Abstract

文章提出了一个 DGF (Directed Greybox Fuzzing)
有效地到达指定的位置
然后做了一个叫AFLGO的实现

# Introduction

常见的导向fuzz会使用以下技巧

## Patch Testing

对着patch搞

## crash reproduction

因为隐私问题 一般不会记录用户的输入
根据crash栈和环境变量复现crash

## static analysis report verification

基于静态分析找

## information flow detection

基于sink和source

---

大部分存在的导向fuzz都是基于符号执行的
用SMT来解约束

文章提出了Directed symbolic execution (DSE)
这玩意是要考虑给重的东西在可以接受的时间内玩出一个解

这里把到达问题变成了一个优化问题
缩小给定target和种子之间的距离

文章的贡献可以总结为：

- 综合了灰盒fuzz和模拟退火算法(Simulated Annealing)
- 计算 距离
- aflgo的实现
- aflgo和oss fuzz的集成
- 大范围的测试工具

# Motivating Example

用OpenSSL做为样例

# 3. Technique

提出了 DFG directed greybox fuzzing

## 3.2 A Measure of Distance between a Seed Input and Multiple Target Locations

## 3.3 Annealing-based Power Schedules

# 4. Evaluation

## 4.1 Implementation

## 4.2 Infrastructure

# 5 Application1: patch testing

把AFLGO和Katch相比

# 6. Application 2: Continuous Fuzzing

利用OSS来做

# 7. Application 3: Crash Reproducetion

# 8. Threats to validity

# 

感觉是很程序分析的做法
但是实验非常值得参考
