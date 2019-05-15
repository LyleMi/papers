# Abstract

学了一个预测模型 给定输入 给出执行流
可以减少无用的执行

# Introduction

# Related Work

# Methodology / Apporach

跑一些 跑完了预测 如果high / medium的case就跑 low就扔掉

## 3.1 Generating Candidate Inputs

## 3.2 Modeling Programs via Path Prediction

先跑 跑出来的case作为训练样本

## 3.3 Estimating Uncertainty via Entropy

用熵来衡量 熵高的是大爷

```
H(x) = ∑ Pr( pi | x ) log(Pr( pi | x ))
```

pi是执行路径 x是input
Pr(pi|x)是在输入x的时候 执行到pi的概率

# Evaluation

# Limitation

# Bibliography
