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
`python get_entries.py`
