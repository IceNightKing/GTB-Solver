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

### 2024/06/03 - v4.3

- \[Add\] 新增了程式狀態自檢
- \[Opt\] 優化了日誌輔助處理模式的輸出樣式
- \[Opt\] 代碼優化

### 2024/05/12 - v4.2

- \[Add\] 新增了日誌輔助處理模式
- \[Add\] 新增了主題輔助記錄模式
- \[Add\] 新增了半自動發送模式
- \[Opt\] 詞庫更新

### 2024/04/18 - v4.1

- \[Add\] 新增了詞頻統計指數
  - 詞頻統計指數依時間梯度加權計算自多位玩家提供的總計約 15,000 回合的遊戲數據，僅供參考
- \[Opt\] 程式現在預設依照詞頻統計指數降序輸出
  - 如仍需依照原規則輸出，請自行在詞庫檔案 `GTB_Thesaurus_Demo.xlsx` 內以 English 欄為排序依據，依照英文字母升序排序
- \[Opt\] 詞庫更新

### 2024/04/02 - v4.0

- \[Add\] 繁體中文輸入匹配支援
- \[Add\] 日文輸入匹配支援
- \[Fix\] 修復了字元 `'` 無法被匹配的問題

  ``` TXT
  # 現在以下主題已經能夠被正確匹配
  0.25 - Santa's Workshop - 聖誕老人工作坊
  0.00 - Santa's Sleigh - 聖誕老人的雪橇
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
  0.00 - Mrs. Claus - 聖誕老奶奶
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
  3.00 - T-Shirt - T恤 - Tricou
  1.75 - T-Rex - 暴龍
  0.00 - Jack-O-Lantern - 南瓜燈
  0.00 - Trick-or-Treating - 不給糖就搗蛋
  ```

- \[Fix\] 修復了詞庫欄名設定不正確可能造成的 `KeyError` 崩潰

### 2024/02/04 - Demo_202402

- \[Add\] 多語言 `readme` 支援
- \[Add\] 新增了輸出萌化模式
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

### 3. 設定 Hypixel 伺服器語言為英文（推薦）

