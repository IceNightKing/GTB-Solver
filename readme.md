<h1 align="center">
  <br>
  GTB-Solver
  <br>
</h1>

<h3 align="center">
GTB-Solver Demo Branch | <a href="https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme.md">[Beta] GTB-Solver OCR Branch</a>
</h3>

## ⚜ Function Introduction

**[简体中文](./readme_zh.md) | [繁體中文](./readme_cht.md) | [日本語](./readme_jp.md) | English**

Quickly guess the theme of "Guess The Build" game on Hypixel server based on English or Simplified Chinese hints and regular expressions.

## ⚜ Update Log

### 2024/03/25 - v3.6

- \[Add\] Added thesaurus self-check
- \[Opt\] Now the user can match Shortcut(s) by prefixing `@sc`
- \[Opt\] Now the user can match Multiword(s) by prefixing `@mw`

### 2024/03/17 - v3.5

- \[Add\] Added matching word count prompt for non-multi-word count result(s)
- \[Opt\] Now the user can switch the output language within the program
- \[Opt\] Code optimization

### 2024/02/29 - v3.4

- \[Opt\] Now the user can exit the program normally by pressing `Ctrl+C`
- \[Opt\] Code optimization

### 2024/02/20 - v3.3

- \[Fix\] Fixed an issue where the character `.` could not be matched

  ``` TXT
  # The following theme(s) have now been able to be matched correctly
  Mrs. Claus
  ```

- \[Opt\] Code optimization

### 2024/02/14 - v3.2

- \[Add\] [GTB-Solver OCR Branch Link](https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme.md "GTB-Solver OCR Branch")
- \[Add\] macOS & Linux system support
- \[Add\] English & Simplified Chinese matching selection support
- \[Fix\] Fixed `re.error` crash that could be caused by illegitimate user inputs

### 2024/02/13 - v3.1

- \[Fix\] Fixed an issue that the number of related dependency libraries may be insufficient even after running `Installation of Dependency Libraries.bat` to install the related dependency libraries
- \[Opt\] Updated the way the system language is fetched to work with future versions of Python

### 2024/02/08 - v3.0

- \[Add\] Simplified Chinese input matching support
- \[Fix\] Fixed an issue where the character `-` could not be matched

  ``` TXT
  # The following theme(s) have now been able to be matched correctly
  Jack-O-Lantern
  T-Rex
  Trick-or-Treating
  T-Shirt - Tricou
  ```

- \[Fix\] Fixed `KeyError` crash that could be caused by incorrectly configured thesaurus column name

### 2024/02/04 - Demo_202402

- \[Add\] Multi-language `readme` support
- \[Add\] Output moe mode support
- \[Fix\] Fixed `OverflowError` crash that could be caused by illegitimate user inputs
- \[Fix\] Fixed `re.error` crash that could be caused by illegitimate user inputs
- \[Opt\] Program output language now depends on system language by default
- \[Opt\] Thesaurus update
- \[Opt\] Code refactoring

## ⚜ Pre-conditions

### 1. Setting up the Python runtime environment

