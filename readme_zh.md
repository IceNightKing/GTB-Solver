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

**[한국어](./readme_uni.md) | [Русский](./readme_uni.md) | [Deutsch](./readme_uni.md) | [Français](./readme_uni.md) | [Español](./readme_uni.md) | [Português](./readme_uni.md) | [Italiano](./readme_uni.md)**

依据多语言提示及正则表达式快速猜测 Hypixel 服务器《建筑猜猜乐》小游戏中的建筑主题。

> **淦翻红牌ldx，一人盲猜虐全场！**

## ⚜ 更新日志

### 2024/08/02 - v5.0

- \[Add\] 新增了随机复制模式
- \[Add\] 韩语输入匹配支持
- \[Add\] 俄语输入匹配支持
- \[Add\] 德语输入匹配支持
- \[Add\] 法语输入匹配支持
- \[Add\] 西班牙语输入匹配支持
- \[Add\] 葡萄牙语输入匹配支持
- \[Add\] 意大利语输入匹配支持
- \[Opt\] 现在用户可以通过前缀 `@kor` 匹配韩语
- \[Opt\] 现在用户可以通过前缀 `@ru` 匹配俄语
- \[Opt\] 现在用户可以通过前缀 `@de` 匹配德语
- \[Opt\] 现在用户可以通过前缀 `@fra` 匹配法语
- \[Opt\] 现在用户可以通过前缀 `@spa` 匹配西班牙语
- \[Opt\] 现在用户可以通过前缀 `@pt` 匹配葡萄牙语
- \[Opt\] 现在用户可以通过前缀 `@it` 匹配意大利语
- \[Opt\] 日志辅助处理模式支持处理范围扩充至简体中文、繁体中文、日语、韩语、俄语、德语、法语、西班牙语、葡萄牙语、意大利语、英语
- \[Opt\] 日志辅助处理模式支持对比范围扩充至简体中文、繁体中文、日语、韩语、俄语、德语、法语、西班牙语、葡萄牙语、意大利语、英语、Shortcut(s)、Multiword(s)
- \[Opt\] 词库更新

### 2024/06/03 - v4.3

- \[Add\] 新增了程序状态自检
- \[Opt\] 优化了日志辅助处理模式的输出样式
- \[Opt\] 代码优化

### 2024/05/12 - v4.2

- \[Add\] 新增了日志辅助处理模式
- \[Add\] 新增了主题辅助记录模式
- \[Add\] 新增了半自动发送模式
- \[Opt\] 词库更新

### 2024/04/18 - v4.1

- \[Add\] 新增了词频统计指数
  - 词频统计指数依时间梯度加权计算自多位玩家提供的共计约 15,000 回合的游戏数据，仅供参考
- \[Opt\] 程序现在默认按照词频统计指数降序输出
  - 如仍需按照原规则输出，请自行在词库文件 `GTB_Thesaurus_Demo.xlsx` 内以 English 列为排序依据，按照英语字母升序排序
- \[Opt\] 词库更新

### 2024/04/02 - v4.0

- \[Add\] 繁体中文输入匹配支持
- \[Add\] 日语输入匹配支持
- \[Fix\] 修复了字符 `'` 无法被匹配的问题

  ``` TXT
  # 现在以下主题已经能够被正确匹配
  0.25 - Santa's Workshop - 圣诞老人工坊
  0.00 - Santa's Sleigh - 圣诞雪橇
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
  0.00 - Mrs. Claus - 圣诞老奶奶
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
  3.75 - T-Shirt - T恤 - Tricou
  1.75 - T-Rex - 霸王龙
  0.00 - Jack-O-Lantern - 南瓜灯
  0.00 - Trick-or-Treating - 不给糖就捣蛋
  ```

- \[Fix\] 修复了词库列名设置不正确可能造成的 `KeyError` 崩溃

### 2024/02/04 - Demo_202402

- \[Add\] 多语言 `readme` 支持
- \[Add\] 新增了输出萌化模式
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

### 3. 设置 Hypixel 服务器语言为英语（推荐）

