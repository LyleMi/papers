# Abstract

提了一个数据流敏感Fuzz 叫GreyOne
做了一个工具 Fuzzing-Driven Taint Inference (FTI)
基于Taint 做了一个输入优先级模型 来确定哪个分支更值得探索
最后做了一个 constraint conformance (约束一致性)

然后在LAVA和19个真实世界的测试程序上做了测试
在LAVA上找到了所有公开的漏洞 还找到了336个没有确认的洞
在realworld程序上 GREYONE 比 AFL / VUzzer / CollAFL / Angora / Honggfuzz 等Fuzzer都要好
最后找到了105个新的bug 其中41个申到了CVE

# Introduction

## 1.1 Question to Address

RQ1: How to Perform lightweight and accurate taint analysis for efficient fuzzing?

RQ2: How to efficiently guide mutation with taint?

RQ3: How to tune fuzzers' evolution direction with data flow features?

## 1.2 Our Solution

*Fuzzing-Driven Taint Inference(FTI)*

*Taint-Guided Mutation*

*Conformance-Guied Evolution*

搞 hard-to-reach branches

## 1.3 Result

## Contributions

+ 提出了一个 taint-guided 变异策略，提出branch探索和输入编译的优先策略
+ 提出了一个 conformance-guided evolution solution 来指引 Fuzz 的方向
+ 实现了一个GREYONE原形系统
+ 找到了105个未知的漏洞

# 2. Desin of GREYONE

大部分流程和AFL相似 但是增加了一个 FTI

## 2.1 Fuzzing-driven Taint Inference

*Intuition*

如果一个变量的值在修改一个Byte之后改了
那么 很直觉的 这个变量是和相应的byte相关的

*Interface Rule for FTI*

### 2.1.1 Taint Inference

#### Byte-Level Mutation

#### Variable Value Monitoring

#### Taint Inferecne

### 2.1.2 Comparison with Traditional Taint Analysis

#### Manual Efforts

几乎不需要人工

#### Speed

#### Accuracy

#### Head-to-Head Comparison

改byte后 其他的fuzzer关注覆盖率的变化
但是本文关注的是值的变化

### 2.1.3 Identify Direct Copies of Inputs

在一些场景下 输入的bytes会被直接复制给变量
然后和常量/计算过的变量对比

## 2.2 Taint-Guided Mutation

### 2.2.1 Prioritize Bytes to Mutate

如果一个字节的修改可以导致更多的未触发分支被触发
那么这个字节的优先级应该更高

### 2.2.1 Prioritize Branches to Explore

如果一个分支被触发是因为权值高的字节变动
那么这个分支的权值也是高的

### 2.2.3 Determine Where and How to Mutate

#### Where to mutate

开始遍历变异 出现新的覆盖之后
更新branch和bytes的权重

#### How to mutate direct copies of input?

如果是直接相关的输入
那么记录对应的位置 和 比较的常量
修改输入

#### How to mutate indirect copies of input?

如果找不到直接对应的 那么还是做权值的传递

#### Mitigate the under-taint issue

## 2.3 Conformance-Guided Evolution

考虑到有的分支很难触发（非直接相关的依赖）
文章考虑用复杂的数据流特征来做

### 2.3.1 Conformance Calcultaion

#### Conformance of an untouched branch

#### Conformance of a basic block

#### Conformance of a test case

# 3. Implementation

## 3.1 Modularized Framework

#### Test Case Scoring

#### Seed Priorization

#### Seed Mutation Algorithms

#### State Manager

#### Selective Testing

## 3.2 Staticc Analysis and Instrumentation

#### Coverage Tracking

#### Conformance Tracking

#### Variable Value Monitoring

# 4. Evaluation

#### Experiment Setup

# 5. Further Analysis

## 5.1 Performance of FTI

### 5.1.1 Completeness of Tain Inference

### 5.1.2 Overhead of Taint Inference

## 5.2 Improvements Breakdown

# 6. Related Work

## 6.1 Taint Inference

## 6.2 Seed Mutation

# 7. Conclusion

# Comment

## Q1

如果字节里面有长度等属性 那么一个位置对应的字节含义就变了？
