On average, CollAFL covered 20% more
program paths, found 320% more unique crashes and 260% more
bugs than AFL in 200 hours. In total, CollAFL found 157 new
security bugs with 95 new CVEs assigned.

粗看了一眼 好像主要和AFL的不同在于提出了一个很好的hash算法 解决了AFL计算路径不准的问题

# III.

## A. Coverage Granularity

coverage粒度有三种
- block
    - vuzzer
    - libfuzzer
    - honggfuzz
- edge
    - afl
- path

## B. Trivial Solution for Hash Collision

最直觉的想法是扩大bitmap的size
但是这种方案会带来非常大的性能损耗
