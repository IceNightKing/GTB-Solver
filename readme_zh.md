<h1 align="center">
  <br>
  建筑猜猜宝
  <br>
</h1>

<h3 align="center">
<a href="https://github.com/IceNightKing/GTB-Solver/blob/master/readme_zh.md">建筑猜猜宝 Demo 分支</a> | [Beta] 建筑猜猜宝 OCR 分支
</h3>

<h3 align="center">
<font color="orange">🚫 注意：建筑猜猜宝 OCR 分支目前处于 Beta 测试阶段，尚不具备可用性！ 😇</font>
</h3>

## ⚜ 功能简介

**简体中文 | [繁體中文](./readme_cht.md) | [日本語](./readme_jp.md) | [English](./readme.md)**

依据英语提示及光学字符识别快速猜测 Hypixel 服务器《建筑猜猜乐》小游戏中的建筑主题。

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

### 3. 修改光学字符识别区域

- 定位动作栏上方的主题提示区域，获取左上角与右下角坐标，依照 `配置修改方法 1` 修改光学字符识别区域

### 4. 修改游戏内相关设置

- 为提高识别准确性，建议按照以下步骤修改游戏内相关设置
  - `选项...` > `辅助功能设置...` > `文本背景 : 全局`
  - `选项...` > `聊天设置...` > `文本背景不透明度 : 60%`
  - `选项...` > `聊天设置...` > `宽度 : 40px`

> **提示**：以上为 **Minecraft 1.19** 的相关设置修改方法，仅供参考。若您的实际游戏版本不同，修改方法可能会有所改变

### 5. 切换 Hypixel 服务器语言至英语

- 于 Hypixel 服务器内输入 `/lang en` 即可完成切换

## ⚜ 使用方法

### 1. 运行主程序

- **Windows**：前置条件满足后，运行 `GTB-Solver-OCR.bat` 即可
- **macOS & Linux**：前置条件满足后，运行 `GTB-Solver-OCR.sh` 即可

### 2. 退出主程序

- 本程序默认重复运行，按下 `Ctrl+C` 以退出程序

## ⚜ 识别结果（以 Water Bottle 为例）

``` Python
主题: _____ ______
光学字符识别结果: _____ ______
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

主题: _a___ ______
光学字符识别结果: _a___ ______
Magic Carpet - 魔毯
Paint Bucket - 油漆桶 - Fargburk
Table Tennis - 乒乓球 - Bordtenni
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
# 在此即可依据玩家建筑大致轮廓进行选择

主题: _a___ _o____
光学字符识别结果: _a___ _o____
Water Bottle - 水瓶 - Waterfle
```

## ⚜ 配置修改

### 1. 修改光学字符识别区域

- 默认识别区域为左上角坐标 `(1000, 1200)`、右下角坐标 `(1550, 1300)` 的矩形区域。如需修改光学字符识别区域，请在 `GTB-Solver-OCR_main.py` 内找到以下代码，修改坐标值即可

``` Python
Left, Top = 1000, 1200
Right, Bottom = 1550, 1300
```

- 注意：光学字符识别区域会根据您游戏窗口的大小和位置而产生变化

### 2. 修改重复识别间隔

- 默认识别间隔为 `3.0` 秒。如需修改重复识别间隔，请在 `GTB-Solver-OCR_timer.py` 内找到以下代码，修改数值即可

``` Python
Interval_Time = 3.0
```

### 3. 修改 GPU 加速识别状态

- 默认开启。如需关闭 GPU 加速识别模式，请在 `GTB-Solver-OCR_main.py` 内找到以下代码，替换 `True` 为 `False` 即可

``` Python
GPU_Mode = True
```

- 注意：启用 GPU 加速识别模式需要设备本身具备支持 CUDA 的 NVIDIA GPU，安装合适的 [GPU 驱动程序](https://www.nvidia.cn/Download/index.aspx?lang=cn "NVIDIA Driver Downloads")、[CUDA 工具包](https://developer.nvidia.com/cuda-downloads "NVIDIA CUDA Toolkit Downloads")以及对应版本的 [PyTorch](https://pytorch.org/get-started/locally/ "Install PyTorch Locally")，否则仍将使用 CPU 进行识别

### 4. 修改词库文件路径或更换词库文件

- 默认路径为 `GTB-Solver-OCR_main.py` 同文件夹。如需修改词库文件路径或更换词库文件，请在 `GTB-Solver-OCR_main.py` 内找到以下代码，替换引号内的路径即可（支持中文路径）

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- 注意：词库文件内应至少存在 English 列（严格区分大小写）

### 5. 修改程序输出语言

- 默认输出语言为系统语言，若系统语言尚未支持，则为英语。如需修改程序输出语言，请在 `GTB-Solver-OCR_main.py` 与 `GTB-Solver-OCR_timer.py` 内找到以下代码，于引号内加入对应语言代码即可

``` Python
Multi_Lang = ""
```

- 语言代码列表

  | 输出语言 | 语言代码 |
  | :----: | :----: |
  | 简体中文 | zh |
  | 繁体中文 | cht |
  | 日语 | jp |
  | 英语 | en |

### 6. 修改输出萌化状态

- 默认关闭。如需开启输出萌化模式，请在 `GTB-Solver-OCR_main.py` 与 `GTB-Solver-OCR_timer.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
Moe_Mode = False
```

### 7. 修改自动复制状态

- 默认关闭。如需自动复制首个匹配结果至剪贴板，请在 `GTB-Solver-OCR_main.py` 内找到以下代码，替换 `False` 为 `True` 即可

``` Python
Auto_Copy = False
```

## ⚜ 注意事项

- 本项目仅作 Demo 演示之用，所提供的词库文件 `GTB_Thesaurus_Demo.xlsx` 内含 100 对示例词汇及少量 Shortcut(s) & Multiword(s)，您可在原有基础上继续补充使用或依据前述配置修改方法更换词库文件
- 滥用建筑猜猜宝会给您带来不公平的游戏优势！请在有限范围内合理使用，作者对因滥用本程序而导致的封禁问题概不负责