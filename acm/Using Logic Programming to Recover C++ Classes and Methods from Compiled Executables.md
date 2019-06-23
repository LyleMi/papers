Using Logic Programming to Recover C++ Classes
and Methods from Compiled Executables

# 摘要

C++引入了一些抽象信息，例如类和方法等，这些的引入极大地帮助人在使用C++程序时设计算法。不幸的是，这些抽象信息在编译C++源代码时会丢失，这会妨碍对C++可执行文件的理解。

在本文中，作者提出了一个系统，OOAnalyzer，静态地使用创新的设计从可执行文件中以一个可扩展的方式恢复详细的C++抽象方式。

OOAnalyzer的设计受到手工分析的启发，在手工分析时，涉及到的是逻辑推理，领域知识和直觉。

而后作者编纂了这个将轻量级符号分析与基于Prolog的推理相结合的系统。与大多数现有工作不同，OOAnalyzer能够恢复多态和非多态C++类。

我们在评估中表明OOAnalyzer在测试语料库中达到了87%的准确率，语料库中包括恶意软件和真实世界的软件，如Firefox和MySQL的。

这些恢复的抽象可以帮助分析师理解C++恶意软件和普通软件的行为，也可以改进C++可执行文件的程序分析精度。

# 摘要

软件迅速增长的复杂性，并没有显示出放缓的迹象。为了应对这种日益增加的复杂性，软件工程转向面向对象（OO）编程语言，如C++，提供高级抽象的自然框架用于构建大型复杂应用程序。

OO编程范例侧重于复杂的，用户创建的数据称为绑定相关数据（成员）和类的类的结构操作（方法）在一起。这组织相关数据和操作很大程度上使开发人员能够管理C++源代码更有效地编写代码并构建更复杂的软件。

不幸的是，与其前身一样，C++允许程序员使用以实现速度和速度的精神执行危险的操作安全性的灵活性。 因此，漏洞就不足为奇了在开发人员竞争中，在C++软件中很常见在可能不安全的情况下开发更大，更复杂的程序语言。更令人惊讶的是，恶意软件作者越来越多地写作他们在C++中的恶意代码（例如，Duqu，Stuxnet和Flamer）
利用其工程效益。

进一步加剧这些问题的是高级别的事实编译期间C++对象的抽象丢失
进程，这使得分析C++可执行文件难以为人类服务分析师和自动算法都一样。 例如，一种算法搜索免费使用后的漏洞需要了解对象构造函数[7]，以及试图理解的分析师恶意软件样本的行为将从知道中大大受益哪些方法在相关类[9]。 研究人员也有证明了许多漏洞利用保护措施更有效C++抽象，以及保护和效率的水平改进了C++抽象的准确性。 例如，研究人员在可执行级控制流完整性（CFI）保护中系统[1,35]最近表明了整体保护水平通过合并可以显着改善攻击关于C++抽象的知识[8,19,21,34]。

虽然有可以从可执行文件中恢复C++抽象的现有系统，它们中的大多数依赖于虚函数表（vftables）作为其主要信息源，因此只考虑多态类（即具有虚方法的类）。

在本文中，我们通过开发一个新的来解决这个限制系统，OOAnalyzer，可以准确地恢复详细的C++抽象关于所有类和方法，包括类列表，每个类的方法，之间的关系（例如继承）类，以及构造函数和特殊方法的列表虚拟方法。 OOAnalyzer避免了以前工作的局限性通过利用复杂的推理系统来自各种来源的信息，包括一些产量关于所有类型的信息（即，不仅仅是多态的类）。 例如，OOAnalyzer可以观察对象的动作用于学习关系的指针，例如方法调用方法和类之间，这些信息与任何在目标程序中调用的方法。

OOAnalyzer的设计受到众多观察的推动人类分析师推测C++程序的增量时尚[23,27]。特别是，他们经常做简单，低级通过在二进制代码中发现模式，然后结合使用这些发现使用逻辑推理，领域知识和直觉。

