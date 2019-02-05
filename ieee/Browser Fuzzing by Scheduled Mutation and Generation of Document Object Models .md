[Review]Browser Fuzzing by Scheduled Mutation and Generation of Document Object Models

Author: Ying-Dar Lin Feng-Ze Liao Shih-Kun Huang Yuan-Cheng Lai
 Dept of Computer Science, National Chiao Tung University, Taiwan
 Dept. of Information Management, National Taiwan University of Science and Technology, Taiwan

## 1 技术简介

文章提出了一个命名为scheduled DOM fuzzing (SDF)的fuzz方法，由一些有联系的浏览器fuzz工具和一个名为BFF的fuzz框架结合而来。
文中对浏览器fuzz架构进行了优化，然后对种子生成做了目标化，也会动态的改变。
文中也提出了一种计算方式，计算哪种结合可以提供更多的crash。
最后实验证明，文章提出的方法展示SDF大概比其他的方法有效2.27倍。

### 1.1 符号表

S => seed的集合
Mut => mutation的集合
Input => 输入的集合，(seed, mutation)对
PS => seed及其概率的和
PM => mutation及其概率的和
t => 给定的fuzz时间
tout => 给定的超时时间
b => 执行fuzz结果的浏览器
CRS => 执行结果

### 1.2 伪代码

```

def alg():
    S = generateSeed()
    Mut = generateMutation()
    label_1:
    Schedule(S)
    s_n = select(PS)
    Schedule(Mut)
    mut_n = select(PM)
    label2:
    B.execute(s_n, mut_n)
    if B.crash:
        update(PS, PM, CRS)
        if not Run(SDF, t):
            goto lable_1
    else:
        if Run(b, t_out):
            update(PS, PM, CRS)
        else:
            goto label_2
```

### 1.3 流程

在安排种子的过程中，计算了seed和mutation的选择概率，这里认为遇到crash多的seed/mutation的优先级比较高

## 2 亮点

算法的主要优点在于动态的计算了seed，mutation的选择概率，使用更大概率的种子来生成样例

## 3 局限性
## 4 技术展望

这种其实就是反馈的方式？
那么能不能进一步？
做机器学习?

## 5 todo

[1-3] nothing

[4-5] introduce fuzz

white-box fuzz

    CRAXfuzz[7]
    Coverset[8]

black-box fuzz

    zzuf[9]
    BFF[10]
    FOE[11]
    fuzzSim[12]
    SDF

only target browser
    
    bf3[14]
    crossfuzz[15]
    ndujafuzz[16]

browser fuzz [19]
    static 
    dynamic
