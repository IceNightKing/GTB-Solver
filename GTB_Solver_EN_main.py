# 欢迎使用 GTB_Solver_EN, 本程序由 IceNight 编写, 请在有限范围内合理使用, 作者对因滥用本程序而导致的封禁问题概不负责
# 当前版本: Demo_202402

import colorama
from colorama import Fore, Style
import locale
import pandas as pd
import re
import pyperclip

# 请在下方提供词库文件路径
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
# 本程序现已支持: 简体中文(zh)、繁體中文(cht)、日本語(jp)、English(en)
Multi_Lang = ""
# 输出萌化开关
Moe_Mode = False
# 首个匹配结果自动复制开关
Auto_Copy = False

def output_message(key, lang, Moe_Mode = False):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB_Solver_EN will output in English'
        },
        "program_note": {
            "zh": "温馨提示: 本程序默认重复运行, 输入 0 以退出程序",
            "cht": "溫馨提示: 本程式默認重複運行, 輸入 0 以退出程式",
            "jp": "注: このプログラムはデフォルトで繰り返し実行されます、プログラムを終了するには「0」を入力します",
            "en": "Note: GTB_Solver_EN runs repeatedly by default, enter 0 to exit the program"
        },
        "error_thesaurus_file_not_found": {
            "zh": "错误: 未找到词库文件, 请检查文件路径是否配置正确",
            "cht": "錯誤: 未找到詞庫檔案, 請檢查檔案路徑是否配寘正確",
            "jp": "エラー: シソーラス・ファイルが見つかりません、ファイルのパスが正しく設定されているか確認してください",
            "en": "Error: Thesaurus file not found, please check if the file path is configured correctly"
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
    lang = Multi_Lang
else:
    def get_system_language():
        system_lang, _ = locale.getdefaultlocale()
        return system_lang
    system_lang = get_system_language()

    if "zh" in system_lang.lower():
        if "cht" in system_lang.lower() or "hk" in system_lang.lower() or "mo" in system_lang.lower() or "tw" in system_lang.lower():
            lang = "cht"
        else:
            lang = "zh"
    elif "jp" in system_lang.lower():
        lang = "jp"
    elif "en" in system_lang.lower():
        lang = "en"
    else:
        print(Fore.YELLOW + output_message("unsupported_language", system_lang.split("_")[0], Moe_Mode) + Style.RESET_ALL)
        lang = "en"

if lang not in ["zh", "cht", "jp", "en"]:
    print(Fore.YELLOW + output_message("unsupported_language", lang, Moe_Mode) + Style.RESET_ALL)
    lang = "en"
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
                pattern += r"[a-zA-Z]{" + num + r"}"
                num = ""
            if char in bracket_chars or (char in rep_chars and prev_char in rep_chars and prev_char):
                pattern += re.escape(char)
            else:
                pattern += char
            prev_char = char
    if num:
        pattern += r"[a-zA-Z]{" + num + r"}"
    return pattern

while True:
    user_input = input(Fore.RED + output_message("input_prompt", lang, Moe_Mode) + Style.RESET_ALL).lower()
    if user_input == "0":
        print(Fore.MAGENTA + output_message("exit_program", lang, Moe_Mode) + Style.RESET_ALL)
        break

    input_pattern = pattern_from_input(user_input)
    try:
        matching_rows = df[df["English"].str.lower().str.contains("^" + input_pattern + "$")]
    except OverflowError:
        print(Fore.YELLOW + output_message("match_failed", lang, Moe_Mode) + Style.RESET_ALL)
        continue

    if not matching_rows.empty:
        color_count = 0
        for index, row in matching_rows.iterrows():
            def get_text_color(color_count):
                return Fore.GREEN if color_count%2 != 0 else ""
            text_color = get_text_color(color_count)

            en_text = f'{text_color}{row["English"]}{Style.RESET_ALL}'
            text_row = f"{en_text}"
            if lang == "zh" or lang == "cht":
                zh_text = f'{text_color}{row["简体中文"]}{Style.RESET_ALL}'
                text_row += f" - {zh_text}"
            if row["Shortcut(s)"] != "-":
                sc_text = f'{text_color}{row["Shortcut(s)"]}{Style.RESET_ALL}'
                text_row += f" - {sc_text}"
            if row["Multiword(s)"] != "-":
                mw_text = f'{text_color}{row["Multiword(s)"]}{Style.RESET_ALL}'
                text_row += f" - {mw_text}"
            print(text_row)
            color_count += 1

            if copy_to_clipboard:
                if row["Shortcut(s)"] != "-":
                    pyperclip.copy(row["Shortcut(s)"].split(" & ")[0].lower())
                elif row["Multiword(s)"] != "-":
                    pyperclip.copy(row["Multiword(s)"].split(" & ")[0].lower())
                else:
                    if lang == "zh" or lang == "cht":
                        pyperclip.copy(row["简体中文"].lower())
                    else:
                        pyperclip.copy(row["English"].lower())
                copy_to_clipboard = False

        copy_to_clipboard = True if Auto_Copy else False
        print(Fore.YELLOW + "------------------------------" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + output_message("match_failed", lang, Moe_Mode) + Style.RESET_ALL)

colorama.deinit()