- 于 Hypixel 服务器内输入 `/lang en` 即可完成设置

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
5. **空格**：**不会**被匹配，需手动输入至匹配式内
6. **正则表达式字符**：部分可用
7. **默认匹配**：英语+简体中文
8. **精确匹配**：如无需进行多语言匹配，可在匹配式内加入对应前缀进行精确匹配

    - 匹配内容及对应前缀列表

      | 匹配内容 | 对应前缀 |
      | :----: | :----: |
      | 简体中文 | @zh |
      | 繁体中文 | @cht |
      | 日语 | @jp |
      | 韩语 | @kor |
      | 俄语 | @ru |
      | 德语 | @de |
      | 法语 | @fra |
      | 西班牙语 | @spa |
      | 葡萄牙语 | @pt |
      | 意大利语 | @it |
      | 英语 | @en |
      | Shortcut(s) | @sc |
      | Multiword(s) | @mw |

> **提示**：在默认匹配模式下，输入空格、连字符或大于 7 的数字后仅会匹配到英语，输入任意简体中文后仅会匹配到简体中文

## ⚜ 猜测方法（以 Water Bottle 为例）

### 1. 使用数字+字母进行猜测

``` TXT
主题：_____ ______
请输入匹配式：5 6
该主题字数为 12 个字母
19.75 - Water Bucket - 水桶 - Vandspand
13.50 - Table Tennis - 乒乓球 - Bordtenni
11.50 - Ender Dragon - 末影龙
10.25 - Train Tracks - 铁轨 - Rail - Rautatie
10.00 - Light Switch - 照明开关 - Lysbryter
10.00 - Water Bottle - 水瓶 - Waterfle
9.00 - Paint Bucket - 油漆桶 - Fargburk
9.00 - Swiss Cheese - 瑞士奶酪
8.50 - Horse Racing - 赛马 - Zavod koni
6.75 - Chili Pepper - 红辣椒 - Piment
6.75 - Magic Carpet - 魔毯
6.00 - Scuba Diving - 水肺潜水 - Buceo
5.25 - Fruit Basket - 果篮 - Obstkorb
5.25 - Solar System - 太阳系 - Solsystem
3.75 - Build Battle - 建筑大师
3.50 - Horse Riding - 骑马 - Ridning
0.25 - Snowy Forest - 积雪森林
```

``` TXT
主题：_a___ ______
请输入匹配式：1a3 6
该主题字数为 12 个字母
19.75 - Water Bucket - 水桶 - Vandspand
13.50 - Table Tennis - 乒乓球 - Bordtenni
10.00 - Water Bottle - 水瓶 - Waterfle
9.00 - Paint Bucket - 油漆桶 - Fargburk
6.75 - Magic Carpet - 魔毯
# 在此即可依据玩家建筑大致轮廓进行选择
```

``` TXT
主题：_a___ _o____
请输入匹配式：1a3 1o4
该主题字数为 2 个字
10.00 - Water Bottle - 水瓶 - Waterfle
```

### 2. 结合使用正则表达式进行猜测

``` TXT
主题：_a___ ______
请输入匹配式：.a3 .*
19.75 - Water Bucket - 水桶 - Vandspand
13.50 - Table Tennis - 乒乓球 - Bordtenni
11.75 - Water Slide - 水上滑梯 - Tobogan
10.25 - Magic Hat - 魔法帽子 - Joben
10.00 - Water Bottle - 水瓶 - Waterfle
9.25 - Paper Airplane - 纸飞机 - Papirfly
9.00 - Paint Bucket - 油漆桶 - Fargburk
8.00 - Games Controller - 游戏手柄 - Controller
7.25 - Party Hat - 派对帽子
7.00 - Candy Cane - 糖果手杖 - Acadea
6.75 - Magic Carpet - 魔毯
6.75 - Water Balloon - 水气球 - Gavettone
6.25 - Water Park - 水上乐园
5.50 - Magma Cube - 岩浆怪
5.50 - Paint Palette - 调色板 - Verfpalet
5.50 - Table Cloth - 桌布 - Dug
4.75 - Magic Wand - 魔术棒
0.75 - Santa Claus - 圣诞老人
0.00 - Candy Buckets - 糖果篮子
```

``` TXT
主题：_a___ _o____
请输入匹配式：.a3 .o.*
10.00 - Water Bottle - 水瓶 - Waterfle
8.00 - Games Controller - 游戏手柄 - Controller
# 在此即可依据玩家建筑大致轮廓进行选择
```

``` TXT
主题：_a___ _o___e
请输入匹配式：.a3 .o.*e
该主题字数为 2 个字
10.00 - Water Bottle - 水瓶 - Waterfle
```

### 3. 使用简体中文进行猜测

