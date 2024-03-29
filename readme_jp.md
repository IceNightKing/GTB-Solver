<h1 align="center">
  <br>
  GTB-Solver
  <br>
</h1>

<h3 align="center">
GTB-Solver Demo ブランチ | <a href="https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme_jp.md">[Beta] GTB-Solver OCR ブランチ</a>
</h3>

## ⚜ 機能概要

**[简体中文](./readme_zh.md) | [繁體中文](./readme_cht.md) | 日本語 | [English](./readme.md)**

英語または簡体字中国語のヒントと正規表現に基づいて、Hypixel サーバー上の「Guess The Build」ゲームのテーマを素早く推測します。

## ⚜ 更新ログ

### 2024/03/25 - v3.6

- \[Add\] シソーラスのセルフチェックを追加しました
- \[Opt\] これで、ユーザーは `@sc` を接頭辞として「Shortcut(s)」にマッチさせることができます
- \[Opt\] これで、ユーザーは `@mw` を接頭辞として「Multiword(s)」にマッチさせることができます

### 2024/03/17 - v3.5

- \[Add\] 複数の単語カウントではない結果に対して、一致する単語カウントのプロンプトが表示されるようになりました
- \[Opt\] これで、ユーザーはプログラム内で出力言語を切り替えることができるようになります
- \[Opt\] コードの最適化

### 2024/02/29 - v3.4

- \[Opt\] これで、ユーザーは `Ctrl+C` を押してプログラムを通常どおり終了できるようになります
- \[Opt\] コードの最適化

### 2024/02/20 - v3.3

- \[Fix\] 文字 `.` がマッチしない問題を修正しました

  ``` TXT
  # 以下のテーマが正しくマッチングできるようになりました
  Mrs. Claus
  ```

- \[Opt\] コードの最適化

### 2024/02/14 - v3.2

