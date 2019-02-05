ACG and CIG防止了加载不受信任的代码。
所以这篇文章选择了绕过。

CFG does a good job in stopping most code-reuse attacks through

control-flow hijacking (ROP etc.). However, because CFG is a coarse-grained CFI implementation and the check itself is primarily enforced

in user mode, it is subjected to various bypasses.

Once CFG is breached, we have two options to achieve arbitrary code execution:
    • ROP only
    • Interactive runtime