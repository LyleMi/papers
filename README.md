# Papers

Recently read academic papers, articles on Web Security/Fuzzing, etc., and some reading notes written by myself or excerpted from other sources.

## Table of Contents

- [Recommend Conferences](#recommend-conferences)
- [ACM](#acm)
- [ACM CCS](#acm-ccs)
- [ACSAC](#acsac)
- [ASE](#ase)
- [Arxiv](#arxiv)
- [AsiaCCS](#asiaccs)
- [Black Hat](#black-hat)
- [Black Hat Asia](#black-hat-asia)
- [Black Hat EU](#black-hat-eu)
- [Black Hat USA](#black-hat-usa)
- [Black Hat WorkShop](#black-hat-workshop)
- [Blog](#blog)
- [CCS](#ccs)
- [DSN](#dsn)
- [Defcon](#defcon)
- [ESEC/FSE](#esecfse)
- [FSE](#fse)
- [H2HC](#h2hc)
- [HITB](#hitb)
- [ICSE](#icse)
- [ICST](#icst)
- [IEEE](#ieee)
- [IEEE S&P](#ieee-sp)
- [IEEE-ACM](#ieee-acm)
- [IJCAI](#ijcai)
- [ISCA](#isca)
- [ISSTA](#issta)
- [MS](#ms)
- [Misc](#misc)
- [NDSS](#ndss)
- [OOPSLA](#oopsla)
- [Offensive](#offensive)
- [OffensiveCon](#offensivecon)
- [PLDI](#pldi)
- [PPT](#ppt)
- [QPSS](#qpss)
- [RAID](#raid)
- [SIGMOD](#sigmod)
- [SIGPLAN](#sigplan)
- [Secwest](#secwest)
- [TSE](#tse)
- [USENIX ATC](#usenix-atc)
- [Usenix](#usenix)
- [WOOT](#woot)
- [Whitepaper](#whitepaper)

# Recommend Conferences

| Conference | Full Name | dblp Link |
| ----- | ----- | ----- |
| CCS | ACM Conference on Computer and Communications Security | https://dblp.uni-trier.de/db/conf/uss/ |
| Usenix | USENIX Security Symposium | https://dblp.uni-trier.de/db/conf/ccs/ |
| S&P | IEEE Symposium on Security and Privacy | https://dblp.uni-trier.de/db/conf/sp/ |
| NDSS | ISOC Network and Distributed System Security Symposium | https://dblp.uni-trier.de/db/conf/ndss/ |

## ACM

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Using Logic Programming to Recover C++ Classes and Methods from Compiled Executables | Schwartz |  | 2018 | Decompile |
| Automatic exploit generation |  |  |  | Fuzz |
| Predicting vulnerable software components |  |  |  | Fuzz |
| Scheduling Black-box Mutational Fuzzing |  |  |  | Fuzz |
| Symbolic execution for software testing three decades later |  |  |  | Fuzz |
| evaluating fuzz testing |  |  |  | Fuzz |

## ACM CCS

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Alert Alchemy: SOC Workflows and Decisions in the Management of NIDS Rules | Mathew Vermeer | Technische Universiteit Delft | 2023 | NIDS |
| Black Ostrich: Web Application Scanning with String Solvers | Benjamin Eriksson | Chalmers Tekniska Högskola | 2023 | Web;Spider |
| Don't Leak Your Keys: Understanding, Measuring, and Exploiting the AppSecret Leaks in Mini-Programs | Yue Zhang | The Ohio State University | 2023 | Mini-Program;Secret Leak |
| Finding All Cross-Site Needles in the DOM Stack: A Comprehensive Methodology for the Automatic XS-Leak Detection in Web Browsers | Dominik Trevor Noß | Ruhr-Universität Bochum | 2023 | DOM |
| Lost along the Way: Understanding and Mitigating Path-Misresolution Threats to Container Isolation | Zhi Li | Huazhong University of Science and Technology | 2023 | Container Isolation |
| PyRTFuzz: Detecting Bugs in Python Runtimes via Two-Level Collaborative Fuzzing | Wen Li | Washington State University | 2023 | Fuzz;Python |
| Silence is not Golden: Disrupting the Load Balancing of Authoritative DNS Servers | Fenglu Zhang | Tsinghua University | 2023 | DNS |
| TsuKing: Coordinating DNS Resolvers and Queries into Potent DoS Amplifiers | Wei Xu | Wei Xu | 2023 | Tsinghua University |
| Understanding and Detecting Abused Image Hosting Modules as Malicious Services | Geng Hong | Fudan University, Shanghai, China | 2023 | Abuse |
| Whole-Program Control-Flow Path Attestation | Nikita Yadav | Indian Institute of Science | 2023 | Control-Flow |

## ACSAC

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Opening Pandora's Box through ATFuzzer: Dynamic Analysis of AT Interface for Android Smartphones | Imtiaz Karim | Purdue University | 2019 | Fuzz |

## ASE

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| BigFuzz: Efficient Fuzz Testing for Data Analytics using Framework Abstraction | Qian Zhang | University of California, Los Angeles | 2020 | Fuzz |
| Learning-Guided Network Fuzzing for Testing Cyber-Physical System Defences | Yuqi Chen | Singapore University of Technology and Design, Singapore | 2019 | Fuzz |
| FairFuzz: A Targeted Mutation Strategy for Increasing Greybox Fuzz Testing Coverage | Caroline Lemieux | University of California, Berkeley, USA | 2018 | Fuzz;AFL |

## Arxiv

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Building Fast Fuzzers | Rahul Gopinath and Andreas Zeller | CISPA | 2019 | Fuzz |
| Improving Grey-Box Fuzzing by Modeling Program Behavior |  |  | 2019 | Fuzz |
| Adaptive Grey-Box Fuzz-Testing with Thompson Sampling |  |  |  | Fuzz |
| Attention Is All You Need |  |  |  | Fuzz |
| Deep Reinforcement Fuzzing |  |  |  | Fuzz |
| FuzzerGym A Competitive Framework for Fuzzing |  |  |  | Fuzz |
| Fuzzing Art, Science and Engineering |  |  |  | Fuzz |
| Leveraging Textual Specifications for Grammar-based Fuzzing of Network Protocols |  |  |  | Fuzz |
| NEUZZ Efficient Fuzzing with Neural Program Learning |  |  |  | Fuzz |
| NEUZZ Efficient Fuzzing with Neural Program Smoothing |  |  |  | Fuzz |
| Not all bytes are equal  Neural byte sieve for fuzzing |  |  |  | Fuzz |
| TensorFuzz Debugging Neural Networks with Coverage-GUided Fuzzing |  |  |  | Fuzz |
| neural machine translation inspired binary code similarity comparison beyond function pairs |  |  |  | Fuzz |

## AsiaCCS

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| A Feature-Oriented Corpus for Understanding, Evaluating and Improving Fuzz Testing | Xiaogang Zhu | Swinburne University of Technology | 2019 | Fuzzing |
| PTrix Efficient Hardware-Assisted Fuzzing for COTS Binary | Yaohui Chen | Northeastern University | 2019 | Fuzz |
| Practical Side-Channel Attacks against WPA-TKIP | Domien Schepers |  | 2019 | Wi;Fi |
| ScriptProtect: Mitigating UnsafeThird-Party JavaScript Practices | Marius Musch | TU Braunschweig | 2019 | XSS |

## Black Hat

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| A New Class of DNS Vulnerabilities Affecting Many DNS-as-Service Platforms | Shir Tamari | Wiz.io | 2021 | DNS;Cloud |
| ALPACA: Application Layer Protocol Confusion - Analyzing and Mitigating Cracks in TLS Authentication | Marcus Brinkmann | Ruhr University Bochum | 2021 | TLS |
| Another Road Leads to the Host: From a Message to VM Escape on Nvidia vGPU | Wenxiang Qian | Tencent Blade Team | 2021 | VM Escape |
| Breaking the Isolation: Cross-Account AWS Vulnerabilities | Shir Tamari | Wiz.io | 2021 | AWS;Cloud |
| Bypassing Windows Hello for Business and Pleasure | Omer Tsarfati | CyberArk | 2021 | Windows;Auth |
| Do You Speak My Language? Make Static Analysis Engines Understand Each Other | Ibrahim Elsayed | Facebook | 2021 | Static Analysis |
| Let's Attack Let's Encrypt | Haya Shulman |  | 2021 | Crypto;CA |
| Mobius Band: Explore Hyper-V Attack Interface through Vulnerabilities Internals | Zhenhao Hong | Ant Group Light-Year Security Lab | 2021 | Hyper-V;Exploit |
| hAFL1: Our Journey of Fuzzing Hyper-V and Discovering a 0-Day | Peleg Hadar | SafeBreach Labs | 2021 | Fuzz;Virtual |
| 0-days & Mitigations: Roadways to Exploit and Secure Connected BMW Cars | Zhiqiang Cai | KeenLab | 2019 | Car |
| API-Induced SSRF: How Apple Pay Scattered Vulnerabilities Across the Web | Joshua Maddux | PKC Security | 2019 | Web;SSRF;API |
| All the 4G Modules Could be Hacked | Shupeng Gao | Baidu Security Lab | 2019 | 4G;IoT |
| Attack Surface as a Service | Anna Westelius | Arkose Labs | 2019 | PPT |
| Attacking And Defending The Microsoft Cloud | Sean Metcalf |  | 2019 | Web |
| Battle Of Windows Service A Silver Bullet To Discover File Privilege Escalation Bugs Automatically | Wenxu Wu (@Ma7h1as) | Xuanwu Lab of Tencent | 2019 | Windows;Fuzz;Logic |
| DevSecOps : What, Why and How | Anant Shrivastava | NotSoSecure | 2019 | DevSecOps |
| Dragonblood: Attacking the Dragonfly Handshake of WPA3 | Mathy Vanhoef | New York University Abu Dhabi | 2019 | Wifi |
| Exploiting Qualcomm WLAN and Modem Over The Air | Xiling Gong | Tencent Blade Team | 2019 | WLAN |
| HTTP Desync Attacks: Smashing into the Cell Next Door | James Kettle | PortSwigger Web Security | 2019 | Web |
| HostSplit: Exploitable Antipatterns in Unicode Normalization | Jonathan Birch | Microsoft | 2019 | IDN |
| I'm Unique, Just Like You: Human Side-Channels and Their Implications for Security and Privacy | Matt Wixey | PwC | 2019 | Social Engineering |
| Infiltrating Corporate Intranet Like NSA - Pre-auth RCE on Leading SSL VPNs | Orange Tsai | DEVCORE | 2019 | Web |
| Monsters in the Middleboxes: Building Tools for Detecting HTTPS Interception | Luke Valenta | Cloudflare | 2019 | Web |
| Munoz SSO Wars The Token Menace | Alvaro Munoz |  | 2019 | Web;Auth;SAML |
| Practical Approach to Automate the Discovery and Eradication of Open-Source Software Vulnerabilities at Scale | Aladdin Almubayed | Netflix | 2019 | Supply Chain |
| The Enemy Within: Modern Supply Chain Attacks | Eric Doerr | MSRC | 2019 | Supply Chain |
| WebAssembly A New World of Native Exploits On The Web |  |  | 2018 | WebAssembly |
| HEIST HTTP Encrypted Information Can Be Stolen Through TCP Windows |  |  | 2016 | HTTPS Side-Channel |
| Molinyawe Shell On Earth From Browser To System Compromise |  |  | 2016 | Fuzz |
| Unicorn: Next Generation CPU Emulator Framework | NGUYEN Anh Quynh  |  | 2015 | Emulator |
| the power of pair one template that reveals 100 plus uaf ie vulnerabilities |  |  | 2014 | Fuzz |
| Stone Pixel Perfect Timing Attacks with HTML5 |  |  | 2013 | WebSec |
| Dont Trust The DOM Bypassing XSS Mitigations Via Script Gadgets |  |  |  | Web |
| Exposing Hidden Exploitable Behaviors In Programming Languages Using Differential Fuzzing |  |  |  | Fuzz |
| It's A PHP Unserialization Vulnerability Jim But Not As We Know It |  |  |  |  |

## Black Hat Asia

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Dynamic Process Isolation | Pietro Borrello | Sapienza University of Rome | 2022 | Cloud;Spectre |
| Remote Memory-Deduplication Attacks | Erik Kraft | Graz University of Technology | 2022 | Cloud |

## Black Hat EU

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| HTTP/2: The Sequel is Always Worse | James Kettle | Director of Research, PortSwigger | 2021 | HTTP/2;smuggling |
| New Ways of IPV6 Scanning | Shupeng Gao | Senior Security Researcher, Baidu | 2021 | IPv6;scan |
| BlueMaster: Bypassing and Fixing Bluetooth-based Proximity Authentication | Youngman Jung | Samsung Electronics | 2019 | Bluetooth |
| Booting the iOS Kernel to an Interactive Bash Shell on QEMU | Jonathan Afek | HCL/AppScan | 2019 | iOS |
| Chain of Fools: An Exploration of Certificate Chain Validation Mishaps | James Barclay | Duo Security | 2019 | Cryptography |
| Far Sides of Java Remote Protocols | An Trinh | Viettel Cyber Security | 2019 | Java |
| Fatal Fury on ESP32: Time to Release Hardware Exploits |  |  | 2019 |  |
| Fuzzing and Exploiting Virtual Channels in Microsoft Remote Desktop Protocol for Fun and Profit | Chun Sung Park | Korea University | 2019 | Fuzz;RDP |
| Mobile Network Hacking, IP Edition | Karsten Nohl |  | 2019 | Mobile |
| New Exploit Technique In Java Deserialization Attack | Yongtao Wang | BCM Social Corp | 2019 | Java;Deserialization |
| Practical Side-Channel Attacks Against WPA-TKIP | Mathy Vanhoef | New York University Abu Dhabi | 2019 | WiFi |
| Reverse Engineering and Exploiting Builds in the Cloud | Etienne Stalmans | Salesforce Heroku | 2019 |  |
| Side Channel Attacks in 4G and 5G Cellular Networks | Syed Hussain | Purdue University | 2019 | Mobile;telecommunication |
| Site Isolation: Confining Untrustworthy Code in the Web Browser | Nasko Oskov | Google | 2019 | Browser;Web |
| Sneak into Your Room: Security Holes in the Integration and Management of Messaging Protocols on Commercial IoT Clouds | Yan Jia | NCNIPC | 2019 | IoT |

## Black Hat USA

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| A Journey Into Fuzzing WebAssembly Virtual Machines | Patrick Ventuzelo | FuzzingLabs | 2022 | Fuzz;WebAssembly |
| A New Trend for the Blue Team - Using a Practical Symbolic Engine to Detect Evasive Forms of Malware/Ransomware | Sheng-Hao Ma | TXOne | 2022 | symbolic execution;malware detection |
| Another Way to Talk with Browser: Exploiting Chrome at Network Layer | Rong Jian | 360 | 2022 | Chrome;WASM |
| Attacks From a New Front Door in 4G & 5G Mobile Networks | Altaf Shaik | Technische Universität Berlin | 2022 | IoT |
| Backdooring and Hijacking Azure AD Accounts by Abusing External Identities | Dirk-jan Mollema | Outsider Security | 2022 | Azure AD |
| Better Privacy Through Offense: How To Build a Privacy Red Team | Scott Tenaglia | Privacy Red Team, Meta | 2022 | Privacy |
| Blasting Event-Driven Cornucopia: WMI-based User-Space Attacks Blind SIEMs and EDRs | Claudiu Teodorescu |  | 2022 | WMI |
| BrokenMesh: New Attack Surfaces of Bluetooth Mesh | Han Yan | Baidu | 2022 | Bluetooth |
| Cautious: A New Exploitation Method! No Pipe but as Nasty as Dirty Pipe | Zhenpeng Lin | Northwestern University | 2022 | Linux;Privilege Escalation |
| Controlling the Source: Abusing Source Code Management Systems | Brett Hawkins | IBM | 2022 | Git |
| DNSSEC Downgrade Attacks | Haya Shulman | Fraunhofer SIT | 2022 | DNSSEC |
| Devils Are in the File Descriptors: It Is Time To Catch Them All | Le Wu | Baidu | 2022 | File Descriptors |
| DirectX: The New Hyper-V Attack Surface | Zhenhao Hong | Ant Group Light-Year Security Lab | 2022 | Hyper-V |
| Do Not Trust the ASA, Trojans! | Jacob Baines | Rapid7 | 2022 | Cisco |
| Don't Get Owned by Your Dependencies: How Firefox Uses In-process Sandboxing To Protect Itself From Exploitable Libraries (And You Can Too!) | Shravan Narayan | UC San Diego | 2022 | Firefox;Sandbox |
| ELF Section Docking: Revisiting Stageless Payload Delivery | Dimitry Snezhkov | IBM | 2022 | Malware |
| ElectroVolt: Pwning Popular Desktop Apps While Uncovering New Attack Surface on Electron | Aaditya Purani | Cure53 | 2022 | Electron |
| Elevating Kerberos to the Next Level | James Forshaw | Google Project Zero | 2022 | Kerberos |
| Google Reimagined a Phone. It was Our Job to Red Team and Secure it. | Farzan Karimi | Google | 2022 | Android |
| IAM The One Who Knocks | Igal Gofman | Ermetic | 2022 | IAM;Cloud |
| Is WebAssembly Really Safe? --Wasm VM Escape and RCE Vulnerabilities Have Been Found in New Way | Zhao Hai | Cyberpeace Tech Co., Ltd. | 2022 | WebAssembly |
| Kubernetes Privilege Escalation: Container Escape == Cluster Admin? | Yuval Avrahami | Palo Alto Network | 2022 | Kubernetes;Privilege Escalation |
| Let's Dance in the Cache - Destabilizing Hash Table on Microsoft IIS | Orange | DEVCORE | 2022 | IIS;Hash;Cache |
| New Memory Forensics Techniques to Defeat Device Monitoring Malware | Andrew Case |  | 2022 | Memory Forensics |
| PISE: Protocol Inference using Symbolic Execution and Automata Learning | Gabi Nakibly |  | 2022 | Protocol;Reverse |
| Process Injection: Breaking All macOS Security Layers With a Single Vulnerability | Thijs Alkemade |  | 2022 | macOS |
| Return to Sender - Detecting Kernel Exploits with eBPF | Guillaume Fournier | Datadog | 2022 | eBPF |
| Scaling the Security Researcher to Eliminate OSS Vulnerabilities Once and For All | Jonathan Leitschuh | HUMAN Security Inc. | 2022 | OSS |
| Stalloris: RPKI Downgrade Attack | Philipp Jeitner | SIT | 2022 | PKI |
| The Battle Against the Billion-Scale Internet Underground Industry: Advertising Fraud Detection and Defense | Zheng Huang | Baidu | 2022 | Advertising Fraud |
| The COW (Container On Windows) Who Escaped the Silo | Eran Segal | SafeBreach | 2022 | Windows;Container |
| The Journey of Hunting In-the-Wild Windows LPE 0day | Quan Jin | DBAPPSecurity | 2022 | 0day |
| To Flexibly Tame Kernel Execution With Onsite Analysis | Xuhua Ding | Singapore Management University | 2022 | Kernel |
| Trace Me if You Can: Bypassing Linux Syscall Tracing | Rex Guo | Lacework | 2022 | Syscall;Linux;Bypass |
| eBPF ELFs JMPing Through the Windows | Richard Johnson | Trellix Threat Labs | 2022 | eBPF;Windows |
| About Directed Fuzzing and Use-After-Free: How to Find Complex & Silent Bugs? | Sébastien Bardin   |  | 2020 | Fuzz |
| Decade of the RATs – Custom Chinese Linux Rootkits for Everyone | Kevin Livelli | Director of Threat Intelligence, BlackBerry | 2020 | Malware |
| Defending Containers Like a Ninja: A Walk through the Advanced Security Features of Docker & Kubernetes | Sheila Berta | Head of Research, Dreamlab Technologies | 2020 | Defense;Cloud |
| Demystifying Modern Windows Rootkits | Bill Demirkapi |  | 2020 | Rootkit |
| Detecting Access Token Manipulation | William Burgess | Elastic | 2020 | Windows |
| Detecting Fake 4G Base Stations in Real Time | Cooper Quintin | Senior Staff Technologist, Electronic Frontier Foundation | 2020 | Mobile |
| Discovering Hidden Properties to Attack the Node.js Ecosystem | Feng Xiao | Georgia Institute of Technology | 2020 | Web |
| Emulating Samsung's Baseband for Security Testing | Grant Hernandez | Security Researcher, University of Florida | 2020 | Mobile;Hardware;Emulate |
| Escaping Virtualized Containers | Yuval Avrahami | Palo Alto Networks | 2020 | Virtualize |
| Fooling Windows through Superfetch | Mathilde Venault | ESIEA | 2020 | Windows |
| HTTP Request Smuggling in 2020 – New Variants, New Defenses and New Challenges | Amit Klein | VP Security Research, SafeBreach | 2020 | Web |
| Hiding Process Memory via Anti-Forensic Techniques | Frank Block | Security Researcher, ERNW Research GmbH | 2020 | Malware;Forensics |
| Mind Games: Using Data to Solve for the Human Element | Masha Sedova | Elevate Security | 2020 | Social Enginner |
| NoJITsu: Locking Down JavaScript Engines | Taemin Park | University of California, Irvine | 2020 | JavaScript |
| OTRazor: Static Code Analysis for Vulnerability Discovery in Industrial Automation Scripts | Federico Maggi | Trend Micro Research | 2020 | Audit |
| Room for Escape: Scribbling Outside the Lines of Template Security | Alvaro Muñoz;Oleksandr Mirosh | GitHub | 2020 | Web |
| Routopsy: Modern Routing Protocol Vulnerability Analysis and Exploitation | Szymon Ziolkowski  | SensePost | 2020 | Router |
| Virtually Private Networks | Charl van der Walt | Global Head of Security Research, Orange Cyberdefense | 2020 | Web |
| Web Cache Entanglement: Novel Pathways to Poisoning | James Kettle | PortSwigger Web Security | 2020 | Web |
| When TLS Hacks You | Joshua Maddux | Latacora | 2020 | Web |
| You have No Idea Who Sent that Email: 18 Attacks on Email Sender Authentication | Jianjun Chen |  | 2020 | Social Enginner |
| Understanding The Attack Surface And Attack Resilience Of Project Spartans New EdgeHTML Rendering Engine | Mark Vincent Yason | IBM X-Force Advanced Research | 2015 | Edge;Attack |

## Black Hat WorkShop

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Embedded Devices Security and Firmware Reverse Engineering | Jonas Zaddach |  | 2013 | Embedded Devices;Firmware;Reverse Engineering |

## Blog

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| IDN Visual Security Deep Thinking |  |  | 2019 | IDN |
| Pass-the-Hash in Windows 10 39170 | Lukasz Cyra |  | 2019 | Windows;NTLM |
| Edge Type Confusion 利用 |  |  |  |  |

## CCS

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| A formally verified configuration for Hardware Security Modules in the cloud | Riccardo Focardi | University Ca' Foscari, Venice and Cryptosense | 2021 | Hardware;Cloud |
| All your credentials are belong to us: On Insecure WPA2-Enterprise Configurations | Man Hong Hue | The Chinese University of Hong Kong | 2021 | WPA2 |
| An In-Depth Symbolic Security Analysis of the ACME Standard | Karthikeyan Bhargavan | INRIA Paris, France | 2021 | ACME;Symbolic Security Analysis |
| Chunk-Level Password Guessing: Towards Modeling Refined Password Composition Representations | Ming Xu | Fudan University | 2021 | Password Guessing |
| DNS Cache Poisoning Attack: Resurrections with Side Channels | Keyu Man | University of California, Riverside | 2021 | DNS;Cache Poisoning |
| ECMO: Peripheral Transplantation to Rehost Embedded Linux Kernels | Muhui Jiang | The Hong Kong Polytechnic University | 2021 | Embedded;Rehost |
| Let's Downgrade Let's Encrypt | Tianxiang Dai | ATHENE Center & Fraunhofer SIT | 2021 | HTTPS |
| New Directions in Automated Traffic Analysis | Jordan Holland | Princeton University | 2021 | Traffic |
| Realtime Robust Malicious Traffic Detection via Frequency Domain Analysis | Chuanpu Fu | Tsinghua University | 2021 | Traffic;Domain |
| SoFi: Reflection-Augmented Fuzzing for JavaScript Engines | Xiaoyu He | Institute of Information Engineering, Chinese Academy of Sciences | 2021 | Fuzz;JavaScript |
| Spinner: Automated Dynamic Command Subsystem Perturbation | Meng Wang | University of Virginia | 2021 | Web |
| T-Reqs: HTTP Request Smuggling with Differential Fuzzing | Bahruz Jabiyev | Northeastern University | 2021 | HTTP;Differential Fuzzing |
| Towards Transparent and Stealthy Android OS Sandboxing via Customizable Container-Based Virtualization | Wenna Song | Wuhan University | 2021 | Android;Virtualization |
| V-SHUTTLE: Scalable and Semantics-Aware Hypervisor Fuzzing | Gaoning Pan | Ant Group | 2021 | Hypervisor;Fuzzing |
| Bypassing Tor Exit Blocking with Exit Bridge Onion Services | Zhao Zhang | Georgetown University | 2020 | Tor |
| CLAPS: Client-Location-Aware Path Selection in Tor | Florentin Rochet | UCLouvain | 2020 | Tor |
| DNS Cache Poisoning Attack Reloaded: Revolutions with Side Channels | Keyu Man,Zhiyun Qian | University of California, Riverside | 2020 | DNS cache poisoning;side channel |
| DNS Cache Poisoning Attack Reloaded: Revolutions with Side Channels | Keyu Man | University of California, Riverside | 2020 | DNS |
| PMForce: Systematically Analyzing postMessage Handlers at Scale | Marius Steffens | CISPA | 2020 | Web |
| SQUIRREL: Testing Database Management Systems with Language Validity and Coverage Feedback | Rui Zhong, Yongheng Chen, Hong Hu, Hangfan Zhang, Wenke Lee, Dinghao Wu | Software Systems Security Team at Penn State University | 2020 | Fuzz;SQL |
| The Cookie Hunter: Automated Black-box Auditing for WebAuthentication and Authorization Flaws | Kostas Drakonakis | FORTH ICS, Greece | 2020 | Web;Auth |
| TrafficSliver: Fighting Website Fingerprinting Attacks with Traffic Splitting | Wladimir De la Cadena | University of Luxembourg | 2020 | Web;Fingerprinting |
| Zombie Awakening: Stealthy Hijacking of Active Domains through DNS Hosting Referral | Eihal Alowaisheq | Indiana University | 2020 | DNS |
| 1 Trillion Dollar Refund – How To Spoof PDF Signatures | Vladislav Mladenov | Ruhr University Bochum | 2019 | PDF |
| Charting the Attack Surface of Trigger-Action IoT Platforms | Qi Wang | University of Illinois at Urbana-Champaign | 2019 | IoT |
| LibreCAN: Automated CAN Message Translator | Mert D. Pesé | University of Michigan | 2019 | CAN |
| Matryoshka: fuzzing deeply nested branches | Peng Chen | ByteDance AI Lab | 2019 | Fuzz |
| Principled Unearthing of TCP Side Channel Vulnerabilities | Yue Cao | UC Riverside | 2019 | TCP;Side Channel |
| Your Cache Has Fallen: Cache-Poisoned Denial-of-Service Attack | Hoai Viet Nguyen | Cologne University of Applied Sciences, Germany | 2019 | Web;Cache |
| Hawkeye: towards a desired directed grey box fuzzer |  |  | 2018 | Fuzz |
| Code-Reuse Attacks for the Web Breaking Cross-Site Scripting Mitigations via Script Gadgets |  |  | 2017 | Web XSS |
| Designing New Operating Primitives to Improve Fuzzing Performance | Wen Xu | Georgia Institute of Technology Virginia Tech | 2017 | Fuzz;Speed |
| Designing New Operating Primitives to Improve Fuzzing Performance | Wen Xu | Georgia Institute of Technology Virginia Tech | 2017 | Fuzz;Speed |
| Directed Greybox Fuzzing |  |  | 2017 | Fuzz |
| SlowFuzz: Automated Domain-Independent Detection of Algorithmic Complexity Vulnerabilities | los Petsios | Columbia University | 2017 | Fuzz |
| Coverage-based Greybox Fuzzing as Markov Chain | Marcel Böhme | School of Computing, National University of Singapore | 2016 | Fuzz |
| 25 Million flows later - Large-scale detection of DOM-based XSS |  |  | 2013 |  |
| Tappan Zee (North) Bridge: Mining Memory Accesses for Introspection | Brendan Dolan-Gavitt | Georgia Tech | 2013 | Introspection;reverse engineering |
| Block Oriented Programming Automating Data-Only Attacks |  |  |  | Exploit |
| Deterministic Browser |  |  |  | Browser |
| HyCC: Compilation of Hybrid Protocols for Practical Secure Computation |  |  |  | Fuzz |
| IMF Infeered Model-based Fuzzer |  |  |  | Fuzz |
| POISED Spotting Twitter Spam Off the Beaten Paths |  |  |  | Spam |
| Predicting Impending Exposure to Malicious Content from User Behavior |  |  |  |  |
| Rewriting History Changing the Archived Web from the Present |  |  |  |  |
| SemFuzz Semantics-based Automatic Generation of Proof-of-Concept Exploits |  |  |  | Fuzz |
| The TypTop System Personalized Typo-Tolerant Password Checking |  |  |  |  |
| Threat Intelligence Computing |  |  |  | Threat Intelligence |
| Trends, challenge, and shifts in software vulnerability mitigation |  |  |  |  |
| Web Sixth Sense A Study of Scripts Accessing Smartphone Sensors |  |  |  |  |
| When Good Components Go Bad Formally Secure Compilation Despite Dynamic Compromise |  |  |  |  |
| Yet Another Text Captcha Solver A Generative Adversarial Network Based Approach |  |  |  |  |

## DSN

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Your IoTs Are (Not) Mine: On the Remote BindingBetween IoT Devices and Users | Jiongyi Chen | The Chinese University of Hong Kong | 2019 | IoT |

## Defcon

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Extension-Land - exploits and rootkits in your browser extensions | Barak Sternberg | SentinelOneLabs | 2021 | brower extension |
| Offensive Golang Bonanza - Writing Golang Malware | Ben Kurtz |  | 2021 | Golang;Malware |
| Firmware slap: automating discovery of exploitable vulnerabilities in firmware | Christopher roberts |  | 2019 | Firmware |
| Analysis of Mutation and Generation Based Fuzzing |  |  |  | Fuzz |
| geoff mcdonald meddle framework updated |  |  |  | Fuzz |

## ESEC/FSE

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Boosting Fuzzer Efficiency:An Information Theoretic Perspective | Marcel Böhme | Monash University | 2020 | Fuzz |

## FSE

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| CrFuzz: Fuzzing Multi-purpose Programs through Input Validation | Suhwan Song | Seoul National University | 2020 | Fuzz |
| Detecting Critical Bugs in SMT Solvers using Blackbox Mutational Fuzzing | Muhammad Numair Mansur | MPI-SWS, Germany | 2020 | Fuzz |
| Fuzzing: On the Exponential Cost of Vulnerability Discovery | Marcel Böhme | Monash University, Australia | 2020 | Fuzz |
| MTFuzz: Fuzzing with a Multi-task Neural Network | Dongdong She | Columbia University | 2020 | Fuzz |
| Steelix: Program-State Based Binary Fuzzing | Yuekang Li | Nanyang Technological University | 2017 | Fuzz |
| KATCH High-Coverage Testing of Software Patches | Paul Dan Marinescu |  | 2013 | Fuzz;Patch |

## H2HC

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Embedded Research & Automation | Brian Butterly |  | 2019 | Embedded;Fuzz |

## HITB

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| API Security Through External Attack Surface Management | Phillip Wylie |  | 2022 | API Security; |
| Browser Hacking with ANGLE | Jeonghoon Shin |  | 2022 | Browser |
| Building an Army of Bots by Hijacking a Unicorn’s Twitter Handle | Rahul Sasi |  | 2022 | OSINT |
| EDR Evasion Primer for Red Teamers | Karsten Nohl |  | 2022 | EDR |
| Scripts-behavioral ML Classification Using Windows 10 AMSI-instrumentation | Ankit Garg | MS | 2022 | Windows;Defender |
| Windows Bribery for Invisible Persistence | Sebastian Castro |  | 2022 | Windows |
| Building Next-Gen Security Analysis Tools With Qiling Framework | KaiJern LAU | qiling.io | 2020 | Emulation |
| Static Code Analysis Recognition Evasion | Andreas Wiegenstein | AP Cyber Security | 2019 | Code Analysis |
| From Out of Memory to Remote Code Execution | Yuki Chen |  | 2017 | Fuzz |
| The ECMA and The Chakra | Natalie Silvanovich |  |  | Fuzz |
| The Secret of ChakraCore |  |  |  |  |

## ICSE

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| MemLock: Memory Usage Guided Fuzzing | Cheng Wen | Shenzhen University;Ant Financial | 2020 | Fuzz;AFL |
| Typestate-Guided Fuzzer for Discovering Use-after-Free Vulnerabilities | Haijun Wang | Ant Financial Services Group | 2020 | Fuzz;UAF |
| DifFuzz Differential Fuzzing for Side-Channel Analysis | Shirin Nilizadeh | uta.edu | 2019 | Differential Fuzz |
| REST-ler: Automatic Intelligent REST API Fuzzing | Vaggelis Atlidakis | Columbia University | 2019 | Fuzz Web RESTful |
| SLF: Fuzzing without Valid Seed Inputs | Wei You | Purdue University | 2019 | Fuzz |
| Superion Grammar-Aware Greybox Fuzzing | Junjie Wang | Fudan University | 2019 | Fuzz;AST |

## ICST

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| AFLNET: A Greybox Fuzzer for Network Protocols | Van-Thuan Pham | Monash University | 2020 | Fuzz; Network |
| SeqFuzzer An Industrial Protocol Fuzzing Framework in Deep Learning Perspective | Hui Zhao | National Trusted Embedded Software Engineering Technology Research Center | 2019 | Fuzz |
| SeqFuzzer: An Industrial Protocol Fuzzing Framework in Deep Learning Perspective | Nicolas Coppik | DEEDS Group, TU Darmstadt | 2019 | Fuzz |

## IEEE

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| End User and Administrator Mental Models of HTTPS |  |  | 2019 | Web |
| Full-speed Fuzzing Reducing Fuzzing Overhead through Coverage-guided Tracing |  |  | 2019 | Fuzz |
| Fuzzing File Systems via Two-Dimensional Input Space Exploration |  |  | 2019 | Fuzz |
| HOLMES Real-time APT Detection through Correlation of Suspicious Information Flows |  |  | 2019 | APT |
| ProFuzzer On-the-fly Input Type Probing for Better Zero-day Vulnerability Discovery |  |  | 2019 | Fuzz |
| RAZZER Finding Kernel Race Bugs through Fuzzing |  |  | 2019 | Fuzz Kernel Race |
| Resident Evil Understanding Residential IP Proxy as a Dark Service |  |  | 2019 | 生态 |
| Angora: Efficient Fuzzing by Principled Search | Peng Chen |  | 2018 | Fuzz |
| GramFuzz: Fuzzing Testing of Web Browsers Based on Grammar Analysis and Structural Mutation |  |  | 2013 | Fuzz |
| Browser Fuzzing by Scheduled Mutation and Generation of Document Object Models |  |  |  | Fuzz |
| CollAFL Path Sensitive Fuzzing |  |  |  | Fuzz |
| Research on Android browser fuzzing based on bitmap structure |  |  |  | Fuzz |
| Software Crash Analysis for Automatic Exploit Generation by Modeling Attacks as Symbolic Continuations |  |  |  | Fuzz |
| Violating Assumptions with Fuzzing |  |  |  | Fuzz |

## IEEE S&P

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Measuring and Mitigating the Risk of IP Reuse on Public Clouds | Eric Pauley | Pennsylvania State University | 2022 | Cloud |
| Dragonblood: Analyzing the Dragonfly Handshake of WPA3 and EAP-pwd | Mathy Vanhoef | New York University Abu Dhabi | 2020 | Wifi |
| IJON: Exploring Deep State Spaces via Fuzzing | Cornelius Aschermann, Sergej Schumilo, Ali Abbasi, and Thorsten Holz | Ruhr University Bochum | 2020 | Fuzz |
| KARONTE: Detecting Insecure Multi-binary Interactions in Embedded Firmware | Nilo Redini | ucsb-seclab | 2020 | Embedded |
| PANGOLIN: Incremental Hybrid Fuzzing with Polyhedral Path Abstraction | Heqing Huang | The Hong Kong University of Science and Technology, China | 2020 | Fuzz |
| SAVIOR: Towards Bug-Driven Hybrid Testing |  |  | 2020 | Fuzz;Hybrid |
| Tactical Provenance Analysis for Endpoint Detection and Response Systems | Wajih Ul Hassan |  | 2020 | EDR |
| TaintScope: A Checksum-Aware Directed Fuzzing Tool for Automatic Software Vulnerability Detection | Tielei Wang |  | 2020 | taint;fuzz |
| Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing | Stefan Nagy | Virginia Tech | 2019 | Fuzz |
| T-Fuzz: fuzzing by program transformation | Hui Peng | Purdue University | 2018 | Fuzz;Black Box |
| Finding and preventing bugs in JavaScript bindings | Fraser Brown | Stanford University | 2017 | Fuzz;JavaScript |
| HVLearn: Automated black-box analysis of hostname verification in SSL/TLS implementations | Sivakorn |  | 2017 | Fuzz |
| NEZHA: Efficient Domain-Independent Differential Testing |  |  | 2017 | Fuzz;Differential |
| (State of) The Art of War: Offensive Techniques in Binary Analysis | Yan Shoshitaishvili | UCSB | 2016 | Angr;Binary Analysis |
| The Limitations of Deep Learning in Adversarial Settings | Nicolas Papernot |  | 2016 | GAN;Machine Learning |
| The BORG: Nanoprobing Binaries for Buffer Overreads | Matthias Neugschwandtner | Vienna University of Technology | 2015 | Fuzz;Taint |
| Skyfire Data Driven Seed Generation for Fuzzing |  |  |  | Fuzz |

## IEEE-ACM

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Learn&Fuzz: Machine Learning for Input Fuzzing | Godefroid |  | 2017 | Fuzz |

## IJCAI

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Locate Then Detect：Web Attack Detection via Attention-based Deep Neural Networks | Tianlong Liu,Jianan Yan | Ali | 2019 | Web;Machine Learning;WAF |

## ISCA

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Debunking the 100X GPU vs. CPU Myth: An Evaluation of Throughput Computing on CPU and GPU | Victor W Lee;Changkyu Kim;Jatin Chhugani;Michael Deisher;Daehyun Kim;Anthony D. Nguyen;Nadathur Satish;Mikhail Smelyanskiy;Srinivas Chennupaty;Per Hammarlund;Ronak Singhal and Pradeep Dubey | Intel Corporation | 2010 | Computer Architecture |

## ISSTA

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Active Fuzzing for Testing and Securing Cyber-Physical Systems | Yuqi Chen | Singapore Management University | 2020 | Fuzz |
| Learning Input Tokens for Effective Fuzzing | Björn Mathis | CISPA Helmholtz Center for Information Security | 2020 | Fuzz |
| WEIZZ: Automatic Grey-Box Fuzzingfor Structured Binary Formats | Andrea Fioraldi | Sapienza University of RomeItaly | 2020 | Fuzz;Structured |
| DeepHunter: A Coverage-Guided Fuzz Testing Framework for Deep Neural Networks | Xiaofei Xie | Nanyang Technological University | 2019 | Fuzz |
| Deferred Concretization in Symbolic Execution via Fuzzing | Awanish Pandey | Computer Sc. and Engg. | 2019 | Fuzz |
| Semantic Fuzzing with Zest | Rohan Padhye | University of California, Berkeley | 2019 | Fuzz |
| Badger: Complexity Analysis with Fuzzing and Symbolic Execution | Yannic Noller | Humboldt University of Berlin | 2018 | Fuzz |
| Compiler Fuzzing through Deep Learning | Chris Cummins | Pavlos Petoumenos | 2018 | Fuzz |
| PerfFuzz: Automatically Generating Pathological Inputs | Caroline Lemieux | University of California, Berkeley, USA | 2018 | Fuzz |
| Make It Work, Make It Right, Make It Fast: Building a Platform-Neutral Whole-System Dynamic Binary Analysis Platform | Andrew Henderson | Department of EECS | 2014 | binary analysis;taint analysis;virtual machine introspection |

## MS

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| neural fuzzing mcr |  |  |  | Fuzz |

## Misc

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Bitcoin: A Peer-to-Peer Electronic Cash System | Satoshi Nakamoto | Bitcoin.Org | 2008 | Bitcoin |
| Tor: The Second-Generation Onion Router | Dingledine | Naval Research Lab Washington DC | 2004 | Tor |
| Critical Vulnerability in Browser Security Metrics |  |  |  | Fuzz |
| Drive by Key Extraction Cache Attacks from Portable Code |  |  |  | Fuzz |
| Escaping Internet Explorer Protected Mode |  |  |  | Fuzz |
| Fuzzing JavaScript Engine APIs |  |  |  | Fuzz |
| Test Harness For Web Browser Fuzz Testing |  |  |  | Fuzz |
| The Security Architecture of the Chromium Browser |  |  |  | Fuzz |
| X41 Browser Security White Paper |  |  |  | Fuzz |
| browser ui security whitepaper |  |  |  | Fuzz |
| cure53 browser security whitepaper |  |  |  | Fuzz |

## NDSS

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Subverting Stateful Firewalls with Protocol States | Amit Klein | Bar Ilan University | 2022 | TCP/IP |
| A Devil of a Time: How Vulnerable is NTP to Malicious Timeservers? | Yarin Perry | The Hebrew University of Jerusalem | 2021 | NTP |
| Peerlock: Flexsealing BGP | Tyler McDaniel | University of Tennessee, Knoxville | 2021 | BGP |
| Cross-Origin State Inference (COSI) Attacks: Leaking Web Site States through XS-Leaks | Avinash Sudhodanan | IMDEA Software Institute | 2020 | Web;Frontend |
| Deceptive Previews: A Study of the Link Preview Trustworthiness in Social Platforms | Giada Stivala | CISPA | 2020 | Web;Social |
| HotFuzz: Discovering Algorithmic Denial-of-Service Vulnerabilities Through Guided Micro-Fuzzing | William Blair | Boston University | 2020 | Fuzz;SlowFuzz |
| Melting Pot of Origins: Compromising the Intermediary Web Services that Rehost Websites | Takuya Watanabe | NTT | 2020 | Web |
| Not All Coverage Measurements Are Equal: Fuzzing by Coverage Accounting for Input Prioritization | Yanhao Wang | Institute of Software, Chinese Academy of Sciences | 2020 | Fuzz |
| UNICORN: Runtime Provenance-Based Detector for Advanced Persistent Threats | Xueyuan Han |  | 2020 | APT |
| A Systematic Framework to Generate Invariants for Anomaly Detection in Industrial Control Systems | Cheng Feng | Imperial College London | 2019 | ICS |
| Analyzing Semantic Correctness with Symbolic Execution: A Case Study on PKCS#1 v1.5 Signature Verification | Sze Yiu Chau | Purdue University | 2019 | Fuzz;Symbolic Execution |
| BadBluetooth Breaking Android Security Mechanisms via Malicious Bluetooth Peripherals | Fenghao Xu | The Chinese University of Hong Kong | 2019 | Bluetooth |
| CodeAlchemist: Semantics-Aware Code Generation to Find Vulnerabilities in JavaScript Engines | HyungSeok Han | KAIST | 2019 | Fuzz |
| DIAT: Data Integrity Attestation for Resilient Collaboration of Autonomous Systems | Tigist Abera | Technische Universität Darmstadt | 2019 | IoT |
| DIAT: Data Integrity Attestation for Resilient Collaboration of Autonomous Systems | Z. Berkay Celik | Penn State University | 2019 | IoT |
| DNS Cache-Based User Tracking | Amit Klein | Bar Ilan University | 2019 | DNS;Privacy |
| Distinguishing Attacks from Legitimate Authentication Traffic at Scale | Cormac Herley | Microsoft | 2019 | Side Channel |
| Don’t Trust The Locals: Investigating the Prevalence of Persistent Client-Side Cross-Site Scripting in the Wild |  |  | 2019 | XSS |
| How Bad Can It Git? Characterizing Secret Leakage in Public GitHub Repositories | Michael Meli | North Carolina State University | 2019 | Privacy;Git |
| ICSREF: A Framework for Automated Reverse Engineering of Industrial Control Systems Binaries | Anastasis Keliris | NYU | 2019 | IoT;Reverse Engineering |
| IOTFUZZER: Discovering Memory Corruptions in IoT Through App-based Fuzzing | Jiongyi Chen | The Chinese University of Hong Kong | 2019 | IoT;Fuzz |
| JavaScript Template Attacks: Automatically Inferring Host Information for Targeted Exploits | Michael Schwarz | Graz University of Technology | 2019 | Side;Channel |
| Master of Web Puppets: Abusing Web Browsers for Persistent and Stealthy Computation | Panagiotis Papadopoulos | FORTH-ICS | 2019 | Web;HTML5;Browseer API |
| NAUTILUS:Fishing for Deep Bugs with Grammars |  |  | 2019 | Fuzz;Browser |
| Neural Machine Translation Inspired Binary Code Similarity Comparison beyond Function Pairs |  |  | 2019 | NLP Binary |
| One Engine To Serve 'em All: Inferring Taint Rules Without Architectural Semantics | Zheng Leong Chua | National University of Singapore | 2019 |  |
| PeriScope: An Effective Probing and Fuzzing Framework for the Hardware-OS Boundary | Dokyung Song | University of California, Irvine | 2019 | Fuzz;Hardware |
| Profit: Detecting and Quantifying Side Channels in Networked Applications | Nicolás Rosner | University of California, Santa Barbara | 2019 | Side Channel |
| REDQUEEN: Fuzzing with Input-to-State Correspondence | Cornelius Aschermann,Sergej Schumilo,Tim Blazytko,Robert Gawlik and Thorsten Holz |  | 2019 | Fuzz |
| REDQUEEN: Fuzzing with Input-to-State Correspondence | Cornelius Aschermann, Sergej Schumilo, Tim Blazytko, Robert Gawlik, Thorsten Holz | Ruhr-Universität Bochum | 2019 | Fuzzing |
| Send Hardest Problems My Way: Probabilistic Path Prioritization for Hybrid Fuzzing | Lei Zhao | Wuhan University | 2019 | Hybrid Fuzzing |
| Send Hardest Problems My Way: Probabilistic Path Prioritization for Hybrid Fuzzing | Lei Zhao | Wuhan University | 2019 | Fuzz |
| Synode: Understanding and Automatically Preventing Injection Attacks on Node.js | SOLA |  | 2019 | Web;Auomatica |
| TextBugger: Generating Adversarial Text Against Real-world Applications | Jinfeng Li | Zhejiang University | 2019 | Adversarial |
| Unveiling your keystrokes: A Cache-based Side-channel Attack on Graphics Lib | Daimeng Wang | University of California Riverside | 2019 | Side-channel |
| What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices | Marius Muench | EURECOM | 2018 | Fuzz;Embedded |
| VUzzer Application-aware Evolutionary Fuzzing | Sanjay Rawat |  | 2017 | Fuzz |
| Driller: Augmenting Fuzzing Through Selective Symbolic Execution | Nick Stephens, John Grosen, Christopher Salls, Andrew Dutcher, Ruoyu Wang, Jacopo Corbetta, Yan Shoshitaishvili, Christopher Kruegel, Giovanni Vigna | UCSB | 2016 | Fuzz;Selective Symbolic Execution |
| Towards Automated Dynamic Analysis for Linux-based Embedded Firmware | Daming D. Chen | CMU | 2016 | Firmware |
| Avatar: A Framework to Support Dynamic Security Analysis of Embedded Systems' Firmwares | Jonas Zaddach | EURECOM, France | 2014 | Fuzz;Firmware |
| VulDeePecker |  |  |  |  |

## OOPSLA

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Compiler Fuzzing: How Much Does It Matter? | MICHAËL MARCOZZI | Imperial College London, United Kingdom | 2019 | Fuzz |
| FuzzFactory: Domain-Specific Fuzzing with Waypoints | Rohan Padhye | University of California at Berkeley, USA | 2019 | Fuzz |

## Offensive

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Attacking Edge Through the JavaScript Compiler |  |  | 2019 | Exploit |
| Chrome IPC Exploitation |  |  | 2019 | Exploit |
| Coverage-Guided USB Fuzzing with Syzkaller |  |  | 2019 | Fuzz |
| Fuzzil: Guided Fuzzing for JavaScript Engines | Samuel Groß |  | 2019 | Fuzz |
| From Assembly to JavaScript and back |  |  | 2018 |  |

## OffensiveCon

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Attacking JavaScript Engines in 2022 | Samuel Groß;Amy Burnett |  | 2022 | JavaScript |
| BeaconFuzz A Journey into Ethereum 2.0 Blockchain Fuzzing and Vulnerability Discovery | Patrick Ventuzelo  | FuzzingLabs | 2022 | Fuzz;Ethereum |
| From Assembly to JavaScript and back |  |  | 2018 | Fuzz |

## PLDI

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Parser-Directed Fuzzing | Mathis | cispa | 2019 | Fuzz |
| Coverage-Directed Differential Testing of JVM Implementations | Yuting Chen | SJTU | 2016 | Fuzz;JVM;Differential |

## PPT

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Attacking Modern Web Technologies |  |  | 2018 | HTML5 Security |
| php internals exploit dev |  |  | 2018 | PHP Fuzz |
| BrowserFuzzing |  |  | 2014 |  |
| 1day browser exploitaion |  |  |  | Fuzz |
| Blink Rendering |  |  |  | Fuzz |
| Taking Browsers Fuzzing to the next (DOM) Level |  |  |  | Fuzz |
| ZeroNights2017 darko fuzzer |  |  |  | Fuzz |
| the art of fuzzing slides |  |  |  | Fuzz |

## QPSS

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| PowerFL: Fuzzing VxWorks embedded system | Peter Goodman |  | 2019 | Embedded;Fuzz;IoT |

## RAID

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Cyber Threat Intelligence Modeling Based on Heterogeneous Graph Convolutional Network | Jun Zhao | Beihang University | 2020 | Threat Intelligence |
| CRYPTOREX: Large-scale Analysis of Cryptographic Misuse in IOT Devices | Li Zhang | Jinan University | 2019 | Crypto;IoT |

## SIGMOD

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| ACIDRain: Concurrency-Related Attacks on Database-Backed Web Applications | Todd Warszawski | Stanford InfoLab | 2017 | Web |

## SIGPLAN

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Parser-Directed Fuzzing |  |  | 2019 | Fuzz |
| Synthesizing program input grammars | Osbert Bastani |  | 2017 | Fuzz |
| Fast and Precise Hybrid Type Inference for JavaScript | Brian Hackett | Mozilla | 2012 | Fuzz;JavaScript |

## Secwest

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Chakra vulnerability and exploit bypass all system mitigation |  |  |  |  |
| Shellcodes are for the 99% |  |  |  | Fuzz |

## TSE

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Smart Greybox Fuzzing | Van-Thuan Pham |  | 2019 | Fuzz |

## USENIX ATC

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Soteria: Automated IoT Safety and Security Analysis | Z.Berkay Celik | The Pennsylvania State University | 2018 | IoT |
| Gdev: First-Class GPU Resource Management in the Operating System | Shinpei Kato | Department of Computer Science, UC Santa Cruz | 2012 | GPU |

## Usenix

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| An Input-Agnostic Hierarchical Deep Learning Framework for Traffic Fingerprinting | Jian Qu;Xiaobo Ma;Jianfeng Li | Xi’an Jiaotong University | 2023 | Deep Learning;Traffic;Fingerprinting |
| Attacks are Forwarded: Breaking the Isolation of MicroVM-based Containers Through Operation Forwarding | Jietao Xiao;Nanzi Yang | State Key Lab of ISN, School of Cyber Engineering, Xidian University, China | 2023 | Container Escape |
| Bleem: Packet Sequence Oriented Fuzzing for Protocol Implementations | Zhengxiong Luo;Junze Yu;Feilong Zuo;Jianzhong Liu;Yu Jiang | Tsinghua University | 2023 | Fuzz;Protocol |
| Detecting Multi-Step IAM Attacks in AWS Environments via Model Checking | Ilia Shevrin | Citi | 2023 | AWS;IAM |
| Did the Shark Eat the Watchdog in the NTP Pool? Deceiving the NTP Pool’s Monitoring System | Jonghoon Kwon | ETH Zürich | 2023 | NTP |
| Downgrading DNSSEC: How to Exploit Crypto Agility for Hijacking Signed Zones | Elias Heftrig | ATHENE Fraunhofer SIT | 2023 | DNS Hijacking |
| NAUTILUS: Automated RESTful API Vulnerability Detection | Gelei Deng | Nanyang Technological University | 2023 | Web |
| Pool-Party: Exploiting Browser Resource Pools for Web Tracking | Peter Snyder | Brave Software | 2023 | Browser |
| TRIDENT: Towards Detecting and Mitigating Web-based Social Engineering Attacks | Zheng Yang | Georgia Institute of Technology | 2023 | web;ad-block |
| Trojan Source: Invisible Vulnerabilities | Nicholas Boucher | University of Cambridge | 2023 | Unicode; human |
| We Really Need to Talk About Session Tickets: A Large-Scale Analysis of Cryptographic Dangers with TLS Session Tickets | Sven Hebrok | Paderborn University | 2023 | TLS |
| COMRace: Detecting Data Race Vulnerabilities in COM Objects | Fangming Gu | iie | 2022 | Windows |
| Characterizing the Security of Github CI Workflows | Igibek Koishybayev | North Carolina State University | 2022 |  |
| Creating a Secure Underlay for the Internet | Henry Birge-Lee | Princeton University | 2022 | internet;route |
| Drifuzz: Harvesting Bugs in Device Drivers from Golden Seeds | Zekun Shen | NYU | 2022 | Fuzz |
| Exploring the Unchartered Space of Container Registry Typosquatting | Guannan Liu | George Mason University | 2022 | typosquatting |
| FRAMESHIFTER: Security Implications of HTTP/2-to-HTTP/1 Conversion Anomalies | Bahruz Jabiyev | Northeastern University | 2022 | HTTP |
| FuzzOrigin: Detecting UXSS vulnerabilities in Browsers through Origin Fuzzing | Sunwoo Kim | Samsung Research | 2022 | Browsers;Fuzz;UXSS |
| Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing | Tobias Scharnowski | Ruhr-Universität Bochum | 2022 | Fuzz;IoT;emulator |
| GET /out: Automated Discovery of Application-Layer Censorship Evasion Strategies | Michael Harrity | University of Maryland | 2022 |  |
| Lumos: Identifying and Localizing Diverse Hidden IoT Devices in an Unfamiliar Environment | Rahul Anand Sharma | Carnegie Mellon University | 2022 | IoT;eavesdrop |
| Mining Node.js Vulnerabilities via Object Dependence Graph and Query | Song Li | Johns Hopkins University | 2022 | Node.js;AST;GraphQL |
| Morphuzz: Bending (Input) Space to Fuzz Virtual Devices | Alexander Bulekov | Boston University | 2022 | Fuzz;IoT;virtual |
| Off-Path Network Traffic Manipulation via Revitalized ICMP Redirect Attacks | Xuewei Feng | Department of Computer Science and Technology & BNRist | 2022 | ICMP |
| Online Website Fingerprinting: Evaluating Website Fingerprinting Attacks on Tor in the Real World | Giovanni Cherubin | EPFL SPRING Lab | 2022 | Fingerprinting;Tor |
| PolyCruise: A Cross-Language Dynamic Information Flow Analysis | Wen Li | Washington State University | 2022 | Cross-Language;Code Audit |
| Practical Privacy-Preserving Authentication for SSH | Lawrence Roy | Oregon State University | 2022 | SSH |
| RapidPatch: Firmware Hotpatching for Real-Time Embedded Devices | Yi He | Tsinghua University | 2022 | Firmware;Hotpatch |
| Spoki: Unveiling a New Wave of Scanners through a Reactive Network Telescope | Raphael Hiesgen | Freie Universität Berlin | 2022 | Scan |
| StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing | Bodong Zhao | Institute for Network Science and Cyberspace / BNRist | 2022 | Stateful fuzz |
| Stateful Greybox Fuzzing | Jinsheng Ba | National University of Singapore | 2022 | Fuzz |
| The Security Lottery: Measuring Client-Side Web Security Inconsistencies | Sebastian Roth | CISPA Helmholtz Center for Information Security | 2022 | Web |
| Under the Hood of DANE Mismanagement in SMTP | Hyeonmin Lee | Seoul National University | 2022 | SMTP |
| Uninvited Guests: Analyzing the Identity and Behavior of Certificate Transparency Bots | Brian Kondracki | Stony Brook University | 2022 | CT |
|  | You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion |  | 2021 | AI |
| Android SmartTVs Vulnerability Discovery via Log-Guided Fuzzing | Yousra Aafer | University of Waterloo | 2021 | Fuzz;IoT |
| Automatic Firmware Emulation through Invalidity-guided Knowledge Inference | Wei Zhou | National Computer Network Intrusion Protection Center, University of Chinese Academy of Sciences | 2021 | Emulation;IoT |
| Automatic Policy Generation for Inter-Service Access Control of Microservices | Xing Li | Zhejiang University | 2021 | Microservice;Policy |
| Blind In/On-Path Attacks and Applications to VPNs | William J. Tolley | Breakpointing Bad/Arizona State University | 2021 | VPN;Hijack |
| Causal Analysis for Software-Defined Networking Attacks | Benjamin E. Ujcich | Georgetown University | 2021 | SDN |
| Constraint-guided Directed Greybox Fuzzing | Gwangmu Lee | Seoul National University | 2021 | Greybox Fuzz; |
| Fine Grained Dataflow Tracking with Proximal Gradients | Gabriel Ryan | Columbia University | 2021 | Taint Analysis |
| Fingerprinting in Style: Detecting Browser Extensions via Injected Style Sheets | Pierre Laperdrix | Univ. Lille, CNRS, Inria | 2021 | Fingerprint;Browser |
| Jetset: Targeted Firmware Rehosting for Embedded Systems | Evan Johnson | University of California, San Diego | 2021 | Firmware;Rehosting |
| LZR: Identifying Unexpected Internet Services | Liz Izhikevich | Stanford University | 2021 | port scan |
| ReDMArk: Bypassing RDMA Security Mechanisms | Benjamin Rothenberger |  | 2021 | RDMA |
| Reducing Bias in Modeling Real-world Password Strength via Deep Learning and Dynamic Dictionaries | Dario Pasquini | Sapienza University of Rome, Institute of Applied Computing CNR | 2021 | Auth |
| Weak Links in Authentication Chains: A Large-scale Analysis of Email Sender Spoofing Attacks | Kaiwen Shen | Tsinghua University | 2021 | Mail |
| Weaponizing Middleboxes for TCP Reflected Amplification | Kevin Bock | University of Maryland; Abdulrahman Alaraj | 2021 | Web;DoS |
| A Longitudinal and Comprehensive Study of the DANE Ecosystem in Email | Hyeonmin Lee | Seoul National University | 2020 | Email;DNS |
| AURORA: Statistical Crash Analysis for Automated Root Cause Explanation | Tim Blazytko | Ruhr-Universität Bochum | 2020 | Automated |
| Agamotto: Accelerating Kernel Driver Fuzzing with Lightweight Virtual Machine Checkpoints | Dokyung Song | University of California, Irvine | 2020 | Fuzz;Kernel |
| Analysis of DTLS Implementations Using Protocol State Fuzzing | Paul Fiterau-Brostean | Uppsala University | 2020 | Fuzz |
| Automatic Techniques to Systematically Discover New Heap Exploitation Primitives | Insu Yun | Georgia Institute of Technology | 2020 | Heap;Exploit |
| Cached and Confused: Web Cache Deception in the Wild | Seyed Ali Mirheidari | University of Trento | 2020 | Cache Deception |
| EcoFuzz: Adaptive Energy-Saving Greybox Fuzzing as a Variant of the Adversarial Multi-Armed Bandit | Tai Yue | National University of Defense Technology | 2020 | Fuzz |
| EcoFuzz: Adaptive Energy-Saving Greybox Fuzzing as aVariant of the Adversarial Multi-Armed Bandit | Tai Yue, Pengfei Wang, Yong Tan | National University of Defense Technology | 2020 | Fuzz;AI |
| FANS: Fuzzing Android Native System Services via Automated Interface Analysis | Baozheng Liu,Chao Zhang | Tsinghua University | 2020 | Fuzz;Android |
| Frankenstein: Advanced Wireless Fuzzing to Exploit New Bluetooth Escalation Targets | Jan Ruge | Secure Mobile Networking Lab, TU Darmstadt | 2020 | Fuzz;Bluetooth;Emulate;Firmware |
| FuzzGen: Automatic Fuzzer Generation | Kyriakos Ispoglou | Daniel Austin | 2020 | Fuzz |
| FuzzGuard: Filtering out Unreachable Inputs in Directed Grey-box Fuzzing through Deep Learning | Peiyuan Zong | IIE | 2020 | Fuzz;Deep Learning |
| FuzzGuard: Filtering out Unreachable Inputs in Directed Grey-box Fuzzingthrough Deep Learning | Peiyuan Zong | UCAS | 2020 | Fuzz |
| Fuzzing Error Handling Code using Context-Sensitive Software Fault Injection | Zu-Ming Jiang | Tsinghua University | 2020 | Fuzz |
| GREYONE: Data Flow Sensitive Fuzzing | Shuitao Gan | State Key Laboratory of Mathematical Engineering and Advanced Computing | 2020 | Fuzz |
| HALucinator: Firmware Re-hosting Through Abstraction Layer Emulation | Abraham A Clements | Sandia National Laboratories | 2020 | Firmware |
| KOOBE: Towards Facilitating Exploit Generation of Kernel Out-Of-Bounds Write Vulnerabilities | Weiteng Chen | UC Riverside | 2020 | OOB;Exploit |
| MUZZ: Thread-aware Grey-box Fuzzing for Effective Bug Hunting in Multithreaded Programs | Hongxu Chen | University of Science and Technology of China and Nayang Technological University | 2020 | Fuzz |
| Montage: A Neural Network Language Model-Guided JavaScript Engine Fuzzer | Suyoung Lee | KAIST | 2020 | Fuzz;NN |
| NXNSAttack: Recursive DNS Inefficiencies and Vulnerabilities | Lior Shafir | Tel Aviv University | 2020 | DNS;DoS |
| NXNSAttack: Recursive DNS Inefficiencies and Vulnerabilities | Yehuda Afek | Tel-Aviv University | 2020 | DNS |
| P2IM Scalable and Hardware-independent Firmware Testing via Automatic Peripheral Interface Modeling | Bo Feng, Alejandro Mera, and Long Lu | Northeastern University | 2020 | Fuzz |
| ParmeSan: Sanitizer-guided Greybox Fuzzing | Sebastian Österlund | Vrije Universiteit Amsterdam | 2020 | Fuzz |
| Poison Over Troubled Forwarders: A Cache Poisoning Attack Targeting DNS Forwarding Devices | Xiaofeng Zheng | Tsinghua University | 2020 | DNS;Cache Poisoning |
| Symbolic execution with SymCC: Don't interpret, compile! | Sebastian Poeplau | EURECOM | 2020 | Fuzz |
| Sys: A Static/Symbolic Tool for Finding Good Bugs in Good (Browser) Code | Fraser Brown, Stanford University; Deian Stefan, UC San Diego; Dawson Engler, Stanford University | Stanford University | 2020 | Browser;Vuln Discovery |
| The Industrial Age of Hacking | Timothy Nosco | United States Army | 2020 | Training |
| USBFuzz: A Framework for Fuzzing USB Drivers by Device Emulation | Hui Peng | Purdue University | 2020 | Fuzz;Emulation |
| All Your Clicks Belong to Me: Investigating Click Interception on the Web | Mingxue Zhang and Wei Meng | Pennsylvania State University | 2019 | Web;Click hijack |
| An Empirical Analysis of Single Sign-On Account Hijacking and Session Management on the Web |  |  | 2019 | Web, SSO |
| Discovering and Understanding the Security Hazards in the Interactions between IoT Devices, Mobile Apps, and Clouds on Smart Home Platforms | Wei Zhou | IIE | 2019 | IoT |
| EnFuzz: Ensemble Fuzzing with Seed Synchronization among Diverse Fuzzers | Yuanliang Chen, Yu Jiang, Fuchen Ma, Jie Liang, Mingzhe Wang, Chijin Zhou | Tsinghua University | 2019 | Fuzz |
| FIRM-AFL: High-Throughput Greybox Fuzzing of IoT Firmware via Augmented Process Emulation | Yaowen Zheng | School of Cyber Security, University of Chinese Academy of Sciences, China | 2019 | Fuzz;Firm |
| GRIMOIRE: Synthesizing Structure while Fuzzing | Tim Blazytko, Cornelius Aschermann, Moritz Schlögel, Ali Abbasi, Sergej Schumilo, Simon Wörner | Ruhr-Universität Bochum | 2019 | Fuzz |
| Leaky Images: Targeted Privacy Attacks in the Web | Cristian-Alexandru Staicu and Michael Pradel | TU Darmstadt | 2019 | Web;Side Channel |
| MOPT-Optimized Mutation Scheduling for Fuzzers |  |  | 2019 | Fuzz |
| Mobile Private Contact Discovery at Scale | Daniel Kales | Graz University of Technology | 2019 | Mobile |
| The KNOB is Broken: Exploiting Low Entropy in the Encryption Key Negotiation Of Bluetooth BR/EDR | Daniele Antonioli | SUTD | 2019 | Bluetooth;protocol |
| Toward the Analysis of Embedded Firmware through Automated Re-hosting | Eric Gustafson | UCSB | 2019 | Firmware;virtualize |
| An Empirical Study of CORS |  |  | 2018 | CORS |
| Empirical Analysis of Redirection Hijacking in Content Delivery Networks |  |  | 2018 | CDN |
| Fuze |  |  | 2018 |  |
| Fuzzing with Code Fragments |  |  | 2018 | Fuzz |
| Watermarking Deep Neural Networks by Backdooring |  |  | 2018 | Deep Learning |
| Syntia: Synthesizing the Semantics of Obfuscated Code |  |  | 2017 | Obfuscate |
| Stealing Machine Learning Models via Prediction APIs | Florian Tramer |  | 2016 | Model Stealing |
| k-fingerprinting A Robust Scalable Website Fingerprinting Technique |  |  | 2016 | fingerprint |
| Effective Attacks and Provable Defenses for Website Fingerprinting |  |  | 2014 | Fingerprint |
| Dowsing for Overflows: A Guided Fuzzer to Find Buffer Boundary Violations | Istvan Haller | VU University Amsterdam | 2013 | Guied Fuzz |
| ZMap: Fast Internet-wide Scanning and Its Security Applications | Zakir Durumeric | University of Michigan | 2013 | scanner |
| Author Attribute Anonymity by Adversarial Training of Neural Machine Translation |  |  |  |  |
| Automatic Generation of Data-Oriented Exploits |  |  |  |  |
| Fortifying Web Protocols via Browser-Side Security Monitoring |  |  |  |  |
| Generalized Transferability for Evasion and Poisoning Attacks |  |  |  |  |
| MoonShine Optimizing OS Fuzzer Seed Selection with Trace Distillation |  |  |  |  |
| NAVEX Precise and Scalable Exploit Generation for Dynamic Web Applications |  |  |  |  |
| Optimizing seed selection for fuzzing |  |  |  | Fuzz |
| QSYM A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing |  |  |  |  |
| Reverse Engineering Ethereum’s Opaque Smart Contracts |  |  |  |  |
| SoK Make JIT-Spray Great Again |  |  |  |  |
| Towards Principled Bug Bounties and Exploit-Resistant Smart Contracts |  |  |  |  |

## WOOT

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Unicorefuzz: On the Viability of Emulation for Kernelspace Fuzzing | Dominik Maier, Benedikt Radtke, and Bastian Harren, TU Berlin | TU Berlin | 2019 | Unicorn;FUzz |

## Whitepaper

| Title | Authors | Organization | Year | Keywords |
| --- | --- | --- | --- | --- |
| Android Enterprise Security White Paper | Google | Google | 2019 | Android |
| Hardwear 2018 BLE Security Essentials |  | Smartlockpicking.com | 2018 | BLE |

## Disclaimer

To make the paper more accessible, please place the PDF version of the paper in the repo. All pdfs are collected from the Internet. If this article violates your copyright, please contact me to delete it.
