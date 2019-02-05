[Review]GramFuzz Fuzzing Testing of Web Browsers Based on Grammar Analysis and Structural Mutation

## 1 技术简介

### 1.1 主流程伪代码

```python
webFiles = Crawler.getHTMLfromInternet()
trainSets = new TrainSets(webFiles)
initCases = new InitialCases(webFiles, Pocs)
grammarLibrary = {JsLib, HTMLLib, CSSLib} = new GrammarLibrary(trainSets)
grammarNode = new GrammarNode(grammarLibrary)
testCases = new Testcases(grammarNode, mutatePattern(initCases))
```

### 1.2 Extract the Grammar Node 伪代码

```python
currentNode = rootNode
grammarNodeDB = []

def searchLeafNode(n):
    tmp = new Node()
    tmp.code = n.code
    tmp.type = n.type
    grammarNodeDB.push(tmp)


def searchChildNode(n):
    searchLeafNode(n)
    tmp = n.nextLeafNode()
    while tmp is not None:
        searchLeafNode(tmp)
        tmp = n.nextLeafNode()

def main(rootNode):
    searchChildNode(rootNode)
```

### 1.3 样例生成

这里样例生成有几个注意的点

- 选择较小的初始样例，使得crash更容易分析，程序也运转得更快
- 初始样例最好有比较多的Js和css文件，js的func call和css的结构最好比较复杂

在选择好初始样例之后，使用下面的方式来改变

- 用一个随机的节点类型来替代当前的节点类型
- 把当前的节点复制到其他的一个随机位置
- 删除当前节点
- 改变当前节点的内容
- 不改变当前节点

## 2 亮点

其他的fuzz方式无视语法和代码结构，只使用了一些简单的mutation策略。

测试者不需要对DOM树，CSS，或者Js语法有了解，只要使用代码库就可以了
从真实HTML文件中的代码会对接口有更高的覆盖率
生成测试样例使用了语法树的方法，给测试例子触发漏洞以更多的可能性

## 3 局限性
## 4 技术展望
## 5 todo

fuzz technologies

    generation [9-12]
        jsfunfuzz[13]
    mutation [13-14]
        Langfuzz[15]