OOAnalyzer采用轻量级静态符号二进制文件分析和基于Prolog的推理系统来编纂人类分析师方法，允许它有效地搜索代码模式这表明更高级别的OO计划属性。更多重要的是，OOAnalyzer的推理系统也允许它推理假设通过模棱两可的场景。当OOAnalyzer被卡住而无法取得进展，它可以暂时推广一个关于程序的不确定性，以获得更高的确定性OOAnalyzer推断出新场景，好像它是真的。如果那种情况导致矛盾，OOAnalyzer使用Prolog的能够回溯以搜索替代推理路径。

这个能力对于推理OO程序至关重要，而OO程序通常包含在推理之前需要解决的模糊属性可以有效进步。

OOAnalyzer的推理系统允许它扩展到大型的真实世界Firefox和MySQL等程序。 因为它的推理组件可以应对不完整，矛盾和模糊事实上，我们设计的OOAnalyzer使用简单但可扩展的静态象征性分析，以产生作为基础的初始事实更高层次的推理。 

OOAnalyzer也获得了可扩展性关于领域中的OO属性和高级语言的推理OO抽象，而不仅仅是详细的推理，低级可执行语义。

我们还提出了一个新的编辑距离度量来评估恢复的C++抽象的质量。 大多数现有系统恢复通过发现vftables来进行分类，这使评估变得微不足道因为每个vftable都可以映射到其相应的源代码类和比较。

因为OOAnalyzer可以恢复非多态性类，没有相应的自然标识符如vftables，并不总是有明确的对应关系在OOAnalyzer恢复的类和之间的类之间源代码。 编辑距离使我们能够评估质量没有这种通信我们的结果。 

使用我们的新指标，我们在我们的评估中显示，OOAnalyzer平均而言78％的方法在正确的类上，并且可以区分构造函数平均召回率和精确度分别为0.88和0.88。

最后，贡献可以分为三个部分：

1. 我们设计并实现了OOAnalyzer，一个用于恢复的系统可伸缩的可执行文件中详细的C++抽象方式。OOAnalyzer恢复有关所有类的信息和方法，包括非多态类。

2. 我们建议使用编辑距离作为评估的度量系统返回的C++抽象的质量OOAnalyzer。 我们表明可以使用调试符号为这种比较产生了基本的事实。

3. 我们在恶意软件样本上评估OOAnalyzer并且众所周知的干净的程序包括Firefox和MySQL。我们证明OOAnalyzer能够准确地恢复最多C++类及其方法（平均占78％的方法），并且可以识别特殊方法，例如构造函数，析构函数，vftables和虚拟方法（平均F分数为0.87,0.41,0.97和0.88）。

# 背景

## 虚函数

有时程序员可能希望调用一个方法对象不知道对象的确切类型，在这种情况下我们说方法和类都是多态的。例如，一个配置文件可以选择实现对象的类。在C++，多态方法称为虚函数。当一个调用虚函数，在运行时选择其实现基于对象的类型（而不是指向的类型）。

虚函数通过包含隐式类来实现指向虚函数表（vftable）的成员宾语。虚函数表包含每个虚拟的条目可以在该类型的对象上调用的函数。

Visual C++在编译时计算这些虚函数表和构造函数或者析构函数可以使用如下代码来安装vftable到当前对象：

```
mov eax，objptr
mov [eax]，vftableptr
```

许多相关工作依赖虚拟功能表作为主要功能信息来源，因此只能恢复信息关于多态类或虚函数。

## 类关系

子类 父类

## 2.3 Method Implementation and thiscall

thiscall 把 对象的指针 赋给 ecx

## 2.4 Runtime Type Identification

开启RTTI的时候 多态会有 类名和基类的信息
但是恶意软件有时候会把RTTI关掉

# 3. Design

OOAnalyzer的设计是被实际中做逆向的时候启发的。
一般做逆向的时候，考虑的是把逻辑合起来，领域的知识再加上一点直觉。

一般就是开始瞎看，然后看到一点熟悉的东西。
反应过来是什么。
这种就是靠常用的模式。

## 3.1 Design Goals and Motivations

### 3.1.1 Support for Non-polymorphic Classes

