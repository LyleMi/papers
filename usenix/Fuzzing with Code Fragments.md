Lang Fuzz

generic rather than special
context-free


## Workflow

+ Language Grammar
+ Sample Code
+ Test Suite
=> Lang Fuzz => Mutated Test

## 3. How LangFuzz works

LangFuzz 基于生成和基于变异都在做，但是更主要的是变异的过程。
因为LangFuzz做得不那么完善，如果生成的话，会遇到各种问题，其中一个处理不好语义的问题，比如会生成一个没有定义的变量的调用。
所以，更多的使用变异，语义完备的Case中来做。

### 3.1 Code Mutation

变异包括学习阶段和主阶段。
在学习阶段，使用分成一个个代码块的代码作为输入。在大量的输入中，可以建立一个代码片段库。学完之后就是主要的阶段。这个时候，会随机选择一些片段，然后用同类型的来替换。
(wtf...) 这样换了之后，可能会因为语法和上下文、语义出现问题，文中说接受这个trade-off，(wtf...)


### 3.2 Code Generation

在上一步 基本没有自己的东西 就算变异也是用的输入的case。
那很正常的，如果能自己生成case就更好了。
很自然的想法是随机跑语法树。但是完全随机可能也会出问题，没有有效的输出。
而且语义的约束很麻烦，这里参考文献 CSmith[22] 搞出来一些东西。

### 3.3 Adjusting Fragments to Environment

again, langfuzz不做特定的语意解析，就会出现上下文的问题，这里做了一个fix。
emm，就是把没有定义的identifer给了个定义。

## 4. The Langfuzz Implementation

#### learning phase

#### working phase

1. random select serveral code fragments
2. pick one of possible interpretations
3. mutated

### 4.1 Code Parsing

use antlr, 考虑的主要是这个实用性很广，而且一些语言存在通用性

### 4.2 Code Generation

emm 就是前面的再提了一遍

### 4.3 Running Tests

emm 跑的funfuzz的testcase
然后用的一个他们称之为driver的东西一直跑 来省时间
emm 然后就炸了 有的变量不知道啥时候出现过 影响了 然后case没得复现

最后缩减case用的是delta algorithm[24][9] 不知道是什么...

### 4.4 Parameters

## 5. Evaluation

### 5.1 vs funfuzz

funfuzz是对js高度定制化的，有很多语法的细节和优化，而且时刻跟着js的更新

langfuzz这里的优势反而是他没有做这个，这样的话可以随便迁移

然后比较的标准是

- 发现的case的overlap
- 发现的defects的数量

#### 5.1.1 Testing Windows

用的是TraceMonkey...

2012年的文章 测的08年的引擎


### 结论

感觉能发主要是泛用性做得很好
缺点就是之前提到的 没有在语义上做东西
而且文章主要使用 defecte 来评价 而不是Vuln 感觉很有问题

