# Abstract

开局就把应用场景描述得很清楚：

- 针对Patch
- 对着危险位置fuzz
    - sys call
    - 危险位置
- 有stack trace的情况下复现

然后说自己提出了一个 DGF (Directed Greybox Fuzzing)
能够有效的解决这些问题

一个退火算法来做种子和变异的选择
做了一个叫AFLGO的实现 并完成了对应的实验
AFLGO可以在白盒符号执行导向fuzz和非导向灰盒fuzz下都获得比较好的结果

把AFLGO集成到了OSS-Fuzz上 找到了39个bug 获得了17个CVE编号

# 1. Introduction

灰盒fuzz很有效 很轻量 而且已然取得了一些成果
但是灰盒不能导向 但是导向是很重要的
导向的大部分时间都花在指向特定的位置上
常见的导向fuzz会使用以下技巧

## Patch Testing

对着patch做 当有修改发生的时候 去尝试找是否引入了问题

## crash reproduction

因为隐私问题 一般不会记录用户的输入
所以根据crash栈和环境变量复现crash 也是一个值得研究的课题

## static analysis report verification

基于静态分析能找到很多潜在的危险位置
而后通过定向fuzz能够确定风险是否存在

## information flow detection

设置sink和source 

---

符号执行用程序分析和约束求解来解决问题
因为符号执行的在路径探索问题上优势 大部分存在的导向fuzz都是基于符号执行的

SMT来解约束

文章提出了Directed symbolic execution (DSE)
把可达问题变成了优化问题
考虑到大部分路径是不可达的

KATCH用KLEE引擎来做

白盒符号执行 和 灰盒模糊测试

但是 DSE的效率
考虑给重量级的东西在可以接受的时间内解出一个输入

文章就想到用符号执行给出一个方向 然后用fuzz去到达
在heartbleed的测试上 AFLGO 20分钟出现了poc
而KATCH 24小时都没有结果

文章提出了专注与缩小给定target和种子之间的距离的DGF
在高层次上 文章把可达问题变成了优化问题
然后 提出了一个启发式的算法来解决这个问题

为了算种子之间的距离 文章首先计算了
每个基本块到指定目标之间的距离

文章的贡献可以总结为：

- 综合了灰盒fuzz和模拟退火算法(Simulated Annealing)
- 提出了计算距离的方式
- aflgo的实现
- aflgo和oss fuzz的集成
- 大范围的测试工具

# 2. Motivating Example

用Heartbleed做为样例

## 2.1 Heartbleed and Patch Testing

这里用了一些马尔科夫链那篇文章的想法

## 2.2 Fuzzing the Heartbleed-Introducing Source Code Commit

# 3. Technique

提出了 DFG directed greybox fuzzing
所有程序分析的工作都在编译的时候做掉
提了一个 inter-procedural measure of distance
基于这个测量方式 又提出了一个 power schedule

## 3.1 Greybox Fuzzing

## 3.2 A Measure of Distance between a Seed Input and Multiple Target Locations

## 3.3 Annealing-based Power Schedules

## 3.4 Scalability of Directed Greybox Fuzzing

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
