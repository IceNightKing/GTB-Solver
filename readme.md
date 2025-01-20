<h1 align="center">
  <br>
  GTB-Solver
  <br>
</h1>

<h3 align="center">
GTB-Solver Demo Branch | <a href="https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme.md">[Beta] GTB-Solver OCR Branch</a>
</h3>

## ⚜ Function Introduction

**[简体中文](./readme_zh.md "简体中文(zh)") | [繁體中文](./readme_cht.md "繁體中文(cht)") | [日本語](./readme_jp.md "日本語(jp)") | [한국어](./readme_uni.md#한국어 "한국어(kor)") | [Русский](./readme_uni.md#русский "Русский(ru)") | [Deutsch](./readme_uni.md#deutsch "Deutsch(de)") | [Français](./readme_uni.md#français "Français(fra)") | [Español](./readme_uni.md#español "Español(spa)") | [Português](./readme_uni.md#português "Português(pt)") | [Italiano](./readme_uni.md#italiano "Italiano(it)") | English**

Quickly guess the theme of "Guess The Build" game on Hypixel server based on multi-language hints and regular expressions.

<details>
  <summary>View Update Log</summary>

### 2025/01/20 - v5.1

- \[Add\] Added player warning control mode
- \[Add\] Added player warning control enhanced mode
- \[Fix\] Fixed `NameError` crash caused by user setting `MULTI_LANG = "zh"`
- \[Opt\] Adapted the newly added chat titles for "Build Battle" game mode on Hypixel server
- \[Opt\] The program now compares the number of characters corresponding to the matching expression with the number of characters in the current round theme captured by log assisted processing mode, and sends a notification if the two are not equal
- \[Opt\] Optimized some translations of program output languages
- \[Opt\] Thesaurus update

### 2024/08/02 - v5.0

- \[Add\] Added random copying mode
- \[Add\] Korean input matching support
- \[Add\] Russian input matching support
- \[Add\] German input matching support
- \[Add\] French input matching support
- \[Add\] Spanish input matching support
- \[Add\] Portuguese input matching support
- \[Add\] Italian input matching support
- \[Opt\] Now the user can match Korean by prefixing `@kor`
- \[Opt\] Now the user can match Russian by prefixing `@ru`
- \[Opt\] Now the user can match German by prefixing `@de`
- \[Opt\] Now the user can match French by prefixing `@fra`
- \[Opt\] Now the user can match Spanish by prefixing `@spa`
- \[Opt\] Now the user can match Portuguese by prefixing `@pt`
- \[Opt\] Now the user can match Italian by prefixing `@it`
- \[Opt\] The log assisted processing mode supports processing in Simplified Chinese, Traditional Chinese, Japanese, Korean, Russian, German, French, Spanish, Portuguese, Italian and English
- \[Opt\] The log assisted processing mode supports comparing in Simplified Chinese, Traditional Chinese, Japanese, Korean, Russian, German, French, Spanish, Portuguese, Italian, English, Shortcut(s) and Multiword(s)
- \[Opt\] Thesaurus update

### 2024/06/03 - v4.3

- \[Add\] Added program self-check
- \[Opt\] Optimized the output style of log assisted processing mode
- \[Opt\] Code optimization

### 2024/05/12 - v4.2

- \[Add\] Added log assisted processing mode
- \[Add\] Added theme auxiliary recording mode
- \[Add\] Added semi-automatic sending mode
- \[Opt\] Thesaurus update

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
  5.00 - Farmer's Market
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
  5.00 - Sci-fi
  4.50 - T-Shirt - Tricou
  1.75 - T-Rex
  0.00 - Jack-O-Lantern
  0.00 - Trick-or-Treating
  ```
- \[Fix\] Fixed `KeyError` crash that could be caused by incorrectly configured thesaurus column name

### 2024/02/04 - Demo_202402

- \[Add\] Multi-language `readme` support
- \[Add\] Added output moe mode
- \[Fix\] Fixed `OverflowError` crash that could be caused by illegitimate user inputs
- \[Fix\] Fixed `re.error` crash that could be caused by illegitimate user inputs
- \[Opt\] Program output language now depends on system language by default
- \[Opt\] Thesaurus update
- \[Opt\] Code refactoring

</details>

## ⚜ Innovation Points

🔹 Supports guessing using regular expressions  
🔹 Adapts multilingual thesaurus and supports guessing using multiple languages  
🔹 Supports comparing themes that have already been guessed by in-game players to avoid repeated guesses  
🔹 The default output is in descending order according to word frequency statistical index, which improves the guessing correct rate  
🔹 Supports avoiding players at the top of the wins leaderboard  

## ⚜ Pre-conditions

### 1. Set up the Python runtime environment

- [Visit the official Python website to download](https://www.python.org/downloads/ "Python Source Releases")
  - It is recommended that you install Python 3.10 and above, bugs in older versions will not be fixed
  - When installing Python for the first time, be sure to check `Add Python x.x to PATH` to add environment variables

### 2. Install the related dependency libraries

- **Windows**: Run `Installation of Dependency Libraries.bat` to install the related dependency libraries
- **macOS & Linux**: Run `Installation of Dependency Libraries.sh` to install the related dependency libraries

### 3. Set Hypixel server language to English (Recommend)

- Type `/lang en` in Hypixel server to complete the setup

## ⚜ How to Use

### 1. Run the main program

- **Windows**: Once the pre-conditions are met, run `GTB-Solver.bat`
- **macOS & Linux**: Once the pre-conditions are met, run `GTB-Solver.sh`

### 2. Exit the main program

- GTB-Solver runs repeatedly by default, enter `0` or press `Ctrl+C` to exit the program

## ⚜ Matching Rules

1. **Number**: Number of underscores
2. **Letter**: Will be matched and can be inserted directly before and after the number

> [!TIP]
> Letters are not case sensitive when entering

3. **Hyphen**: Will be matched and can be inserted directly before and after the number
4. **Space**: Will **NOT** be matched, needs to be manually entered into the matching expression
5. **Regular Expression Characters**: Partially available
6. **Default Matching**: English
7. **Exact Matching**: If there is no need for multi-language matching, you can add the corresponding prefix to the matching expression for exact matching

    - Matching Content and Corresponding Prefix List

      | Matching Content | Corresponding Prefix |
      | :----: | :----: |
      | Simplified Chinese | @zh |
      | Traditional Chinese | @cht |
      | Japanese | @jp |
      | Korean | @kor |
      | Russian | @ru |
      | German | @de |
      | French | @fra |
      | Spanish | @spa |
      | Portuguese | @pt |
      | Italian | @it |
      | English | @en |
      | Shortcut(s) | @sc |
      | Multiword(s) | @mw |

## ⚜ How to Guess (Take Water Bottle as an Example)

### 1. Use numbers + letters to guess

``` TXT
Theme: _____ ______
Please enter the matching expression: 5 6
The theme is 12 characters long
20.50 - Water Bucket - Vandspand
14.25 - Table Tennis - Bordtenni
12.25 - Ender Dragon
10.75 - Light Switch - Lysbryter
10.75 - Water Bottle - Waterfle
10.25 - Train Tracks - Rail - Rautatie
9.75 - Paint Bucket - Fargburk
9.25 - Horse Racing - Zavod koni
9.00 - Swiss Cheese
6.75 - Magic Carpet
6.00 - Scuba Diving - Buceo
5.25 - Fruit Basket - Obstkorb
5.25 - Solar System - Solsystem
5.00 - Greek Temple
5.00 - Solar Panels
4.50 - Build Battle
0.25 - Snowy Forest
```

``` TXT
Theme: _a___ ______
Please enter the matching expression: 1a3 6
The theme is 12 characters long
20.50 - Water Bucket - Vandspand
14.25 - Table Tennis - Bordtenni
10.75 - Water Bottle - Waterfle
9.75 - Paint Bucket - Fargburk
6.75 - Magic Carpet
# Here you can choose according to the general outline of the player's building
```

``` TXT
Theme: _a___ _o____
Please enter the matching expression: 1a3 1o4
The theme is 12 characters long
10.75 - Water Bottle - Waterfle
```

### 2. Guessing in conjunction with the use of regular expressions

``` TXT
Theme: _a___ ______
Please enter the matching expression: .a3 .*
20.50 - Water Bucket - Vandspand
14.25 - Table Tennis - Bordtenni
12.50 - Water Slide - Tobogan
10.75 - Water Bottle - Waterfle
10.25 - Magic Hat - Joben
9.75 - Paint Bucket - Fargburk
9.25 - Paper Airplane - Papirfly
8.00 - Games Controller - Controller
7.75 - Candy Cane - Acadea
7.75 - Paint Palette - Verfpalet
7.25 - Party Hat
6.75 - Magic Carpet
6.75 - Water Balloon - Gavettone
6.25 - Magma Cube
6.25 - Table Cloth - Dug
6.25 - Water Park
4.75 - Magic Wand
0.75 - Santa Claus
0.00 - Candy Buckets
```

``` TXT
Theme: _a___ _o____
Please enter the matching expression: .a3 .o.*
10.75 - Water Bottle - Waterfle
8.00 - Games Controller - Controller
# Here you can choose according to the general outline of the player's building
```

``` TXT
Theme: _a___ _o___e
Please enter the matching expression: .a3 .o.*e
The theme is 12 characters long
10.75 - Water Bottle - Waterfle
```

## ⚜ Configuration Modification

### 1. Modify the path of the thesaurus file or replace the thesaurus file

- The default path is the same folder as `GTB-Solver_main.py`. If you need to modify the path of the thesaurus file or replace the thesaurus file, please find the following code in `GTB-Solver_main.py` and replace the path in quotation marks

``` Python
GTB_THESAURUS = r"GTB_Thesaurus_Demo.xlsx"
```

> [!WARNING]
> There should be at least an "English" column in the thesaurus file (strictly case sensitive)

### 2. Modify the program output language

- The default output language is the system language, or English if the system language is not yet supported. If you need to modify the default output language of the program, please find the following code in `GTB-Solver_main.py` and add the corresponding language code in quotation marks. If you only need to temporarily modify the program output language, you can directly enter the corresponding switching command

``` Python
MULTI_LANG = ""
```

- Language Code and Switching Command List

  | Output Language | Language Code | Switching Command |
  | :----: | :----: | :----: |
  | Simplified Chinese | zh | /lang zh |
  | Traditional Chinese | cht | /lang cht |
  | Japanese | jp | /lang jp |
  | Korean | kor | /lang kor |
  | Russian | ru | /lang ru |
  | German | de | /lang de |
  | French | fra | /lang fra |
  | Spanish | spa | /lang spa |
  | Portuguese | pt | /lang pt |
  | Italian | it | /lang it |
  | English | en | /lang en |

### 3. Modify the output moe mode status

- The output moe mode is disabled by default. If you need to enable the output moe mode, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
MOE_MODE = False
```

### 4. Modify the automatic copying mode status

- The automatic copying mode is disabled by default. If you need to automatically copy the first matching entry to the clipboard, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
AUTO_COPY = False
```

### 5. Modify the random copying mode status

- The random copying mode is disabled by default. If you need to randomly copy one of the expressions in Simplified Chinese, Traditional Chinese, Japanese, Korean, Russian, German, French, Spanish, Portuguese or Italian of the first matching entry to the clipboard during automatic copying, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
RAC_MODE = False
```

> [!NOTE]
> Enabling random copying mode requires enabling automatic copying mode at the same time. For details on how to enable automatic copying mode, see `Configuration Modification Method 4`

### 6. Modify the log assisted processing mode status

- The log assisted processing mode is disabled by default. If you need to output game-related status online, compare the themes guessed by players in the game with the already output matching entries, and re-output them after filtering, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
LAP_MODE = False
```

- Example of Output Style (Among them, `3` is the current round, `10` is the total rounds, `NoticeYou` is the name of the builder of the current round, and `13` is the number of characters in the current round theme including spaces)

  ``` TXT
  [3/10] NoticeYou(13)
  ```

- Example of Comparative Guessing (Take Conveyor Belt as an Example)

  ``` TXT
  Theme: ________ ___
  [3/10] NoticeYou(13)
  Please enter the matching expression: 8 4
  The theme is 13 characters long
  13.00 - Swimming Pool - Basen
  7.50 - Wrecking Ball - Sloopkogel
  4.50 - Conveyor Belt - Forderband
  0.00 - Presents Pile
  ```

  ``` TXT
  [3/10] NoticeYou(13)
  NoticeMW: basen
  Detects that the player guessed theme(s) Swimming Pool but did not guess correctly, and the filtered matching entries will be output accordingly
  7.50 - Wrecking Ball - Sloopkogel
  4.50 - Conveyor Belt - Forderband
  0.00 - Presents Pile
  ```

  ``` TXT
  [3/10] NoticeYou(13)
  NoticeRU: шар для сноса зданий
  Detects that the player guessed theme(s) Swimming Pool, Wrecking Ball but did not guess correctly, and the filtered matching entries will be output accordingly
  4.50 - Conveyor Belt - Forderband
  0.00 - Presents Pile
  ```

> [!TIP]
> The log assisted processing mode supports processing when the server language is set to Simplified Chinese, Traditional Chinese, Japanese, Korean, Russian, German, French, Spanish, Portuguese, Italian or English, and supports to compare the themes guessed by players using Simplified Chinese, Traditional Chinese, Japanese, Korean, Russian, German, French, Spanish, Portuguese, Italian, English, Shortcut(s) or Multiword(s). If your thesaurus file version is different, the actual comparison effect may change

### 7. Modify the path of the log file

- The default path is `C:\Minecraft\.minecraft\logs\latest.log`, and it is for reference only, please modify it according to the actual situation. If you need to modify the path of the log file, please find the following code in `GTB-Solver_main.py` and replace the path in quotation marks

``` Python
LOG_FILE = r"C:\Minecraft\.minecraft\logs\latest.log"
```

### 8. Modify the repeat reading interval of the log file

- The default interval is `0.05` seconds. If you need to modify the repeat reading interval of the log file, please find the following code in `GTB-Solver_main.py` and modify the value

``` Python
LAP_INTERVAL = 0.05
```

> [!TIP]
> It is recommended to set the interval in the range of `0.01` ~ `0.20` seconds. If you find that the game-related status is not updated in time or fail to capture the themes guessed by players after enabling the log assisted processing mode, you can reduce the repeat reading interval appropriately

### 9. Modify the custom copy content at the end of the game

- The default copy content is `Good Game`. If you need to modify the custom copy content at the end of the game, please find the following code in `GTB-Solver_main.py` and replace the content in the quotation marks

``` Python
CUSTOM_CONTENT = "Good Game"
```

> [!NOTE]
> Custom content will only be copied when automatic copying mode and log assisted processing mode are enabled. For details on how to enable automatic copying mode, see `Configuration Modification Method 4`, and for how to enable log assisted processing mode, see `Configuration Modification Method 6`

### 10. Modify the theme auxiliary recording mode status

- The theme auxiliary recording mode is disabled by default. If you need to record the correct theme to the auxiliary recording file for subsequent statistical processing, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
TAR_MODE = False
```

> [!NOTE]
> Enabling theme auxiliary recording mode requires enabling log assisted processing mode at the same time. For details on how to enable log assisted processing mode, see `Configuration Modification Method 6`

### 11. Modify the path of the theme auxiliary recording file

- The default path is the same folder as `GTB-Solver_main.py`. If you need to modify the path of the theme auxiliary recording file, please find the following code in `GTB-Solver_main.py` and replace the path in quotation marks

``` Python
GTB_TAR_FILE = r"GTB_TAR_File.txt"
```

### 12. Modify the semi-automatic sending mode status

- The semi-automatic sending mode is disabled by default. If you need to automatically send the first matching entry to the game after entering the matching expression, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
SAS_MODE = False
```

> [!NOTE]
> Enabling semi-automatic sending mode requires enabling automatic copying mode and log assisted processing mode at the same time. For details on how to enable automatic copying mode, see `Configuration Modification Method 4`, and for how to enable log assisted processing mode, see `Configuration Modification Method 6`

### 13. Modify the semi-automatic sending interval

- The default interval is `2.0` seconds. If you need to modify the interval between sends, please find the following code in `GTB-Solver_main.py` and modify the value

``` Python
SAS_INTERVAL = 2.0
```

> [!TIP]
> This interval is the additional pause time after subtracting the remaining cooldown time of the repeat guess, it is recommended to set the interval in the range of `1.0` ~ `5.0` second(s). Setting the interval too short may trigger the server's anti-spam mechanism and result in being kicked out of the game

### 14. Modify the game window title

- The semi-automatic sending mode activates the first window containing the word `Minecraft` by default. If you are using a non-original client, please find the following code in `GTB-Solver_main.py` and replace the content in quotation marks with the game window title

``` Python
WINDOW_TITLE = "Minecraft"
```

### 15. Modify the player warning control mode status

- The player warning control mode is disabled by default. If you need to warn the subsequent players entering the waiting room in real time and send a notification after the players in player warning control list enter the waiting room, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
PWC_MODE = False
```

> [!TIP]
> This mode cannot warn players who are playing anonymously

> [!NOTE]
> Enabling player warning control mode requires enabling log assisted processing mode at the same time. For details on how to enable log assisted processing mode, see `Configuration Modification Method 6`

### 16. Modify the player warning control enhanced mode status

- The player warning control enhanced mode is disabled by default. If you want to automatically return to the game lobby after the players in player warning control list enter the waiting room, please find the following code in `GTB-Solver_main.py` and replace `False` with `True`

``` Python
PWCE_MODE = False
```

> [!NOTE]
> Enabling player warning control enhanced mode requires enabling player warning control mode and semi-automatic sending mode at the same time. For details on how to enable player warning control mode, see `Configuration Modification Method 15`, and for how to enable semi-automatic sending mode, see `Configuration Modification Method 12`

### 17. Modify the path of the player warning control offline list file

- The default path is the same folder as `GTB-Solver_main.py`. If you need to modify the path of the player warning control offline list file, please find the following code in `GTB-Solver_main.py` and replace the path in quotation marks

``` Python
PWC_OFFLINE_LIST = r"GTB_PWC_Offline_List.json"
```

### 18. Modify the player warning control mode threshold

- Adds the top `500` players in the "Guess The Build" wins leaderboard to player warning control list by default. If you need to modify the player warning control mode threshold, please find the following code in `GTB-Solver_main.py` and modify the value

``` Python
PWC_THRESHOLD = 500
```

> [!TIP]
> This threshold can currently be set in the range of `1` ~ `1000`

### 19. Modify the player warning control mode blacklist

- The player warning control mode blacklist is empty by default. If you need to add additional players to player warning control list, please find the following code in `GTB-Solver_main.py` and add the player name to the list

``` Python
PWC_BLACKLIST = []
```

### 20. Modify the player warning control mode whitelist

- The player warning control mode whitelist is empty by default. If you need to delete players that may appear in player warning control list, please find the following code in `GTB-Solver_main.py` and add the player name to the list

``` Python
PWC_WHITELIST = []
```

## ⚜ Important Notes

> [!IMPORTANT]
> This project is for Demo **ONLY**, the provided thesaurus file `GTB_Thesaurus_Demo.xlsx` contains 100 pairs of sample words and a few Shortcut(s) & Multiword(s), you can continue to supplement it on the original basis or replace the thesaurus file according to the aforementioned configuration modification method

> [!CAUTION]
> Abuse of GTB-Solver will give you an unfair advantage in the game! Please use it reasonably within a limited scope. The developer is **NOT** responsible for the BAN caused by abuse of the program

---

<p align="center">Made with Love ❤️</p>