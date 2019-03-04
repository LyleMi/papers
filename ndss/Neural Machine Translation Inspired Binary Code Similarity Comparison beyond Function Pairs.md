https://securitygossip.com/blog/2019/03/04/neural-machine-translation-inspired-binary-code-similarity-comparison-beyond-function-pairs/?tdsourcetag=s_pctim_aiomsg

作者：Fei Zuo, Xiaopeng Li, Patrick Young, Lannan Luo, Qiang Zeng, Zhexin Zhang

单位：University of South Carolina, Temple University

会议：NDSS 2019

论文：https://arxiv.org/abs/1808.04706
Background

函数或者代码相似性比较一直以来都是比较热门的话题，一般问题都是给定两个函数或者代码片段，比较两个函数的语义是否相等。这篇论文里作者做的代码相似性比较是基于二进制层面的。此前代码相似比较常用的方法为fuzz或者符号执行，符号执行比较好理解，通过给定相同的输入，查看输出的符号式是否相等。作者在这篇论文里，在此前问题的基础上提出了更高一级的相似性比较，即不同处理器架构的二进制代码语义相似性比较。
Motivation

二进制程序经过反汇编之后则为一条条汇编指令，这些汇编指令则可以看做是纯文本，那么，代码相似性比较是不是可以看作自然语言的相似性比较，从而使用NLP进行处理会不会有意想不到的收获。作者的观点即是，将一条汇编指令当作一个word而将一个basic-block当作一个sentence。通过神经网络进行训练挖掘出其中的语义表示，从而将本来代码相似比较问题转换为自然语言相似比较问题。
conception

AUC: The AUC value is equivalent to the probability that a randomly chosen positive example is ranked higher than a randomly chosen negative example

简单一点：随机选取两个样本一正一负，AUC值越高，取到正值排在负值的概率越高，即AUC越高，分类效果越好

word embedding / sentence embedding: 可以看作是词或者句子在使用向量表示情况下的一种模型。

Word2vec: 一种用来生成词word embedding的方法/算法/模型
Main Steps

    指令 –> instruction embedding
    基本块 –> block embedding
    相似性比较

instruction embedding generation

汇编代码预处理：

    所有数字常数替换为0，保留符号
    所有字符串常量替换为<STR>
    所有函数名替换为FOO
    其他常量替换为<TAG>

basic-block embedding generation

使用RNN中的LSTM训练word embedding从而生成bbl embedding。
Implementation
训练数据集生成

    源代码库：openssl, coreutils, findutils, diffutils,binutils

    修改llvm后端，使得相同IR基本块编译出的二进制代码基本块具有相同的ID，即在ARM和X86架构上，由同一IR生成的BBL具有相同的ID，作者以此作为训练数据
    使用n-gram 来产生不同语义基本块？

代码相似性比较

比较多个基本块组成的序列是否相似：

    从CFG的角度展开待比较的代码序列，从而生成多条代码序列
    将这多条代码序列与目标代码多条代码路径序列进行比较，找出最后公共子序列，通过收集到的数据来确定多个基本块组成的序列是否相似

Evaluation
环境配置

ubuntu 14.04

64bit 2.7GHZ Core I7

32G RAM

No GPU
训练框架

tensorflow

Keras ：以tensorflow为后端
数据集组成

原始数据集：同上

组成：80训练，10%验证，10%测试
测试结果

由于汇编指令有限，显然不经过预处理，被测试目标里面许多元素，类似于数字，字符串等常量占了很大一部分。从而导致被测试数据里面有大量的数据无法在训练数据集中找到

这是这篇论文里最主要的一张图，这张图里，作者使用SVM模型进行比较，SVM模型使用从基本块中抽取到的一些特征，如跳转，函数调用，字符串常量等为依据进行相似性比较，从图中可以看到，使用不同的编译优化级别，或者是不同编译优化级别间的相似性比较，大基本块或者小基本块，作者的NLP方法都是占优的。
调参结果

作者在这里调节了NLP中使用的一些参数，如训练Epoch，训练dimensions, network layers。多是和NLP相关和数据，作为安全相关的研究，也只有一步步的地做实验，观测结果。没有太多的理论的推导。作者解释大多数原因为消耗的内存时间越多，结果越准确，而这个结果会在消耗的内存时间到达一个阀值后趋于平衡。
时间

随着训练层数增加，时间示增长，不同的模型也会有不同的时间消耗，作者使用的LSTM模型消耗时间最长。单位是秒每层，这里作者的训练时间是可以接受的，但是考虑到作者的训练数据集，不过几十万条指令，实在是太少，也应该是这个级别的时间。

测试时间：平均第个基本块相似度比较消耗0.41毫秒。
代码相似性比较

这里我觉得应该是毕竟重要的一部分，但是作者并没有给出太多的数据，比如作者提到进行MD5函数的相似性比较时，作者使用openssl中的md5函数作为比较对象，来查看cryptlib,openssh,libgcrypt,mysql,glibc中是否包含md5的代码片段，仅仅交待一句其中包含了md5代码片段，相似性在范围在86%到94%之间，而其他并没有这个相似性，没有具体的数据。
评价

由于目前我也在做NLP函数相似性比较的工作，所以我选择了这篇论文。这篇论文的idea曾经我也讨论过，但是我此前想到是这个做法不现实，原因是汇编语言什么语义信息而是零散的片段，NLP可能无法正确的理解他的语义。

在这篇论文里，有一些值得借鉴的地方，比如他对于汇编语言的预处理，使得能够过滤掉许多具体含义的字符，而以固定的字符串代码，这样在不失语义的情况下，极大提高了NLP的功能。

但是在这篇论文里， 我觉得有一点不足，就是最后的数据部分，函数相似性比较应该是比较重要的部分，作者应该将具体的数据展示出来，比如在不同的阀值下，会有多少误报和漏报等等。此外我觉得作者没有将他的工作与一些更好的相似性比较工具进行对比，比如bindiff。

对于作者选取的数据集与测试集，我有一点看法，即，虽然训练集与测试数据集虽然不重叠，但是对于同一个库，他的代码风格是极类似的，甚至有时为了追求代码的优雅美观，有些库会特意编写一些代码使得整个库看起来十分对称，这样使得作者的测试数据很漂亮。实际上作者应该选取另外的一些库进行测试再展示出具体数据。

对于NLP来说，训练数据集的大小十分重要，几十万条汇编指令的文本大小也不过几十M，这对于NLP训练来说是否足够是个问题。通过NLP训练数据集一般为几个G的文本数据。训练数据集小的一个重要结果就是在特定的测试范围外表现会很差。
