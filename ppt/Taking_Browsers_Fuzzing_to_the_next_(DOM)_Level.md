    [review]

## 1 技术简介

### DOM level 1

The common approach in browser fuzzing leverages on DOM Level 1
interfaces for performing DOM mutations
    1. random HTML elements are created and randomly added to the HTML document tree
    2. the DOM tree is crawled and elements references are collected
    3. elements attributes and function calls are tweaked
    4. random DOM nodes are deleted
    5. garbage collection is forced
    6. the collected references are crawled and tweaked again
• Effective but some limitations:
    – every DOM mutation is performed on a single HTML element, no mass mutations
    – quite static: execution flow can only be altered by the number and the type of randomly
generated DOM nodes (e.g different tag names, attributes, etc)

指的就是最常规的随便生成dom元素的fuzz

### DOM level 2

给dom元素加点逻辑吧

### DOM level 3

再用上dom事件又如何？

## 2 亮点
## 3 局限性
## 4 技术展望
## 5 todo
