https://securitygossip.com/blog/2019/10/25/cryptorex-large-scale-analysis-of-cryptographic-misuse-in-iot-devices/

Abstract

密码学函数在安全通信和数据存储中具有重要的地位。大多数密码学函数的定义和实现都是安全的，但可能会被开发人员错误的封装或者使用。在IoT设备中这个问题更加广泛，由于IoT设备资源受限，开发人员往往会在安全和性能之间折衷，有意或者无意的造成密码学误用。

在这篇文章中，作者设计了一个密码学误用分析框架，可以对IoT设备固件进行密码学误用识别。框架会将不同架构的二进制代码转化为通用的中间表示并进行静态污点分析。对于自定义的密码学函数，框架会在污点分析的过程中动态识别和更新函数列表并追踪函数参数。

作者实现了框架原型CRYPTOREX，并对不同厂商不同架构的521个IoT固件镜像进行了实验测试。实验的结果中CRYPTOREX成功的发现了679个密码学误用，平均每个固件的分析时间为1120秒。
Introduction

IoT设备一般装有多种传感器，并且会连接网络，所以比一般的嵌入式设备更容易导致安全问题，比如泄露用户隐私数据。 之前针对IoT设备漏洞识别的研究主要针对内存破坏、认证绕过等等传统漏洞，但是目前还没有工具能自动识别IoT设备中的密码学误用漏洞，也没有针对IoT设备密码学误用的大规模安全分析。 现有的针对密码学误用的研究一般是针对Android和IOS设备，但是IoT应用会根据设备不同的CPU架构编译成不同的机器码，所以这些研究并不适用。 另外，之前的研究依赖于特定的密码库，并没有考虑到开发者自定义的密码函数。即使密码库的实现再严谨再安全，如果开发者进行了错误的封装，也会造成密码学误用。

作者的创新点主要有以下几点： 1. 将不同架构的固件二进制代码转化为通用的中间表示 2. 考虑了开发者封装的密码库函数，在分析过程中动态更新crypto API列表，提高了识别的精度。
Background
IoT固件分析方法

针对IoT固件的安全分析，一般分为动态和静态两种。 动态分析 优点：精度高 缺点：debug接口可能被禁用，模拟执行时缺失NVRAM

静态分析 优点：不依赖于模拟执行 缺点：不同架构有不同的调用约定和栈布局
密码学误用

    Rule 1. Do not use ECB mode for encryption.
        对相同的数据块加密产生相同的结果，不可抵抗选择明文攻击
    Rule 2. Do not use a non-random IV for CBC encryption
        对相同的数据加密产生相同的结果，安全性略高于ECB，但仍不足以提供安全保证
    Rule 3. Do not use constant encryption key.
        攻击者可以直接解密数据
    Rule 4. Do not use constant salts for password-based encryption(PBE)
        PBE是指基于口令的加密，加盐散列，多轮迭代后生成密钥
    Rule 5. Do not use fewer than 1000 iterations for PBE
        可能会被暴力破解
    Rule 6. Do not use static seeds for random number generation functions.
        种子固定，随机数可预测

Intermediate Representation

作者的分析主要针对函数参数，旨在分析参数的类型(常量or变量),选择的中间表示是VEXIR。VEXIR支持静态数据流分析，对于不同架构的二进制文件，以统一的格式表示寄存器和内存位置。 #### static program slicing VEXIR会将二进制代码转化为单入口多出口的IRSB(IR Super-Block)，可以利用IRSB构建CFG和DFG。 #### Base operations 反汇编后，一条汇编代码会被转化为VEX的多条语句，例如 <div class=’bogus-wrapper’>
<div class=”highlight”><table><tr><td class=”gutter”><pre class=”line-numbers”>1 2 3 4 5 6 7 </pre></td><td class=’code’><pre>subs R2, R2, #8 t0 = GET:I32(16) t1 = 0x8:I32 t3 = Sub32(t0,t1) PUT(16) = t3 PUT(68) = 0x59FC8:I32</pre></td></tr></table></div>
</div> VEX会将所有的操作分类成四种基本语句

Implementation

CRYPTOREX的分析过程分成以下五个步骤： 1. Firmware Acquisition and Pre-processing 2. Lifting to VEX IR 3. Inter-procedural Control Flow Graph Construction 4. Cross-file Call Graph Construction 5. Taint Analysis
Firmware Acquisition and Pre-processing

