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

## Leaky-pipe circuit topology

## Congestion control

## Directory servers

## Variable exit policies

## End-to-end integrity checking

## Rendezvous points and hidden services

# Related Work

# 3. Design goals and assumptions

## Goal

### Deployability

### Usability

### Flexibility

### Simple design

## Non-goals

### Not peer-to-peer

### Not secure against end-to-end attacks

### No protocol normalization

### Not steganographic

## 3.1 Threat Model

# 4. The Tor Design

## 4.1 Cells

## 4.2 Circuits and streams

### Constructing a circuit

### Relay cells

## 4.3 Opening and closing streams

## 4.4 Integrity checking on streams

## 4.5 Rate limiting and fairness

## 4.6 Congestion control

### Circuit-level throttling

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

## 6.2 Exit policies and abuse

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
