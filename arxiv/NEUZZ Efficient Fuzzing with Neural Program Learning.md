# NEUZZ: Efficient Fuzzing with Neural Program Learnin

## 1. Introduction

AFL AFLFast BFF zzuf等基于代码覆盖率反馈算法的Fuzzer，经常在一段长时间的变异之后就不会出现新的代码覆盖率提高了。这其中的关键问题是由于基于代码覆盖率反馈的输入生成模式没能利用不同变异和变异所产生的变化来去了解程序的行为模式。除此之外，自定义的变异策略需要大量人工，也是一个有挑战性的工作。现有的symbolic执行来进行程序分析得方法也过于hevyweight。

近来，已经出现了一些利用机器学习进行模糊测试的研究：

1. Konstantin Böttinger, Patrice Godefroid, and Rishabh Singh. 2018. Deep Reinforcement Fuzzing. arXiv preprint arXiv:1801.04589 (2018)
2. Patrice Godefroid, Hila Peleg, and Rishabh Singh. 2017. Learn&Fuzz: Machine Learning for Input Fuzzing. In Proceedings of the 32nd IEEE/ACM International Conference on Automated Software Engineering
3. Mohit Rajpal, William Blum, and Rishabh Singh. 2017. Not All Bytes Are Equal: Neural Byte Sieve for Fuzzing. arXiv preprint arXiv:1711.04596 (2017)

然而这些研究在漏洞挖掘数量或者代码覆盖率上相比于现有的AFL并没有非常明显的提升，更重要的是，使用RNN以及RL的overhead可能过大。

本篇文章提出了一种利用机器学习进行Fuzz的方法，不像其他研究者主要研究利用机器学习学习输入的文件格式，我们尝试学习出输入和程序代码覆盖之间的关系。

我们认为代码覆盖率导向的Fuzzing能够被表达为一种优化问题，这种问题的目标是选择一系列变异，这些变异能够最大化代码覆盖率。然而通常来说，这是一个比较难的组合优化问题

我们可以从侧面解决这个问题：**首先学习近似连续并且可微神经规划的神经网络，这个神经网络能够作为离散程序的代理，在连续的神经网络中寻找输入能够最大化代码覆盖率是一个数值优化问题，这个问题能够被梯度下降解决。trade-off是说不是所有输入都能被预测产生新的代码覆盖**

然而，由于每次使用新的测试输入运行程序的花销很小，只要神经网络对程序逻辑建模合理，我们的方法能够做到很高效。我们的实验表明即便是当前这种不完整的模型也极大的浩宇传统基于evolutionary 的方法。

根据 Honglak Lee, Roger Grosse, Rajesh Ranganath, and Andrew Y Ng. 2009. ConvolutionalDeepBeliefNetworksforScalableUnsupervisedLearningofHierarchical Representations. In Proceedings of the 26th Annual International Conference on Machine Learning，**CNN有能力从原始inputs中extract结构化信息**。

更重要的是，我们的CNN模型中的前馈性质能够比RNN和RL有更短的训练时间。一旦我们使用CNN来训练由evolutionary  Fuzzer生成的部分样本之后，我们就可以使用梯度下降来识别能使代码覆盖率最大化的变异策略。

测试了6中不同文件格式（ELF, PDF, XML, ZIP, TTF, and JPEG），目标程序平均代码行数47,546。NEUZZ比AFL效果好得多，在相同时间NEUZZ找到的边覆盖比AFL多70倍。更重要的NEUZZ比AFL多找到了36个新的bug。我们和基于RNN神经网络的Fuzzer(Mohit Rajpal, William Blum, and Rishabh Singh. 2017. Not All Bytes Are Equal: Neural Byte Sieve for Fuzzing. arXiv preprint arXiv:1711.04596 (2017). )进行了比较，边覆盖高了9倍，训练时间减少了16倍。

我们主要的贡献如下：

我们引入了新的轻量级的学习方法以及利用有效的神经网络来Fuzz目标程序。我们使用梯度下降的方法来更有效的找到变异策略来最大化代码覆盖率

我们设计了一种有效的学习**代理神经网络**：给定一个测试输入，能够预测控制流的边覆盖。我们设计，实现并且评估了我们的方法

## Fuzzing as a learning problem

Fuzzing其实是一个优化问题，这个问题的目标是生成新的输入，这些输入能够能够最大限度的发现bug。然而，由于预测bug在程序中出现的位置是非常困难的，因此通常意义上，找到更多的边覆盖是找到bug的替代方法。现在大多数Fuzzer都是使用evolutionary 方法来生成变异的输入，然而这种方法经常会很难找到比较“稀有”的输入以及很难触发的分支。

### 利用神经网络进行Fuzzing

通常来说，针对任意程序找到能够最大化边覆盖的变异策略是一个很困难的组合最优求解问题，因为程序的逻辑**是分离**的并且是任意复杂的(arbitrarily complex)，我们的方法背后的insight 是将传统程序中的分离的逻辑类比于学习一个连续的可区分的神经网络(The key insight behind our approach is to approximate the discrete logic of a traditional program by learning a continuous and differentiable neural program) 这样的可区分的神经网络能够被用来指导输入生成过程，以便最大化边覆盖。需要注意的是，实际边覆盖的数量依赖于神经程序对于程序逻辑的建模的准确性。然而，由于每一次运行目标程序测试输入的cost很低，输入生成过程仍然很有效，即便神经网络程序并没有很好地模拟目标程序的逻辑。我们利用神经网络程序模拟程序逻辑的的基本理论是万能近似理论：在给定足够多的训练数据的情况下，一个多层的神经网络能够模拟任意的函数

#### 神经程序

神经程序是一个能够通过学习潜在的目标程序的逻辑来预测目标软件行为的神经网络。神经程序被设计来预测的实际的程序行为依赖于神经程序的使用。举例来说，一些研究在给定输入输出样本的前提下来合成神经程序，以便在给定新的输入的时候能够预测出程序输出。**这样的神经程序经常定义、使用更为精确、可区分的操作而不是典型的传统神经网络中的分层转换**(Such neural programs often define and use more sophisticated differentiable operations than classic layerwise transformations used in traditional neural networks.)。然而这些精确模型针对于大型、复杂程序的可测量性仍然是不确定的。更重要的是这些操作可能是和任务相关的而不是通用的。

#### 神经结构

CNN可以从字节流中学习输入的结构性
RL依赖于输入输出的稳定性 所以不行

### 2.2 方法概述

#### 2.2.1 输入形式

输入ast可能会带有一些先验知识
但是本文使用字节流

#### 2.2.2 输出形式

输出覆盖率的向量

#### 2.2.3 数据源

普通fuzz生成的输入

### 2.3 样例

几个问题
- 怎么定位要变异的byte
- how to arrive at the exact perturbation to introduce in the mutation
- how to handle the nonlinearity in the code that solver-based
techniques 

## 3. 方法

### 3.1 神经网络学习

输入是字节流

输出是边覆盖，但是对其做处理
去掉每次都能覆盖