利用爬虫从不同厂商的网站上爬取IoT设备固件。利用Binwalk解压爬取的固件，识别文件系统并且提取二进制文件。
Lifting to VEX IR

作者从libcrypto, libcrypt, cryptlib, LibTomCrypt, libgcrypt, wolfcrypt, Nettle七个密码库中提取crypto API，利用Buildroot对可执行文件头进行分析，过滤没有调用crypto API的二进制文件，从而降低了二进制文件转化到IR的开销。

作者直接利用Angr进行VEX IR的转化，但是遇到了以下问题： 1. Angr只考虑了显式调用，如果调用函数的地址是在内存或者寄存器上，Angr无法识别，所以Angr得到的调用关系不完整 2. 变量的类型信息丢失，会影响到数据流追踪 3. 函数传参一般通过寄存器、栈或者两者皆用。将二进制转化到IR时，某些特定架构的调用约定会丢失。

为了解决上述问题，作者开发了IDA脚本，用来 1)恢复寄存器或者内存中的跳转地址，2)推断并保存数据的类型信息以及数据段引用表，3）预先提取不同架构的传参规则，实验过程中根据不同的架构使用对应的传参规则。
Inter-procedural Control Flow Graph Construction

从每个可执行文件的入口点，深度优先遍历函数和基本块，从而构建ICFG。另外作者也考虑了从入口点不可达的函数的调用关系，因为这些函数可能被其他可执行文件当作动态库里的函数调用。 对于隐式调用或者跳转，作者利用之前保存的数据段引用表来确定跳转地址；或者是模拟执行跳转之前的指令计算跳转地址。
Cross-file Call Graph Construction

考虑到开发者会对crypto API进行封装，作者进一步生成了跨文件的函数调用图，从而可以更准确的追踪函数参数的传递。 以低级的crypto API为起点，递归的将其调用者加到调用链上。这里是作者之前提到的动态更新crypto API

-w480
Taint Analysis

由于作者制定的密码学误用规则比较简单，所以最后的污点分析也比较简单。 作者制定的规则可以分为三类，第一类是使用ECB模式，直接检查二进制文件中是否调用了ECB相关的函数就可以确定；第二类是PBE的迭代次数小于1000；第三类是固定的种子或者字符串。 作者使用了后向追踪(backward tracking)的静态污点分析。先确定crypto API中可能被误用的参数，将其标记为污点源，再从它的调用者中寻找参数的来源，递归此过程直到找到一个常量或者指向常量的指针，就可以确定一个密码学误用。 利用Angr的use-define chain算法生成数据依赖。
Evaluation

### Experiment Setup 作者从网上爬取了12个不同厂商的1327个固件，成功解压了其中的521个，共有7种不同的架构。 -w537 此外，作者从7个不同的密码库中提取了165个crypto API，并对这些API中的190个参数进行了追踪。 -w531 ### Findings CRYPTOREX从126个有漏洞的固件中发现了679个密码学误用，涉及8个厂商。详细的结果如下图所示。 -w1098 作者发现，使用ECB加密这一密码学误用出现的次数最多，其次是固定密钥和固定盐值，再次是固定IV和小迭代次数。另外，作者没有发现关于固定随机数种子的密码学误用，进一步研究发现随机数的种子都是从/dev/urandom或者/dev/random获取(?). -w513 ### Accuracy #### False positives 作者随机选取了30个样本进行了手动分析，确认了其中的29个固件的密码学误用，准确率96.7%。误报的一个样例如下： -w530 -w538
False negatives

作者随机选取了10个CRYPTOREX未检测出密码学误用的固件进行了手动分析，没有发现漏报。 ### Performance 作者用171个小时完成了对1327个固件的分析，平均一个固件用时1120秒(对于521个成功解压的固件)。 为了分析哪些因素对性能有重要影响，作者选择了14个样本统计了以下数据。作者观察到提取IR花费了大量的时间。另外，被分析的固件大小越大，构造ICFG的时间越长。而ICFG的复杂度越高，路径分支越多，污点分析的时间就会越长。 另外，作者说由于这是关于IoT设备密码学误用分析的首次工作，所以不宜与移动平台上类似的工作进行横向对比。 
