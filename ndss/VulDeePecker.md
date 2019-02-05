VulDeePecker

## Abstract

漏洞发现和其他的问题有很大的不同 因此把深度学习作为漏洞发现的工具需要一些指导性的原则
用代码段来表示程序，然后把这些代码段变成向量，最后就是一个代码相似度的问题

## Introduction

已知的查找漏洞的方式有两个主要的缺点
- 很高的人力
- 高的误报率

而且自动化的方式对人工标注的要求很高

### Contribution

1. 开始用deep learing做vuln detection
2. 做出了设计和实现
3. 搞了一个database

<!-- 

发现一个很骚的操作 没有洞 没关系
找最近的补丁去做diff 盯着diff找洞可能性要高很多
然后再说是自己弄的

-->

## II. Guiding Proinciples

A. How To Represent Software?

principle 1. => 要把程序变成一个向量，主要是变成IR，要能表示程序和数据间的依赖关系

B. What is an appropriate granularity?

principle 2. => code gadget 作为粒度

c. How to select neural networks?

principle 3. => blstm

## References

19. Toward large-scale vulnerability discovery using machine learning ``ACM``
28. VUDDY: A scalable approach for vulnerable code clone discovery ``IEEE s&p``
32. VulPecker: An automated vulnerability detection system based on code similarity analysis
37. The beauty and the beast: Vulnerabilities in Red Hat’s packages ``usenix`` 2009
38.
49.
59.
60.

