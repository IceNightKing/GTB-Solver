<h1 align="center">
  <br>
  GTB-Solver
  <br>
</h1>

<h3 align="center">
<a href="https://github.com/IceNightKing/GTB-Solver/blob/master/readme.md">GTB-Solver Demo Branch</a> | [Beta] GTB-Solver OCR Branch
</h3>

<h3 align="center">
<font color="orange">🚫 Note: GTB-Solver OCR branch is currently in Beta testing and is not yet available! 😇</font>
</h3>

## ⚜ Function Introduction

**[简体中文](./readme_zh.md) | [繁體中文](./readme_cht.md) | [日本語](./readme_jp.md) | English**

Quickly guess the theme of "Guess The Build" game on Hypixel server based on English hints and optical character recognition.

## ⚜ Pre-conditions

### 1. Setting up the Python runtime environment

- [Visit the official Python website to download](https://www.python.org/downloads/ "Python Source Releases")
  - It is recommended that you install Python 3.10 and above, bugs in older versions will not be fixed
  - When installing Python for the first time, be sure to check `Add Python x.x to PATH` to add environment variables

### 2. Install the related dependency libraries

- **Windows**: Run `Installation of Dependency Libraries.bat` to install the related dependency libraries
- **macOS & Linux**: Run `Installation of Dependency Libraries.sh` to install the related dependency libraries

### 3. Modify the optical character recognition area

- Locate the theme hints area above the actionbar, get the coordinates of the upper left and lower right corners, and modify the optical character recognition area according to `Configuration Modification Method 1`

### 4. Modify the relevant in-game settings

- To improve recognition accuracy, it is recommended that you follow the steps below to modify the relevant in-game settings
  - `Options...` > `Accessibility Settings...` > `Text Background: Everywhere`
  - `Options...` > `Chat Settings...` > `Text Background Opacity: 60%`
  - `Options...` > `Chat Settings...` > `Width: 40px`

> **Tip**: The above is the relevant settings modification method for **Minecraft 1.19**, and it is for reference only. If your actual game version is different, the modification method may change

### 5. Switch Hypixel server language to English

- Type `/lang en` in the Hypixel server to switch

## ⚜ How to Use

### 1. Run the main program

- **Windows**: Once the preconditions are met, run `GTB-Solver-OCR.bat`
- **macOS & Linux**: Once the preconditions are met, run `GTB-Solver-OCR.sh`

### 2. Exit the main program

- GTB-Solver runs repeatedly by default, press `Ctrl+C` to exit the program

## ⚜ Recognition Results (Taking Water Bottle as an Example)

``` Python
Theme: _____ ______
Optical character recognition result: _____ ______
Build Battle
Chili Pepper - Piment
Ender Dragon
Fruit Basket - Obstkorb
Horse Racing - Zavod koni
Horse Riding - Ridning
Light Switch - Lysbryter
Magic Carpet
Paint Bucket - Fargburk
Scuba Diving - Buceo
Snowy Forest
Solar System - Solsystem
Swiss Cheese
Table Tennis - Bordtenni
Train Tracks - Rail - Rautatie
Water Bottle - Waterfle
Water Bucket - Vandspand

Theme: _a___ ______
Optical character recognition result: _a___ ______
Magic Carpet
Paint Bucket - Fargburk
Table Tennis - Bordtenni
Water Bottle - Waterfle
Water Bucket - Vandspand
# Here you can choose according to the general outline of the player's building

Theme: _a___ _o____
Optical character recognition result: _a___ _o____
Water Bottle - Waterfle
```

## ⚜ Configuration Modification

### 1. Modify the optical character recognition area

- The default recognition area is a rectangle with coordinates `(1000, 1200)` in the upper left corner and `(1550, 1300)` in the lower right corner. If you need to modify the optical character recognition area, please find the following code in `GTB-Solver-OCR_main.py` and modify the coordinates

``` Python
Left, Top = 1000, 1200
Right, Bottom = 1550, 1300
```

- Note: The optical character recognition area will vary depending on the size and position of your game window

### 2. Modify the repeat recognition interval

- The default recognition interval is `3.0` seconds. If you need to modify the repeat recognition interval, please find the following code in `GTB-Solver-OCR_main.py` and modify the value

``` Python
Interval_Time = 3.0
```

### 3. Modify the GPU acceleration recognition status

- The GPU acceleration recognition mode is disabled by default. To enable the GPU acceleration recognition mode, please find the following code in `GTB-Solver-OCR_main.py` and replace `False` with `True`

``` Python
GPU_Mode = False
```

- Note: Enabling GPU acceleration recognition mode requires that the device has an NVIDIA GPU with CUDA, install the appropriate [GPU Driver](https://www.nvidia.com/Download/index.aspx?lang=en-us "NVIDIA Driver Downloads"), [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads "NVIDIA CUDA Toolkit Downloads"), and the corresponding version of [PyTorch](https://pytorch.org/get-started/locally/ "Install PyTorch Locally"), or it will still use the CPU for recognition

### 4. Modify the path of the thesaurus file or replace the thesaurus file

- The default path is the same folder as `GTB-Solver-OCR_main.py`. If you need to modify the path of the thesaurus file or replace the thesaurus file, please find the following code in `GTB-Solver-OCR_main.py` and replace the path in quotation marks (Chinese path is supported)

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- Note: There should be at least an "English" column in the thesaurus file (strictly case sensitive)

### 5. Modify the program output language

- The default output language is the system language, or English if the system language is not yet supported. If you need to modify the program output language, please find the following code in `GTB-Solver-OCR_main.py`, and add the corresponding language code in quotation marks

``` Python
Multi_Lang = ""
```

- Language Code List

  | Output Language | Language Code |
  | :----: | :----: |
  | Simplified Chinese | zh |
  | Traditional Chinese | cht |
  | Japanese | jp |
  | English | en |

### 6. Modify the output moe status

- The output moe mode is disabled by default. To enable the output moe mode, please find the following code in `GTB-Solver-OCR_main.py`, and replace `False` with `True`

``` Python
Moe_Mode = False
```

### 7. Modify the automatic copying status

- The automatic copying mode is disabled by default. To automatically copy the first matching result to the clipboard, please find the following code in `GTB-Solver-OCR_main.py` and replace `False` with `True`

``` Python
Auto_Copy = False
```

## ⚜ Important Notes

- This project is for Demo ONLY, the provided thesaurus file `GTB_Thesaurus_Demo.xlsx` contains 100 pairs of sample words and a few Shortcut(s) & Multiword(s), you can continue to supplement it on the original basis or replace the thesaurus file according to the aforementioned configuration modification method
- Abuse of GTB-Solver will give you an unfair advantage in the game! Please use it reasonably within a limited scope. The author is NOT responsible for the BAN caused by the abuse of the program