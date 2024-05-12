"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on multi-language hints and regular expressions.
Version: 4.2
Author: IceNight
GitHub: https://github.com/IceNightKing
"""

# ------------------------- Configuration Modification -------------------------
# Modify the path of the thesaurus file or replace the thesaurus file
GTB_THESAURUS = r"GTB_Thesaurus_Demo.xlsx"
# Modify the program output language: 简体中文(zh), 繁體中文(cht), 日本語(jp), English(en)
MULTI_LANG = ""
# Modify the output moe status
MOE_MODE = False
# Modify the automatic copying status
AUTO_COPY = False
# Modify the log assisted processing status
LAP_MODE = False
# Modify the path of the log file
LOG_FILE = r"C:\Minecraft\.minecraft\logs\latest.log"
# Modify the repeat reading interval of the log file (sec)
LAP_INTERVAL = 0.05
# Modify the custom copy content at the end of the game
CUSTOM_CONTENT = "Good Game"
# Modify the theme auxiliary recording status
TAR_MODE = False
# Modify the path of the theme auxiliary recording file
GTB_TAR_FILE = r"GTB_TAR_File.txt"
# Modify the semi-automatic sending status
SAS_MODE = False
# Modify the semi-automatic sending interval (sec)
SAS_INTERVAL = 2.0
# Modify the game window title
WINDOW_TITLE = "Minecraft"
# ------------------------------------------------------------------------------

import colorama
from colorama import Fore, Style
import locale
import os
import pandas as pd
import re
import pyperclip
import threading
from collections import deque
import time
import pyautogui

def output_language():
    global lang

    if MULTI_LANG:
        lang = MULTI_LANG.lower()
    else:
        system_lang, _ = locale.getlocale()

        if any(re.search(r'\b{}\b'.format(system_lang_part), system_lang.lower()) for system_lang_part in {"zh", "chinese"}):
            if any(re.search(r'\b{}\b'.format(system_lang_part), system_lang.lower()) for system_lang_part in {"cht", "traditional", "hk", "hong_kong", "mo", "macao", "tw", "taiwan"}):
                lang = "cht"
            else:
                lang = "zh"
        elif any(re.search(r'\b{}\b'.format(system_lang_part), system_lang.lower()) for system_lang_part in {"ja", "jp", "japanese"}):
            lang = "jp"
        elif any(re.search(r'\b{}\b'.format(system_lang_part), system_lang.lower()) for system_lang_part in {"en", "english"}):
            lang = "en"
        else:
            print(f'{Fore.YELLOW}{output_message("unsupported_language", system_lang.split("_")[0], moe)}{Style.RESET_ALL}')
            lang = "en"

    if lang not in {"zh", "cht", "jp", "en"}:
        print(f'{Fore.YELLOW}{output_message("unsupported_language", lang, moe)}{Style.RESET_ALL}')
        lang = "en"

def output_message(key, lang, moe = False, word_chars = "", e = "", theme_chars = "", output_del_elem = "", correct_theme = "", LAP_guess_cnt = ""):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
        },
        "program_info": {
            "zh": "欢迎使用建筑猜猜宝 v4.2 ",
            "cht": "歡迎使用建築猜猜寶 v4.2 ",
            "jp": "GTB-Solver v4.2 へようこそ",
            "en": "Welcome to GTB-Solver v4.2"
        },
        "program_note": {
            "zh": "温馨提示：建筑猜猜宝默认重复运行，输入 0 或按下 Ctrl+C 以退出程序",
            "cht": "溫馨提示：建築猜猜寶預設重複運行，輸入 0 或按下 Ctrl+C 以退出程式",
            "jp": "注：GTB-Solver はデフォルトで繰り返し実行されます。「0」を入力するか、「Ctrl+C」を押してプログラムを終了します",
            "en": "Note: GTB-Solver runs repeatedly by default, enter 0 or press Ctrl+C to exit the program"
        },
        "thesaurus_self_check_starts": {
            "zh": "词库状态自检",
            "cht": "詞庫狀態自檢",
            "jp": "シソーラス・セルフチェック開始",
            "en": "Thesaurus Self-check"
        },
        "thesaurus_self_check_completed": {
            "zh": "词库自检完成",
            "cht": "詞庫自檢完成",
            "jp": "シソーラス・セルフチェック完了",
            "en": "Self-check Completed"
        },
        "error_thesaurus_file_not_found": {
            "zh": "错误：未找到词库文件，请检查文件路径是否设置正确",
            "cht": "錯誤：未找到詞庫檔案，請檢查檔案路徑是否設定正確",
            "jp": "エラー：シソーラス・ファイルが見つかりません、ファイルのパスが正しく設定されているか確認してください",
            "en": "Error: Thesaurus file not found, please check if the file path is configured correctly"
        },
        "error_thesaurus_column_not_found": {
            "zh": "错误：未找到 English 列，请检查词库列名是否设置正确",
            "cht": "錯誤：未找到 English 欄，請檢查詞庫欄名是否設定正確",
            "jp": "エラー：「English」カラムが見つかりません、シソーラス・カラム名が正しく設定されているか確認してください",
            "en": 'Error: "English" column not found, please check if the the thesaurus column name is configured correctly'
        },
        "error_log_file_not_found": {
            "zh": "错误：未找到日志文件，日志辅助处理模式启动失败，请检查文件路径是否设置正确",
            "cht": "錯誤：未找到日誌檔案，日誌輔助處理模式啟動失敗，請檢查檔案路徑是否設定正確",
            "jp": "エラー：ログファイルが見つからなかったため、ログアシスト処理モードを開始できませんでした。ファイルのパスが正しく設定されているか確認してください",
            "en": "Error: The log assisted processing mode failed to start because the log file was not found, please check if the file path is configured correctly"
        },
        "error_log_decoding_failed": {
            "zh": "错误：未能成功解码日志文件，日志辅助处理模式启动失败，请删除日志文件后重新开始游戏",
            "cht": "錯誤：未能成功解碼日誌檔案，日誌輔助處理模式啟動失敗，請刪除日誌檔案後重新開始遊戲",
            "jp": "エラー：ログファイルが正常にデコードできなかったため、ログアシスト処理モードを開始できませんでした。ログファイルを削除してゲームを再起動してください",
            "en": "Error: The log assisted processing mode failed to start because the log file could not be decoded successfully. Please delete the log file and restart the game"
        },
        "error_TAR_file_decoding_failed": {
            "zh": "错误：未能成功解码主题辅助记录文件，主题辅助记录模式启动失败，请删除辅助记录文件后重新开始游戏",
            "cht": "錯誤：未能成功解碼主題輔助記錄檔案，主題輔助記錄模式啟動失敗，請刪除輔助記錄檔案後重新開始遊戲",
            "jp": "エラー：テーマ補助記録ファイルが正常にデコードできなかったため、テーマ補助記録モードを開始できませんでした。補助記録ファイルを削除してゲームを再起動してください",
            "en": "Error: The theme auxiliary recording mode failed to start because the theme auxiliary recording file could not be decoded successfully. Please delete the auxiliary recording file and restart the game"
        },
        "error_TAR_disabled_LAP": {
            "zh": "错误：主题辅助记录模式启动失败，因为前置的日志辅助处理模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：主題輔助記錄模式啟動失敗，因為前置的日誌輔助處理模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回のログアシスト処理モードが有効になっていないため、テーマ補助記録モードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "en": "Error: The theme auxiliary recording mode failed to start because the previous log assisted processing mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_SAS_disabled_autocopy": {
            "zh": "错误：半自动发送模式启动失败，因为前置的自动复制模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：半自動發送模式啟動失敗，因為前置的自動複製模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回の自動コピーモードが有効になっていないため、半自動送信モードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "en": "Error: The semi-automatic sending mode failed to start because the previous automatic copying mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_SAS_disabled_LAP": {
            "zh": "错误：半自动发送模式启动失败，因为前置的日志辅助处理模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：半自動發送模式啟動失敗，因為前置的日誌輔助處理模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回のログアシスト処理モードが有効になっていないため、半自動送信モードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "en": "Error: The semi-automatic sending mode failed to start because the previous log assisted processing mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_SAS_window_not_found": {
            "zh": "错误：未找到游戏窗口，当前内容半自动发送失败，请检查游戏窗口名称是否设置正确",
            "cht": "錯誤：未找到遊戲窗口，本次內容半自動發送失敗，請檢查遊戲窗口名稱是否設定正確",
            "jp": "エラー：ゲームウィンドウが見つからなかったため、現在のコンテンツの半自動送信に失敗しました。ゲームウィンドウのタイトルが正しく設定されているか確認してください",
            "en": "Error: The current content semi-automatic sending failed because the game window was not found. Please check if the game window title is set correctly"
        },
        "error_exception": {
            "zh": f'错误：{e} ',
            "cht": f'錯誤：{e} ',
            "jp": f'エラー：{e} ',
            "en": f'Error: {e}'
        },
        "input_prompt": {
            "zh": "请输入匹配式：",
            "cht": "請輸入匹配式：",
            "jp": "マッチする式を入力してください：",
            "en": "Please enter the matching expression: "
        },
        "exit_program": {
            "zh": "您已退出程序",
            "cht": "您已退出程式",
            "jp": "プログラムを終了しました",
            "en": "You have exited the program"
        },
        "output_en_word_chars": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマの英字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long'
        },
        "output_zh_word_chars": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題簡體中文字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの簡体字中国語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Simplified Chinese'
        },
        "output_cht_word_chars": {
            "zh": f'该主题繁体中文字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの繁体字中国語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Traditional Chinese'
        },
        "output_jp_word_chars": {
            "zh": f'该主题日语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題日文字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Japanese'
        },
        "language_switched": {
            "zh": "已将语言设置为简体中文",
            "cht": "已將語言設定為繁體中文",
            "jp": "言語を日本語に設定しました",
            "en": "You set your language to English"
        },
        "match_failed": {
            "zh": "匹配失败，未在当前词库中找到匹配条目",
            "cht": "匹配失敗，未在當前詞庫中找到匹配條目",
            "jp": "マッチに失敗しました、現在のシソーラスに一致するものが見つかりませんでした",
            "en": "Match failed, no matching entry found in the current thesaurus"
        },
        "output_LAP_game_round": {
            "zh": "游戏回合：",
            "cht": "遊戲回合：",
            "jp": "ゲームラウンド：",
            "en": "Game Round: "
        },
        "output_LAP_builder_name": {
            "zh": "建筑师：",
            "cht": "建築師：",
            "jp": "建築家：",
            "en": "Builder: "
        },
        "output_LAP_builder_left": {
            "zh": "本回合的建筑师离开了游戏！跳过",
            "cht": "當前回合的建築師離開了遊戲！跳過",
            "jp": "このラウンドの建築家がゲームから退出しました。スキップ中",
            "en": "The builder of this round has left the game! Skipping"
        },
        "output_LAP_builder_AFK": {
            "zh": "本回合的建筑师处于挂机状态！跳过",
            "cht": "當前回合的建築師處於掛網狀態！跳過",
            "jp": "このラウンドの建築家が無操作状態です。スキップ中",
            "en": "The builder of this round is AFK! Skipping"
        },
        "output_LAP_builder_unplaced": {
            "zh": "本回合的建筑师尚未放置任何方块！跳过",
            "cht": "當前回合的建築師沒有放置任何方塊！跳過",
            "jp": "このラウンドの建築家がブロックを設置していません。スキップ中",
            "en": "The builder of this round hasn't placed any blocks! Skipping"
        },
        "output_LAP_theme_chars": {
            "zh": f'本回合主题字数为 {Fore.YELLOW}{theme_chars}{Fore.CYAN} 个字',
            "cht": f'當前回合主題字數為 {Fore.YELLOW}{theme_chars}{Fore.CYAN} 個字',
            "jp": f'このラウンドのテーマの文字数は {Fore.YELLOW}{theme_chars}{Fore.CYAN} です',
            "en": f'The theme of this round is {Fore.YELLOW}{theme_chars}{Fore.CYAN} characters long'
        },
        "output_LAP_guess_info": {
            "zh": f'检测到有玩家猜测了主题 {Fore.YELLOW}{output_del_elem}{Fore.RED} 但未猜对，即将据此输出筛选后的匹配条目',
            "cht": f'偵測到有玩家猜測了主題 {Fore.YELLOW}{output_del_elem}{Fore.RED} 但未猜對，即將據此輸出篩選後的匹配條目',
            "jp": f'プレイヤーがテーマ {Fore.YELLOW}{output_del_elem}{Fore.RED} を推測したが正しく推測しなかったことを検出し、それに応じてフィルタリングされたマッチするエントリが出力されます',
            "en": f'Detects that the player guessed theme(s) {Fore.YELLOW}{output_del_elem}{Fore.RED} but did not guess correctly, and the filtered matching entries will be output accordingly'
        },
        "output_LAP_correct_guess": {
            "zh": f'检测到您正确猜出主题！本回合辅助猜测已暂停',
            "cht": f'偵測到您正確猜出主題！當前回合輔助猜測已暫停',
            "jp": f'テーマを正しく推測したことが検出されました。このラウンドでは、アシストによる推測は一時停止されています',
            "en": f'Detects that you have correctly guessed the theme! Assisted guessing has been paused for this round'
        },
        "output_LAP_correct_theme": {
            "zh": f'本回合的主题是 {Fore.YELLOW}{correct_theme}{Fore.CYAN} ',
            "cht": f'當前回合的主題是 {Fore.YELLOW}{correct_theme}{Fore.CYAN} ',
            "jp": f'このラウンドのテーマは {Fore.YELLOW}{correct_theme}{Fore.CYAN} でした',
            "en": f'The theme of this round was {Fore.YELLOW}{correct_theme}{Fore.CYAN}'
        },
        "output_TAR_theme_added": {
            "zh": f'已将主题 {Fore.YELLOW}{correct_theme}{Fore.GREEN} 添加至辅助记录文件',
            "cht": f'已將主題 {Fore.YELLOW}{correct_theme}{Fore.GREEN} 新增至輔助記錄檔案',
            "jp": f'テーマ {Fore.YELLOW}{correct_theme}{Fore.GREEN} が補助記録ファイルに追加されました',
            "en": f'Theme {Fore.YELLOW}{correct_theme}{Fore.GREEN} has been added to the auxiliary recording file'
        },
        "output_LAP_game_over": {
            "zh": f'本场游戏结束，日志辅助处理模式共计帮助您猜测了 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 次',
            "cht": f'本場遊戲結束，日誌輔助處理模式總計幫助您猜測了 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 次',
            "jp": f'ゲームは終了しました。ログアシスト処理モードにより、合計 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 回推測できました',
            "en": f'The game is over, and the log assisted processing mode has helped you guess {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} time(s) in total'
        },
        "output_SAS_content_sent": {
            "zh": f'已发送剪贴板内容 {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} 至游戏内',
            "cht": f'已發送剪貼簿內容 {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} 至遊戲內',
            "jp": f'クリップボードのコンテンツ {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} をゲームに送信しました',
            "en": f'Sent clipboard content {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} to the game'
        }
    }

    moe_suffix = {
        "zh": "喵~",
        "cht": "喵~",
        "jp": "ニャー~",
        "en": " meow~"
    }

    if key == "input_prompt" and moe:
        input_prompt_moe = {
            "zh": "请输入奇妙咒语：",
            "cht": "請輸入奇妙咒語：",
            "jp": "魔法の呪文を入力してください：",
            "en": "Please enter the marvelous spell: "
        }
        return input_prompt_moe.get(lang, input_prompt_moe["en"])

    if key == "output_LAP_builder_left" and moe:
        output_LAP_builder_left_moe = {
            "zh": "本回合的建筑师回到快乐老家了！跳过喵~",
            "cht": "當前回合的建築師回到快樂老家了！跳過喵~",
            "jp": "このラウンドの建築家は幸せな故郷に戻ってきました。スキップ中ニャー~",
            "en": "The builder of this round has returned to the happy hometown! Skipping meow~"
        }
        return output_LAP_builder_left_moe.get(lang, output_LAP_builder_left_moe["en"])

    if key == "output_LAP_builder_AFK" and moe:
        output_LAP_builder_AFK_moe = {
            "zh": "本回合的建筑师沉浸在了幻想乡之中！跳过喵~",
            "cht": "當前回合的建築師沉浸在了幻想鄉之中！跳過喵~",
            "jp": "このラウンドの建築家は幻想郷に浸っています。スキップ中ニャー~",
            "en": "The builder of this round is immersed in Gensokyo! Skipping meow~"
        }
        return output_LAP_builder_AFK_moe.get(lang, output_LAP_builder_AFK_moe["en"])

    if key == "output_LAP_builder_unplaced" and moe:
        output_LAP_builder_unplaced_moe = {
            "zh": "本回合建筑师的智商尚未占领高地！跳过喵~",
            "cht": "當前回合建築師的智商尚未佔領高地！跳過喵~",
            "jp": "このラウンドの建築家はあまり賢く見えません。スキップ中ニャー~",
            "en": "The builder of this round doesn't look too smart! Skipping meow~"
        }
        return output_LAP_builder_unplaced_moe.get(lang, output_LAP_builder_unplaced_moe["en"])

    message = messages.get(key, {}).get(lang, messages["unsupported_language"]["en"])
    message += f'{moe_suffix.get(lang, moe_suffix["en"])}' if moe else ""
    return message

def pattern_from_input(user_input):
    global column_prefix_dic

    column_prefix_dic = {
        "@en": "English",
        "@zh": "简体中文",
        "@cht": "繁體中文",
        "@jp": "日本語",
        "@sc": "Shortcut(s)",
        "@mw": "Multiword(s)"
    }
    target_column = None
    num = pattern = ""
    banned_chars = r'()'

    for prefix, column in column_prefix_dic.items():
        if user_input.startswith(prefix) and column in df.columns:
            user_input = user_input[len(prefix):]
            user_input = r'[a-zA-Z]' if prefix in {"@sc", "@mw"} and user_input in {"1", ".", "_"} else user_input
            user_input = r'[a-zA-Z].*' if prefix in {"@sc", "@mw"} and user_input in {".*", "_*", "1.*", "1_*", "..*", "._*", "_.*", "__*"} else user_input
            target_column = column if user_input else target_column
            break

    for char in user_input:
        if char.isdigit():
            num += char
        else:
            if num:
                pattern += rf"[a-zA-Z\u4E00-\u9FFF\u3040-\u30FF\uFF66-\uFF9F-.'《》]{{{num}}}"
                num = ""
            pattern += re.escape(char) if char in banned_chars else ("." if char == "_" else char)
    pattern += rf"[a-zA-Z\u4E00-\u9FFF\u3040-\u30FF\uFF66-\uFF9F-.'《》]{{{num}}}" if num else ""
    return pattern, target_column

def input_thesaurus():
    global df

    print(f'{Fore.MAGENTA}{output_message("program_info", lang, moe)}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}{output_message("program_note", lang, moe)}{Style.RESET_ALL}')

    if not os.path.exists(GTB_THESAURUS):
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_file_not_found", lang, moe)}{Style.RESET_ALL}')
        exit()
    else:
        df = pd.read_excel(GTB_THESAURUS, keep_default_na = False).replace("", "%")

    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_starts", lang, moe)} {"-" * 10}{Style.RESET_ALL}')
    for column in ["English", "简体中文", "繁體中文", "日本語", "Shortcut(s)", "Multiword(s)"]:
        print(f'{Fore.CYAN}{column}  \t\t\t{Fore.GREEN}●{Style.RESET_ALL}') if column in df.columns else print(f'{Fore.CYAN}{column}  \t\t\t{Fore.RED}●{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_completed", lang, moe)} {"-" * 10}{Style.RESET_ALL}')

    if "English" not in df.columns:
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, moe)}{Style.RESET_ALL}')
        exit()

def input_matching():
    global lang_code_dic, LAP_match_lst_dic
    global lang, copy_to_clipboard

    while True:
        lang_code_dic = {
            "en": "English",
            "zh": "简体中文",
            "cht": "繁體中文",
            "jp": "日本語"
        }
        matching_rows = None
        lang_switch = matched_rows = False
        copy_to_clipboard = AUTO_COPY

        user_input = input(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}').lower()
        input_pattern, target_column = pattern_from_input(user_input)

        if user_input == "0":
            print(f'{Fore.MAGENTA}{output_message("exit_program", lang, moe)}{Style.RESET_ALL}')
            break
        elif user_input.startswith("/lang "):
            new_lang = user_input.split()[1]
            if new_lang in {i for i in lang_code_dic}:
                lang = new_lang
                lang_switch = True

        try:
            if target_column and target_column in df.columns:
                matching_rows = df[df[target_column].astype(str).str.lower().str.contains(f'^{input_pattern}$', na = False)]
            else:
                for lang_code, full_lang in lang_code_dic.items():
                    if lang_code == lang and full_lang in df.columns and lang != "en":
                        matching_rows = df[df[["English", full_lang]].apply(lambda x: x.astype(str).str.lower().str.contains(f'^{input_pattern}$', na = False)).any(axis = 1)]
                        matched_rows = True
                        break
                matching_rows = df[df["English"].astype(str).str.lower().str.contains(f'^{input_pattern}$', na = False)] if not matched_rows else matching_rows
        except (OverflowError, re.error):
            print(f'{Fore.YELLOW}{output_message("match_failed", lang, moe)}{Style.RESET_ALL}')
            continue
        except KeyError:
            print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, moe)}{Style.RESET_ALL}')
            exit()

        if not matching_rows.empty:
            word_chars_lst_dic = {
                "English": [],
                "简体中文": [],
                "繁體中文": [],
                "日本語": []
            }
            LAP_match_lst_dic = {
                "WF": [],
                "English": [],
                "简体中文": [],
                "繁體中文": [],
                "日本語": [],
                "Shortcut(s)": [],
                "Multiword(s)": []
            }
            target_column_code = {v: k for k, v in lang_code_dic.items()}.get(target_column, None)
            output_word_chars_flag = False
            color_cnt = 0

            def get_wf_color(wf_row):
                thresholds = [(1.00, Fore.BLUE), (4.00, Fore.WHITE), (7.00, Fore.GREEN), (10.00, Fore.YELLOW), (13.00, Fore.RED)]
                for threshold, color in thresholds:
                    if wf_row < threshold:
                        return color
                return Fore.MAGENTA

            def process_row(row):
                global copy_to_clipboard, retry_flag

                if "WF" in df.columns:
                    if row["WF"] != "%":
                        wf_row = "{:.2f}".format(row["WF"])
                        wf_color = get_wf_color(float(wf_row))
                        LAP_match_lst_dic["WF"].append(f'{wf_color}{wf_row}')
                        text_row = f'{wf_color}{wf_row}{Style.RESET_ALL} - '
                    else:
                        LAP_match_lst_dic["WF"].append(row["WF"])
                else:
                    text_row = ""

                text_color = Fore.GREEN if color_cnt%2 != 0 else ""

                if row["English"] != "%":
                    LAP_match_lst_dic["English"].append(row["English"])
                    text_row += f'{text_color}{row["English"]}{Style.RESET_ALL}'
                else:
                    LAP_match_lst_dic["English"].append(f'{Fore.BLUE}NULL')
                    text_row += f'{Fore.BLUE}NULL{Style.RESET_ALL}'

                for lang_code, full_lang in lang_code_dic.items():
                    if full_lang in df.columns and full_lang != "English":
                        LAP_match_lst_dic[full_lang].append(row[full_lang])
                        if (lang_code == lang or target_column == full_lang) and row[full_lang] != "%":
                            text_row += f' - {text_color}{row[full_lang]}{Style.RESET_ALL}'

                for column in ["Shortcut(s)", "Multiword(s)"]:
                    if column in df.columns:
                        LAP_match_lst_dic[column].append(row[column])
                        if row[column] != "-":
                            text_row += f' - {text_color}{row[column]}{Style.RESET_ALL}'

                retry_flag = True
                print(text_row)

                if copy_to_clipboard:
                    for column in ["Shortcut(s)", "Multiword(s)"]:
                        if column in df.columns and row[column] != "-":
                            pyperclip.copy(row[column].split(" & ")[0].lower())
                            copy_to_clipboard = False
                            break
                    if copy_to_clipboard:
                        for lang_code, full_lang in lang_code_dic.items():
                            if lang_code == lang and full_lang in df.columns and row[full_lang] != "%":
                                pyperclip.copy(row[full_lang].lower())
                                copy_to_clipboard = False
                                break
                        if copy_to_clipboard and row["English"] != "%":
                            pyperclip.copy(row["English"].lower())
                            copy_to_clipboard = False

            for _, row in matching_rows.iterrows():
                for word_chars_lang in word_chars_lst_dic:
                    if target_column in {i for i in word_chars_lst_dic} and target_column != "English" and row[target_column] != "%":
                        word_chars_lst_dic[target_column].append(len(str(row[target_column])))
                        break
                    if word_chars_lang == lang_code_dic[lang] and word_chars_lang in df.columns and word_chars_lang != "English" and row[word_chars_lang] != "%":
                        word_chars_lst_dic[word_chars_lang].append(len(str(row[word_chars_lang])))
                        break
                word_chars_lst_dic["English"].append(len(str(row["English"]))) if row["English"] != "%" else ""

            for word_chars_lang in word_chars_lst_dic:
                word_chars_lst_dic[word_chars_lang] = sorted(set(word_chars_lst_dic[word_chars_lang]))

            for lang_code, full_lang in lang_code_dic.items():
                if target_column in {i for i in word_chars_lst_dic} and len(word_chars_lst_dic[target_column]) == 1:
                    print(f'{Fore.CYAN}{output_message(f"output_{target_column_code}_word_chars", lang, moe, word_chars_lst_dic[target_column][0])}{Style.RESET_ALL}')
                    output_word_chars_flag = True
                    break
                if lang_code == lang and len(word_chars_lst_dic[full_lang]) == 1:
                    print(f'{Fore.CYAN}{output_message(f"output_{lang_code}_word_chars", lang, moe, word_chars_lst_dic[full_lang][0])}{Style.RESET_ALL}')
                    output_word_chars_flag = True
                    break
            print(f'{Fore.CYAN}{output_message("output_en_word_chars", lang, moe, word_chars_lst_dic["English"][0])}{Style.RESET_ALL}') if not output_word_chars_flag and len(word_chars_lst_dic["English"]) == 1 else ""

            for _, row in matching_rows.iterrows():
                process_row(row)
                color_cnt += 1
            print(f'{Fore.YELLOW}{"-" * 30}{Style.RESET_ALL}')

        else:
            if lang_switch:
                print(f'{Fore.MAGENTA}{output_message("language_switched", lang, moe)}{Style.RESET_ALL}')
            else:
                print(f'{Fore.YELLOW}{output_message("match_failed", lang, moe)}{Style.RESET_ALL}')

def LAP_main():
    global LAP_match_lst_dic
    global retry_flag, cooldown_time_flag, SAS_flag
    global current_cooldown_time

    LAP_match_lst_dic = {
        "WF": [],
        "English": [],
        "简体中文": [],
        "繁體中文": [],
        "日本語": [],
        "Shortcut(s)": [],
        "Multiword(s)": []
    }
    player_guess_lst = []
    current_player_guess_lst = []
    del_elem_lst = []
    current_game_round = current_builder_name = current_theme_chars = current_player_guess = current_correct_theme = ""
    retry_flag = builder_left_flag = builder_AFK_flag = builder_unplaced_flag = correct_guess_flag = game_over_flag = False
    cooldown_time_flag = SAS_flag = False
    current_cooldown_time = 0.0
    LAP_guess_cnt = 0

    try:
        while True:
            if not os.path.exists(LOG_FILE):
                print(f'{Fore.YELLOW}{output_message("error_log_file_not_found", lang, moe)}{Style.RESET_ALL}')
                break
            else:
                with open(LOG_FILE, "r", encoding = "GB18030") as latest_log:
                    log_last_lines = deque(latest_log, maxlen = 2)
                    log_prev_line = log_last_lines[0]
                    log_last_line = log_last_lines[1]

                    COMMON_FORMAT_PREFIX = r'\[\d{2}:\d{2}:\d{2}\] \[Render thread/INFO\]: \[System\] \[CHAT\] '

                    search_game_round = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:Round: |回合：|ラウンド：)(.*)/(.*)',
                        log_last_line
                    )
                    search_builder_name = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:Builder: |建筑师：|建築師：|建築家：)(.*)',
                        log_last_line
                    )
                    search_builder_left = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The owner left|The plot owner has left the game|该领地的主人离开了|領地主人已離線|領地的主人離開遊戲了|所有者が退出しました|プロットの所有者がゲームから退出しました)',
                        log_last_line
                    )
                    search_builder_AFK = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The plot owner is AFK|该领地的主人暂时离开了|領地的主人在掛網|プロットの所有者が無操作状態です)',
                        log_last_line
                    )
                    search_builder_unplaced = re.search(
                        rf"{COMMON_FORMAT_PREFIX}(?:The plot owner hasn't placed any blocks|该领地的主人尚未放置任何方块|領地的主人沒有放置任何方塊|プロットの所有者がブロックを設置していません)",
                        log_last_line
                    )
                    search_theme_chars = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The theme is |该主题字数为|主題為 |テーマの文字数は )(.*)(?: characters long|个字| 個字| です)',
                        log_last_line
                    )
                    search_player_guess = re.search(
                        rf'{COMMON_FORMAT_PREFIX}.*?(?:Rookie|Untrained|Amateur|Apprentice|Experienced|Seasoned|Trained|Skilled|Talented|Professional|Expert|Master|#10 Builder|#[1-9] Builder|初来乍到|未经雕琢|初窥门径|学有所成|驾轻就熟|历练老成|技艺精湛|炉火纯青|技惊四座|巧夺天工|闻名于世|建筑大师|#10建筑师|#[1-9]建筑师|初來乍到|技藝生疏|初窺門徑|學徒|駕輕就熟|識途老馬|技藝精湛|爐火純青|技驚四座|巧奪天工|聞名於世|大師|#10 建築師|#[2-9] 建築師|冠絕當世|新人|一般人|アマチュア|見習|経験者|熟達者|ベテラン|熟練者|人材|職業人|専門家|マスター|#10 建築家|#[1-9] 建築家).*?: (.*)',
                        log_last_line
                    )
                    search_correct_guess = re.search(
                        rf'{COMMON_FORMAT_PREFIX}\+.*?\((?:Correct Guess|正确的猜测|正確的猜測|正確な推測)\)',
                        log_prev_line
                    )
                    search_correct_theme = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The theme was: |主题是：|主題是：|お題は：)(.*)(?:!|！)',
                        log_last_line
                    )
                    search_game_over = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:Want to play again|想再来一局吗|想再玩一次嗎|もう一度プレイしますか)',
                        log_last_line
                    )
                    search_cooldown_time = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:You must wait [1-3] seconds? in between guesses|你必须等待[1-3]秒才能再次猜测|你必須等待 [1-3] 秒後才能再次猜題|推測の間は [1-3] 秒間開ける必要があります)',
                        log_last_line
                    )

                    if search_game_round:
                        game_round = search_game_round.group(1)
                        total_round = search_game_round.group(2)
                        if current_game_round != game_round:
                            current_game_round = game_round
                            LAP_match_lst_dic = {
                                "WF": [],
                                "English": [],
                                "简体中文": [],
                                "繁體中文": [],
                                "日本語": [],
                                "Shortcut(s)": [],
                                "Multiword(s)": []
                            }
                            player_guess_lst = []
                            current_player_guess_lst = []
                            del_elem_lst = []
                            retry_flag = builder_left_flag = builder_AFK_flag = builder_unplaced_flag = correct_guess_flag = game_over_flag = False
                            SAS_flag = False
                            LAP_guess_cnt = 0 if game_round == 1 else LAP_guess_cnt
                            print(f'\r\x1b[K{Fore.CYAN}{output_message("output_LAP_game_round", lang, moe = False)}{Fore.YELLOW}{game_round}{Fore.CYAN}/{Fore.YELLOW}{total_round}{Style.RESET_ALL}')
                            print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_builder_name:
                        builder_name = search_builder_name.group(1)
                        if current_builder_name != builder_name:
                            current_builder_name = builder_name
                            print(f'\r\x1b[K{Fore.CYAN}{output_message("output_LAP_builder_name", lang, moe = False)}{Fore.YELLOW}{builder_name}{Style.RESET_ALL}')
                            print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_builder_left and not builder_left_flag:
                        builder_left_flag = True
                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_builder_left", lang, moe)}{Style.RESET_ALL}')
                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_builder_AFK and not builder_AFK_flag:
                        builder_AFK_flag = True
                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_builder_AFK", lang, moe)}{Style.RESET_ALL}')
                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_builder_unplaced and not builder_unplaced_flag:
                        builder_unplaced_flag = True
                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_builder_unplaced", lang, moe)}{Style.RESET_ALL}')
                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_theme_chars:
                        theme_chars = search_theme_chars.group(1)
                        if current_theme_chars != theme_chars:
                            current_theme_chars = theme_chars
                            print(f'\r\x1b[K{Fore.CYAN}{output_message("output_LAP_theme_chars", lang, moe, theme_chars = theme_chars)}{Style.RESET_ALL}')
                            print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_player_guess and not correct_guess_flag:
                        player_guess = search_player_guess.group(1).replace(" ", "").lower()
                        if current_player_guess != player_guess or retry_flag:
                            current_player_guess = player_guess
                            player_guess_lst.append(player_guess)
                            player_guess_lst = sorted(set(player_guess_lst))

                            if current_player_guess_lst != player_guess_lst or retry_flag:
                                current_player_guess_lst = player_guess_lst.copy()
                                indices_to_remove = []
                                retry_flag = elem_matched = False
                                elem_color_cnt = 0

                                for player_answer in current_player_guess_lst:
                                    for key, value in LAP_match_lst_dic.items():
                                        if key != "WF":
                                            normalized_value = [elem.split(" & ")[0].replace(" ", "").lower() for elem in value]
                                            if player_answer in normalized_value:
                                                index = normalized_value.index(player_answer)
                                                if index not in indices_to_remove:
                                                    indices_to_remove.append(index)

                                if indices_to_remove:
                                    for index in sorted(indices_to_remove, reverse = True):
                                        for key in LAP_match_lst_dic.keys():
                                            if index < len(LAP_match_lst_dic[key]):
                                                for lang_code, full_lang in lang_code_dic.items():
                                                    if lang_code == lang and key == full_lang and full_lang in df.columns:
                                                        del_elem_lst.append(LAP_match_lst_dic[full_lang][index])
                                                        del_elem_lst_seen = set()
                                                        del_elem_lst_dedup = []
                                                        for i in del_elem_lst:
                                                            if i not in del_elem_lst_seen:
                                                                del_elem_lst_seen.add(i)
                                                                del_elem_lst_dedup.append(i)
                                                        del_elem_lst = del_elem_lst_dedup
                                                        break
                                                del LAP_match_lst_dic[key][index]

                                    separator_dic = {
                                        "zh": "、",
                                        "cht": "、",
                                        "jp": "・",
                                        "en": ", "
                                    }
                                    output_del_elem = separator_dic.get(lang, ", ").join(del_elem_lst)
                                    print(f'\r\x1b[K{Fore.RED}{output_message("output_LAP_guess_info", lang, moe, output_del_elem = output_del_elem)}{Style.RESET_ALL}')
                                    print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "") if not LAP_match_lst_dic["English"] else ""

                                    for i in range(len(LAP_match_lst_dic["English"])):
                                        elem_color = Fore.GREEN if elem_color_cnt%2 != 0 else ""

                                        for lang_code, full_lang in lang_code_dic.items():
                                            if lang_code == lang and full_lang != "English":
                                                elements_row = ' - '.join(
                                                    f'{elem_color}{LAP_match_lst_dic[key][i]}{Style.RESET_ALL}'
                                                    for key in ["WF", "English", full_lang, "Shortcut(s)", "Multiword(s)"]
                                                    if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}
                                                )
                                                if AUTO_COPY and i == 0:
                                                    for key in ["Shortcut(s)", "Multiword(s)", full_lang, "English"]:
                                                        if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}:
                                                            pyperclip.copy(LAP_match_lst_dic[key][i].split(" & ")[0].lower())
                                                            break
                                                elem_matched = True
                                                break
                                        if not elem_matched:
                                            elements_row = ' - '.join(
                                                f'{elem_color}{LAP_match_lst_dic[key][i]}{Style.RESET_ALL}'
                                                for key in ["WF", "English", "Shortcut(s)", "Multiword(s)"]
                                                if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}
                                            )
                                            if AUTO_COPY and i == 0:
                                                for key in ["Shortcut(s)", "Multiword(s)", "English"]:
                                                    if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}:
                                                        pyperclip.copy(LAP_match_lst_dic[key][i].split(" & ")[0].lower())
                                                        break

                                        elem_color_cnt += 1
                                        print(elements_row)

                                    if LAP_match_lst_dic["English"]:
                                        SAS_flag = True
                                        LAP_guess_cnt += 1
                                        print(f'{Fore.YELLOW}{"-" * 30}{Style.RESET_ALL}')
                                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_correct_guess and not correct_guess_flag:
                        correct_guess_flag = True
                        SAS_flag = False
                        print(f'\r\x1b[K{Fore.GREEN}{output_message("output_LAP_correct_guess", lang, moe)}{Style.RESET_ALL}')
                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_correct_theme:
                        correct_theme = search_correct_theme.group(1)
                        if current_correct_theme != correct_theme:
                            current_correct_theme = correct_theme
                            correct_guess_flag = True
                            SAS_flag = False

                            print(f'\r\x1b[K{Fore.CYAN}{output_message("output_LAP_correct_theme", lang, moe, correct_theme = correct_theme)}{Style.RESET_ALL}')
                            if TAR_MODE:
                                try:
                                    if not os.path.exists(GTB_TAR_FILE):
                                        with open(GTB_TAR_FILE, "w", encoding = "GB18030") as TAR_file:
                                            TAR_file.write(f'{correct_theme}\n')
                                    else:
                                        with open(GTB_TAR_FILE, "a", encoding = "GB18030") as TAR_file:
                                            TAR_file.write(f'{correct_theme}\n')
                                    print(f'{Fore.GREEN}{output_message("output_TAR_theme_added", lang, moe, correct_theme = correct_theme)}{Style.RESET_ALL}')
                                except UnicodeDecodeError:
                                    print(f'{Fore.YELLOW}{output_message("error_TAR_file_decoding_failed", lang, moe)}{Style.RESET_ALL}')
                            print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_game_over and not game_over_flag:
                        game_over_flag = True

                        pyperclip.copy(CUSTOM_CONTENT)
                        SAS_flag = True

                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_game_over", lang, moe, LAP_guess_cnt = LAP_guess_cnt)}{Style.RESET_ALL}')
                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

                    if search_cooldown_time and not cooldown_time_flag:
                        cooldown_time_flag = True
                        current_cooldown_time = time.time()

                    if SAS_MODE and AUTO_COPY and SAS_flag:
                        SAS_main()

                time.sleep(LAP_INTERVAL)

    except UnicodeDecodeError:
        print(f'{Fore.YELLOW}{output_message("error_log_decoding_failed", lang, moe)}{Style.RESET_ALL}')

def SAS_main():
    global cooldown_time_flag, SAS_flag
    global current_cooldown_time

    MC_windows = pyautogui.getWindowsWithTitle(WINDOW_TITLE)

    if MC_windows:
        current_SAS_time = time.time()
        current_cooldown_time = current_SAS_time - 3 if not current_cooldown_time else current_cooldown_time
        SAS_sleep_time = current_SAS_time - current_cooldown_time

        if cooldown_time_flag and SAS_sleep_time < 3:
            time.sleep(3 - SAS_sleep_time)

        cooldown_time_flag = SAS_flag = False
        time.sleep(SAS_INTERVAL)

        MC_windows[0].activate()
        pyautogui.press("t")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

        print(f'\r\x1b[K{Fore.GREEN}{output_message("output_SAS_content_sent", lang, moe)}{Style.RESET_ALL}')
        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

    else:
        cooldown_time_flag = SAS_flag = False
        print(f'\r\x1b[K{Fore.YELLOW}{output_message("error_SAS_window_not_found", lang, moe)}{Style.RESET_ALL}')
        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end = "")

def solver():
    global moe

    moe = MOE_MODE

    try:
        output_language()
        input_thesaurus()

        if LAP_MODE:
            LAP_thread = threading.Thread(target = LAP_main)
            LAP_thread.daemon = True
            LAP_thread.start()

        if TAR_MODE:
            if not LAP_MODE:
                print(f'{Fore.YELLOW}{output_message("error_TAR_disabled_LAP", lang, moe)}{Style.RESET_ALL}')

        if SAS_MODE:
            if not AUTO_COPY:
                print(f'{Fore.YELLOW}{output_message("error_SAS_disabled_autocopy", lang, moe)}{Style.RESET_ALL}')
            if not LAP_MODE:
                print(f'{Fore.YELLOW}{output_message("error_SAS_disabled_LAP", lang, moe)}{Style.RESET_ALL}')

        time.sleep(0.2)
        input_matching()

    except KeyboardInterrupt:
        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("exit_program", lang, moe)}{Style.RESET_ALL}')
        exit()

    except Exception as e:
        print(f'\r\x1b[K{Fore.YELLOW}{output_message("error_exception", lang, moe, e = e)}{Style.RESET_ALL}')
        exit()

if __name__ == "__main__":
    colorama.init(autoreset = True)
    solver()
    colorama.deinit()