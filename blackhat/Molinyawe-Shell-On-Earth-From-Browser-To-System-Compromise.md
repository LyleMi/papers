回顾

自从Pwn2Own成立以来，比赛逐渐发展到今天的全球舞台。 在一开始的时候，完成exp往往只需要很短的开发时间。 近年来，exploit mitigations提高了漏洞发现和exp开发的成本。

在2013年的时候，Pwn2Own涉及到的技术有下面这些
•    Address Space Layout Randomization (ASLR)
•    Data Execution Prevention (DEP)
•    Stack Cookies
•    Low Fragmentation Heap
•    JavaScript Just-in-Time (JIT) Mitigations
•    Structured Exception Handling Overwrite Protection (SEHOP)
•    Supervisor Mode Execution Protection (SMEP)
•    Application Sandboxing Technology

而随着技术的不断发展，利用技术也越来越复杂

同样的，防御技术也越来越发达，自从2013年以来，浏览器有了越来越多的防御技术

•    VTGuard
•    ForceASLR
•    AppContainer
•    Pool Integrity Checks
•    Kernel ASLR
•    Enhanced Mitigation Experience Toolkit (EMET)
•    PartitionAlloc
•    Java Click-to-Play
•    Control Flow Guard
•    Isolated Heap
•    Memory Protection
•    win32k Access Prevention in Chrome
•    Adobe Flash Isolated Heap
•    Adobe Flash Memory Protection

同样的，沙盒技术也在不断发展，在最开始的时候，挖到漏洞就很容易执行或者提权，但是到后来，提权变得越来越困难。使得参赛者们只有直接通过内核去提权。

## full chain analysis

### Apple Safari Vulnerability to Kernel Execution by Tencent Security Team Shield

这里用了一个UAF和内核race condition提权