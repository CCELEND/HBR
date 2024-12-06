# 图鉴自动化获取脚本
炽焰天穹国服风格 Heaven Burns Red Style Chart 图鉴

# Install
## 1、python3.9 及以上
## 2、selenium3.1.1
pip3 install selenium=3.1.1
## 3、安装最新版本的 chrome 浏览器
## 4、chromedriver 驱动
当前目录下有一个下载好的 chromedriver，版本是：130.0.6723.116 (r1356013)。
如果不能运行就去下载最新的 Stable 稳定的版本：https://googlechromelabs.github.io/chrome-for-testing/

# Use
运行 HBRbrochure.py 即可

# 测试
访问：https://game.bilibili.com/tool/hbr/#/file/more
在浏览器控制台运行下面命令，得到的是风格的 ID：
document.querySelectorAll('div.style-item.card').forEach(element => {
    console.log(element.getAttribute('data-id'));
});

得到 SS 风格前3条 ID：
Array.from(document.querySelectorAll('div.style-item.card')).slice(0, 3).forEach(element => {
        console.log(element.getAttribute('data-id'));
});
