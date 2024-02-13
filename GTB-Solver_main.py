"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on English or Simplified Chinese hints and regular expressions.
Version: 3.1
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

def output_message(key, lang, Moe_Mode = False):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
        },
        "program_information": {
            "zh": "欢迎使用建筑猜猜宝 v3.1 ",
            "cht": "歡迎使用建築猜猜寶 v3.1 ",
            "jp": "GTB-Solver v3.1 へようこそ",
            "en": "Welcome to GTB-Solver v3.1"
        },
        "program_note": {
            "zh": "温馨提示: 本程序默认重复运行, 输入 0 以退出程序",
            "cht": "溫馨提示: 本程式默認重複運行, 輸入 0 以退出程式",
            "jp": "注: このプログラムはデフォルトで繰り返し実行されます、プログラムを終了するには「0」を入力します",
            "en": "Note: GTB-Solver runs repeatedly by default, enter 0 to exit the program"
        },
        "error_thesaurus_file_not_found": {
            "zh": "错误: 未找到词库文件, 请检查文件路径是否配置正确",
            "cht": "錯誤: 未找到詞庫檔案, 請檢查檔案路徑是否配寘正確",
            "jp": "エラー: シソーラス・ファイルが見つかりません、ファイルのパスが正しく設定されているか確認してください",
            "en": "Error: Thesaurus file not found, please check if the file path is configured correctly"
        },
        "error_thesaurus_column_not_found": {
            "zh": "错误: 未找到 English 列, 请检查词库列名是否配置正确",
            "cht": "錯誤: 未找到 English 欄, 請檢查詞庫欄名是否配置正確",
            "jp": "エラー: 「English」カラムが見つかりません、シソーラス・カラム名が正しく設定されているか確認してください",
            "en": 'Error: "English" column not found, please check if the the thesaurus column name is configured correctly'
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
        "match_failed": {
            "zh": "匹配失败, 未在当前词库中找到匹配条目",
            "cht": "匹配失敗, 未在當前詞庫中找到匹配條目",
            "jp": "マッチに失敗しました、現在のシソーラスに一致するものが見つかりませんでした",
            "en": "Match failed, no matching entry found in the current thesaurus"
        },
    }
    moe_suffixes = {
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
    message += f'{moe_suffixes.get(lang, moe_suffixes["en"])}' if Moe_Mode else ""
    return message

colorama.init(autoreset = True)
copy_to_clipboard = True if Auto_Copy else False

if Multi_Lang:
    lang = Multi_Lang.lower()
else:
    def get_system_language():
        system_lang, _ = locale.getlocale()
        return system_lang
    system_lang = get_system_language()

    if any(system_lang_part in system_lang.lower() for system_lang_part in {"zh", "chinese"}):
        lang = "cht" if any(system_lang_part in system_lang.lower() for system_lang_part in {"cht", "traditional", "hk", "hong kong", "mo", "macao", "tw", "taiwan"}) else "zh"
    elif any(system_lang_part in system_lang.lower() for system_lang_part in {"ja", "jp", "japanese"}):
        lang = "jp"
    elif any(system_lang_part in system_lang.lower() for system_lang_part in {"en", "english"}):
        lang = "en"
    else:
        print(Fore.YELLOW + output_message("unsupported_language", system_lang.split("_")[0], Moe_Mode) + Style.RESET_ALL)
        lang = "en"

if lang not in {"zh", "cht", "jp", "en"}:
    print(Fore.YELLOW + output_message("unsupported_language", lang, Moe_Mode) + Style.RESET_ALL)
    lang = "en"
print(Fore.MAGENTA + output_message("program_information", lang, Moe_Mode) + Style.RESET_ALL)
print(Fore.CYAN + output_message("program_note", lang, Moe_Mode) + Style.RESET_ALL)

try:
    df = pd.read_excel(GTB_Thesaurus)
except FileNotFoundError:
    print(Fore.YELLOW + output_message("error_thesaurus_file_not_found", lang, Moe_Mode) + Style.RESET_ALL)
    exit()

def pattern_from_input(user_input):
    pattern = ""
    num = ""
    special_chars = r"^$*-+=:?!|()[]{}"
    bracket_chars = r"()[]{}"
    rep_chars = r"*+?"
    prev_char = ""
    if user_input and user_input[0] in special_chars:
        pattern += re.escape(user_input[0])
        user_input = user_input[1:]
    for char in user_input:
        if char.isdigit():
            num += char
        else:
            if num:
                pattern += r"[a-zA-Z\u4e00-\u9fa5-]{" + num + r"}"
                num = ""
            pattern += re.escape(char) if char in bracket_chars or (char in rep_chars and prev_char in rep_chars and prev_char) else char
            prev_char = char
    pattern += r"[a-zA-Z\u4e00-\u9fa5-]{" + num + r"}" if num else ""
    return pattern

while True:
    user_input = input(Fore.RED + output_message("input_prompt", lang, Moe_Mode) + Style.RESET_ALL).lower()
    if user_input == "0":
        print(Fore.MAGENTA + output_message("exit_program", lang, Moe_Mode) + Style.RESET_ALL)
        break

    input_pattern = pattern_from_input(user_input)
    try:
        matching_rows = df[df[["English", "简体中文"]].apply(lambda x: x.str.lower().str.contains("^" + input_pattern + "$")).any(axis = 1)] if "简体中文" in df.columns else df[df["English"].str.lower().str.contains("^" + input_pattern + "$")]
    except OverflowError:
        print(Fore.YELLOW + output_message("match_failed", lang, Moe_Mode) + Style.RESET_ALL)
        continue
    except KeyError:
        print(Fore.YELLOW + output_message("error_thesaurus_column_not_found", lang, Moe_Mode) + Style.RESET_ALL)
        exit()

    if not matching_rows.empty:
        color_count = 0
        for index, row in matching_rows.iterrows():
            def get_text_color(color_count):
                return Fore.GREEN if color_count%2 != 0 else ""
            text_color = get_text_color(color_count)
            text_row = f'{text_color}{row["English"]}{Style.RESET_ALL}'
            text_row += f' - {text_color}{row["简体中文"]}{Style.RESET_ALL}' if lang in {"zh", "cht"} else ""
            text_row += f' - {text_color}{row["Shortcut(s)"]}{Style.RESET_ALL}' if row["Shortcut(s)"] != "-" else ""
            text_row += f' - {text_color}{row["Multiword(s)"]}{Style.RESET_ALL}' if row["Multiword(s)"] != "-" else ""
            print(text_row)
            color_count += 1

            if copy_to_clipboard:
                if row["Shortcut(s)"] != "-":
                    pyperclip.copy(row["Shortcut(s)"].split(" & ")[0].lower())
                elif row["Multiword(s)"] != "-":
                    pyperclip.copy(row["Multiword(s)"].split(" & ")[0].lower())
                else:
                    pyperclip.copy(row["简体中文"].lower()) if lang in {"zh", "cht"} else pyperclip.copy(row["English"].lower())
                copy_to_clipboard = False

        copy_to_clipboard = True if Auto_Copy else False
        print(Fore.YELLOW + "------------------------------" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + output_message("match_failed", lang, Moe_Mode) + Style.RESET_ALL)

colorama.deinit()