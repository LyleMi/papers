# Abstract

还是在说覆盖率制导的缺陷
不如梯度下降的玩法

# Introduction

梯度下降算法看上去是一件很不错的事情
但是他并不能直接用到fuzz上
因为程序有非常多不连续的行为和复杂的分支

然后作者发现可以创建一个smooth surrogate function来解决这个问题

这篇文章是在各种文件格式上 （ELF PDF XML ZIP TTF JPEG）和10个fuzzer做比较，有比较好的效果

总的来说 这篇文章有下面这些贡献

- 第一次提出了smoothing的重要性
- 做出了一个最有效的神经网络
- 说明这个梯度可以很有效的用来指导生成和变异
- 实现了NEUZZ

# OPTIMIZATION BASICS

 
