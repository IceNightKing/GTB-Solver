# GTB_Solver_EN
依据英语提示及正则表达式快速猜测 Hypixel 服务器《建筑猜猜乐》小游戏中的建筑主题。  
Quickly guess the theme of "Guess The Build" game on Hypixel server based on English hints and regular expressions.  
> **淦翻红牌ldx，一人盲猜虐全场！**  

## 前置条件
### 1. 搭建 Python 运行环境
- [前往 Python 官网下载](https://www.python.org/downloads/ "Python Source Releases")  
  - 建议安装 Python 3.10 及以上版本，较老版本出现的问题我们将不再维护  
  - 首次安装 Python 时请注意勾选 `Add Python x.x to PATH` 添加环境变量  
### 2. 安装相关依赖库
- 运行 `Installation of Dependency Libraries.bat` 安装相关依赖库  
  - 若您位于中国大陆且相关依赖库的下载速度较慢，可尝试通过 `pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/` 指令更换下载源  
### 3. 切换 Hypixel 服务器语言至英语
- 于 Hypixel 服务器内输入 `/lang en` 即可完成切换  

## 使用方法
### 运行主程序
- 前置条件满足后，运行 `GTB_Solver_EN.bat` 即可  

## 猜测方法（以 Water Bottle 为例）
### 1. 使用数字+字母进行猜测
``` Python
主题: _____ ______
请输入部分英语: 5 6
Build Battle - 建筑大师
Chili Pepper - 红辣椒 - Piment
Ender Dragon - 末影龙
Fruit Basket - 果篮 - Obstkorb
Horse Racing - 赛马
Horse Riding - 骑马
Light Switch - 照明开关
Magic Carpet - 魔毯
Paint Bucket - 油漆桶
Scuba Diving - 水肺潜水 - Buceo
Snowy Forest - 积雪森林
Solar System - 太阳系
Swiss Cheese - 瑞士奶酪
Table Tennis - 乒乓球 - Ping Pong
Train Tracks - 铁轨 - Rail - Rautatie
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶

主题: _a___ ______
请输入部分英语: 1a3 6
Magic Carpet - 魔毯
Paint Bucket - 油漆桶
Table Tennis - 乒乓球 - Ping Pong
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶
# 在此即可依据玩家建筑大致轮廓进行选择

主题: _a___ _o____
请输入部分英语: 1a3 1o4
Water Bottle - 水瓶 - Waterfle
```
### 2. 结合使用正则表达式进行猜测
``` Python
主题: _a___ ______
请输入部分英语: .a3 .*
Candy Buckets - 糖果篮子
Candy Cane - 糖果手杖
Games Controller - 游戏手柄
Magic Carpet - 魔毯
Magic Hat - 魔法帽子
Magic Wand - 魔术棒
Magma Cube - 岩浆怪
Paint Bucket - 油漆桶
Paint Palette - 调色板 - Verfpalet
Paper Airplane - 纸飞机 - Papirfly
Party Hat - 派对帽子
Santa Claus - 圣诞老人
Table Cloth - 桌布 - Dug
Table Tennis - 乒乓球 - Ping Pong
Water Balloon - 水气球
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶
Water Park - 水上乐园
Water Slide - 水上滑梯 - Tobogan

主题: _a___ _o____
请输入部分英语: .a3 .o.*
Games Controller - 游戏手柄
Water Bottle - 水瓶 - Waterfle
# 在此即可依据玩家建筑大致轮廓进行选择

主题: _a___ _o___e
请输入部分英语: .a3 .o.*e
Water Bottle - 水瓶 - Waterfle
```

## 配置修改
### 1. 修改词库文件路径或更换词库文件
- 默认路径为 `GTB_Solver_EN_main.py` 同文件夹，如需修改词库文件路径或更换词库文件，请于 `GTB_Solver_EN_main.py` 内找到以下代码，更换引号内的路径即可（支持中文路径）  
``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```
### 2. 修改程序输出语言
- 默认语言为简体中文，如需修改程序输出语言，请于 `GTB_Solver_EN_main.py` 内找到以下代码，更换引号内的语言代码即可  
``` Python
Multi_Lang = "zh"
```
- 语言代码列表  

| 输出语言 | 语言代码 |
| :----: | :----: |
| 简体中文 | zh |
| 繁體中文 | cht |
| 日本語 | jp |
| English | en |
### 3. 修改自动复制状态
- 默认关闭，如需自动复制首个匹配结果至剪贴板，请于 `GTB_Solver_EN_main.py` 内找到以下代码，更换 `False` 为 `True` 即可  
``` Python
Auto_Copy = False
```

## 注意事项
- 本项目仅作 Demo 演示之用，所提供的词库文件 `GTB_Thesaurus_Demo.xlsx` 内含 100 对示例词汇及少量 Shortcut(s) & Multiword(s)，您可在原有基础上继续补充使用或依据前述配置修改方法更换词库文件  
- 滥用 GTB_Solver_EN 会给您带来不公平的游戏优势！请在有限范围内合理使用，作者对因滥用本程序而导致的封禁问题概不负责  
