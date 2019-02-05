这篇的方向是防Timing Attack

文章认为 一次timing attack 有三个要素 一个是攻击者 一个是要获取的目标 一个是时间的参照物 那么一个很直白的想法就是把这几个要素区分开

提了一个RF（reference frames）的概念，由OS实现，每个RF有独立的时钟

## 2. Threat Model

这里从三个方面来展现威胁模型

### In-scope Attacks

- JavaScript Performance Fingerprinting. 
- Inference of Cross-origin Resource via Loading Time
    - 比如 twitter load的时间就可以猜大概有多少好友
- Inference of Image Contents via SVG Filtering

### A Motivating Example

- The synchronous attack
- The asynchronous attack

这种attack 大意是在一个performence.now的时间范围内，搞多个count++，来分割时间片

```
function nextEdge() {
    // 跑完一个.now 因为可能是从中间开始的
    start = performance.now();
    count = 0;

    do {
        count++;
    } while (start == performance.now());

    return count;
}

function fingerprinting() {
    nextEdge();
    fingerprint = nextEdge();
}

function sideChannelSync() {
    fingerprint = fingerprinting();
    nextEdge();
    start = performance.now();
    targetSecret();
    stop = performance.now();
    remain = nextEdge();
    duration = (stop - start) + (fingerprint - remain) /
        fingerprint * grain;
}
total = 0;

function countFunc() { total++; }

function callback() { duration = total * u; }

function sideChannelAsync() {
    targetSecretAsync(callback);
    setInterval(countFunc, u);
}
```

### Out-of-scope Attacks

- Server-side
- User-related

## ref

an adversary can infer the size of an external, cross-site resource based on the loading time [45,46]
a website can fingerprint the type of the browser based on the performance of JavaScript [33, 34]
two adversaries can talk to each other via a covert channel [38,45]
Stone[44] shows that an adversary can apply an SVG filter on an image and infer the contents based on how long the filtering process takes
clock-edge technique invented by Kohlbrenner and Shacham [26]