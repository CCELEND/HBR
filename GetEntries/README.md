# 词条自动化获取脚本  
自动获取词条数据并保存为 Excel 文件，顶级词条行用黄色背景填充
# Install
1. python3.9 及以上
2. numpy, pandas, openpyxl, requests  
`pip install --upgrade numpy`  
`pip install --upgrade pandas openpyxl`  
`pip install requests`

# Use
1. 修改 config.ini 配置文件
* 填入洗孔的 seed 和 index:  
ChangeAbility_seed=  
ChangeAbility_index=  
* 填入装备的 seed 和 index:  
RandomMainAbility_seed=  
RandomMainAbility_index=
* 控制获取数据数:  
修改 DataCount(50倍数) 即可，这里默认是获取100条数据  
DataCount=100
2. 运行
* 获取洗孔和装备的词条:  
`python get_entries.py`
* 只获取洗孔词条:  
`python get_index_wash_entries.py`
* 只获取装备词条:  
`python get_index_equipments.py`
* GUI 的版本：  
`python GetEntriesGUI.py`
* 本地计算真实随机值的版本：
`python GetEntriesGUILocal.py`
# api 测试（开发测试用）
1. 访问：https://hbrapi.fuyumi.xyz/
2. 在浏览器控制台运行下面命令
* 洗词条 api:  
`t = await fetch(
	window.location.href + 'api/ChangeAbility?_seed=' + 洗孔seed + '&_index=' + 洗孔index
),
a = await t.json();
console.log(a);`
* 打装备 api:  
`t = await fetch(
	window.location.href + 'api/RandomMainAbility?_seed=' + 装备seed + '&_index=' + 装备index
),
a = await t.json();
console.log(a);`
# 关于真实随机值
9个条目的区间：（智慧、DP、体力，精神）  
[1, 477218601]  
[477218601, 954437201]  
[954437201, 1431655801]  
[1431655801, 1908874401]  
[1908874401, 2386093001]  
[2386093001, 2863311601]  
[2863311601, 3340530201]  
[3340530201, 3817748801]  
[3817748801, 4294967295]  
7个条目的区间：（职业）  
攻击者：[1, 613566801]  
破盾者：[613566801, 1227133601]  
减益者：[1227133601, 1840700401]  
增益者：[1840700401, 2454267201]  
破坏者：[2454267201, 3067834001]  
治疗者：[3067834001, 3681400801]  
防御者：[3681400801, 4294967295]
# 关于新饰品吊饰
吊饰用的是装备词条，每炼金一次 index+1。顶级词条可以获得+3或者+4的吊饰，概率通过计算得知是大致是：55%、45%。  
+0：0~1,460,288,87  
+1：1,460,288,880\~2,920,577,759  
+2：2,920,577,760\~3,693,671,873  
+3：3,693,671,874\~4,080,218,930  
+4：4,080,218,931\~4,294,967,294  
占比：34%，34%，18%，9%，5%
