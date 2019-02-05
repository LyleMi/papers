很神奇的用timing attack读图片的文章

## Thinking in Frames - using requestAnimationFrame to time browser operations

这里用到了``window.requestAnimationFrame``
这个函数是为了创建比较流畅的动画

## Browser History Sniffing

### Detecting Redraw Events

```
<a href="http://www.google.com" id="link1">############</a>
<script>
var el = document.getElementById('link1');
el.href = 'http://www.yahoo.com';
// below lines are required for Chrome to force style update
el.style.color = 'red';
el.style.color = '';
</script>
```

非常厉害的思路 改掉href和style 强制浏览器刷新页面 看重绘时间

#### Method 1 - Asynchronous URL Lookup

- 插入一堆link指向同一个url
- 用requestAnimationFrame计时
- 猜测是否发生了重绘

#### Method 2 - Changing Link Targe

- 插入一堆link指向同一个肯定没有访问过的url
- 更新这些url
- 用requestAnimationFrame计时

#### Method 4 - Binary chop history sniffing

- 二分
- 为了比较多的时候

## CSS, SVG and Filters

SVG的filter在ie上是用GPU加速的 但是FF和Chrome是用C++实现的

// 这篇文章非常硬啊 是怼了浏览器源码的