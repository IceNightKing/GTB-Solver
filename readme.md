# GTB_Solver_EN

**[简体中文](./readme_zh.md) | [繁體中文](./readme_cht.md) | [日本語](./readme_jp.md) | English**

Quickly guess the theme of "Guess The Build" game on Hypixel server based on English hints and regular expressions.  

## Update Log
### 2024/02/04 - Demo_202402
- \[Add\] Multi-language `readme` support  
- \[Add\] Output moe mode support  
- \[Fix\] Fixed `OverflowError` crash that could be caused by illegitimate user inputs  
- \[Fix\] Fixed `re.error` crash that could be caused by illegitimate user inputs  
- \[Opt\] Program output language now depends on system language by default  
- \[Opt\] Thesaurus update  
- \[Opt\] Code refactoring  

## Pre-conditions
### 1. Setting up the Python runtime environment
- [Go to the official Python website to download](https://www.python.org/downloads/ "Python Source Releases")  
  - It is recommended that you install Python 3.10 and above, bugs with older versions will no longer be maintained  
  - When installing Python for the first time, be sure to check `Add Python x.x to PATH` to add environment variables  
### 2. Install the related dependency libraries
- Run `Installation of Dependency Libraries.bat` to install the related dependency libraries  
### 3. Switch Hypixel server language to English
- Type `/lang en` in the Hypixel server to switch  

## How to Use
### Run the main program
- Once the preconditions are met, run `GTB_Solver_EN.bat`  

## How to Guess (Taking Water Bottle as an Example)
### 1. Use numbers + letters to guess
``` Python
Theme: _____ ______
Please enter the matching expression: 5 6
Build Battle
Chili Pepper - Piment
Ender Dragon
Fruit Basket - Obstkorb
Horse Racing
Horse Riding
Light Switch
Magic Carpet
Paint Bucket
Scuba Diving - Buceo
Snowy Forest
Solar System
Swiss Cheese
Table Tennis - Ping Pong
Train Tracks - Rail - Rautatie
Water Bottle - Waterfle
Water Bucket

Theme: _a___ ______
Please enter the matching expression: 1a3 6
Magic Carpet
Paint Bucket
Table Tennis - Ping Pong
Water Bottle - Waterfle
Water Bucket
# Here you can choose according to the general outline of the player's building

Theme: _a___ _o____
Please enter the matching expression: 1a3 1o4
Water Bottle - Waterfle
```
### 2. Guessing in conjunction with the use of regular expressions
``` Python
Theme: _a___ ______
Please enter the matching expression: .a3 .*
Candy Buckets
Candy Cane
Games Controller
Magic Carpet
Magic Hat
Magic Wand
Magma Cube
Paint Bucket
Paint Palette - Verfpalet
Paper Airplane - Papirfly
Party Hat
Santa Claus
Table Cloth - Dug
Table Tennis - Ping Pong
Water Balloon
Water Bottle - Waterfle
Water Bucket
Water Park
Water Slide - Tobogan

Theme: _a___ _o____
Please enter the matching expression: .a3 .o.*
Games Controller
Water Bottle - Waterfle
# Here you can choose according to the general outline of the player's building

Theme: _a___ _o___e
Please enter the matching expression: .a3 .o.*e
Water Bottle - Waterfle
```

## Configuration Modification
### 1. Modify the path of the thesaurus file or replace the thesaurus file
- The default path is the same folder as `GTB_Solver_EN_main.py`. If you need to modify the path of the thesaurus file or replace the thesaurus file, please find the following code in `GTB_Solver_EN_main.py` and replace the path in quotation marks (Chinese path is supported)  
``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```
### 2. Modify the program output language
- The default output language is the system language, or English if the system language is not yet supported. If you need to modify the program output language, please find the following code in `GTB_Solver_EN_main.py` and add the corresponding language code in quotation marks  
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

### 3. Modify the output moe status
- The output moe status is turned off by default. To enable the output moe mode, please find the following code in `GTB_Solver_EN_main.py` and replace `False` with `True`  
``` Python
Moe_Mode = False
```
### 4. Modify the automatic copying status
- The automatic copying status is turned off by default. To automatically copy the first matching result to the clipboard, please find the following code in `GTB_Solver_EN_main.py` and replace `False` with `True`  
``` Python
Auto_Copy = False
```

## Important Notes
- This project is for Demo ONLY, the provided thesaurus file `GTB_Thesaurus_Demo.xlsx` contains 100 pairs of sample words and a few Shortcut(s) & Multiword(s), you can continue to supplement it on the original basis or replace the thesaurus file according to the aforementioned configuration modification method  
- Abuse of GTB_Solver_EN will give you an unfair advantage in the game! Please use it reasonably within a limited scope. The author is NOT responsible for the BAN caused by the abuse of the program  