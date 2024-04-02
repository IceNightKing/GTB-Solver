<h1 align="center">
  <br>
  建築猜猜寶
  <br>
</h1>

<h3 align="center">
建築猜猜寶 Demo 分支 | <a href="https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme_cht.md">[Beta] 建築猜猜寶 OCR 分支</a>
</h3>

## ⚜ 功能簡介

**[简体中文](./readme_zh.md) | 繁體中文 | [日本語](./readme_jp.md) | [English](./readme.md)**

依據多語言提示及正規表示式快速猜測 Hypixel 伺服器《你蓋我猜》小遊戲中的建築主題。

> **淦翻紅牌ldx，一人盲猜虐全場！**

## ⚜ 更新日誌

### 2024/04/02 - v4.0

- \[Add\] 繁體中文輸入匹配支援
- \[Add\] 日文輸入匹配支援
- \[Fix\] 修復了字元 `'` 無法被匹配的問題

  ``` TXT
  # 現在以下主題已經能夠被正確匹配
  Santa's Sleigh - 聖誕老人的雪橇
  Santa's Workshop - 聖誕老人工作坊
  ```

- \[Opt\] 現在使用者可以透過前綴 `@cht` 匹配繁體中文
- \[Opt\] 現在使用者可以透過前綴 `@jp` 匹配日文
- \[Opt\] 詞庫更新

### 2024/03/25 - v3.6

- \[Add\] 新增了詞庫狀態自檢
- \[Opt\] 現在使用者可以透過前綴 `@sc` 匹配 Shortcut(s)
- \[Opt\] 現在使用者可以透過前綴 `@mw` 匹配 Multiword(s)

### 2024/03/17 - v3.5

- \[Add\] 新增了在非多字數結果下的匹配字數提示
- \[Opt\] 現在使用者可以在程式內切換輸出語言
- \[Opt\] 代碼優化

### 2024/02/29 - v3.4

- \[Opt\] 現在使用者按下 `Ctrl+C` 也能夠正常退出程式
- \[Opt\] 代碼優化

### 2024/02/20 - v3.3

- \[Fix\] 修復了字元 `.` 無法被匹配的問題

  ``` TXT
  # 現在以下主題已經能夠被正確匹配
  Mrs. Claus - 聖誕老奶奶
  ```

- \[Opt\] 代碼優化

### 2024/02/14 - v3.2

- \[Add\] [建築猜猜寶 OCR 分支連結](https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme_cht.md "GTB-Solver OCR Branch")
- \[Add\] macOS & Linux 系統支援
- \[Add\] 英文 & 簡體中文匹配選擇支援
- \[Fix\] 修復了使用者輸入不合法可能造成的 `re.error` 崩潰

### 2024/02/13 - v3.1

- \[Fix\] 修復了運行 `Installation of Dependency Libraries.bat` 安裝相關依賴程式庫後仍可能出現依賴程式庫數量不足的問題
- \[Opt\] 更新了獲取系統語言的方式以適配 Python 的未來版本

### 2024/02/08 - v3.0

- \[Add\] 簡體中文輸入匹配支援
- \[Fix\] 修復了字元 `-` 無法被匹配的問題

  ``` TXT
  # 現在以下主題已經能夠被正確匹配
  Jack-O-Lantern - 南瓜燈
  T-Rex - 暴龍
  Trick-or-Treating - 不給糖就搗蛋
  T-Shirt - T恤 - Tricou
  ```

- \[Fix\] 修復了詞庫欄名配置不正確可能造成的 `KeyError` 崩潰

### 2024/02/04 - Demo_202402

- \[Add\] 多語言 `readme` 支援
- \[Add\] 輸出萌化模式支援
- \[Fix\] 修復了使用者輸入不合法可能造成的 `OverflowError` 崩潰
- \[Fix\] 修復了使用者輸入不合法可能造成的 `re.error` 崩潰
- \[Opt\] 程式輸出語言現在預設取決於系統語言
- \[Opt\] 詞庫更新
- \[Opt\] 代碼重構

## ⚜ 前置條件

### 1. 搭建 Python 運作環境

