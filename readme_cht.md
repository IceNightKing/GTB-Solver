# GTB_Solver_EN

**[简体中文](./readme_zh.md) | 繁體中文 | [日本語](./readme_jp.md) | [English](./readme.md)**

依據英文提示及正規表示式快速猜測 Hypixel 伺服器《你蓋我猜》小遊戲中的建築主題。  
> **淦翻紅牌ldx，一人盲猜虐全場！**  

## 更新日誌
### 2024/02/04 - Demo_202402
- \[Add\] 多語言 `readme` 支援  
- \[Add\] 輸出萌化模式支援  
- \[Fix\] 修復了用戶輸入不合法可能造成的 `OverflowError` 崩潰  
- \[Fix\] 修復了用戶輸入不合法可能造成的 `re.error` 崩潰  
- \[Opt\] 程式輸出語言現在預設取決於系統語言  
- \[Opt\] 詞庫更新  
- \[Opt\] 代碼重構  

## 前置條件
### 1. 搭建 Python 運作環境
- [前往 Python 官網下載](https://www.python.org/downloads/ "Python Source Releases")  
  - 建議安裝 Python 3.10 及以上版本，較舊版本出現的問題我們將不再維護  
  - 首次安裝 Python 時請注意勾選 `Add Python x.x to PATH` 新增環境變量  
### 2. 安裝相關依賴程式庫
- 運行 `Installation of Dependency Libraries.bat` 安裝相關依賴程式庫  
### 3. 切換 Hypixel 伺服器語言為英文
- 於 Hypixel 伺服器內輸入 `/lang en` 即可完成切換  

## 使用方法
### 運行主程式
- 前置條件滿足後，運行 `GTB_Solver_EN.bat` 即可  

## 猜測方法（以 Water Bottle 為例）
### 1. 使用數字+字母進行猜測
``` Python
主題: _____ ______
請輸入匹配式: 5 6
Build Battle - 建筑大师
Chili Pepper - 红辣椒 - Piment
Ender Dragon - 末影龙
Fruit Basket - 果篮 - Obstkorb
Horse Racing - 赛马
Horse Riding - 骑马
Light Switch - 照明开关
Magic Carpet - 魔毯
Paint Bucket - 油漆桶
Scuba Diving - 水肺潜水 - Buceo
Snowy Forest - 积雪森林
Solar System - 太阳系
Swiss Cheese - 瑞士奶酪
Table Tennis - 乒乓球 - Ping Pong
Train Tracks - 铁轨 - Rail - Rautatie
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶

主題: _a___ ______
請輸入匹配式: 1a3 6
Magic Carpet - 魔毯
Paint Bucket - 油漆桶
Table Tennis - 乒乓球 - Ping Pong
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶
# 在此即可依據玩家建築大致輪廓進行選擇

主題: _a___ _o____
請輸入匹配式: 1a3 1o4
Water Bottle - 水瓶 - Waterfle
```
### 2. 結合使用正規表示式進行猜測
``` Python
主題: _a___ ______
請輸入匹配式: .a3 .*
Candy Buckets - 糖果篮子
Candy Cane - 糖果手杖
Games Controller - 游戏手柄
Magic Carpet - 魔毯
Magic Hat - 魔法帽子
Magic Wand - 魔术棒
Magma Cube - 岩浆怪
Paint Bucket - 油漆桶
Paint Palette - 调色板 - Verfpalet
Paper Airplane - 纸飞机 - Papirfly
Party Hat - 派对帽子
Santa Claus - 圣诞老人
Table Cloth - 桌布 - Dug
Table Tennis - 乒乓球 - Ping Pong
Water Balloon - 水气球
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶
Water Park - 水上乐园
Water Slide - 水上滑梯 - Tobogan

主題: _a___ _o____
請輸入匹配式: .a3 .o.*
Games Controller - 游戏手柄
Water Bottle - 水瓶 - Waterfle
# 在此即可依據玩家建築大致輪廓進行選擇

主題: _a___ _o___e
請輸入匹配式: .a3 .o.*e
Water Bottle - 水瓶 - Waterfle
```

## 配置修改
### 1. 修改詞庫檔案路徑或更換詞庫檔案
- 預設路徑為 `GTB_Solver_EN_main.py` 同資料夾。如需修改詞庫檔案路徑或更換詞庫檔案，請在 `GTB_Solver_EN_main.py` 內找到以下代碼，替換引號內的路徑即可（支援中文路徑）  
``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```
### 2. 修改程式輸出語言
- 預設輸出語言為系統語言，若系統語言尚未支援，則為英文。如需修改程式輸出語言，請在 `GTB_Solver_EN_main.py` 內找到以下代碼，於引號內加入對應語言代碼即可  
``` Python
Multi_Lang = ""
```
- 語言代碼串列  

| 輸出語言 | 語言代碼 |
| :----: | :----: |
| 簡體中文 | zh |
| 繁體中文 | cht |
| 日語 | jp |
| 英文 | en |

### 3. 修改輸出萌化狀態
- 預設關閉。如需開啟輸出萌化模式，請在 `GTB_Solver_EN_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可  
``` Python
Moe_Mode = False
```
### 4. 修改自動複製狀態
- 預設關閉。如需自動複製首個匹配結果至剪貼簿，請在 `GTB_Solver_EN_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可  
``` Python
Auto_Copy = False
```

## 注意事項
- 本項目僅作 Demo 演示之用，所提供的詞庫文件 `GTB_Thesaurus_Demo.xlsx` 內含 100 對範例詞彙及少量 Shortcut(s) & Multiword(s)，您可在原有基礎上繼續補充使用或依據前述配置修改方法更換詞庫文件  
- 濫用 GTB_Solver_EN 會為您帶來不公平的遊戲優勢！請在有限範圍內合理使用，作者對因濫用本程序而導致的封鎖問題概不負責  