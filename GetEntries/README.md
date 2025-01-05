# 词条自动化获取脚本

# Install
1. python3.9 及以上
2. numpy, pandas, openpyxl, requests  
`pip install --upgrade numpy`  
`pip install --upgrade pandas openpyxl`  
`pip install requests`

# Use
1. 填入变量
* 填入洗孔的 seed 和 index:  
ChangeAbility_seed = ""  
ChangeAbility_index = ""  
* 填入装备的 seed 和 index:  
RandomMainAbility_seed = ""  
RandomMainAbility_index = ""
* 控制获取数据数:  
修改 count(50倍数) 即可，这里是获取100条数据  
index_wash_entries = get_index_wash_entries(ChangeAbility_seed, ChangeAbility_index, count=100)  
index_equipments = get_index_equipments(RandomMainAbility_seed, RandomMainAbility_index, count=100)  
2. 运行  
`python get_entries.py`