很多已有的工作都是依赖虚函数表的。这样就只能恢复多态的类的信息。

但是OOAnalyzer的野心很大，不想这么做，因为这样会没法处理一些东西。

### 3.1.2 Logic Programming to Resolve Ambiguity

一些C++属性在可执行级别是模棱两可的，这使得受过教育猜测恢复C++抽象的重要部分。暧昧属性发生是因为具有不同C++抽象的程序可以具有等效的运行时（即可执行的）语义因此可以产生相同的可执行文件。

允许OOAnalyzer从有根据的猜测中获取和恢复，Prolog在其设计中占据显着位置。 Prolog既用作机制简洁地编码包含OOAnalyzer的规则推理过程和作为搜索一致模型的策略该计划。 OAnalyzer也充分利用了Prolog的优势回溯功能，使其能够应对错误的假设和猜测。

每当推理不一致时检测到，Prolog允许OOAnalyzer回溯或“倒带”自上次猜测以来所做的任何推理。我们第6.4节显示没有制作和恢复的能力从有根据的猜测，OOAnalyzer的平均错误率气球显着（从21.8％到81％）。

## 3.2 Design Overview

OOAnalyzer将可执行程序作为输入，并首先提取构成推理基础的低级事实。 它然后推断使用当前事实隐含的新事实推理规则，直到它无法得出新的结论。 它然后确定一个直接扣除的模糊属性是不可能的，并假设断言或猜测一个事实。 

断言事实后，它推断了后果通过返回前向推理的猜测。 什么时候可以达到没有新的结论，它最终验证了C++的一致性抽象模型。 如果模型不一致，系统地说OOAnalyzer重温它通过假设做出的猜测推理，从最近的一个开始。 当前模型内部一致，没有提出的猜测，OOAnalyzer为用户输出发现的模型。

### 3.2.1 Executable Fact Exporter

Executable Fact Exporter是负责执行“传统”二进制分析步骤将汇编指令拆解和提升到语义表示，将指令划分为单独的函数，并进行语义分析。 有很多方法可以执行语义分析，并且为了可扩展性，OOAnalyzer使用轻量级的符号分析。 OOAnalyzer也提出了一个数字简化可执行文件特征的假设由合理的编译器发出。

Executable Fact Exporter产生的事实称为初始事实。它们通常描述低级程序行为，例如调用一个关于对象指针的方法，这些行为形成了系统中所有其他结论所依据的基础。

这些事实是近似值，大多数都有单侧错误。 如结果，大多数OOAnalyzer的规则都假设最初的事实是“低信心。”非正式地说，这意味着他们需要得到验证或者在使用之前通过其他事实证实，因为他们可能是错的！

所有初始事实都是静态的，意思是他们在后来的推理阶段没有被修改过OOAnalyzer。

### 3.2.2 Forward Reasoning

OOAnalyzer关于该计划的原因通过在事实基础中匹配事实基础上的内置规则集。

每个推理规则都是具有一个或多个前提条件的推理规则并得出结论。 如果满足所有前提条件通过事实基础，然后将结论添加到事实基础中。 

原来，事实基础仅包括发出的初始事实由可执行事实导出器。 随着推理的进行，更多的事实通过前瞻推理和假设推理加入。前瞻性和假设性推理所发出的事实是被称为实体事实。 不同于最初的事实，通常描述一个可执行语义的属性，实体事实描述的一个方面我们的系统试图恢复的C++抽象，以及关于这些属性的中间结论。 

实体事实是动态断言和收回作为程序的模型在推理过程中演变。

### 3.2.3 Hypothetical Reasoning

有时候OOAnalyzer无法做到在重要之前达成新的前瞻性推理结论
关于该程序的属性已解决。 

继续制作在这些场景中取得进展，OOAnalyzer确定了一个模棱两可的问题并做出有根据的猜测，我们称之为假设推理。 

OOAnalyzer有假设的推理规则该功能类似于转发推理规则，而是描述OOAnalyzer应该制造的模棱两可的情况它的猜测。 

