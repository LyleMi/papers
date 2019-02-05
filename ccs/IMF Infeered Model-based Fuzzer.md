# Abstract

目前的fuzz 都比较naive 就主要是通过调内核api来做这件事情 然后这篇paper就要搞事情

# Intro

2015年 nvd 报告有248个内核洞 2016年达到478个
然后linux每天代码增长都达到了4k lines
大部分的人做fuzz 都是随机调用kernel api 然后给随机参数
而问题在于，调用之间是有关联的，一个write调用如果之前没有合适的open，是不ok的
这篇paper的想法来自于系统调用就算是相同的，也可能在某些方面有不同的结果，比如因为aslr和进程顺序
那跑两次，就有两个traces，比较一下就知道哪些是常量了
所以贡献是

- 通过多次执行的api logs，给出一个良好的api调用序列
- 实现了这个想法，然后在macOS上跑了
- 找到了32个kernel panic
- 数据和代码开源了

# Background

## 2.1 api fuzzing

api fuzz不一样的点在于 出的bug不一定是bug，因为可能外面有检查

## 2.2 kernel fuzzing 

- randon based kernel fuzzing
    - 随机api调用
- type-aware kernel fuzzing
    - 准备好了一些值供调用
- hooking based kernel fuzzing
    - 在正常跑其他东西的时候hook调一些函数
- feedback-driven kernel fuzzing
    - code coverage

# Motivation

借助正常跑的时候的一些东西