- [前往 Python 官網下載](https://www.python.org/downloads/ "Python Source Releases")
  - 建議安裝 Python 3.10 及以上版本，較舊版本出現的問題我們將不再維護
  - 首次安裝 Python 時請注意勾選 `Add Python x.x to PATH` 新增環境變量

### 2. 安裝相關依賴程式庫

- **Windows**：運行 `Installation of Dependency Libraries.bat` 安裝相關依賴程式庫
- **macOS & Linux**：運行 `Installation of Dependency Libraries.sh` 安裝相關依賴程式庫

### 3. 切換 Hypixel 伺服器語言為英文（推薦）

- 於 Hypixel 伺服器內輸入 `/lang en` 即可完成切換

## ⚜ 使用方法

### 1. 運行主程式

- **Windows**：前置條件滿足後，運行 `GTB-Solver.bat` 即可
- **macOS & Linux**：前置條件滿足後，運行 `GTB-Solver.sh` 即可

### 2. 退出主程式

- 本程式預設重複運行，輸入 `0` 或按下 `Ctrl+C` 以退出程式

## ⚜ 匹配規則

1. **數字**：下橫線的數量
2. **字母**：會被匹配，可直接插入到數字前後

    - 輸入字母時無需區分大小寫

3. **繁體中文**：會被匹配，可直接插入到數字前後
4. **連字符**：會被匹配，可直接插入到數字前後
5. **空格**：不會被匹配，需手動輸入至匹配式內
6. **正規表示式字元**：部分可用
7. **預設匹配**：英文+繁體中文
8. **精確匹配**：如無需進行多語言匹配，可在匹配式內加入對應前綴進行精確匹配

    - 匹配內容及對應前綴列表

      | 匹配內容 | 對應前綴 |
      | :----: | :----: |
      | 簡體中文 | @zh |
      | 繁體中文 | @cht |
      | 日文 | @jp |
      | 英文 | @en |
      | Shortcut(s) | @sc |
      | Multiword(s) | @mw |

> **提示**：在預設匹配模式下，輸入空格、連字符或大於 8 的數字後僅會匹配到英文，輸入任意繁體中文後僅會匹配到繁體中文

## ⚜ 猜測方法（以 Water Bottle 為例）

### 1. 使用數字+字母進行猜測

``` TXT
主題: _____ ______
請輸入匹配式: 5 6
此主題字數為 12 個字母
Build Battle - 建築大賽
Chili Pepper - 辣椒 - Piment
Ender Dragon - 終界龍
Fruit Basket - 水果籃 - Obstkorb
Horse Racing - 賽馬 - Zavod koni
Horse Riding - 騎馬 - Ridning
Light Switch - 電燈開關 - Lysbryter
Magic Carpet - 魔毯
Paint Bucket - 油漆桶 - Fargburk
Scuba Diving - 水肺潛水 - Buceo
Snowy Forest - 冰雪森林
Solar System - 太陽系 - Solsystem
Swiss Cheese - 瑞士起司
Table Tennis - 乒乓球 - Bordtenni
Train Tracks - 鐵軌 - Rail - Rautatie
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
```

``` TXT
主題: _a___ ______
請輸入匹配式: 1a3 6
此主題字數為 12 個字母
Magic Carpet - 魔毯
Paint Bucket - 油漆桶 - Fargburk
Table Tennis - 乒乓球 - Bordtenni
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
# 在此即可依據玩家建築大致輪廓進行選擇
```

``` TXT
主題: _a___ _o____
請輸入匹配式: 1a3 1o4
此主題字數為 2 個字
Water Bottle - 水瓶 - Waterfle
```

### 2. 結合使用正規表示式進行猜測

``` TXT
主題: _a___ ______
請輸入匹配式: .a3 .*
Candy Buckets - 糖果籃
Candy Cane - 拐杖糖 - Acadea
Games Controller - 遊戲控制器 - Controller
Magic Carpet - 魔毯
Magic Hat - 魔法頭飾 - Joben
Magic Wand - 魔杖
Magma Cube - 岩漿立方怪
Paint Bucket - 油漆桶 - Fargburk
Paint Palette - 調色盤 - Verfpalet
Paper Airplane - 紙飛機 - Papirfly
Party Hat - 派對帽
Santa Claus - 聖誕老人
Table Cloth - 桌布 - Dug
Table Tennis - 乒乓球 - Bordtenni
Water Balloon - 水球 - Gavettone
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
Water Park - 水上樂園
Water Slide - 滑水道 - Tobogan
```

``` TXT
主題: _a___ _o____
請輸入匹配式: .a3 .o.*
Games Controller - 遊戲控制器 - Controller
Water Bottle - 水瓶 - Waterfle
# 在此即可依據玩家建築大致輪廓進行選擇
```

``` TXT
主題: _a___ _o___e
請輸入匹配式: .a3 .o.*e
此主題字數為 2 個字
Water Bottle - 水瓶 - Waterfle
```

### 3. 使用繁體中文進行猜測

``` TXT
主題: 水_
請輸入匹配式: 水1
此主題字數為 2 個字
Crystal - 水晶
Fruit - 水果
Jellyfish - 水母 - Kwal
Kettle - 水壺 - Tetera
Otter - 水獺
Puddle - 水坑 - Pla
Underwater - 水下 - Pod woda
Water Balloon - 水球 - Gavettone
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
# 在此即可依據玩家建築大致輪廓進行選擇
# 鑒於提示時間靠後，不建議使用繁體中文猜測兩字及兩字以下主題
```

## ⚜ 配置修改

### 1. 修改詞庫檔案路徑或更換詞庫檔案

- 預設路徑為 `GTB-Solver_main.py` 同資料夾。如需修改詞庫檔案路徑或更換詞庫檔案，請在 `GTB-Solver_main.py` 內找到以下代碼，替換引號內的路徑即可（支援中文路徑）

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- 注意：詞庫檔案內應至少存在 English 欄（嚴格區分大小寫）

### 2. 修改程式輸出語言

- 預設輸出語言為系統語言，若系統語言尚未支援，則為英文。如需修改程式預設輸出語言，請在 `GTB-Solver_main.py` 內找到以下代碼，於引號內加入對應語言代碼即可。如僅需暫時性修改程式輸出語言，直接輸入對應切換指令即可

``` Python
Multi_Lang = ""
```

- 語言代碼與切換指令列表

  | 輸出語言 | 語言代碼 | 切換指令 |
  | :----: | :----: | :----: |
  | 簡體中文 | zh | /lang zh |
  | 繁體中文 | cht | /lang cht |
  | 日文 | jp | /lang jp |
  | 英文 | en | /lang en |

### 3. 修改輸出萌化狀態

- 預設關閉。如需開啟輸出萌化模式，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
Moe_Mode = False
```

### 4. 修改自動複製狀態

- 預設關閉。如需自動複製首個匹配結果至剪貼簿，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
Auto_Copy = False
```

## ⚜ 注意事項

- 本項目僅作 Demo 演示之用，所提供的詞庫檔案 `GTB_Thesaurus_Demo.xlsx` 內含 100 對範例詞彙及少量 Shortcut(s) & Multiword(s)，您可在原有基礎上繼續補充使用或依據前述配置修改方法更換詞庫檔案
- 濫用建築猜猜寶會為您帶來不公平的遊戲優勢！請在有限範圍內合理使用，作者對因濫用本程序而導致的封鎖問題概不負責