程序的分析只有在完成时才完成所有模棱两可的属性都已得到解决。 既然是假设的规则只提供对模糊属性的有根据的猜测，它是错误的猜测可能导致不一致该计划的模型。 因此，模型必须通过一致性
在得到的实体事实被接受之前进行检查。

### 3.2.4 Consistency Checking

当OOAnalyzer检测到不一致时在当前的事实基础上，它回溯并系统地重温早期的猜测，从最近的猜测开始。 一致性检查由特殊实现一套检测矛盾而不是断言新事实的规则。

从概念上讲，一致性规则可以作为约束来实现阻止前向推理和假设规则得出不一致的结论。 但这种设计不允许OOAnalyzer回溯并纠正问题的根本原因（即一个糟糕的猜测），这可能发生得更早。 通过分离我们的一致性规则并强制OOAnalyzer回溯当他们被侵犯时，它允许OOAnalyzer利用前瞻推理的结论，但在他们领导时还原它们到一个不一致的状态。

# 4. REASONING SYSTEM

## 4.1 Symbolic Analysis

OOAnalyzer的fact explore采用轻量级符号分析。这是作为Pharos二进制文件的一个特性提供的分析框架（第5节）。 

Pharos的象征性分析尝试最后表示寄存器和存储器的最终值函数作为符号表达式的函数象征性的输入。 

例如，如果函数增加eax和eax的初始符号值表示为输出eax_init eax的状态是eax_init + 1. 

每个函数都是符号摘要是使用轻量级，程序内，pathand计算的流敏感数据流算法。程序间推理稍后发生在系统的Prolog部分; 有关详细信息，请参见第4.2节。OOAnalyzer还在Pharos中使用辅助分析进行跟踪对象指针的传播和识别调用约定

OOAnalyzer的符号分析设计为轻量级因此，与传统的二进制符号不同分析[4,5,25,26]在很多方面。首先，OOAnalyzer做到了不使用SMT约束求解器来推断是否特定程序执行是可行的。相反，OOAnalyzer假设所有执行路径都是可行的。 OOAnalyzer关于每个人的原因路径分开（即，它是路径敏感的），但防止指数路径爆炸[25]只展开循环五次迭代和设置符号表达式最大大小的阈值。

内存模型决定两个符号内存地址是否为别名通过查看符号存储器地址表达式是否相等在应用简化和规范化规则之后。

尽管它很简单，但OOAnalyzer的符号分析表现出色有两个原因。首先，大多数初始事实描述编译器编写操作诸如对象指针和实体之类的实体的代码虚函数表，这类代码很少使用复杂的循环，分支或内存解除引用是更多的祸根一般静态二进制分析。第二，即使是象征性的分析确实犯了一个明显的错误，后来的组成部分OOAnalyzer通常可以检测并从中恢复。

## 4.2 Initial Facts

正如我们在第3.2.1节中所解释的那样，事实发出了初步fact explore并且通常描述低级程序行为等计算当前方法对象的偏移量或调用一个使用对象指针的方法。 

表1提供了一个简短的总结选定的初始事实和汇编代码模式的例子会产生它们。

最重要的初始事实类别之一描述对象指针的创建，操作和使用。 这些事实使OOAnalyzer能够推断出两者之间的关系不依赖于RTTI或vftables的类和方法大部分先前的工作 使用其符号分析，OOAnalyzer指定每个对象指针的唯一标记，似乎传递给一个函数使用thiscall调用约定，然后记录当分配这样的指针（ObjPtrAllocation）时，调用on方法（ObjPtrInvoke），或者在与现有的偏移量处创建的方法对象指针（ObjPtrOffset）。 最后一个事实经常揭示一个对象
实例被存储为类成员（即组合）。 最后，为了启用关于对象指针的程序间推理，ThisCallMethod事实将方法链接到符号对象指针
它们被调用。

另一组重要的初始事实是用于激活的事实假设的推理规则，反过来产生高度自信实体事实。 

