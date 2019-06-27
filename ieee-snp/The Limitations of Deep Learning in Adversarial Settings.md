# Abstract

深度学习很有用。
但是，存在对抗样本这种东西。
然后这篇文章在DNN上做了一个攻击
来误导分类

# Introduction

现在就考虑行车安全这种东西。
对抗样本就是能够造成算法误分类的样本。

这篇文章有以下贡献

# 2. Threat Model Taxonomy in Deep Learning

## 2.2 Adversarial Goals

- Confidence Reduction
    - 减少分类的confience
- Misclassification
    - 把一个输出分类到另外一个不正确的分类上去
- Targeted misclassification
    - 让输入到一个特定的分类上去
- Source/target misclassification
    - 让一个特定的输入 能到一个特定的分类上去

## 2.3 Adversarial Capabilities

*Training data and network architecture*

攻击者能够获取 训练数据 T，网络用的算法和函数
也能获取DNN的结构信息 F

*Network Architecture*

*Training data*

*Oracle*

攻击者有能力用模型来预言

*Samples*

攻击者能够拿到 输入 输出对

# 3. Approach

给了一个方法 把给定的 source 污染到选定的目标

## 3.1 Studying a Simple Neural Network

大概用AND做了一个例子 讲

(1) small input variations can lead to extreme neural network output variations
(2) not all regions from the input domain are conducive to find adversarial samples
(3) the forward derivative reduces the adversarial-sample search space

## 3.2. Generalizing to Deep Neural Networks

### 3.2.1. Forward Derivative of a Deep Neural Network

### 3.2.2. Adversarial Saliency Maps

### 3.2.3. Modifying samples

# 4. Application of the Approach

# 5. Evaluation

考虑几件事情

+ 是否能exploit任意样本
+ 是否能对比样本之间的易受攻击程度
+ 人能否感受到区别

## 5.1. Crafting large amounts of adversarial samples

## 5.2. Hardness and defense mechanisms

### 5.2.2. Hardness measure

### 5.2.3. Adversarial distance

## 5.3. Human perception of adversarial samples

# 6. Discussion

# 7. Related Work

# 8. Conclusions

# Limitation

# Bibliography

# Summary

# Strength

# Weakness

# Comment
