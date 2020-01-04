# Abstract

Tor: 基于回路的低延时匿名通信服务。

第二代 洋葱服务 增加了：

- 转发秘密性
- 拥塞控制
- 目录服务器
- 完整性检查
- 可配置的退出策略
- 基于汇聚点的本地隐藏

基本不需要特权 不需要修改内核
节点间只需要少量的同步
在匿名性、可靠性、效率间做了有理由的权衡

# Overview

洋葱路由是一个基于TCP的隐蔽信道

Clients选择一个路径构成回路 每个node都被称为Circuit
每个节点知道自己的前驱和后继 但是不知道除此之外的其他节点

## Perfect forward secrecy

传输节点存了也不能重放

## Separation of “protocol cleaning” from anonymity

用socks5代理 实现协议无关性

## No mixing, padding, or traffic shaping 

## Many TCP streams can share one circuit

一个电路可以多个TCP复用

## Leaky-pipe circuit topology

可以从中间任何一个位置跳出去
不会因为出口节点炸了就炸了
或者因为出口节点被监听而不安全

## Congestion control

早期的tor基本只用了路由设备本身的拥塞控制
在后来的版本中开始做软件层面的拥塞控制

## Directory servers

开始tor考虑把路由用洪泛的方式发出去
后来觉得不太Ok 引入了目录服务器
用户周期性的从目录服务器取信息

## Variable exit policies

可变的退出节点

## End-to-end integrity checking

端到端的完整性检查

## Rendezvous points and hidden services

// 没太看懂这段

# 2. Related Work

*Mix-Net* 公钥密码学 每轮之间有包顺序的变换

有两类匿名网络 一类是 Babel Mix-Master Mixminion 最大化匿名程度 但是引入了延时 不能适应高交互的应用 如浏览网页、聊天、SSH

tor是另一类 低延迟 可以处理一些双向交互

最简单的匿名服务是像 Anonymizer 只有一跳的代理

Java Anon Proxy 做了一些改进 但是仍然只有一跳 存在很多局限性

PipeNet 实现了一个和tor差不多的东西 但是可以被单用户打掉
ISDN mixes

一些p2p的实现 tarzan morphmix

hordes 基于大众来做 但是用了多播
Hebivore和p5 也依赖于广播

基于电路的做法最好改一下tcp报文 把源地址目的地址改掉

分布式的系统要防止攻击者瞎加节点
Tor是基于少数有名的dir节点

# 3. Design goals and assumptions

## Goal

### Deployability

易部署

### Usability

易用

### Flexibility

灵活

### Simple design

设计简单

## Non-goals

### Not peer-to-peer

非P2P的设计

### Not secure against end-to-end attacks

端到端的是防不住的

### No protocol normalization

不会改协议特征

### Not steganographic

不会隐瞒谁进入了网络

## 3.1 Threat Model

在分析匿名网络的时候 一般会假设有一个老大哥
不过Tor并不在有一个很强的敌手的时候提供保护
这里假设敌手可以 观察部分网络流量 可以生成/修改/删除/延迟 网络流量
可以搞一些tor节点 而且会改这些节点 而且可以渗透掉一些节点

tor预计搞一些东西 来防止网络流量被分析

# 4. The Tor Design

tor是一层层的
每个用户都在用户层搞一个
每一个onion的路由都有一个长期的身份验证用key 和一个短期的 洋葱key
身份验证key 是用来签名tls  签名路由的描述 （key / 地址 / 带宽 / 退出策略）
短期key用来解密消息

## 4.1 Cells

控制命令

- padding
- create / create
- destroy

relay 命令

- relay date
- relay begin
- relay end
- relay teardown
- relay connected
- relay extend
- relay extended
- relay truncate
- relay truncated
- relay sendme
- relay drop

结构

```
| 2      | 1     | 509                                  |
| CircID | CMD   | DATA                                 |

| 2      | 1     | 2        | 6      | 2   | 1   | 498  |
| CircID | Relay | StreamId | Digest | Len | CMD | DATA |
```

## 4.2 Circuits and streams

初版本的tor给每一个TCP链接都建立stream
后来觉得这样不太现实 建立链路的成本太高了