用于的初始事实组识别构造函数就是一个很好的例子。 如果方法总是如此首先在一个对象上调用（NoCallsBefore），返回该对象传递给它的指针（ReturnsSelf），并且不读取对象中的任何数据成员（UninitializedReads），然后是可能是一个构造函数，假设的推理将使用这些断言构造函数事实和假设理由的事实后果。 大多数实体事实都有相应的可能触发关于该实体的假设推理的最初事实，这将在下一节进一步讨论。 出于空间原因，我们不包括表1中的所有初始事实，但可以在OOAnalyzer源存储库中找到它们

## 4.3 Entity Facts

entity facts 描述了属性抽象实体，如方法，虚函数表和类包含OOAnalyzer恢复的C++抽象。

实体事实可以根据他们描述的实体类型大致组织，包括（1）方法; （2）虚函数表和虚拟基表; （3）类之间的关系; （4）sizes; （5）类。

表2显示了具有此排序的所选实体事实的列表。

大多数实体事实至少有一个相应的初始事实触发关于该实体的推理。 例如，事实导出器通过扫描相邻的内存来识别内存中可能的vftables可能合理地成为代码地址并发出这些条目的条目作为低置信度的初始PossibleVFTableEntry事实。 

如果推理规则证实了它们在当前模型中的存在，OOAnalyzer动态断言VFTableEntry等实体事实以进行确认表的存在和内容。 

这种两层推理是用于许多实体事实。

类关系由几个事实描述。 衍生 - 类事实反映了一个类继承自另一个类，而ComposedObject事实表明组成。 因为继承和组合通常在可执行级别看起来相似，OOAnalyzer也使用了一个中间事实ObjectInObject当DerivedClass或ComposedObject为true时为true，但不是两者都是（即DerivedClass⊕ComposedObject）。 最后，事实是HasNoBase显式表示类不从另一个类继承。有些规则能够证明没有基类的存在实际上识别特定的类，表示为¬HasNoBase。

size限制了类和vftables的潜在大小。约束类的大小（ClassSize）是从分配中获得的和成员组成，可以用来反驳基于观察的某些继承关系较小的类不能从更大的类派生的大小vftables（VFTableSize）也可以有界。 例如，一个vftable不能太大，以至于它与另一个已知的vftable重叠，派生类的vftable不能小于其基类vftable。

OOAnalyzer将类表示为允许它的方法集推理非多态类，没有类的自然标识符，例如vftable地址。 原来，每个方法都被认为是它自己的单例类，但最终是使用类合并事实合并其他类CLA=Clb，表示两个先前不同的类真的是同一个班级。

Cla合并时Clb，任何现有的事实CLB更新为引用Cla而不是。 班级-CallsMethod事实提供了在对象上调用M的证据Cl类，表示M必须直接在Cl上定义或其中一个祖先。 

这反过来有助于假设的推理计算可以分配给M的候选类。 因为事实是基于对象指针的数据流而不是比vftables，它提供了另一个OOAnalyzer如何的例子能够将方法分配给非多态类。

## 4.4 Reasoning Rules

P1 P2 ... Pn => C
Pi是第i个规则
C是结论

## 4.5 Hypothetical Reasoning Rules

在推不出东西的时候 就开始考虑用猜想的规则

## 4.6 Consistency Checking Rules

一些校验的规则。

# 5. IMPLEMENTATION

# 6. EVALUATION

## 6.1 Program Corpus

选干净的程序和恶意程序

## 6.2 Ground Truth

### 6.2.1 Scope

### 6.2.2 Ground Truth Exceptions

+ 没有调用thiscall的识别不了
+ 没有控制流的时候不好做

## 6.3 Edit Distance as a Class Membership Metric

用编辑距离来衡量

## 6.4 Class Membership Results

# 7. DISCUSSION AND LIMITATIONS

## 7.1 Optimizations

某些编译器优化会修改代码，使得OOAnalyzer难以按照预期的方式工作。 

一个比较有问题的类是整体程序优化（WPO）[17]（由Microsoft的GL开关启用 Visual C++），它允许编译器执行优化在链接时跨多个编译模块。

不幸的是，这个选项的开启会允许编译器违反函数中的ABI约定。

例如，编译器可以决定将对象指针传递给ecx以外的寄存器中的方法，即使声明该方法使用thiscall约定。

