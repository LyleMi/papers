title: Smart Greybox Fuzzing
authors: Van-Thuan Pham

# Abstract

基于当前的
Coverage-based Greybox Fuzzing (CGF) 
文章提出
Smart Greybox Fuzzing (SGF) 

引入了
novel validity-based power schedule

效果
more branch coverage (up to 87% improvement) 

结果
42 zero-day vulnerabilities in widely-used, well-tested tools and libraries; 22 CVEs were assigned

# Introduction

## Contributions

- make greybox fuzzing input format-aware

# 2. MOTIVATING EXAMPLE

## 2.3 Difficulties of Traditional Greybox Fuzzing

# 3. SMART GREYBOX FUZZING

## 3.1 Virtual Structure

文章引入了一个 Virtual Structure 模型

每个输入都可以被解析为多个chunk
每个chunk的结构如下

```c
struct chunk {
  unsigned long
      id; /* The id of the chunk, which either equals its pointer value or, when
             loaded from chunks file, equals to the hashcode of its chunk
             identifer string casted to unsigned long. */
  int type;                /* The hashcode of the chunk type. */
  int start_byte;          /* The start byte, negative if unknown. */
  int end_byte;            /* The last byte, negative if unknown. */
  char modifiable;         /* The modifiable flag. */
  struct chunk *next;      /* The next sibling child. */
  struct chunk *children;  /* The children chunks linked list. */
};
```

## 3.2 Smart Mutation Operators

*Smart Deletion*

*Smart Addition*

*Smart Splicing*

*Maintaining structural integrity*

一个关键的挑战是怎么保证bit-level的变异不会影响结构的完整性。

本文提供了一些用于设置的属性。

*Maintaining semantic integrity*

另一个挑战是如何保证语义级别的完整性。

主要是checksum等内容。

但是这个问题至今没有较为合适的解决方案

## 3.3 Region-based Smart Mutation

### 3.3.1 Stacking Mutations

对于字节级别的变异，只要知道起始位置就可以任意方式去变异。

但是对于结构敏感的变异，增删chunk后，其它所有相关chunk的关系都改变了。

### 3.3.2 Fragment- and Region-based Mutation

### 3.3.3 Deferred Parsing

# 5. EXPERIMENTAL SETUP

## 5.1 Research Questions

RQ-1. Is smart greybox fuzzing more effective and efficient than traditional greybox fuzzing? 

RQ-2. Is smart greybox fuzzing more effective and efficient than smart blackbox fuzzing? 

Q-3. Does mutation stacking contribute to the effectiveness of smart greybox fuzzing? 

RQ-4. Is smart greybox fuzzing more effective than taint analysis-based greybox fuzzing? 
