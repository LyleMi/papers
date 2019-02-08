# We Still Don't Have Secure Cross-Domain Requests: an Empirical Study of CORS

## Abstract

这篇文章发现了CORS (cross-origin resource sharing) 的一些安全上的问题

1. CORS一定程度上放宽松了跨域的写权限
2. CORS给Web交互带来了新的信任风险
3. 因为其复杂性，很多开发者对其没有充分的理解，造成了错误的配置

最后，提出了一个解决方案

## Introduction

SOP(Same Origin Policy) 同源策略保护了网站的安全，但是也带来了不便。
JSON-P这个机制来解决这个问题，但是也有一些安全问题，然后又引入了CORS

被发现的问题可以分为三类

1) CORS策略给出了过多的权限
    - 让本来没得搞的CSRF有得搞
2) CORS本身的风险
    - 信任了三方网站，可以中间人
3) 过于复杂的CORS和大量的误配置

这篇文章为了有说服力 
研究了Aleax Top 前5w的 Web站点
包括其97199966个子站点

## Background

跨域资源可以分为两类：
- 本地跨域
    - DOM
    - Cookie
- 网络跨域
    - Ajax

### 2.1 Cross-Origin Network Access


## 3 Overview of CORS Security Analysis

### 3.1 Threat Model

考虑两类攻击
- Web攻击者
- Active Network 攻击者

### 3.2 Methodology

往网站发跨域请求

### 3.3 Summary of Analysis Results

1) Incomplete Reference Monitor



2) Trust Dependency

相信比较安全性比较差的域名

3) Policy Complexity


## 4. Overly Permissive Sending Permission

### 4.1 Crafting Request Headers

在CORS之前，跨域请求只能用Header，而且值被浏览器所限制
但是JavaScript+CORS则有比较丰富的语义

在RFC中规定了这种限制，但是浏览器中只有Safari实现了

浏览器也限制了CORS ``Content-Type`` 的值为 (``text/plain``, ``multipart/form-data``, ``application/x-form-url-encoded``) 但是可以bypass

另外CORS也只是实现了少部分的限制在header size上

### 4.2 Crafting Request Bodies

没有限制body format
