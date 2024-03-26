"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on English or Simplified Chinese hints and regular expressions.
Version: 3.6
Author: IceNight
GitHub: https://github.com/IceNightKing
"""

# ------------------------- Configuration Modification -------------------------
# Modify the path of the thesaurus file or replace the thesaurus file
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
# Modify the program output language: 简体中文(zh), 繁體中文(cht), 日本語(jp), English(en)
Multi_Lang = ""
# Modify the output moe status
Moe_Mode = False
# Modify the automatic copying status
Auto_Copy = False
# ------------------------------------------------------------------------------

import colorama
from colorama import Fore, Style
import locale
import pandas as pd
import re
import pyperclip

def output_language():
    global lang

    if Multi_Lang:
        lang = Multi_Lang.lower()
    else:
        system_lang, _ = locale.getlocale()

        if any(system_lang_part in system_lang.lower() for system_lang_part in {"zh", "chinese"}):
            lang = "cht" if any(system_lang_part in system_lang.lower() for system_lang_part in {"cht", "traditional", "hk", "hong kong", "mo", "macao", "tw", "taiwan"}) else "zh"
        elif any(system_lang_part in system_lang.lower() for system_lang_part in {"ja", "jp", "japanese"}):
            lang = "jp"
        elif any(system_lang_part in system_lang.lower() for system_lang_part in {"en", "english"}):
            lang = "en"
        else:
            print(f'{Fore.YELLOW}{output_message("unsupported_language", system_lang.split("_")[0], Moe_Mode)}{Style.RESET_ALL}')
            lang = "en"

    if lang not in {"zh", "cht", "jp", "en"}:
        print(f'{Fore.YELLOW}{output_message("unsupported_language", lang, Moe_Mode)}{Style.RESET_ALL}')
        lang = "en"

def output_message(key, lang, Moe_Mode = False, word_count = ""):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
        },
        "program_information": {
            "zh": "欢迎使用建筑猜猜宝 v3.6 ",
            "cht": "歡迎使用建築猜猜寶 v3.6 ",
            "jp": "GTB-Solver v3.6 へようこそ",
            "en": "Welcome to GTB-Solver v3.6"
        },
        "program_note": {
            "zh": "温馨提示: 本程序默认重复运行, 输入 0 或按下 Ctrl+C 以退出程序",
            "cht": "溫馨提示: 本程式預設重複運行, 輸入 0 或按下 Ctrl+C 以退出程式",
            "jp": "注: GTB-Solver はデフォルトで繰り返し実行されます。「0」を入力するか、「Ctrl+C」を押してプログラムを終了します",
            "en": "Note: GTB-Solver runs repeatedly by default, enter 0 or press Ctrl+C to exit the program"
        },
        "thesaurus_self_check_starts": {
            "zh": "词库状态自检",
            "cht": "詞庫狀態自檢",
            "jp": "シソーラスセルフチェック開始",
            "en": "Thesaurus Self-check"
        },
        "thesaurus_self_check_completed": {
            "zh": "词库自检完成",
            "cht": "詞庫自檢完成",
            "jp": "シソーラスセルフチェック完了",
            "en": "Self-check Completed"
        },
        "error_thesaurus_file_not_found": {
            "zh": "错误: 未找到词库文件, 请检查文件路径是否配置正确",
            "cht": "錯誤: 未找到詞庫檔案, 請檢查檔案路徑是否配置正確",
            "jp": "エラー: シソーラス・ファイルが見つかりません、ファイルのパスが正しく設定されているか確認してください",
            "en": "Error: Thesaurus file not found, please check if the file path is configured correctly"
        },
        "error_thesaurus_column_not_found": {
            "zh": "错误: 未找到 English 列, 请检查词库列名是否配置正确",
            "cht": "錯誤: 未找到 English 欄, 請檢查詞庫欄名是否配置正確",
            "jp": "エラー: 「English」カラムが見つかりません、シソーラス・カラム名が正しく設定されているか確認してください",
            "en": 'Error: "English" column not found, please check if the the thesaurus column name is configured correctly'
        },
        "error_exception": {
            "zh": "错误: ",
            "cht": "錯誤: ",
            "jp": "エラー: ",
            "en": "Error: "
        },
        "input_prompt": {
            "zh": "请输入匹配式: ",
            "cht": "請輸入匹配式: ",
            "jp": "マッチする式を入力してください: ",
            "en": "Please enter the matching expression: "
        },
        "exit_program": {
            "zh": "您已退出程序",
            "cht": "您已退出程式",
            "jp": "プログラムを終了しました",
            "en": "You have exited the program"
        },
        "output_en_word_count": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_count}{Fore.CYAN} 个字母',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_count}{Fore.CYAN} 個字母',
            "jp": f'テーマの英語文字数は {Fore.YELLOW}{word_count}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_count}{Fore.CYAN} characters long in English'
        },
        "output_zh_word_count": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_count}{Fore.CYAN} 个字',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_count}{Fore.CYAN} 個字',
            "jp": f'テーマの簡体字中国語文字数は {Fore.YELLOW}{word_count}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_count}{Fore.CYAN} character(s) long in Simplified Chinese'
        },
        "language_switched": {
            "zh": "已将语言设置为简体中文",
            "cht": "已將語言設定為繁體中文",
            "jp": "言語を日本語に設定しました",
            "en": "You set your language to English"
        },
        "match_failed": {
            "zh": "匹配失败, 未在当前词库中找到匹配条目",
            "cht": "匹配失敗, 未在當前詞庫中找到匹配條目",
            "jp": "マッチに失敗しました、現在のシソーラスに一致するものが見つかりませんでした",
            "en": "Match failed, no matching entry found in the current thesaurus"
        }
    }

    moe_suffix = {
        "zh": "喵~",
        "cht": "喵~",
        "jp": "ニャー~",
        "en": " meow~"
    }

    if key == "input_prompt" and Moe_Mode:
        input_prompt_moe = {
            "zh": "请输入奇妙咒语: ",
            "cht": "請輸入奇妙咒語: ",
            "jp": "魔法の呪文を入力してください: ",
            "en": "Please enter the marvelous spell: "
        }
        return input_prompt_moe.get(lang, input_prompt_moe["en"])

    message = messages.get(key, {}).get(lang, messages["unsupported_language"]["en"])
    message += f'{moe_suffix.get(lang, moe_suffix["en"])}' if Moe_Mode else ""
    return message

def pattern_from_input(user_input):
    target_column = None
    pattern = ""
    num = ""
    banned_chars = r'()'

    column_prefix_dic = {
        "@en": "English",
        "@zh": "简体中文",
        "@sc": "Shortcut(s)",
        "@mw": "Multiword(s)"
    }

    for prefix, column in column_prefix_dic.items():
        if user_input.startswith(prefix) and column in df.columns:
            user_input = user_input[3:]
            user_input = r'[a-zA-Z]' if prefix in {"@sc", "@mw"} and user_input in {"1", ".", "_"} else user_input
            target_column = column
            break

    for char in user_input:
        if char.isdigit():
            num += char
        else:
            if num:
                pattern += rf'[a-zA-Z\u4e00-\u9fa5-.]{{{num}}}'
                num = ""
            pattern += re.escape(char) if char in banned_chars else ("." if char == "_" else char)
    pattern += rf'[a-zA-Z\u4e00-\u9fa5-.]{{{num}}}' if num else ""
    return pattern, target_column

def input_thesaurus():
    global df

    try:
        df = pd.read_excel(GTB_Thesaurus)
    except FileNotFoundError:
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_file_not_found", lang, Moe_Mode)}{Style.RESET_ALL}')
        exit()

    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_starts", lang, Moe_Mode)} {"-" * 10}{Style.RESET_ALL}')
    for column in ["English", "简体中文", "Shortcut(s)", "Multiword(s)"]:
        print(f'{Fore.CYAN}{column} \t\t\t{Fore.GREEN}●{Style.RESET_ALL}') if column in df.columns else print(f'{Fore.CYAN}{column} \t\t\t{Fore.RED}●{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_completed", lang, Moe_Mode)} {"-" * 10}{Style.RESET_ALL}')

    if "English" not in df.columns:
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, Moe_Mode)}{Style.RESET_ALL}')
        exit()

def input_matching():
    global lang, lang_switch, copy_to_clipboard

    while True:
        user_input = input(f'{Fore.RED}{output_message("input_prompt", lang, Moe_Mode)}{Style.RESET_ALL}').lower()
        input_pattern, target_column = pattern_from_input(user_input)

        if user_input == "0":
            print(f'{Fore.MAGENTA}{output_message("exit_program", lang, Moe_Mode)}{Style.RESET_ALL}')
            break
        elif user_input.startswith("/lang "):
            new_lang = user_input.split()[1]
            if new_lang in {"zh", "cht", "jp", "en"}:
                lang = new_lang
                lang_switch = True

        try:
            matching_rows = df[df[target_column].str.lower().str.contains(f'^{input_pattern}$', na = False)] if target_column else (df[df[["English", "简体中文"]].apply(lambda x: x.str.lower().str.contains(f'^{input_pattern}$', na = False)).any(axis = 1)] if "简体中文" in df.columns else df[df["English"].str.lower().str.contains(f'^{input_pattern}$', na = False)])
        except (OverflowError, re.error):
            print(f'{Fore.YELLOW}{output_message("match_failed", lang, Moe_Mode)}{Style.RESET_ALL}')
            continue
        except KeyError:
            print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, Moe_Mode)}{Style.RESET_ALL}')
            exit()

        if not matching_rows.empty:
            en_word_count_list = []
            zh_word_count_list = []
            color_count = 0

            for _, row in matching_rows.iterrows():
                en_word_count_list.append(len(str(row["English"])))
                zh_word_count_list.append(len(str(row["简体中文"]))) if "简体中文" in df.columns else ""

            en_word_count_list = sorted(set(en_word_count_list))
            zh_word_count_list = sorted(set(zh_word_count_list))

            if len(en_word_count_list) == 1:
                print(f'{Fore.CYAN}{output_message("output_en_word_count", lang, Moe_Mode, en_word_count_list[0])}{Style.RESET_ALL}')
            elif len(zh_word_count_list) == 1:
                print(f'{Fore.CYAN}{output_message("output_zh_word_count", lang, Moe_Mode, zh_word_count_list[0])}{Style.RESET_ALL}')

            for _, row in matching_rows.iterrows():
                def get_text_color(color_count):
                    return Fore.GREEN if color_count%2 != 0 else ""

                text_color = get_text_color(color_count)
                text_row = f'{text_color}{row["English"]}{Style.RESET_ALL}'
                text_row += f' - {text_color}{row["简体中文"]}{Style.RESET_ALL}' if lang in {"zh", "cht"} and "简体中文" in df.columns else ""
                text_row += f' - {text_color}{row["Shortcut(s)"]}{Style.RESET_ALL}' if "Shortcut(s)" in df.columns and row["Shortcut(s)"] != "-" else ""
                text_row += f' - {text_color}{row["Multiword(s)"]}{Style.RESET_ALL}' if "Multiword(s)" in df.columns and row["Multiword(s)"] != "-" else ""
                print(text_row)
                color_count += 1

                if copy_to_clipboard:
                    if "Shortcut(s)" in df.columns and row["Shortcut(s)"] != "-":
                        pyperclip.copy(row["Shortcut(s)"].split(" & ")[0].lower())
                    elif "Multiword(s)" in df.columns and row["Multiword(s)"] != "-":
                        pyperclip.copy(row["Multiword(s)"].split(" & ")[0].lower())
                    else:
                        pyperclip.copy(row["简体中文"].lower()) if lang in {"zh", "cht"} and "简体中文" in df.columns else pyperclip.copy(row["English"].lower())
                    copy_to_clipboard = False

            copy_to_clipboard = True if Auto_Copy else False
            print(f'{Fore.YELLOW}{"-" * 30}{Style.RESET_ALL}')
        else:
            if lang_switch:
                print(f'{Fore.MAGENTA}{output_message("language_switched", lang, Moe_Mode)}{Style.RESET_ALL}')
                lang_switch = False
            else:
                print(f'{Fore.YELLOW}{output_message("match_failed", lang, Moe_Mode)}{Style.RESET_ALL}')

def solver():
    global lang_switch, copy_to_clipboard

    try:
        lang_switch = False
        copy_to_clipboard = True if Auto_Copy else False
        output_language()
        print(f'{Fore.MAGENTA}{output_message("program_information", lang, Moe_Mode)}{Style.RESET_ALL}')
        print(f'{Fore.CYAN}{output_message("program_note", lang, Moe_Mode)}{Style.RESET_ALL}')
        input_thesaurus()
        input_matching()
    except KeyboardInterrupt:
        print(f'\n{Fore.MAGENTA}{output_message("exit_program", lang, Moe_Mode)}{Style.RESET_ALL}')
        exit()
    except Exception as e:
        print(f'{Fore.YELLOW}{output_message("error_exception", lang, Moe_Mode)}{e}{Style.RESET_ALL}')
        exit()

colorama.init(autoreset = True)
solver()
colorama.deinit()