这种优化使得识别更加困难并跟踪对象指针的数据流。

另一个有问题的是，链接器复用了函数的实现。如果链接器发现两个符号有同一个执行代码，会只存一份代码，然后把两个符号指到一个地址。这种优化会导致在识别类的时候，相等性做不好。

还有一个优化是inline函数。

## 7.2 Other platforms

OOAnalyzer是用Windows Visual ABI来做分析的。
所以其他平台不生效。
作者认为这是一个工程问题，所以没有做进一步的分析。

## 7.3 External classes

dll也是一个问题。类可能分散在其他文件里面。

# 8. RELATED WORK

## 8.1 Recovery of C++ Abstractions

与我们最相似的研究恢复了一系列广泛的C++抽象包括将方法分组到类中，检测类之间关系，检测特殊的函数，例如构造函数和析构函数。

与这些工作相比，OOAnalyzer它是相对独特的，因为它可以静态地恢复信息关于所有类（包括非多态类）。

只有两个其他作品[14,28]试图恢复有关非多态的类的信息，只有一个工作使用了静态的方法。

ObjDigger[14]是OOAnalyzer的前身，它的设计思路和实现方法指导了OOAnalyzer。

ObjDigger试图恢复许多相同的东西C++抽象作为OOAnalyzer，更重要的是，是唯一的我们知道的其他系统能够静态恢复非多态类。

像OOAnalyzer一样，ObjDigger并不依赖在RTTI数据上，而是利用vftable分析和对象指针跟踪。

ObjDigger之间最显着的区别和OOAnalyzer（和发展的主要灵感OOAnalyzer）是ObjDigger使用程序编写的原因码。我们发现，当我们尝试进化ObjDigger进行改进时它的准确性，最终变得太复杂，无法理解它如何分析非常复杂的场景。

在OOAnalyzer，我们克服了这很大程度上是通过引入假设推理而来的允许OOAnalyzer使用复杂场景进行推理简单的规则。我们在6.4节中展示了OOAnalyzer的表现当假设推理被禁用时，情况会更糟。

Lego[28]是另一种可以恢复非多态性的系统来自C++可执行文件的类。与OOAnalyzer（和ObjDigger）不同，

Lego通过处理动态运行时来恢复此信息跟踪，允许它从OO语言中恢复类层次结构除了C++。 除了恢复类，Lego还可以还可以恢复之间的继承和组合关系类，并识别析构函数方法。 

Lego的主要劣势就是说，作为动态分析，它依赖于测试输入触发类和方法的使用。不幸的是，这个当这些输入不可用时，Lego不再适用。 它也是难以与之进行同类比较OOAnalyzer，因为Lego的表现取决于质量它使用的测试用例。

SmartDec[9,10]是可执行文件的C / C++反编译器。 SmartDec自然地恢复了C++抽象，但也有功能反编译所需的，例如控制流结构和异常处理程序分析，OOAnalyzer没有。相近OOAnalyzer，SmartDec跟踪对象指针，执行vftable分析，并不依赖于RTTI。 

然而，SmartDec只会尝试恢复多态类的方法（即类带虚拟功能）

Yoo和Barua [33]描述了一个使用SecondWrite的系统[2]静态恢复各种C++抽象，包括异常处理程序。

他们的系统依赖于RTTI数据，因此只有恢复有关多态类的信息。他们的方法在分析恶意软件时也可能是不可行的禁用RTTI数据以阻止分析。

Katz [15]使用程序分析和机器的组合学习将虚拟调用映射到目标。他们训练分类器估计每种方法基于的方式被派遣的可能性学习了对象使用事件的统计模型，包括读取，写和调用。

这些对象使用事件是使用一个生成的类似于OOAnalyzer的轻量级静态符号分析（Section4.1）。 而OOAnalyzer使用手写的编码规则
C++领域知识，Katz使用自动模型为每个项目培训。 未来的研究可以探索使用机器学习自动生成C++推理规则OOAnalyzer。

## 8.2 Security Protections for C++ Binaries

在早期，控制流完整性（CFI）保护系统[1]从源代码推断控制流转换。

