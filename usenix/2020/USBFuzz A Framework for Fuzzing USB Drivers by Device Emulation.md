# 2. Background

## 2.1 USB Architecture

USB drivers:

- probe routine to initialize the driver
- function routines to interface with other subsystems

## 2.2 USB Security Risks

- Attacks on implicit trust
- Electrical attacks
- Attacks on software vulnerabilities

## 2.3 Fuzzing the USB Interface

# 3. Threat Model

有一个敌手通过USB接口进行攻击

# 4. USBFuzz Design

Approach I: using dedicated hardware

Approach II: data injection in IO stack

usb-fuzzer[16] 改 IO 栈
dummy hcd

PeriScope [50] 改 MMIO / DMA 

*设计目标*

- Low Cost
- Portability
- Minimal Required Knowledge
