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

Quickly guess the theme of "Guess The Build" game on Hypixel server based on multi-language hints and regular expressions.

## ⚜ Update Log

### 2024/04/18 - v4.1

- \[Add\] Added word frequency statistical index
  - The word frequency statistical index is weighted by time gradient and calculated from a total of approximately 15,000 rounds of game data provided by multiple players, and it is for reference only
- \[Opt\] The program now defaults to outputting in descending order according to word frequency statistical index
  - If you still need to output according to the original rules, please use the "English" column as the sort basis in the thesaurus file `GTB_Thesaurus_Demo.xlsx`, and sort in ascending order of English letters
- \[Opt\] Thesaurus update

### 2024/04/02 - v4.0

- \[Add\] Traditional Chinese input matching support
- \[Add\] Japanese input matching support
- \[Fix\] Fixed an issue where the character `'` could not be matched

  ``` TXT
  # The following theme(s) have now been able to be matched correctly
  0.25 - Santa's Workshop
  0.00 - Santa's Sleigh
  ```

- \[Opt\] Now the user can match Traditional Chinese by prefixing `@cht`
- \[Opt\] Now the user can match Japanese by prefixing `@jp`
- \[Opt\] Thesaurus update

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
  0.00 - Mrs. Claus
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
  3.00 - T-Shirt - Tricou
  1.75 - T-Rex
  0.00 - Jack-O-Lantern
  0.00 - Trick-or-Treating
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

### 3. Switch Hypixel server language to English (Recommend)

- Type `/lang en` in the Hypixel server to switch

## ⚜ How to Use

### 1. Run the main program

- **Windows**: Once the preconditions are met, run `GTB-Solver.bat`
- **macOS & Linux**: Once the preconditions are met, run `GTB-Solver.sh`

### 2. Exit the main program

- GTB-Solver runs repeatedly by default, enter `0` or press `Ctrl+C` to exit the program

## ⚜ Matching Rules

1. **Number**: Number of underscores
2. **Letter**: Will be matched and can be inserted directly before and after the number

    - Letters are not case sensitive when entering

3. **Hyphen**: Will be matched and can be inserted directly before and after the number
4. **Space**: Will NOT be matched, needs to be manually entered into the matching expression
5. **Regular Expression Characters**: Partially available
6. **Default Matching**: English
7. **Exact Matching**: If there is no need for multi-language matching, you can add the corresponding prefix to the matching expression for exact matching

    - Matching Content and Corresponding Prefix List

      | Matching Content | Corresponding Prefix |
      | :----: | :----: |
      | Simplified Chinese | @zh |
      | Traditional Chinese | @cht |
      | Japanese | @jp |
      | English | @en |
      | Shortcut(s) | @sc |
      | Multiword(s) | @mw |

## ⚜ How to Guess (Taking Water Bottle as an Example)

### 1. Use numbers + letters to guess

``` TXT
Theme: _____ ______
Please enter the matching expression: 5 6
The theme is 12 characters long
16.00 - Water Bucket - Vandspand
12.00 - Table Tennis - Bordtenni
10.00 - Light Switch - Lysbryter
9.50 - Train Tracks - Rail - Rautatie
9.25 - Ender Dragon
8.25 - Paint Bucket - Fargburk
7.75 - Horse Racing - Zavod koni
7.75 - Water Bottle - Waterfle
7.50 - Swiss Cheese
6.75 - Chili Pepper - Piment
6.75 - Magic Carpet
4.50 - Fruit Basket - Obstkorb
4.50 - Scuba Diving - Buceo
4.50 - Solar System - Solsystem
3.00 - Build Battle
2.75 - Horse Riding - Ridning
0.25 - Snowy Forest
```

``` TXT
Theme: _a___ ______
Please enter the matching expression: 1a3 6
The theme is 12 characters long
16.00 - Water Bucket - Vandspand
12.00 - Table Tennis - Bordtenni
8.25 - Paint Bucket - Fargburk
7.75 - Water Bottle - Waterfle
6.75 - Magic Carpet
# Here you can choose according to the general outline of the player's building
```

``` TXT
Theme: _a___ _o____
Please enter the matching expression: 1a3 1o4
The theme is 12 characters long
7.75 - Water Bottle - Waterfle
```

### 2. Guessing in conjunction with the use of regular expressions

``` TXT
Theme: _a___ ______
Please enter the matching expression: .a3 .*
16.00 - Water Bucket - Vandspand
12.00 - Table Tennis - Bordtenni
11.00 - Water Slide - Tobogan
9.50 - Magic Hat - Joben
8.25 - Paint Bucket - Fargburk
7.75 - Water Bottle - Waterfle
7.00 - Candy Cane - Acadea
7.00 - Paper Airplane - Papirfly
6.75 - Magic Carpet
6.50 - Party Hat
5.50 - Magma Cube
5.25 - Water Balloon - Gavettone
5.00 - Games Controller - Controller
4.75 - Paint Palette - Verfpalet
4.75 - Water Park
4.00 - Magic Wand
4.00 - Table Cloth - Dug
0.75 - Santa Claus
0.00 - Candy Buckets
```

``` TXT
Theme: _a___ _o____
Please enter the matching expression: .a3 .o.*
7.75 - Water Bottle - Waterfle
5.00 - Games Controller - Controller
# Here you can choose according to the general outline of the player's building
```

``` TXT
Theme: _a___ _o___e
Please enter the matching expression: .a3 .o.*e
The theme is 12 characters long
7.75 - Water Bottle - Waterfle
```

## ⚜ Configuration Modification

### 1. Modify the path of the thesaurus file or replace the thesaurus file

- The default path is the same folder as `GTB-Solver_main.py`. If you need to modify the path of the thesaurus file or replace the thesaurus file, please find the following code in `GTB-Solver_main.py` and replace the path in quotation marks

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