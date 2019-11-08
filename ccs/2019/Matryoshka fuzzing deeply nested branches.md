# Abstract

1. we identify all the control flowdependent
conditional statements of the target conditional statement.

2. we select the taint flow-dependent conditional statements

3. we use three strategies to find an input that satisfies
all conditional statements simultaneously

# 1. Introduction

# 2. Background

# 3. Design

## 3.1 Problem

常见的方式是

1. 先用污点分析找可能会影响的Bytes
2. 用梯度算怎么变异
3. 变异后再执行 验证

但是这样的问题 在于 依赖可能是嵌套或者其他的复杂结构
满足一个条件的同时 另外的条件就不满足了

## 3.2 Solution Overview

# Evaluation

# Limitation

# Bibliography

# Summary

# Strength

# Weakness

# Comment

总的来说 就是在分支条件里面做得更细了
考虑到了多级依赖 嵌套的情况
然后做了一个解决方案
