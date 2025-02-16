# 图鉴自动化获取脚本
炽焰天穹国服风格 Heaven Burns Red Style Chart 图鉴

# Install
1. 最新的 python3
2. 安装 selenium  
`pip install selenium`
3. 安装最新版本的 chrome 浏览器
4. 安装 webdriver-manager  
`pip install webdriver-manager`

# Use
双击运行 HBRbrochure.py 即可，要想获取目前国服全部的 SS 风格 ID，请双击运行 get_all_style.py

# 测试（开发测试用）
1. 访问：https://game.bilibili.com/tool/hbr/#/file/more
2. 在浏览器控制台运行下面命令
* 得到风格的 ID：  
`document.querySelectorAll('div.style-item.card').forEach(element => {
    console.log(element.getAttribute('data-id'));
});`

* 得到 SS 风格前3条 ID：  
`Array.from(document.querySelectorAll('div.style-item.card')).slice(0, 3).forEach(element => {
        console.log(element.getAttribute('data-id'));
});`
