<h1 align="center">
  <br>
  建筑猜猜宝
  <br>
</h1>

<h3 align="center">
建筑猜猜宝 Demo 分支 | <a href="https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme_zh.md">[Beta] 建筑猜猜宝 OCR 分支</a>
</h3>

## ⚜ 功能简介

**简体中文 | [繁體中文](./readme_cht.md) | [日本語](./readme_jp.md) | [English](./readme.md)**

依据多语言提示及正则表达式快速猜测 Hypixel 服务器《建筑猜猜乐》小游戏中的建筑主题。

> **淦翻红牌ldx，一人盲猜虐全场！**

## ⚜ 更新日志

### 2024/04/02 - v4.0

- \[Add\] 繁体中文输入匹配支持
- \[Add\] 日语输入匹配支持
- \[Fix\] 修复了字符 `'` 无法被匹配的问题

  ``` TXT
  # 现在以下主题已经能够被正确匹配
  Santa's Sleigh - 圣诞雪橇
  Santa's Workshop - 圣诞老人工坊
  ```

- \[Opt\] 现在用户可以通过前缀 `@cht` 匹配繁体中文
- \[Opt\] 现在用户可以通过前缀 `@jp` 匹配日语
- \[Opt\] 词库更新

### 2024/03/25 - v3.6

- \[Add\] 新增了词库状态自检
- \[Opt\] 现在用户可以通过前缀 `@sc` 匹配 Shortcut(s)
- \[Opt\] 现在用户可以通过前缀 `@mw` 匹配 Multiword(s)

### 2024/03/17 - v3.5

- \[Add\] 新增了在非多字数结果下的匹配字数提示
- \[Opt\] 现在用户可以在程序内切换输出语言
- \[Opt\] 代码优化

### 2024/02/29 - v3.4

- \[Opt\] 现在用户按下 `Ctrl+C` 也能够正常退出程序
- \[Opt\] 代码优化

### 2024/02/20 - v3.3

- \[Fix\] 修复了字符 `.` 无法被匹配的问题

  ``` TXT
  # 现在以下主题已经能够被正确匹配
  Mrs. Claus - 圣诞老奶奶
  ```

- \[Opt\] 代码优化

### 2024/02/14 - v3.2

- \[Add\] [建筑猜猜宝 OCR 分支链接](https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme_zh.md "GTB-Solver OCR Branch")
- \[Add\] macOS & Linux 系统支持
- \[Add\] 英语 & 简体中文匹配选择支持
- \[Fix\] 修复了用户输入不合法可能造成的 `re.error` 崩溃

### 2024/02/13 - v3.1

- \[Fix\] 修复了运行 `Installation of Dependency Libraries.bat` 安装相关依赖库后仍可能出现依赖库数量不足的问题
- \[Opt\] 更新了获取系统语言的方式以适配 Python 的未来版本

### 2024/02/08 - v3.0

- \[Add\] 简体中文输入匹配支持
- \[Fix\] 修复了字符 `-` 无法被匹配的问题

  ``` TXT
  # 现在以下主题已经能够被正确匹配
  Jack-O-Lantern - 南瓜灯
  T-Rex - 霸王龙
  Trick-or-Treating - 不给糖就捣蛋
  T-Shirt - T恤 - Tricou
  ```

- \[Fix\] 修复了词库列名配置不正确可能造成的 `KeyError` 崩溃

### 2024/02/04 - Demo_202402

- \[Add\] 多语言 `readme` 支持
- \[Add\] 输出萌化模式支持
- \[Fix\] 修复了用户输入不合法可能造成的 `OverflowError` 崩溃
- \[Fix\] 修复了用户输入不合法可能造成的 `re.error` 崩溃
- \[Opt\] 程序输出语言现在默认取决于系统语言
- \[Opt\] 词库更新
- \[Opt\] 代码重构

## ⚜ 前置条件

### 1. 搭建 Python 运行环境