``` TXT
主题：水_
请输入匹配式：水1
该主题字数为 2 个字
19.75 - Water Bucket - 水桶 - Vandspand
10.00 - Water Bottle - 水瓶 - Waterfle
8.50 - Jellyfish - 水母 - Kwal
4.25 - Pool - 水池 - Basen
3.75 - Fruit - 水果
2.25 - Crystal - 水晶
2.00 - Well - 水井
1.75 - Otter - 水獭
1.50 - Puddle - 水坑 - Pla
1.25 - Kettle - 水壶 - Tetera
# 在此即可依据玩家建筑大致轮廓进行选择
# 鉴于提示时间靠后，不建议使用简体中文猜测两字及两字以下主题
```

## ⚜ 配置修改

### 1. 修改词库文件路径或更换词库文件

- 默认路径为 `GTB-Solver_main.py` 同文件夹。如需修改词库文件路径或更换词库文件，请在 `GTB-Solver_main.py` 内找到以下代码，替换引号内的路径即可（支持中文路径）

``` Python
GTB_THESAURUS = r"GTB_Thesaurus_Demo.xlsx"
```

- **注意**：词库文件内应至少存在 English 列（严格区分大小写）

### 2. 修改程序输出语言

- 默认输出语言为系统语言，若系统语言尚未支持，则为英语。如需修改程序默认输出语言，请在 `GTB-Solver_main.py` 内找到以下代码，于引号内加入对应语言代码即可。如仅需暂时性修改程序输出语言，直接输入对应切换指令即可

``` Python
MULTI_LANG = ""
```

- 语言代码及切换指令列表

  | 输出语言 | 语言代码 | 切换指令 |
  | :----: | :----: | :----: |
  | 简体中文 | zh | /lang zh |
  | 繁体中文 | cht | /lang cht |
  | 日语 | jp | /lang jp |
  | 韩语 | kor | /lang kor |
  | 俄语 | ru | /lang ru |
  | 德语 | de | /lang de |
  | 法语 | fra | /lang fra |
  | 西班牙语 | spa | /lang spa |
  | 葡萄牙语 | pt | /lang pt |
  | 意大利语 | it | /lang it |
  | 英语 | en | /lang en |

### 3. 修改输出萌化模式状态

- 默认关闭。如需开启输出萌化模式，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
MOE_MODE = False
```

### 4. 修改自动复制模式状态

- 默认关闭。如需自动复制首个匹配条目至剪贴板，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
AUTO_COPY = False
```

### 5. 修改随机复制模式状态

- 默认关闭。如需在自动复制时随机复制首个匹配条目的简体中文、繁体中文、日语、韩语、俄语、德语、法语、西班牙语、葡萄牙语、意大利语表述之一至剪贴板，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
RAC_MODE = False
```

- **注意**：启用随机复制模式需要一并开启自动复制模式。自动复制模式的开启方法详见 `配置修改方法 4`

### 6. 修改日志辅助处理模式状态

- 默认关闭。如需实时输出游戏相关状态，并将游戏内玩家猜测的主题与已经输出的匹配条目进行对比，经筛选后重新输出，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
LAP_MODE = False
```

- 输出样式示例（其中，`3` 为当前回合数，`10` 为总回合数，`NoticeYou` 为当前回合建筑师名称，`12` 为包含空格的当前回合主题字数）

  ``` TXT
  [3/10] NoticeYou(12)
  ```

- 对比猜测示例（以 Shopping Bag 为例）

  ``` TXT
  主题：________ ___
  [3/10] NoticeYou(12)
  请输入匹配式：8 3
  该主题字数为 12 个字母
  9.00 - Shopping Bag - 购物袋 - Handlepose
  7.25 - Sleeping Bag - 睡袋 - Sovepose
  4.75 - Baseball Bat - 棒球棍
  ```

  ``` TXT
  [3/10] NoticeYou(12)
  NoticeSC: sovepose
  检测到有玩家猜测了主题 睡袋 但未猜对，即将据此输出筛选后的匹配条目
  9.00 - Shopping Bag - 购物袋 - Handlepose
  4.75 - Baseball Bat - 棒球棍
  ```

  ``` TXT
  [3/10] NoticeYou(12)
  NoticeJP: 野球バット
  检测到有玩家猜测了主题 睡袋、棒球棍 但未猜对，即将据此输出筛选后的匹配条目
  9.00 - Shopping Bag - 购物袋 - Handlepose
  # 在此即可直接盲猜出正确主题
  ```

