[TOC]

# Abstract

在要Fuzz的程序对输入的结构要求比较高的时候，很多Fuzz的方法会比较麻烦。语法检查和语义检查很难过。

在这篇文章，提出了一个叫做NAUTILUS的方法。用上下文无关语法和代码覆盖制导来更高效的Fuzz。

最后找到了7个mruby的洞，3个PHP的洞，2个ChakraCore的洞，1个Lua的洞。拿到了2600刀和6个CVE。

# I. Introduction

大部分代码覆盖制导的Fuzzer，都需要语料库。但是拿到的语料库一般都是常见的功能，而安全问题更多的出现在不常用的功能上。

## Goals and contributions

+ 实现了Nautilus，结合基于语法和覆盖率两种技术
+ 实现了基于语法的变异、最小化、生成

# II. Background

## A. Fuzzing
## B. Context-Free Grammars

# III. Challenges

## C1: Generation of syntactically and semantically valid inputs
## C2: Independence from corpora
## C3: High coverage of target functionality
## C4: Good performance

# IV. DESIGN OF NAUTILUS

主流程

1. 用自己的框架去编译，来拿到覆盖率的feedback
2. fuzzer解析用户提供的语法
3. 生成少量的初始化case
4. 找到可以生成新覆盖的case
5. 最小化这个case，将其加入队列中
6. 基于是否有新的路径覆盖，对现有case进行变异
7. 或者生成新的case
8. 变异的case加入队列中
9. 尝试运行

## A. Generation

### Naive Generation

随机选一条规则来生成，为了防止连续生成相似的规则
加了一个过滤器的检查

### Uniform Generation

用了下面这篇文章的算法，不是很懂

Bruce McKenzie. Generating strings at random from a context free grammar. 1997

## B. Minimization

出现能增加覆盖率的输入的时候，为了能更好的为之后的Fuzz服务
做了最小化处理

### Subtree Minimization

尝试删减子树，直到所有树都最小

### Recursive Minimization

在删减子树后，尝试做合并，比如 `1+2` 变成 `1`

## C. Mutation

### Random Mutation

随机选一颗树和节点，做变异

### Rules Mutation

一个个节点做操作

### Random Recursive Mutation

随便选一个节点，递归改下去，造成一个复杂的语法结构

### Splicing Mutation

做树之间的操作

### AFL Mutation

- Bit Flips
- Arithmetic Mutations
- Interesting Values

## D. Unparsing

处理没有处理好的东西

# V. IMPLEMENTATION

## A. Target Application Instrumentation
## B. ANTLR Parser
## C. Preparation Phase
## D. Fuzzing Phase

# VI. EVALUATION

## A. Experimental Setup
## B. Vulnerabilities Identified
## C. Evaluation Against Other State-of-the-art Fuzzers
## D. Evaluation of Generation Methods
## E. Evaluation of Mutation Methods

# VII. RELATED WORK

## A. Mutation-Based Approaches
## B. Generation-Based Approaches

# VIII. LIMITATIONS

+ 需要源代码来加入覆盖率测试的指令
+ 需要输入语法

# IX. FUTURE WORK

+ 用AFL-QEMU，去掉源码限制
+ 语法的问题可以自动化的解决

# X. CONCLUSION