- 於 Hypixel 伺服器內輸入 `/lang en` 即可完成設定

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
主題：_____ ______
請輸入匹配式：5 6
此主題字數為 12 個字母
16.75 - Water Bucket - 水桶 - Vandspand
12.00 - Table Tennis - 乒乓球 - Bordtenni
10.25 - Train Tracks - 鐵軌 - Rail - Rautatie
10.00 - Ender Dragon - 終界龍
10.00 - Light Switch - 電燈開關 - Lysbryter
8.50 - Water Bottle - 水瓶 - Waterfle
8.25 - Paint Bucket - 油漆桶 - Fargburk
8.25 - Swiss Cheese - 瑞士起司
7.75 - Horse Racing - 賽馬 - Zavod koni
6.75 - Chili Pepper - 辣椒 - Piment
6.75 - Magic Carpet - 魔毯
4.50 - Fruit Basket - 水果籃 - Obstkorb
4.50 - Scuba Diving - 水肺潛水 - Buceo
4.50 - Solar System - 太陽系 - Solsystem
3.50 - Horse Riding - 騎馬 - Ridning
3.00 - Build Battle - 建築大賽
0.25 - Snowy Forest - 冰雪森林
```

``` TXT
主題：_a___ ______
請輸入匹配式：1a3 6
此主題字數為 12 個字母
16.75 - Water Bucket - 水桶 - Vandspand
12.00 - Table Tennis - 乒乓球 - Bordtenni
8.50 - Water Bottle - 水瓶 - Waterfle
8.25 - Paint Bucket - 油漆桶 - Fargburk
6.75 - Magic Carpet - 魔毯
# 在此即可依據玩家建築大致輪廓進行選擇
```

``` TXT
主題：_a___ _o____
請輸入匹配式：1a3 1o4
此主題字數為 2 個字
8.50 - Water Bottle - 水瓶 - Waterfle
```

### 2. 結合使用正規表示式進行猜測

``` TXT
主題：_a___ ______
請輸入匹配式：.a3 .*
16.75 - Water Bucket - 水桶 - Vandspand
12.00 - Table Tennis - 乒乓球 - Bordtenni
11.00 - Water Slide - 滑水道 - Tobogan
9.50 - Magic Hat - 魔法頭飾 - Joben
8.50 - Water Bottle - 水瓶 - Waterfle
8.25 - Paint Bucket - 油漆桶 - Fargburk
7.00 - Candy Cane - 拐杖糖 - Acadea
7.00 - Paper Airplane - 紙飛機 - Papirfly
6.75 - Magic Carpet - 魔毯
6.50 - Party Hat - 派對帽
6.25 - Water Park - 水上樂園
5.75 - Games Controller - 遊戲控制器 - Controller
5.50 - Magma Cube - 岩漿立方怪
5.50 - Paint Palette - 調色盤 - Verfpalet
5.25 - Water Balloon - 水球 - Gavettone
4.00 - Magic Wand - 魔杖
4.00 - Table Cloth - 桌布 - Dug
0.75 - Santa Claus - 聖誕老人
0.00 - Candy Buckets - 糖果籃
```

``` TXT
主題：_a___ _o____
請輸入匹配式：.a3 .o.*
8.50 - Water Bottle - 水瓶 - Waterfle
5.75 - Games Controller - 遊戲控制器 - Controller
# 在此即可依據玩家建築大致輪廓進行選擇
```

``` TXT
主題：_a___ _o___e
請輸入匹配式：.a3 .o.*e
此主題字數為 2 個字
8.50 - Water Bottle - 水瓶 - Waterfle
```

### 3. 使用繁體中文進行猜測

``` TXT
主題：水_
請輸入匹配式：水1
此主題字數為 2 個字
16.75 - Water Bucket - 水桶 - Vandspand
8.50 - Water Bottle - 水瓶 - Waterfle
7.75 - Underwater - 水下 - Pod woda
6.25 - Jellyfish - 水母 - Kwal
5.25 - Water Balloon - 水球 - Gavettone
3.00 - Fruit - 水果
2.25 - Crystal - 水晶
1.75 - Otter - 水獺
1.50 - Puddle - 水坑 - Pla
1.25 - Kettle - 水壺 - Tetera
# 在此即可依據玩家建築大致輪廓進行選擇
# 鑒於提示時間靠後，不建議使用繁體中文猜測兩字及兩字以下主題
```

## ⚜ 配置修改

### 1. 修改詞庫檔案路徑或更換詞庫檔案

- 預設路徑為 `GTB-Solver_main.py` 同資料夾。如需修改詞庫檔案路徑或更換詞庫檔案，請在 `GTB-Solver_main.py` 內找到以下代碼，替換引號內的路徑即可（支援中文路徑）

``` Python
GTB_THESAURUS = r"GTB_Thesaurus_Demo.xlsx"
```

- **注意**：詞庫檔案內應至少存在 English 欄（嚴格區分大小寫）

### 2. 修改程式輸出語言

- 預設輸出語言為系統語言，若系統語言尚未支援，則為英文。如需修改程式預設輸出語言，請在 `GTB-Solver_main.py` 內找到以下代碼，於引號內加入對應語言代碼即可。如僅需暫時性修改程式輸出語言，直接輸入對應切換指令即可

``` Python
MULTI_LANG = ""
```

- 語言代碼與切換指令列表

  | 輸出語言 | 語言代碼 | 切換指令 |
  | :----: | :----: | :----: |
  | 簡體中文 | zh | /lang zh |
  | 繁體中文 | cht | /lang cht |
  | 日文 | jp | /lang jp |
  | 英文 | en | /lang en |

### 3. 修改輸出萌化模式狀態

- 預設關閉。如需開啟輸出萌化模式，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
MOE_MODE = False
```

### 4. 修改自動複製模式狀態

- 預設關閉。如需自動複製首個匹配條目至剪貼簿，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
AUTO_COPY = False
```

### 5. 修改日誌輔助處理模式狀態

- 預設關閉。如需即時輸出遊戲相關狀態，並將遊戲內玩家猜測的主題與已經輸出的匹配條目進行對比，經篩選後重新輸出，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
LAP_MODE = False
```

- 輸出樣式範例（其中，`3` 為當前回合數，`10` 為總回合數，`NoticeYou` 為當前回合建築師名稱，`12` 為包含空格的當前回合主題字數）

  ``` TXT
  [3/10] NoticeYou(12)
  ```

- 對比猜測範例（以 Shopping Bag 為例）

  ``` TXT
  主題：________ ___
  [3/10] NoticeYou(12)
  請輸入匹配式：8 3
  此主題字數為 12 個字母
  8.25 - Shopping Bag - 購物袋 - Handlepose
  7.25 - Sleeping Bag - 睡袋 - Sovepose
  4.00 - Baseball Bat - 棒球棍
  ```

  ``` TXT
  [3/10] NoticeYou(12)
  NoticeSC: sovepose
  偵測到有玩家猜測了主題 睡袋 但未猜對，即將據此輸出篩選後的匹配條目
  8.25 - Shopping Bag - 購物袋 - Handlepose
  4.00 - Baseball Bat - 棒球棍
  ```

  ``` TXT
  [3/10] NoticeYou(12)
  NoticeJP: 野球バット
  偵測到有玩家猜測了主題 睡袋、棒球棍 但未猜對，即將據此輸出篩選後的匹配條目
  8.25 - Shopping Bag - 購物袋 - Handlepose
  # 在此即可直接盲猜出正確主題
  ```

