# abstract

语法严格的程序一般有语法解析、语义检查然后执行。
一般的bug是在执行阶段，这让fuzz就变得比较麻烦。

## I. Introduction

想要生成有效语义的case的代价是非常昂贵的。
grammar-based fuzzing approaches [22, 23, 24]。

fuzz XSL XML JavaScript 

第一步是学一个 Probabilistic Context Sensitive Grammar (PCSG)，学到语法和语义。
第二步是用PCSG来搞。

用这个generate的sample来fuzz xml库。结果是能生成结构ok的case，很大的增进覆盖率。
找到了19个memory corruption bugs(空指针？) 还有32个DoS (emmm)

Contributions:

- 从样本里面学一个可以描述语法和语义的PCSG
- 用PCSG生成正确的，多样化的，不常见的Case
- 用Case来Fuzz

// 这里考虑不要生成重复的Case，Case的重复度好像我们还没怎么做

## II. Approach Overview

### A. Target Programs

xsl xml js html

用cfg

#### Definition 1. CFG

由四个元素组成

- N 非终止符的有限集
- ∑ 终止符的有限集
- R N中元素和∑中元素的生成规则
- s 开始符号

### B. overview of skyfire

有三个大目标
第一个是生成正确的case，保证语法和语义都是对的。
第二个是生成多样化的case。
第三个是生成不常见的case，来fuzz less-common part。

第一步是搞ast cfg 但是cfg是没有语义的
所以文章是搞了一个csg

## III PCSG Learning

### A. Probabilistic Context-Sensitive Grammar

#### Definition 2. CSG

由四个元素组成

- N 非终止符的有限集
- ∑ 终止符的有限集
- R N中元素和∑中元素的生成规则，但是这个生成规则要带上下文
- s 开始符号

#### Definition 3. PCSG

在PCSG的基础上加了一个概率

### B. Learning a Probabilistic Context-Sensitive Grammar

考虑网上的大量样本，自动学需要两个输入：样本和语法。

通过样本，来计算概率，就知道能不能跑了。

// 这样的问题是有的样本没有一些语法

## IV. Seed Generation

### A. Seed Generation

#### Definition 4. left-most derivation

基于PCSG+CFG做了一个东西

---

但是做出来之后有几个问题

因为一些生成规则是递归的，那么就可以生成很大的样本

因此加了一些启发式的算法

###### Heuristic 1: Favor low-probability production rules

为了生成一些uncommon的case 调整了爆率

###### Heuristic 2: Favor low-frequency production rules
###### Heuristic 3: Favor low-complex production rules
###### Heuristic 4: Restrict the total number of rule applications

### B. Seed Selection

用代码覆盖来指导case生成

### C. Seed Mutation

## V. Implementation And Evaluation

用网上爬的到作为语料库 Heritrix[31]

### A. Evaluation Setup

用的xsl xml js这些 在antlr的社区都有
数据集有5.1TB

用afl来做实现 自己不做

### B. Vulnerabilites and Bugs Discovered

### C. Code Coverage

### D. Effectiveness of Context and Heuristics

CFG based 过不了语义检查
调整了启发式规则，然后比较，发现能减少不必要的case

### E. Performance Overhead

### F. Case Study and Discussion

### G. Preliminary Results for JavaScript

Fuzz Trident

说js不好用覆盖率来提 emmm

Future Work...

## VI. Realted Work


## VII. Conclusions


## 结论

亮点

一个是提出了有一定上下文的CSG
然后提出了能帮助fuzz的PCSG，PCSG主要是有概率，然后启发式条件设置得很好

之前没有仔细看，现在看了发现就是没有做js

berserker可以是他的future work
但是berserker是基于大量人工的
另一个问题在于 人家已经把csg这件事情提了
我们的创新点在哪里呢

那么先提出问题

- 死循环怎么解决
- 作用域
- getter / setter / proxy 

这些问题怎么描述呢

作用域也可以归到上下文里面去 但是这样就只是工程了 不算是学术的创新点

死循环这种其实算是代码执行的问题？ 语义是ok的 但是emm

getter / setter 同理 随便写也可以跑 但是没用