- **提示**：日志辅助处理模式支持处理服务器语言设置为简体中文、繁体中文、日语、韩语、俄语、德语、法语、西班牙语、葡萄牙语、意大利语、英语的情况，并支持对比玩家使用简体中文、繁体中文、日语、韩语、俄语、德语、法语、西班牙语、葡萄牙语、意大利语、英语、Shortcut(s)、Multiword(s) 猜测的主题。若您的词库文件版本不同，实际对比效果可能会发生改变

### 7. 修改日志文件路径

- 默认路径为 `C:\Minecraft\.minecraft\logs\latest.log`，仅供参考，请根据实际情况进行修改。如需修改日志文件路径，请在 `GTB-Solver_main.py` 内找到以下代码，替换引号内的路径即可（支持中文路径）

``` Python
LOG_FILE = r"C:\Minecraft\.minecraft\logs\latest.log"
```

### 8. 修改日志文件重复读取间隔

- 默认间隔为 `0.05` 秒。如需修改日志文件的重复读取间隔，请在 `GTB-Solver_main.py` 内找到以下代码，修改数值即可

``` Python
LAP_INTERVAL = 0.05
```

- **提示**：建议将该间隔设置在 `0.01` ~ `0.20` 秒的范围内。若您发现开启日志辅助处理模式后游戏相关状态更新不及时或未能成功抓取玩家猜测的主题，可适当减小重复读取间隔

### 9. 修改游戏结束时自定义复制内容

- 默认复制内容为 `Good Game`。如需修改游戏结束时自定义复制内容，请在 `GTB-Solver_main.py` 内找到以下代码，替换引号内的内容即可（支持中文）

``` Python
CUSTOM_CONTENT = "Good Game"
```

- **注意**：自动复制模式与日志辅助处理模式开启时，自定义内容才会被复制。自动复制模式的开启方法详见 `配置修改方法 4`，日志辅助处理模式的开启方法详见 `配置修改方法 6`

### 10. 修改主题辅助记录模式状态

- 默认关闭。如需在正确主题出现后将其记录至辅助记录文件内以便后续统计处理，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
TAR_MODE = False
```

- **注意**：启用主题辅助记录模式需要一并开启日志辅助处理模式。日志辅助处理模式的开启方法详见 `配置修改方法 6`

### 11. 修改主题辅助记录文件路径

- 默认路径为 `GTB-Solver_main.py` 同文件夹。如需修改主题辅助记录文件路径，请在 `GTB-Solver_main.py` 内找到以下代码，替换引号内的路径即可（支持中文路径）

``` Python
GTB_TAR_FILE = r"GTB_TAR_File.txt"
```

### 12. 修改半自动发送模式状态

- 默认关闭。如需在输入匹配式后自动发送首个匹配条目至游戏内，请在 `GTB-Solver_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
SAS_MODE = False
```

- **注意**：启用半自动发送模式需要一并开启自动复制模式与日志辅助处理模式。自动复制模式的开启方法详见 `配置修改方法 4`，日志辅助处理模式的开启方法详见 `配置修改方法 6`

### 13. 修改半自动发送间隔

- 默认间隔为 `2.0` 秒。如需修改两次发送间的时间间隔，请在 `GTB-Solver_main.py` 内找到以下代码，修改数值即可

``` Python
SAS_INTERVAL = 2.0
```

- **提示**：该间隔是在减去重复猜测剩余冷却时间后额外的暂停时间，建议将该间隔设置在 `1.0` ~ `5.0` 秒的范围内。该间隔设置过小可能会触发服务器反垃圾信息机制而被踢出游戏

### 14. 修改游戏窗口名称

- 默认激活包含 `Minecraft` 字样的第一个窗口。若您使用了非原版客户端，请在 `GTB-Solver_main.py` 内找到以下代码，替换引号内的内容为游戏窗口名称即可（支持中文）

``` Python
WINDOW_TITLE = "Minecraft"
```

## ⚜ 注意事项

- 本项目仅作 Demo 演示之用，所提供的词库文件 `GTB_Thesaurus_Demo.xlsx` 内含 100 对示例词汇及少量 Shortcut(s) & Multiword(s)，您可在原有基础上继续补充使用或依据前述配置修改方法更换词库文件
- 滥用建筑猜猜宝会给您带来不公平的游戏优势！请在有限范围内合理使用，开发者对因滥用本程序而导致的封禁问题概不负责