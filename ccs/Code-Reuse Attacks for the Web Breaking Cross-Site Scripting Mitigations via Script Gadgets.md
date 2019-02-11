大意是用一些库里面的代码片段 组合起来构成一个xss攻击向量

3.4 Attack Outline

攻击者模型：很典型的攻击者，可以在网页中插入任意的HTML代码

这里攻击者并没有直接插入代码，而是利用插入的HTML元素调用了库中的代码

这里把gadgets分为几个类型

- String manipulation gadgets 这种gadgets可以变换字符串

比如

``inner-h-t-m-l`` 通过 ``dash.replace(/-[a-z]/g, (m) => m[1].toUpperCase())}
`` 就变成了 ``innerHTML``

比如Angular里面就有一个这样的gadget

```
var PREFIX_REGEXP = /^((?:x|data)[:\-_])/i;
var SPECIAL_CHARS_REGEXP = /[:\-_]+(.)/g;
function directiveNormalize(name) {
return name.replace(PREFIX_REGEXP, ..)
.replace(SPECIAL_CHARS_REGEXP, fnCamelCaseReplace);
}
```

- Element construction gadgets 可以创建元素的gadgets

比如

```
document.createElement(input)
document.createElement(.script.)
jQuery(.<. + tag + .>.)
jQuery.html(input) // if input contains <script>
```

- Function creation gadgets 可以创建函数的gadgets


```
// Knockout Function creation gadget.
var body = .with($context){with($data||{}){return{. +
rewrittenBindings + .}}}.;
return new Function(.$context., .$element., body);
// Underscore.js Function creation gadget.
source = .var __t,__p=..,__j=Array.prototype.join,. +
.print=function(){__p+=__j.call(arguments,..);};\n. +
source + .return __p;\n.;
var render = new Function(
settings.variable || .obj., ._., source);
```

- JavaScript execution sink gadgets 可以执行js的gadgets，通常是最后一步

```
eval(input);
inputFunction.apply();
node.innerHTML = .prefix. + input + .suffix.;
jQuery.html(input);
scriptElement.src = input;
node.appendChild(input);
```

- Gadgets in expression parsers 一些现代的js框架把html作为语言的一部分，会parse html中一些特别的地方，并转换为js执行