- **提示**：日誌輔助處理模式支援處理伺服器語言設定為簡體中文、繁體中文、日文、英文的情況，並支援對比玩家使用簡體中文、繁體中文、日文、英文、Shortcut(s)、Multiword(s) 猜測的主題。若您的詞庫檔案版本不同，實際對比效果可能會發生改變

### 6. 修改日誌檔案路徑

- 預設路徑為 `C:\Minecraft\.minecraft\logs\latest.log`，僅供參考，請根據實際情況進行修改。如需修改日誌檔案路徑，請在 `GTB-Solver_main.py` 內找到以下代碼，替換引號內的路徑即可（支援中文路徑）

``` Python
LOG_FILE = r"C:\Minecraft\.minecraft\logs\latest.log"
```

### 7. 修改日誌檔案重複讀取間隔

- 預設間隔為 `0.05` 秒。如需修改日誌檔案的重複讀取間隔，請在 `GTB-Solver_main.py` 內找到以下代碼，修改數值即可

``` Python
LAP_INTERVAL = 0.05
```

- **提示**：建議將該間隔設定在 `0.01` ~ `0.20` 秒的範圍內。若您發現開啟日誌輔助處理模式後遊戲相關狀態更新不及時或未能成功抓取玩家猜測的主題，可適當減少重複讀取間隔

### 8. 修改遊戲結束時自訂複製內容

- 預設複製內容為 `Good Game`。如需修改遊戲結束時自訂複製內容，請在 `GTB-Solver_main.py` 內找到以下代碼，替換引號內的內容即可（支援中文）

``` Python
CUSTOM_CONTENT = "Good Game"
```

- **注意**：自動複製模式與日誌輔助處理模式開啟時，自訂內容才會被複製。自動複製模式的開啟方法詳見 `配置修改方法 4`，日誌輔助處理模式的開啟方法詳見 `配置修改方法 5`

### 9. 修改主題輔助記錄模式狀態

- 預設關閉。如需在正確主題出現後將其記錄至輔助記錄檔案內以便後續統計處理，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
TAR_MODE = False
```

- **注意**：啟用主題輔助記錄模式需要同時開啟日誌輔助處理模式。日誌輔助處理模式的開啟方法詳見 `配置修改方法 5`

### 10. 修改主題輔助記錄檔案路徑

- 預設路徑為 `GTB-Solver_main.py` 同資料夾。如需修改主題輔助記錄檔案路徑，請在 `GTB-Solver_main.py` 內找到以下代碼，替換引號內的路徑即可（支援中文路徑）

``` Python
GTB_TAR_FILE = r"GTB_TAR_File.txt"
```

### 11. 修改半自動發送模式狀態

- 預設關閉。如需在輸入匹配式後自動發送首個匹配條目至遊戲內，請在 `GTB-Solver_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
SAS_MODE = False
```

- **注意**：啟用半自動發送模式需要同時開啟自動複製模式與日誌輔助處理模式。自動複製模式的開啟方法詳見 `配置修改方法 4`，日誌輔助處理模式的開啟方法詳見 `配置修改方法 5`

### 12. 修改半自動發送間隔

- 預設間隔為 `2.0` 秒。如需修改兩次發送間的時間間隔，請在 `GTB-Solver_main.py` 內找到以下代碼，修改數值即可

``` Python
SAS_INTERVAL = 2.0
```

- **提示**：該間隔是在減去重複猜測剩餘冷卻時間後額外的暫停時間，建議將該間隔設置在 `1.0` ~ `5.0` 秒的範圍內。此間隔設定太小可能會觸發伺服器反垃圾訊息機製而被踢出遊戲

### 13. 修改遊戲視窗名稱

- 預設啟動包含 `Minecraft` 字樣的第一個視窗。若您使用了非原版客戶端，請在 `GTB-Solver_main.py` 內找到以下代碼，替換引號內的內容為遊戲視窗名稱即可（支援中文）

``` Python
WINDOW_TITLE = "Minecraft"
```

## ⚜ 注意事項

- 本項目僅作 Demo 演示之用，所提供的詞庫檔案 `GTB_Thesaurus_Demo.xlsx` 內含 100 對範例詞彙及少量 Shortcut(s) & Multiword(s)，您可在原有基礎上繼續補充使用或依據前述配置修改方法更換詞庫檔案
- 濫用建築猜猜寶會為您帶來不公平的遊戲優勢！請在有限範圍內合理使用，作者對因濫用本程序而導致的封鎖問題概不負責