后来，研究人员使用二进制分析和重写技术开发CFI系统可以直接应用于可执行文件而不需要访问源代码[31,35]。 

这样的系统没有采取考虑到任何C++实现机制的知识，并强制执行C++可执行文件的相对粗粒度的策略[21,24]。 

一些研究人员提出了技术这提高了语言无关的精确度[30]关于恢复C++抽象[8,19,21,34,35]更多与OOAnalyzer相当。

vfGuard[21]和VTint [34]是CFI系统的例子包含C++特定保护。 两个系统都识别和恢复有关虚拟调用站点和vftables的信息。

vfGuard尝试根据此信息清理虚拟调用，而VTint将已识别的vftables重定位到只读内存段，并在每次虚拟调用之前检查引用的vftable在只读内存中。

最近，其他C++特定的CFI诸如MARX[19]和VCI[8]等系统已经开始恢复其他信息，例如继承层次结构。

继承等级信息加强执法政策不允许对不相关的类进行虚拟调用。虽然MARX和VCI尝试恢复继承层次结构，它们没有试图确定继承关系的方向OOAnalyzer确实可以进一步加强推断的CFI政策。

所有这四个系统只能恢复C++抽象需要保护虚拟调用，从而只恢复信息关于多态类。相反，OOAnalyzer尝试恢复在其中实现的所有类的所有方法目标二进制，包括非多态方法和类。

## 8.3 Detection of C++ Vulnerabilities

RECALL系统[6,7]恢复了vftables，构造函数和析构函数除了跟踪对象指针的数据流之外。

它使用此信息来检测vftable逃逸漏洞观察到vftable的偏移是否对于预期的过大对象的类型。 OOAnalyzer在其前进中使用了类似的逻辑推理规则（第3.2.2节）将方法分组为类和恢复类之间的关系。

# 9. CONCLUSIONS

我们通过完成OOAnalyzer展示了可以恢复C++的信息。

OOAnalyzer使用轻量级符号分析，以有效地生成一组初始事实，并使用基于Prolog的推理系统对它们进行分析。

我们使用实验评估了OOAnalyzer，并证明它既具有可扩展性而且较为准确。

OOAnalyzer恢复了例如Firefox和MySQL这种复杂程序和基于C++的恶意软件的信息。并能够以较高的精度和方法来标识可执行文件中的类及其方法（平均误差率为21.8％）。而且也能够可以区分特殊方法，如构造函数，析构函数，虚拟功能表和虚拟方法（平均F分数为0.87,0.41，0.97，和0.88）。

# Paper summary

在本文中，作者提出了一个名为OOAnalyzer的系统，该系统可以静态辅助对可执行文件的分析，分析出程序中的相关类之间的关系（比如继承关系等），并且快速了解各个类内部的各个组成部分（例如方法、数据成员、虚函数表、构造函数与析构函数等）。

该系统的主要想法是在二进制代码中识别简单的模式，基于这些模式，使用逻辑推理并结合相关领域的专业知识，甚至是一些直觉（Intuition）等方法来分析目标程序。

而后作者基于轻量级符号执行与基于Prolog的推理相结合的系统。把分析转换成一个代码形式。

与大多数现有工作不同，OOAnalyzer能够恢复多态和非多态C++类。

作者在实验中表明OOAnalyzer在测试语料库中达到了87%的准确率，语料库中包括恶意软件和真实世界的软件。

In this paper, the author proposes a system called OOAnalyzer, which can statically assist in the analysis of executable files, analyze the relationships between related classes in the program (such as inheritance relationships, etc.), and quickly understand the internals of each class. The various components (such as methods, data, virtual function tables, constructors and destructors, etc.).

The main idea of the system is to identify simple patterns in binary code, based on these patterns, using logical reasoning and combining relevant domain expertise, even some intuitive methods to analyze the target program.

The author then performs a system based on lightweight-based notation combined with preamble-based reasoning. Convert the analysis into a coded form.

Unlike most existing jobs, OOAnalyzer is able to recover polymorphic and non-polymorphic C++ classes.

