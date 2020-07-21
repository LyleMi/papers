title: P2IM: Scalable and Hardware-independent Firmware Testing via
Automatic Peripheral Interface Modeling
authors: Bo Feng, Alejandro Mera, Long Lu
organizations: Northeastern University

# Abstract

对固件设备的测试通常受限于硬件支持，难以规模化，这在一定程度上导致了IoT漏洞的泛滥。文章中提出了一种方法，可以执行。P2IM。

用70个样例固件和10个真实设备的固件，包括无人机、机器人、PLC。
在没有人工辅助的情况下，可以执行79%的固件。
找到了7个unique的bug。

# 背景

文章主要目标是微控制器（Microcontrollers, MCU）。
这些是在特定场景下功耗更优的机器。
MCU的固件通常包含：设备驱动、微型操作系统、系统库、一些特殊的逻辑/应用。

## 困难

### 硬件依赖

大部分之前的工作都依靠硬件，但是目前的硬件仿真并不完备，会在相当程度上影响Fuzz效率。使用实体设备的话，在规模化时又会遇到问题。

### 大量外设

每一个固件都会和大量的外设有交互。
这些外设是MCU厂商自定制的，有不同的接口和交互方式。
因此通常需要不同的模拟器。

### 多样化的系统设计

和平常使用的操作系统不同，MCU设备会使用更多的自定制系统/系统库。
这在模糊测试中也是需要考虑的。

### 不完整的测试接口

普通的程序是基于标准I/O或文件，但是固件大部分是从外设中读取的。

## Processor-Peripheral Interfaces

外设有芯片上的 也有芯片外的 (on-chip / off-chip)
文章仅考虑芯片上的。
因为芯片无法直接控制 off-chip

# Abstract Model Definition

## Register Category, Access Patterns and Handling

- Control Registers
    - Access pattern
    - Access handling
- Status Registers
    - Access pattern
    - Access handling
- Data Registers
    - Access pattern
    - Access handling
- Control-Status Registers
    - Access pattern
    - Access handling

## Interrupt Firing

# Automatic Model Instantiation

- identified memory mapped registers, their memory locations, and types
- the access handling strategies for each type of registers
- the enabled interrupts and the firing strategy

## Register Identification

## Register Access Handling & Explorative Execution

## P2IM Implementation

Our implementation includes 2,202 lines of
C code added to QEMU (mostly for dynamic firmware
execution instrumentation), 173 lines of C code for fuzzer
integration, and 1,199 lines of Python code for the explorative
execution part of P2 IM. 

# Evaluation & Fuzzing Results

- whether it satisfies P2IE when executing firmware for different MCU with different OSes
- how its runtime performance is in practice
- whether it can perform fuzz-testing on real firmware in a fully emulated fashion

## Unit Tests on MCU Peripherals & OSes

We also selected 3 widely used MCU
OS/system libraries, (NuttX, RIOT, and Arduino) and 3 target
MCU SoCs (STM32 F103RB, NXP MK64FN1M0VLL12,
and Atmel SAM3X8E)

# 相关研究

IO forwarding 速度

# 参考链接

- [P2IM: Scalable and Hardware-independent Firmware Testing via Automatic Peripheral Interface Modeling](https://www.usenix.org/conference/usenixsecurity20/presentation/feng)
