## 1. Design and implementation of Mandatory Integrity Control

强制完整性控制是Vista引入的。
在该模式中，每个对象都有access control entry(ACE) 在 system access control list (sacl)

sid则表示了这些对象的完整性等级

在访问一些有权限要求的对象之前，就用sid去检查

- no write up 低权限不可以写高权限的文件/内存/...
- no read up 低权限不可以读高权限的文件/内存/...
- no exeucte up

共有六个权限等级：Un-trusted, Low, Medium, High, System, Protected (used for digital right management)

| Intergrity Level | User |
| -------------------- | ------------- |
| System | Local System / NT Services | 
| High | Elevated Administrator | 
| Medium | Un-elevated Administrator / Limited Users |

父进程可以拉起和自己相同或更低完整性的子进程

有两种访问权限，一种是通用的权限（读、写、执行），另一种是对象特有的权限（读文件、终止进程、）

用下面这样的结构来描述对应的权限

```c
typedef struct _GENERIC_MAPPING {
ACCESS_MASK GenericRead;
ACCESS_MASK GenericWrite;
ACCESS_MASK GenericExecute;
ACCESS_MASK GenericAll;
} GENERIC_MAPPING;
typedef GENERIC_MAPPING *PGENERIC_MAPPING
```

## 2. Design and implementation of Protected Mode Internet Explorer

在ie里面，每个网页都以独立tab运行，这些进程互相独立，且都是低完整性
broker进程则是中或者高完整性

IE引入了一个中间层，hook了createProcess/CoCreateInstance/CoGetClassObject等函数，来使得broker可以用中或者低权限来调用一系列的api

broker拉起进程的时候有一个key-value对，会有不同的行为

| Value | Result | Example |
| ----- | ------ | ------- |
| 3 | silently launch as medium | winword |
| 2 | prompts user fofr permission | Default |
| 1 | silently launch as low | iexplore |
| 0 | prevent | cmd |  

对ie7 8, 有一个default policy

| Zone | Policy |
| ---- | ------ |
| Internet | On |
| Local Intranet | Off |
| Trusted Sites | Off |
| Restricted Sites | On |
| Local Computer | Off |

## 3. Generic Attack Patterns against Protected Mode Internet Explorer

Attack Methods:

- Spoofing a website in the Trust Sites List
- Having a Web server addr which is recongised as a member of the Local Intranet ZONE
- xss

另外，任何的url解析的bug
InternetSecurityManager::MapUrlToZone() 都可以造成权限提升

mic没有对本地socket做限制，所以这里可以起一个local network，达到medium

> 等下  可以连smb的话  岂不是可以双星等一系列神洞

在同一个用户下，medium完整性和high完整性有很多攻击向量

一种攻击方式是在kernel object namespace的BaseNameObjects中用name squatting attacks. In this attack, an object with a fixed name can be created which is then opened by an application that trusts the object not to be malicious by virtue of it existing in the local namespace (which was previously a reasonable assumption). This issue has been given as an example of why Protected Mode is not a security boundary by Microsoft.

Another vector is through leaked or duplicated handles. Access control decisions are made at the point that an object is opened, so existing handles may provide access to resources that are only accessible to more privileged contexts if they are transferred between processes. Handles in low integrity processes which have write access rights to higher integrity objects can be considered privileged.
It was through this vector that Skywing escaped from Protected Mode using a leaked handle

The last vector is through objects which are deliberately shared between low integrity processes and higher integrity processes. This includes the Window Station kernel object which is shared between all processes within the same interactive logon session. With full access to the Window Station, low integrity processes also have access to the Global Atom Table, Window Station properties, the user’s clipboard and the “\Default” Desktop object. Such objects can be detected through a tool written as part of this research that locates objects open in low and higher integrity processes; to determine if two handles refer to the same object, the kernel mode pointers to the object’s data structure are compared.

## 4. Bypassing Protected Mode Internet Explorer

从low提权到medium，一个需要考虑的问题是需要找到一个没有用户交互的提权方式。