- \[Add\] [GTB-Solver OCR ブランチリンク](https://github.com/IceNightKing/GTB-Solver/blob/OCR/readme_jp.md "GTB-Solver OCR Branch")
- \[Add\] macOS および Linux システムのサポート
- \[Add\] 英語と簡体字中国語のマッチング選択のサポート
- \[Fix\] 不正なユーザー入力によって引き起こされる可能性のある `re.error` クラッシュを修正しました

### 2024/02/13 - v3.1

- \[Fix\] 関連する依存ライブラリをインストールする `Installation of Dependency Libraries.bat` を実行しても、関連する依存ライブラリの数が不足する場合がある問題を修正しました
- \[Opt\] 将来のバージョンの Python で動作するように、システム言語の取得方法を更新しました

### 2024/02/08 - v3.0

- \[Add\] 簡体字中国語入力マッチングのサポート
- \[Fix\] 文字 `-` がマッチしない問題を修正しました

  ``` TXT
  # 以下のテーマが正しくマッチングできるようになりました
  Jack-O-Lantern
  T-Rex
  Trick-or-Treating
  T-Shirt - Tricou
  ```

- \[Fix\] シソーラス・カラム名が正しく設定されていないことが原因で発生する可能性がある `KeyError` クラッシュを修正しました

### 2024/02/04 - Demo_202402

- \[Add\] 多言語 `readme` ファイルのサポート
- \[Add\] 出力萌えモードのサポート
- \[Fix\] 不正なユーザー入力によって引き起こされる可能性のある `OverflowError` クラッシュを修正しました
- \[Fix\] 不正なユーザー入力によって引き起こされる可能性のある `re.error` クラッシュを修正しました
- \[Opt\] プログラム出力言語はデフォルトでシステム言語に依存するようになりました
- \[Opt\] シソーラスの更新
- \[Opt\] コードのリファクタリング

## ⚜ 前提条件

### 1. Python ランタイム環境のセットアップ

- [Python の公式サイトにダウンロードします](https://www.python.org/downloads/ "Python Source Releases")
  - Python 3.10 以降をインストールすることを推奨します、古いバージョンのバグは修正されません
  - Python を初めてインストールするときは、必ず `Add Python x.x to PATH` をチェックして環境変数を追加してください

### 2. 関連する依存ライブラリをインストールする

- **Windows**: `Installation of Dependency Libraries.bat` を実行して、関連する依存ライブラリをインストールします
- **macOS & Linux**: `Installation of Dependency Libraries.sh` を実行して、関連する依存ライブラリをインストールします

### 3. Hypixel サーバーの言語を英語に切り替える

- Hypixel サーバーに `/lang en` と入力して切り替えます

## ⚜ 使用方法

### 1. メインプログラムを実行する

- **Windows**: 前提条件が満たされたら、`GTB-Solver.bat` を実行します
- **macOS & Linux**: 前提条件が満たされたら、`GTB-Solver.sh` を実行します

### 2. メインプログラムを終了する

- GTB-Solver はデフォルトで繰り返し実行されます。`0` を入力するか、`Ctrl+C` を押してプログラムを終了します

## ⚜ マッチングルール

1. **数字**: アンダースコアの数
2. **アルファベット**: マッチし、数字の前後に直接挿入できます
    - アルファベットを入力する際、大文字と小文字は区別されません
3. **簡体字中国語**: マッチし、数字の前後に直接挿入できます
4. **ハイフン**: マッチし、数字の前後に直接挿入できます
5. **スペース**: マッチしません、マッチする式に手動で入力する必要があります
6. **正規表現文字**: 部分的に使用可能
7. **デフォルトのマッチング**: 英語と簡体字中国語
    - 純粋に数字のマッチする式を入力したときだけ英語にマッチさせたい場合は、接頭辞 `@en` を使用することができます
    - 純粋に数字のマッチする式を入力したときだけ簡体字中国語にマッチさせたい場合は、接頭辞 `@zh` を使用することができます

> **ヒント**: スペース、ハイフン、7 以上の数字を入力すると、英語のみがマッチします。簡体字中国語を入力すると、簡体字中国語のみがマッチします

## ⚜ 推測方法(「Water Bottle」を例にします)

### 1. 数字とアルファベットを使って推測する

``` TXT
テーマ: _____ ______
マッチする式を入力してください: 5 6
テーマの英語文字数は 12 です
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
テーマ: _a___ ______
マッチする式を入力してください: 1a3 6
テーマの英語文字数は 12 です
Magic Carpet
Paint Bucket - Fargburk
Table Tennis - Bordtenni
Water Bottle - Waterfle
Water Bucket - Vandspand
# ここでは、プレイヤーの建物の大まかな輪郭に基づいて選択できます
```

``` TXT
テーマ: _a___ _o____
マッチする式を入力してください: 1a3 1o4
テーマの英語文字数は 12 です
Water Bottle - Waterfle
```

### 2. 正規表現を使って推測する

``` TXT
テーマ: _a___ ______
マッチする式を入力してください: .a3 .*
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
テーマ: _a___ _o____
マッチする式を入力してください: .a3 .o.*
Games Controller - Controller
Water Bottle - Waterfle
# ここでは、プレイヤーの建物の大まかな輪郭に基づいて選択できます
```

``` TXT
テーマ: _a___ _o___e
マッチする式を入力してください: .a3 .o.*e
テーマの英語文字数は 12 です
Water Bottle - Waterfle
```

## ⚜ コンフィギュレーションの変更

### 1. シソーラス・ファイルのパスを変更するか、シソーラス・ファイルを置き換える

- デフォルトのパスは `GTB-Solver_main.py` と同じフォルダです。シソーラス・ファイルのパスを変更したり、シソーラス・ファイルを置き換えたりする必要がある場合は、`GTB-Solver_main.py` で次のコードを見つけて、引用符で囲まれたパスを置き換えてください(中国語のパスはサポートされています)

``` Python
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
```

- 注: シソーラス・ファイルには、少なくとも「English」カラムが必要です(大文字と小文字は厳密に区別されます)

### 2. プログラム出力言語の変更

- デフォルトの出力言語はシステム言語であり、システム言語がサポートされていない場合は英語となります。プログラムのデフォルトの出力言語を変更する必要がある場合は、`GTB-Solver_main.py` で次のコードを見つけて、対応する言語コードを引用符で囲んで追加してください。プログラム出力言語を一時的に変更するだけの場合は、対応する切り替えコマンドを直接入力できます

``` Python
Multi_Lang = ""
```

- 言語コードと切り替えコマンドリスト

  | 出力言語 | 言語コード | 切り替えコマンド |
  | :----: | :----: | :----: |
  | 簡体字中国語 | zh | /lang zh |
  | 繁体字中国語 | cht | /lang cht |
  | 日本語 | jp | /lang jp |
  | 英語 | en | /lang en |

### 3. 出力萌えステータスの変更

- 出力萌えモードはデフォルトでは無効になっています。出力萌えモードを有効にするには、`GTB-Solver_main.py` で次のコードを見つけて、`False` を `True` に置き換えてください

``` Python
Moe_Mode = False
```

### 4. 自動コピーステータスの変更

- 自動コピーモードはデフォルトでは無効になっています。最初にマッチした結果を自動的にクリップボードにコピーするには、`GTB-Solver_main.py` で次のコードを見つけて、`False` を `True` に置き換えてください

``` Python
Auto_Copy = False
```

## ⚜ 重要な注意事項

- このプロジェクトは Demo 専用で、提供されたシソーラス・ファイル `GTB_Thesaurus_Demo.xlsx` には 100 組のサンプル単語といくつかの「Shortcut(s) & Multiword(s)」が含まれています。元のベースで補足し続けることも、前述の構成変更方法に従ってシソーラス・ファイルを置き換えることもできます
- GTB-Solver を悪用すると、ゲームで不当な優位性が得られます。限られた範囲内で合理的に使用してください。プログラムの悪用による BAN について、作者は一切責任を負いません