<h1 align="center">
  <br>
  建築猜猜寶
  <br>
</h1>

<h3 align="center">
<a href="https://github.com/IceNightKing/GTB-Solver/blob/master/readme_cht.md">建築猜猜寶 Demo 分支</a> | [Beta] 建築猜猜寶 OCR 分支
</h3>

<h3 align="center">
<font color="orange">🚫 注意：建築猜猜寶 OCR 分支目前處於 Beta 測試階段，尚不具備可用性！ 😇</font>
</h3>

## ⚜ 功能簡介

**[简体中文](./readme_zh.md) | 繁體中文 | [日本語](./readme_jp.md) | [English](./readme.md)**

依據英文提示及光學字元辨識快速猜測 Hypixel 伺服器《你蓋我猜》小遊戲中的建築主題。

## ⚜ 前置條件

### 1. 搭建 Python 運作環境

- [前往 Python 官網下載](https://www.python.org/downloads/ "Python Source Releases")
  - 建議安裝 Python 3.10 及以上版本，較舊版本出現的問題我們將不再維護
  - 首次安裝 Python 時請注意勾選 `Add Python x.x to PATH` 新增環境變量

### 2. 安裝相關依賴程式庫

- **Windows**：運行 `Installation of Dependency Libraries.bat` 安裝相關依賴程式庫
- **macOS & Linux**：運行 `Installation of Dependency Libraries.sh` 安裝相關依賴程式庫

### 3. 修改光學字元辨識區域

- 定位動作欄上方的主題提示區域，取得左上角與右下角座標，依照 `配置修改方法 1` 修改光學字元辨識區域

### 4. 修改遊戲內相關設定

- 為提高辨識準確性，建議依照以下步驟修改遊戲內相關設定
  - `選項...` > `協助工具設定...` > `文字背景 : 全部`
  - `選項...` > `聊天設定...` > `文字背景不透明度 : 70%`
  - `選項...` > `聊天設定...` > `寬度 : 40px`

> **提示**：以上為 **Minecraft 1.19** 的相關設定修改方法，僅供參考。若您的實際遊戲版本不同，修改方法可能會有所改變

### 5. 切換 Hypixel 伺服器語言為英文

- 於 Hypixel 伺服器內輸入 `/lang en` 即可完成切換

## ⚜ 使用方法

### 1. 運行主程式

- **Windows**：前置條件滿足後，運行 `GTB-Solver.bat` 即可
- **macOS & Linux**：前置條件滿足後，運行 `GTB-Solver.sh` 即可

### 2. 退出主程式

- 本程式預設重複運行，按下 `Ctrl+C` 以退出程式

## ⚜ 辨識結果（以 Water Bottle 為例）

``` Python
主題: _____ ______
光學字元辨識結果: 5 6
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

主題: _a___ ______
光學字元辨識結果: 1a3 6
Magic Carpet - 魔毯
Paint Bucket - 油漆桶 - Fargburk
Table Tennis - 乒乓球 - Bordtenni
Water Bottle - 水瓶 - Waterfle
Water Bucket - 水桶 - Vandspand
# 在此即可依據玩家建築大致輪廓進行選擇

主題: _a___ _o____
光學字元辨識結果: 1a3 1o4
Water Bottle - 水瓶 - Waterfle
```

## ⚜ 配置修改

### 1. 修改光學字元辨識區域

- 預設辨識區域為左上角座標 `(1000, 1200)`、右下角座標 `(1550, 1300)` 的矩形區域。如需修改光學字元辨識區域，請在 `GTB-Solver-OCR_main.py` 內找到以下代碼，修改座標值即可

``` Python
Left, Top = 1000, 1200
Right, Bottom = 1550, 1300
```

- 注意：光學字元辨識區域會根據您遊戲視窗的大小和位置而產生變化

### 2. 修改重複辨識間隔

- 預設辨識間隔為 `3.0` 秒。如需修改重複辨識間隔，請在 `GTB-Solver-OCR_timer.py` 內找到以下代碼，修改數值即可

``` Python
Interval_Time = 3.0
```

### 3. 修改 GPU 加速辨識狀態

- 預設開啟。如需關閉 GPU 加速辨識模式，請在 `GTB-Solver-OCR_main.py` 內找到以下代碼，替換 `True` 為 `False` 即可

``` Python
GPU_Mode = True
```

- 注意：啟用 GPU 加速辨識模式需要裝置本身具備支援 CUDA 的 NVIDIA GPU，安裝適當的 [GPU 驅動程式](https://www.nvidia.com.tw/Download/index.aspx?lang=tw "NVIDIA Driver Downloads")、[CUDA 工具包](https://developer.nvidia.com/cuda-downloads "NVIDIA CUDA Toolkit Downloads")以及對應版本的 [PyTorch](https://pytorch.org/get-started/locally/ "Install PyTorch Locally")，否則仍將使用 CPU 進行辨識

### 4. 修改詞庫檔案路徑或更換詞庫檔案

- 預設路徑為 `GTB-Solver-OCR_main.py` 同資料夾。如需修改詞庫檔案路徑或更換詞庫檔案，請在 `GTB-Solver-OCR_main.py` 內找到以下代碼，替換引號內的路徑即可（支援中文路徑）

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- 注意：詞庫檔案內應至少存在 English 欄（嚴格區分大小寫）

### 5. 修改程式輸出語言

- 預設輸出語言為系統語言，若系統語言尚未支援，則為英文。如需修改程式輸出語言，請在 `GTB-Solver-OCR_main.py` 與 `GTB-Solver-OCR_timer.py` 內找到以下代碼，於引號內加入對應語言代碼即可

``` Python
Multi_Lang = ""
```

- 語言代碼列表

  | 輸出語言 | 語言代碼 |
  | :----: | :----: |
  | 簡體中文 | zh |
  | 繁體中文 | cht |
  | 日語 | jp |
  | 英文 | en |

### 6. 修改輸出萌化狀態

- 預設關閉。如需開啟輸出萌化模式，請在 `GTB-Solver-OCR_main.py` 與 `GTB-Solver-OCR_timer.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
Moe_Mode = False
```

### 7. 修改自動複製狀態

- 預設關閉。如需自動複製首個匹配結果至剪貼簿，請在 `GTB-Solver-OCR_main.py` 內找到以下代碼，替換 `False` 為 `True` 即可

``` Python
Auto_Copy = False
```

## ⚜ 注意事項

- 本項目僅作 Demo 演示之用，所提供的詞庫文件 `GTB_Thesaurus_Demo.xlsx` 內含 100 對範例詞彙及少量 Shortcut(s) & Multiword(s)，您可在原有基礎上繼續補充使用或依據前述配置修改方法更換詞庫文件
- 濫用建築猜猜寶會為您帶來不公平的遊戲優勢！請在有限範圍內合理使用，作者對因濫用本程序而導致的封鎖問題概不負責