```
Alice -> Create c1, E(g^x1)              -> OR1
OR1   -> Create c1, g^y1, H(K1)          -> Alice
Alice -> Relay c1{Extend, OR2, E(g^x2)}  -> OR1
OR1   -> Create c2, E(g^x2)              -> OR2
OR2   -> Create c2, g^y2, H(K2)          -> OR1
OR1   -> Relay c1{Extended, g^y2, H(K2)} -> Alice
Alice -> Relay c1{Begin <website:80>}    -> OR1
OR1   -> Relay c2{Begin <website:80>}    -> OR2
OR2   -> (TCP handshake)                 -> Site
Site  -> (TCP handshake)                 -> OR2
OR2   -> Relay c2{Connected}             -> OR1
OR1   -> Relay c1{Connected}             -> Alice
Alice -> Relay c1{{Data, "HTTP GET"}}    -> OR1
OR1   -> Relay c2{Data, "HTTP GET"}      -> OR2
OR2   -> Relay "HTTP GET"                -> Site
Site  -> (response)                      -> OR2
OR2   -> Relay c2{Data, (response)}      -> OR1
OR1   -> Relay c1{{Data, (response)}}    -> Alice
...
```

### Constructing a circuit


### Relay cells

建立好电路后 开始发relay cell
收到一个cell后 把包给拆了

## 4.3 Opening and closing streams

要开始传的时候 用OP开始
要考虑的一点是开始的DNS
DNS是走UDP的 强迫走TCP不好实现
所以这里最好用隐私敏感的代理
如果中间有环节断了 就断掉整个链路

## 4.4 Integrity checking on streams

没有完整性检查的一个问题是
攻击者可以瞎改
比如改了让FTP的dir命令变成rm *

## 4.5 Rate limiting and fairness

考虑参与Tor的节点都是志愿者 要考虑到带宽本身的使用
tor用了一个token bucket方法
来保证长时间的带宽占比 但是也让短期内能有一个比较高的带宽使用

## 4.6 Congestion control

这里考虑拥塞主要是考虑有可能有瞎打的
比如攻击者想办法找一个重叠的OR-OR链路 然后开始打大流量

### Circuit-level throttling

做电路的流量控制，每个OR追踪两个窗口

- packaging window
    - 允许发多少packaging
- delivery window
    - 发送了多少packaging

### Stream-level throttling

流级别的和链路级别的也类似

# 5. Rendezvous Points and hidden services

Rendezvous 点是为了建立隐藏的网络。

设计要考虑到:

- Access-control
- Robustness
- Smear-resistance
- Application-transparency

## 5.1 Rendezvous points in Tor

## 5.2 Integration with user applications

## 5.3 Previous rendezvous work

# 6. Other design decisions

## 6.1 Denial of service

服务器挂在那 被人发起请求走TLS会很亏
这里考虑可能要让client 做工作量证明

## 6.2 Exit policies and abuse

出口节点可能被攻击者用来搞事

## 6.3 Directory Servers

# 7. Attacks and Defenses

## Passive attacks

- Observing user traffic patterns
    - 流量加密 但是输入输出可以被观测
- Observing user content
    - 大部分节点都是加密的
    - 但是最后一层返回是不加密的
- Option distinguishability
    - 提供了一些隐蔽性 速度相关的配置
    - 因而带来问题
- End-to-end timing correlation
    - 要是有一个老大哥 能看到所有流量
    - 可以通过时间猜
- End-to-end size correlation
    - 要是有一个老大哥 能看到所有流量
    - 可以通过大小猜
- Website fingerprinting

## Active attacks

- Compromise keys
    - 密钥泄漏等情况
- Iterated compromise
- Run a recipient
- Run an onion proxy
- DoS non-observed nodes
- Run a hostile OR
- Introduce timing into messages
- Tagging attacks
- Replace contents of unauthenticated protocols
- Replay attacks
- Smear attacks
- Distribute hostile code

## Directory attacks

- Destroy directory servers
- Subvert a directory server
- Subvert a majority of directory servers
- Encourage directory server dissent
- Trick the directory servers into listing a hostile OR
- Convince the directories that a malfunctioning OR is working

## Attacks against rendezvous points

- Make many introduction requests
- Attack an introduction point
- Compromise an introduction point
- Compromise a rendezvous point

# 8. Early experiences: Tor in the Wild

# 9. Open Questions in Low-latency Anonymity

# 10. Future Directions

- Scalability
- Bandwidth classes
- Incentives
- Cover traffic
- Caching at exit nodes
- Better directory distribution
- Further specification review
- Multisystem interoperability
- Wider-scale deployment
