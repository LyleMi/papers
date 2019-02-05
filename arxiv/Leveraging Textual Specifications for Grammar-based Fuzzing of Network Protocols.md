# Intro

这篇文章看上去非常牛
用nlp的玩法来搞网络协议的fuzz
网络协议这种超级结构化的东西

这篇文章的目标有两个：

- 最小化supervision 
- 换新协议也不用重新训练

这篇文章的贡献主要有

- 把语法的问题变成了NLP的任务
- 提出了一个模型来解决这个问题
- 在实际的协议上测试了这个模型

# Related Work

这篇文章似乎比较有开创性
cite的文章和nlp / fuzz都相关 但是不是这个做法
几篇应用nlp到其他任务
几篇是正常fuzz

# Problem Definition

+ Protocol Grammar-based Fuzzing

协议fuzz要遵循语法规则 emm 

+ Protocol Grammar Extraction

协议语法规定了哪一部分是什么
这篇文章用两个模块来定义语法
第一个模块是由一系列和header对应的fields组成，这部分都有对应的名字，记为f
第二部分由有序的属性组成，称为properties，记为(<f, p>)

在有这两个定义的情况下，定义了两种NLP的任务
第一个是Type Extraction，给定一个文档，提取其filed和property的符号
第二个是Symbol Identification and Linking，把包中的字段和之前提取出的符号结合起来

+ Zero Shot Learning for Entity and Property Linking

传统的方法需要每种协议都定义一个语法集合，因此文章使用了ZSL
学的是学习的函数 学习出来一个函数 这个函数就是做结合这件事情

# Design

设计了NLP来解决这两个问题，目标和之前一样，最小化监督/换协议不用重新训练
在开始用一个程序来读RFC文档，然后normalize文档的结构，再从结构中读取对应的符号和实体
这个自动化的过程可以达到82%的准确率 不过考虑到这不是文章的主要内容 探讨到此为止

用一个两步的方法来完成符号识别任务，第一步先定位其文档的位置，然后在上下文中找到其关联
在过程中始终使用ZSL方法，用分类器来寻找文档文本和协议符号之间的关系
第二步从协议语法中寻找信息，用于之后的生成步骤

## Entity Mention Identification

这个方式的前置条件是预处理过的文档和实体列表
这里用了之前提取出来的值
类似的实体在不同协议之间可能有细微的不同，这里用ZSL来寻找其相似性并建立关联
在接下来训练了一个分类器 分类(e[j], c[j])对 e代表一种实体 c代表某块chunk

## Property Extraction

提取其中的九种属性，包括checksum / port 等
主要是在找大部分协议都具有的属性

## Post-processing 

# Evaluation

# 我的想法

这篇文章提出了用NLP来指导fuzz的方式，有一定的参考意义和借鉴性
其局限性在于使用了大量的RFC文档来建立关联性 在没有对应文档的情况下难以获取足够的先验知识

# 不懂的概念

nlp off- the-shelf 
zero shot learning