- [Visit the official Python website to download](https://www.python.org/downloads/ "Python Source Releases")
  - It is recommended that you install Python 3.10 and above, bugs in older versions will not be fixed
  - When installing Python for the first time, be sure to check `Add Python x.x to PATH` to add environment variables

### 2. Install the related dependency libraries

- **Windows**: Run `Installation of Dependency Libraries.bat` to install the related dependency libraries
- **macOS & Linux**: Run `Installation of Dependency Libraries.sh` to install the related dependency libraries

### 3. Switch Hypixel server language to English

- Type `/lang en` in the Hypixel server to switch

## ⚜ How to Use

### 1. Run the main program

- **Windows**: Once the preconditions are met, run `GTB-Solver.bat`
- **macOS & Linux**: Once the preconditions are met, run `GTB-Solver.sh`

### 2. Exit the main program

- GTB-Solver runs repeatedly by default, enter `0` or press `Ctrl+C` to exit the program

## ⚜ Matching Rules

1. **Number**: number of underscores
2. **Letter**: will be matched and can be inserted directly before and after the number
    - Letters are not case sensitive when entering
3. **Simplified Chinese**: will be matched and can be inserted directly before and after the number
4. **Hyphen**: will be matched and can be inserted directly before and after the number
5. **Space**: will not be matched, needs to be manually entered into the matching expression
6. **Regular expression characters**: partially available
7. **Default matching**: English + Simplified Chinese
    - If you need to match English only when you enter a purely numeric matching expression: prefix `@en` can be used
    - If you need to match Simplified Chinese only when you enter a purely numeric matching expression: prefix `@zh` can be used

> **Tip**: After entering spaces, hyphens or numbers greater than 7, only English will be matched. After entering any Simplified Chinese, only Simplified Chinese will be matched

## ⚜ How to Guess (Taking Water Bottle as an Example)

### 1. Use numbers + letters to guess

``` TXT
Theme: _____ ______
Please enter the matching expression: 5 6
The theme is 12 characters long in English
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
```

``` TXT
Theme: _a___ ______
Please enter the matching expression: 1a3 6
The theme is 12 characters long in English
Magic Carpet
Paint Bucket - Fargburk
Table Tennis - Bordtenni
Water Bottle - Waterfle
Water Bucket - Vandspand
# Here you can choose according to the general outline of the player's building
```

``` TXT
Theme: _a___ _o____
Please enter the matching expression: 1a3 1o4
The theme is 12 characters long in English
Water Bottle - Waterfle
```

### 2. Guessing in conjunction with the use of regular expressions

``` TXT
Theme: _a___ ______
Please enter the matching expression: .a3 .*
Candy Buckets
Candy Cane - Acadea
Games Controller - Controller
Magic Carpet
Magic Hat - Joben
Magic Wand
Magma Cube
Paint Bucket - Fargburk
Paint Palette - Verfpalet
Paper Airplane - Papirfly
Party Hat
Santa Claus
Table Cloth - Dug
Table Tennis - Bordtenni
Water Balloon - Gavettone
Water Bottle - Waterfle
Water Bucket - Vandspand
Water Park
Water Slide - Tobogan
```

``` TXT
Theme: _a___ _o____
Please enter the matching expression: .a3 .o.*
Games Controller - Controller
Water Bottle - Waterfle
# Here you can choose according to the general outline of the player's building
```

``` TXT
Theme: _a___ _o___e
Please enter the matching expression: .a3 .o.*e
The theme is 12 characters long in English
Water Bottle - Waterfle
```

## ⚜ Configuration Modification

### 1. Modify the path of the thesaurus file or replace the thesaurus file

- The default path is the same folder as `GTB-Solver_main.py`. If you need to modify the path of the thesaurus file or replace the thesaurus file, please find the following code in `GTB-Solver_main.py` and replace the path in quotation marks (Chinese path is supported)

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- Note: There should be at least an "English" column in the thesaurus file (strictly case sensitive)

### 2. Modify the program output language

- The default output language is the system language, or English if the system language is not yet supported. If you need to modify the default output language of the program, please find the following code in `GTB-Solver_main.py` and add the corresponding language code in quotation marks. If you only need to temporarily modify the program output language, you can directly enter the corresponding switching command

``` Python
Multi_Lang = ""
```

- Language Code and Switching Command List

  | Output Language | Language Code | Switching Command |
  | :----: | :----: | :----: |
  | Simplified Chinese | zh | /lang zh |
  | Traditional Chinese | cht | /lang cht |
  | Japanese | jp | /lang jp |
  | English | en | /lang en |

### 3. Modify the output moe status

- The output moe mode is disabled by default. To enable the output moe mode, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
Moe_Mode = False
```

### 4. Modify the automatic copying status

- The automatic copying mode is disabled by default. To automatically copy the first matching result to the clipboard, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
Auto_Copy = False
```

## ⚜ Important Notes

- This project is for Demo ONLY, the provided thesaurus file `GTB_Thesaurus_Demo.xlsx` contains 100 pairs of sample words and a few Shortcut(s) & Multiword(s), you can continue to supplement it on the original basis or replace the thesaurus file according to the aforementioned configuration modification method
- Abuse of GTB-Solver will give you an unfair advantage in the game! Please use it reasonably within a limited scope. The author is NOT responsible for the BAN caused by the abuse of the program