The authors showed in the experiment that OOAnalyzer achieved 87% accuracy in the test corpus, including malware and real-world software.

# Paper strengths

+ OOAnalyzer 基于静态分析而不是动态分析。
+ OOAnalyzer 不需要依赖于 RTTI 和 VFTable 来恢复类。
+ OOAnalyzer 可以恢复出具有多态和非多态类形式的类的相关信息。
+ OOAnalyzer 对类的构造函数、成员方法和虚函数表的恢复效果非常好，平均准确度达到88% 以上。

+ OOAnalyzer is based on static analysis rather than dynamic analysis.
+ OOAnalyzer does not need to rely on RTTI and VFTable to recover classes.
+ OOAnalyzer can recover information about classes with polymorphic and non-polymorphic classes.
+ OOAnalyzer has a very good recovery effect on the constructor, member method and virtual function table of the class, with an average accuracy of over 88%.

# Paper weaknesses

OOAnalyzer分析规则基于专家经验，需要大量的手工分析。

如果程序进行了一定的优化处理，OOAnalyzer表现会不太好。

OOAnalyzer的分析限于Visual Studio的ABI，耦合性太高，不易迁移。

OOAnalyzer 无法执行分析不可达的函数。

如果在不同的类中出现了相同的方法，则 OOAnalyzer 也可能会误以为它们是同一个类。

+ The OOAnalyzer analysis rules are based on expert experience and require extensive manual analysis.

+ If the program is optimized, the OOAnalyzer will not perform well.

+ OOAnalyzer's analysis is limited to Visual Studio's ABI, which is too coupled and difficult to migrate.

+ OOAnalyzer cannot analysis functions which are unreachable.

+ OOAnalyzer may also mistakenly think that they are the same class if the same method occurs in different classes.

# Comments for Author

作者仅仅和自己之前的工作做了对比，没有选择其他工作完成实验做对比，对比不够充分。

在选取实验样本上，作者只选取了较小的二进制文件，没有就较大的二进制文件做分析。作者虽然在实验中提到了Firefox，但是没有就Firefox的核心库xul.dll进行分析。

The author only compared it with his previous work, did not choose other work to complete the experiment to compare, the contrast is not enough.

On the selection of the experimental sample, the author only selected a smaller binary file, and did not analyze the larger binary file. Although the author mentioned Firefox in the experiment, there is no analysis of Firefox's core library xul.dll.

# Comments for PC

作者在文中介绍的这款工具，是一款功能强大的 C++ 高级语言抽象结构恢复工具，相比于其它的工具存在很多的优势。

这款工具能够对分析C++程序提供了很多有用的信息，特别是对于我们逆向一些由 C++ 开发的恶意程序，能够让我们方便的了解到恶意程序内部的构造，可以提高我们的对恶意程序的分析效率。

但是这款工具也存在一些可供改进的点，例如工具的时间复杂度过高，对复杂软件的分析能力可能存在问题。另外它对析构函数的识别效果不佳。而且对于编译器优化之后的程序的分析效果也不理想。

The tool introduced by the author in this article is a powerful C++ high-level language abstract structure recovery tool, which has many advantages over other tools.

This tool provides a lot of useful information for analyzing C++ programs, especially for us to reverse some malicious programs developed by C++, which allows us to easily understand the internal structure of malicious programs and improve our analysis of malicious programs. effectiveness.

However, there are some points for improvement in this tool. For example, the time complexity of the tool is too high, and the analysis ability of complex software may be problematic. In addition, its recognition of the destructor is not good. Moreover, the analysis of the program after compiler optimization is not satisfactory.

# 其他

C++ ABI 的主要内容：

- 函数参数传递的方式，比如 x86-64 用寄存器来传函数的前 4 个整数参数
- 虚函数的调用方式，通常是 vptr/vtbl 然后用 vtbl[offset] 来调用
- struct 和 class 的内存布局，通过偏移量来访问数据成员
- name mangling(mangling的目的就是为了给重载的函数不同的签名，以避免调用时的二义性调用)
- RTTI 和异常处理的实现（以下本文不考虑异常处理）
