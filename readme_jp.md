<h1 align="center">
  <br>
  GTB-Solver
  <br>
</h1>

<h3 align="center">
<a href="https://github.com/IceNightKing/GTB-Solver/blob/master/readme_jp.md">GTB-Solver Demo ブランチ</a> | [Beta] GTB-Solver OCR ブランチ
</h3>

<h3 align="center">
<font color="orange">🚫 注: GTB-Solver OCR ブランチは現在 Beta テスト中であり、まだ利用できません！ 😇</font>
</h3>

## ⚜ 機能概要

**[简体中文](./readme_zh.md) | [繁體中文](./readme_cht.md) | 日本語 | [English](./readme.md)**

英語のヒントと光学式文字認識に基づいて、Hypixel サーバー上の「Guess The Build」ゲームのテーマを素早く推測します。

## ⚜ 前提条件

### 1. Python ランタイム環境のセットアップ

- [Python の公式サイトにダウンロードします](https://www.python.org/downloads/ "Python Source Releases")
  - Python 3.10 以降をインストールすることを推奨します、古いバージョンのバグは修正されません
  - Python を初めてインストールするときは、必ず `Add Python x.x to PATH` をチェックして環境変数を追加してください

### 2. 関連する依存ライブラリをインストールする

- **Windows**: `Installation of Dependency Libraries.bat` を実行して、関連する依存ライブラリをインストールします
- **macOS & Linux**: `Installation of Dependency Libraries.sh` を実行して、関連する依存ライブラリをインストールします

### 3. 光学式文字認識エリアを変更する

- アクションバーの上にあるテーマのヒントエリアを見つけ、左上隅と右下隅の座標を取得し、`コンフィギュレーション変更方法 1` に従って光学式文字認識エリアを変更します

### 4. ゲーム内の関連設定を変更する

- 認識精度を向上させるには、以下の手順でゲーム内の関連設定を変更することをお勧めします
  - `設定...` > `アクセシビリティ設定...` > `テキストの背景 : すべて`
  - `設定...` > `チャット設定...` > `背景の不透明度 : 60%`
  - `設定...` > `チャット設定...` > `幅 : 40ピクセル`

> **ヒント**: 上記は **Minecraft 1.19** の関連設定変更方法であり、あくまで参考です。実際のゲームのバージョンが異なる場合、変更方法が変わる可能性があります

### 5. Hypixel サーバーの言語を英語に切り替える

- Hypixel サーバーに `/lang en` と入力して切り替えます

## ⚜ 使用方法

### 1. メインプログラムを実行する

- **Windows**: 前提条件が満たされたら、`GTB-Solver-OCR.bat` を実行します
- **macOS & Linux**: 前提条件が満たされたら、`GTB-Solver-OCR.sh` を実行します

### 2. メインプログラムを終了する

- このプログラムはデフォルトで繰り返し実行されます、`Ctrl+C` を押してプログラムを終了します

## ⚜ 認識結果(「Water Bottle」を例にします)

``` Python
テーマ: _____ ______
光学式文字認識結果: _____ ______
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

テーマ: _a___ ______
光学式文字認識結果: _a___ ______
Magic Carpet
Paint Bucket - Fargburk
Table Tennis - Bordtenni
Water Bottle - Waterfle
Water Bucket - Vandspand
# ここでは、プレイヤーの建物の大まかな輪郭に基づいて選択できます

テーマ: _a___ _o____
光学式文字認識結果: _a___ _o____
Water Bottle - Waterfle
```

## ⚜ コンフィギュレーションの変更

### 1. 光学式文字認識エリアの変更

- デフォルトの認識領域は、左上隅に `(1000, 1200)`、右下隅に `(1550, 1300)` の座標を持つ長方形です。光学式文字認識領域を変更する必要がある場合は、`GTB-Solver-OCR_main.py` で次のコードを見つけて、座標を変更してください

``` Python
Left, Top = 1000, 1200
Right, Bottom = 1550, 1300
```

- 注: 光学式文字認識エリアは、ゲームウィンドウのサイズと位置によって異なります

### 2. 繰り返し認識間隔の変更

- デフォルトの認識間隔は `3.0` 秒です。繰り返し認識間隔を変更する必要がある場合は、`GTB-Solver-OCR_timer.py` で次のコードを見つけて、値を変更してください

``` Python
Interval_Time = 3.0
```

### 3. GPU アクセラレーション認識ステータスの変更

- GPU アクセラレーション認識モードはデフォルトで有効になっています。GPU アクセラレーション認識モードを無効にするには、`GTB-Solver-OCR_main.py` で次のコードを見つけて、`True` を `False` に置き換えてください

``` Python
GPU_Mode = True
```

- 注: GPU アクセラレーション認識モードを有効にするには、デバイスに CUDA 搭載の NVIDIA GPU があり、適切な [GPU ドライバー](https://www.nvidia.co.jp/Download/index.aspx?lang=jp "NVIDIA Driver Downloads")、[CUDA ツールキット](https://developer.nvidia.com/cuda-downloads "NVIDIA CUDA Toolkit Downloads")、および対応するバージョンの [PyTorch](https://pytorch.org/get-started/locally/ "Install PyTorch Locally") をインストールする必要があります。それ以外の場合は、認識に CPU が引き続き使用されます

### 4. シソーラス・ファイルのパスを変更するか、シソーラス・ファイルを置き換える

- デフォルトのパスは `GTB-Solver-OCR_main.py` と同じフォルダです。シソーラス・ファイルのパスを変更したり、シソーラス・ファイルを置き換えたりする必要がある場合は、`GTB-Solver-OCR_main.py` で次のコードを見つけて、引用符で囲まれたパスを置き換えてください(中国語のパスはサポートされています)

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- 注: シソーラス・ファイルには、少なくとも「English」カラムが必要です(大文字と小文字は厳密に区別されます)

### 5. プログラム出力言語の変更

- デフォルトの出力言語はシステム言語であり、システム言語がサポートされていない場合は英語となります。プログラムの出力言語を変更する必要がある場合は、`GTB-Solver-OCR_main.py` および `GTB-Solver-OCR_timer.py` で次のコードを見つけて、対応する言語コードを引用符で囲んで追加してください

``` Python
Multi_Lang = ""
```

- 言語コードリスト

  | 出力言語 | 言語コード |
  | :----: | :----: |
  | 簡体字中国語 | zh |
  | 繁体字中国語 | cht |
  | 日本語 | jp |
  | 英語 | en |

### 6. 出力萌えステータスの変更

- 出力萌えモードはデフォルトでは無効になっています。出力萌えモードを有効にするには、`GTB-Solver-OCR_main.py` および `GTB-Solver-OCR_timer.py` で次のコードを見つけて、`False` を `True` に置き換えてください

``` Python
Moe_Mode = False
```

### 7. 自動コピーステータスの変更

- 自動コピーモードはデフォルトでは無効になっています。最初にマッチした結果を自動的にクリップボードにコピーするには、`GTB-Solver-OCR_main.py` で次のコードを見つけて、`False` を `True` に置き換えてください

``` Python
Auto_Copy = False
```

## ⚜ 重要な注意事項

- このプロジェクトは Demo 専用で、提供されたシソーラス・ファイル `GTB_Thesaurus_Demo.xlsx` には 100 組のサンプル単語といくつかの「Shortcut(s) & Multiword(s)」が含まれています。元のベースで補足し続けることも、前述の構成変更方法に従ってシソーラス・ファイルを置き換えることもできます
- GTB-Solver を悪用すると、ゲームで不当な優位性が得られます。限られた範囲内で合理的に使用してください。プログラムの悪用による BAN について、作者は一切責任を負いません