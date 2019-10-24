# Abstract

大部分云都开始用REST API

基于公开的API 做一个序列

1. 主要做状态检查 状态间的依赖问题
2. 检查参数的返回值 做动态的修改

# Authors

Vaggelis Atlidakis Columbia University
Patrice Godefroid Microsoft Research
Marina Polishchuk Microsoft Research

# 1. Introduction

## Contributions

- 提出了 REST-ler
- 通过实验证明 REST-ler 效果Ok
- 用三种策略在大的空间测试
- 用GitLab做测试

# 2. Processing API Specifications

# 3. REST-ler

## 3.1 Test Generation Algorithm

## 3.2 Implementation Details

整体分为几个模块

+ 入口点
+ parser
+ compiler
+ fuzzing
+ logging

# 4. Evaluation

回答几个问题：

Q1: 依赖和动态反馈是否都是必要的

Q2: REST-ler做的东西是否做得更深了？

Q3: 应该用什么策略

## 4.1 Experimental Setup

自己写了一个MVC的站
对请求做了checksum
做实验了回答Q1

对Gitlab 做实验来回答Q2

## 4.2 Techniques for Effective REST API Fuzzing

用三种不同的策略来做

1. 无视请求类型和响应
2. 无视响应 但是考虑请求类型
3. 根据算法4 来做请求的响应

## 4.3 Deeper Service Exploration

## 4.4 Search Strategies

给了BFS RandomWalk BFS-Fast三种策略

## 4.5 Bug Bucketization

# 5. New Bugs Found in Gitlab

# 6. Related Work

# Comment

## reference

通过重放traffic找bug
3 / 29 / 6 / 37 / 2
