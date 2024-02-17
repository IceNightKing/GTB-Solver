"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on English or Simplified Chinese hints and regular expressions.
Version: 3.2-OCR
Author: IceNight
GitHub: https://github.com/IceNightKing
"""

# ------------------------- Configuration Modification -------------------------
# Modify the coordinates of the upper left corner of the recognition area
Left, Top = 1000, 1200
# Modify the coordinates of the lower right corner of the recognition area
Right, Bottom = 1550, 1300
# Modify the GPU acceleration recognition status
GPU_Mode = True
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
import pyautogui
import cv2
import numpy as np
import easyocr
import re
import pyperclip

def output_message(key, lang, Moe_Mode = False):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
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
        "ocr_result_null": {
            "zh": "识别结果为空",
            "cht": "辨識結果為空",
            "jp": "認識結果は NULL である",
            "en": "The recognition result is null"
        },
        "input_prompt": {
            "zh": "光学字符识别结果:",
            "cht": "光學字元辨識結果:",
            "jp": "光学式文字認識結果:",
            "en": "Optical character recognition result:"
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
            "zh": "奇妙咒语识别结果:",
            "cht": "奇妙咒語辨識結果:",
            "jp": "魔法の呪文認識結果:",
            "en": "Marvelous spell recognition result:"
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

try:
    df = pd.read_excel(GTB_Thesaurus)
except FileNotFoundError:
    print(Fore.YELLOW + output_message("error_thesaurus_file_not_found", lang, Moe_Mode) + Style.RESET_ALL)
    exit()

screenshot = pyautogui.screenshot()
screenshot.save(r"GTB-Solver-OCR_image.jpg")
ocr_img = cv2.imread(r"GTB-Solver-OCR_image.jpg")
ocr_img = ocr_img[Top:Bottom, Left:Right]
ocr_img = cv2.cvtColor(np.array(ocr_img), cv2.COLOR_RGB2BGR)
ocr_img = cv2.cvtColor(ocr_img, cv2.COLOR_BGR2GRAY)
reader = easyocr.Reader(["en"], gpu = GPU_Mode)
results = reader.readtext(ocr_img, detail = 0)

ocr_str = ""
word_count = 0
for word in results:
    ocr_str += " " if word_count != 0 else ""
    ocr_str += word
    word_count += 1
resultlist = re.findall("(?<= is )(.*)", ocr_str)
ocr_result = resultlist[0] if resultlist else output_message("ocr_result_null", lang, Moe_Mode)
print(Fore.RED + output_message("input_prompt", lang, Moe_Mode) + Style.RESET_ALL, ocr_result)

def transform_underscore(ocr_result):
    transformed_str = re.sub(r"_+", lambda match: str(len(match.group(0))), ocr_result)
    return transformed_str
user_input = transform_underscore(ocr_result).lower()

def pattern_from_input(user_input):
    pattern = ""
    num = ""
    special_chars = r"^$*-+=:?!|()[]{}\\"
    banned_chars = r"()[]{}\\"
    rep_chars = r"*+?"
    prev_char = ""
    if user_input and user_input[0] in special_chars:
        pattern += re.escape(user_input[0])
        user_input = user_input[1:]

    if user_input.startswith("@zh"):
        user_input = user_input[3:]
        target_column = "简体中文"
    elif user_input.startswith("@en"):
        user_input = user_input[3:]
        target_column = "English"
    else:
        target_column = None

    for char in user_input:
        if char.isdigit():
            num += char
        else:
            if num:
                pattern += rf"[a-zA-Z\u4e00-\u9fa5-]{{{num}}}"
                num = ""
            pattern += re.escape(char) if char in banned_chars or (char in rep_chars and prev_char in rep_chars and prev_char) else char
            prev_char = char
    pattern += rf"[a-zA-Z\u4e00-\u9fa5-]{{{num}}}" if num else ""
    return pattern, target_column

input_pattern, target_column = pattern_from_input(user_input)
try:
    matching_rows = df[df[target_column].str.lower().str.contains(f"^{input_pattern}$")] if target_column else (df[df[["English", "简体中文"]].apply(lambda x: x.str.lower().str.contains(f"^{input_pattern}$")).any(axis = 1)] if "简体中文" in df.columns else df[df["English"].str.lower().str.contains(f"^{input_pattern}$")])
except OverflowError:
    print(Fore.YELLOW + output_message("match_failed", lang, Moe_Mode) + Style.RESET_ALL)
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

    print(Fore.YELLOW + "------------------------------" + Style.RESET_ALL)
else:
    print(Fore.YELLOW + output_message("match_failed", lang, Moe_Mode) + Style.RESET_ALL)

colorama.deinit()