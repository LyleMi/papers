# III. PERSISTENT CLIENT-SIDE XSS

## C. Persisting Malicious Payloads

### 1) Network Attacker

控制网络 改http response

### 2) Web Attacker

访问攻击者的网页
要有xss 或者控cookie的csrf这类

后面混淆概念了 给了能控cookie的前提条件

果然 后面说没法搞

```
For the Web Attacker, we first check for flows from a URL
to a storage entry, where that storage entry is later used in an
unfiltered flow to a sink. However, out of the 20 domains for
which we discovered such a flow, none could be exploited, for
three reasons. First, flows originated from GET parameters in
the URL, which when changed led to a 404 page. Second, only
the host part of the URL was used to set the domain property
of a cookie, meaning that we were unable to overwrite the
cookie’s value. Third, data from the URL was sanitized (e.g.,
the HTML brackets), rendering our payload non-functional.
To determine the number of persistable XSS flaws, we
follow the methods outlined by prior works 
```

那这篇没什么价值啊