- [前往 Python 官网下载](https://www.python.org/downloads/ "Python Source Releases")
  - 建议安装 Python 3.10 及以上版本，较老版本出现的问题我们将不再维护
  - 首次安装 Python 时请注意勾选 `Add Python x.x to PATH` 添加环境变量

### 2. 安装相关依赖库

- **Windows**：运行 `Installation of Dependency Libraries.bat` 安装相关依赖库
  - 若您位于中国大陆且相关依赖库的下载速度较慢，可尝试通过 `pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/` 指令更换下载源
- **macOS & Linux**：运行 `Installation of Dependency Libraries.sh` 安装相关依赖库
  - 若您位于中国大陆且相关依赖库的下载速度较慢，可尝试通过 `pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/` 指令更换下载源

### 3. 切换 Hypixel 服务器语言至英语（推荐）

- 于 Hypixel 服务器内输入 `/lang en` 即可完成切换

## ⚜ 使用方法

### 1. 运行主程序

- **Windows**：前置条件满足后，运行 `GTB-Solver.bat` 即可
- **macOS & Linux**：前置条件满足后，运行 `GTB-Solver.sh` 即可

### 2. 退出主程序

- 本程序默认重复运行，输入 `0` 或按下 `Ctrl+C` 以退出程序

## ⚜ 匹配规则

1. **数字**：下划线的数量
2. **字母**：会被匹配，可直接插入到数字前后

    - 输入字母时无需区分大小写

3. **简体中文**：会被匹配，可直接插入到数字前后
4. **连字符**：会被匹配，可直接插入到数字前后
5. **空格**：不会被匹配，需手动输入至匹配式内
6. **正则表达式字符**：部分可用
7. **默认匹配**：英语+简体中文
8. **精确匹配**：如无需进行多语言匹配，可在匹配式内加入对应前缀进行精确匹配

    - 匹配内容及对应前缀列表

      | 匹配内容 | 对应前缀 |
      | :----: | :----: |
      | 简体中文 | @zh |
      | 繁体中文 | @cht |
      | 日语 | @jp |
      | 英语 | @en |
      | Shortcut(s) | @sc |
      | Multiword(s) | @mw |

> **提示**：在默认匹配模式下，输入空格、连字符或大于 7 的数字后仅会匹配到英语，输入任意简体中文后仅会匹配到简体中文

## ⚜ 猜测方法（以 Water Bottle 为例）

### 1. 使用数字+字母进行猜测

``` TXT
主题: _____ ______
请输入匹配式: 5 6
该主题字数为 12 个字母
Build Battle - 建筑大师
Chili Pepper - 红辣椒 - Piment
Ender Dragon - 末影龙
Fruit Basket - 果篮 - Obstkorb
Horse Racing - 赛马 - Zavod koni
Horse Riding - 骑马 - Ridning
Light Switch - 照明开关 - Lysbryter
Magic Carpet - 魔毯
Paint Bucket - 油漆桶 - Fargburk
Scuba Diving - 水肺潜水 - Buceo
Snowy Forest - 积雪森林
Solar System - 太阳系 - Solsystem
Swiss Cheese - 瑞士奶酪
Table Tennis - 乒乓球 - Bordtenni
Train Tracks - 铁轨 - Rail - Rautatie
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
```

``` TXT
主题: _a___ ______
请输入匹配式: 1a3 6
该主题字数为 12 个字母
Magic Carpet - 魔毯
Paint Bucket - 油漆桶 - Fargburk
Table Tennis - 乒乓球 - Bordtenni
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
# 在此即可依据玩家建筑大致轮廓进行选择
```

``` TXT
主题: _a___ _o____
请输入匹配式: 1a3 1o4
该主题字数为 2 个字
Water Bottle - 水瓶 - Waterfle
```

### 2. 结合使用正则表达式进行猜测

``` TXT
主题: _a___ ______
请输入匹配式: .a3 .*
Candy Buckets - 糖果篮子
Candy Cane - 糖果手杖 - Acadea
Games Controller - 游戏手柄 - Controller
Magic Carpet - 魔毯
Magic Hat - 魔法帽子 - Joben
Magic Wand - 魔术棒
Magma Cube - 岩浆怪
Paint Bucket - 油漆桶 - Fargburk
Paint Palette - 调色板 - Verfpalet
Paper Airplane - 纸飞机 - Papirfly
Party Hat - 派对帽子
Santa Claus - 圣诞老人
Table Cloth - 桌布 - Dug
Table Tennis - 乒乓球 - Bordtenni
Water Balloon - 水气球 - Gavettone
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
Water Park - 水上乐园
Water Slide - 水上滑梯 - Tobogan
```

``` TXT
主题: _a___ _o____
请输入匹配式: .a3 .o.*
Games Controller - 游戏手柄 - Controller
Water Bottle - 水瓶 - Waterfle
# 在此即可依据玩家建筑大致轮廓进行选择
```

``` TXT
主题: _a___ _o___e
请输入匹配式: .a3 .o.*e
该主题字数为 2 个字
Water Bottle - 水瓶 - Waterfle
```

### 3. 使用简体中文进行猜测

``` TXT
主题: 水_
请输入匹配式: 水1
该主题字数为 2 个字
Crystal - 水晶
Fruit - 水果
Jellyfish - 水母 - Kwal
Kettle - 水壶 - Tetera
Otter - 水獭
Pool - 水池 - Basen
Puddle - 水坑 - Pla
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
Well - 水井
# 在此即可依据玩家建筑大致轮廓进行选择
# 鉴于提示时间靠后，不建议使用简体中文猜测两字及两字以下主题
```

## ⚜ 配置修改

### 1. 修改词库文件路径或更换词库文件

- 默认路径为 `GTB-Solver_main.py` 同文件夹。如需修改词库文件路径或更换词库文件，请在 `GTB-Solver_main.py` 内找到以下代码，替换引号内的路径即可（支持中文路径）

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- 注意：词库文件内应至少存在 English 列（严格区分大小写）

### 2. 修改程序输出语言

- 默认输出语言为系统语言，若系统语言尚未支持，则为英语。如需修改程序默认输出语言，请在 `GTB-Solver_main.py` 内找到以下代码，于引号内加入对应语言代码即可。如仅需暂时性修改程序输出语言，直接输入对应切换指令即可

``` Python
Multi_Lang = ""
```

- 语言代码及切换指令列表

  | 输出语言 | 语言代码 | 切换指令 |
  | :----: | :----: | :----: |
  | 简体中文 | zh | /lang zh |
  | 繁体中文 | cht | /lang cht |
  | 日语 | jp | /lang jp |
  | 英语 | en | /lang en |

### 3. 修改输出萌化状态

- 默认关闭。如需开启输出萌化模式，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
Moe_Mode = False
```

### 4. 修改自动复制状态

- 默认关闭。如需自动复制首个匹配结果至剪贴板，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
Auto_Copy = False
```

## ⚜ 注意事项

- 本项目仅作 Demo 演示之用，所提供的词库文件 `GTB_Thesaurus_Demo.xlsx` 内含 100 对示例词汇及少量 Shortcut(s) & Multiword(s)，您可在原有基础上继续补充使用或依据前述配置修改方法更换词库文件
- 滥用建筑猜猜宝会给您带来不公平的游戏优势！请在有限范围内合理使用，作者对因滥用本程序而导致的封禁问题概不负责