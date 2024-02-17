"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on English or Simplified Chinese hints and regular expressions.
Version: 3.2-OCR
Author: IceNight
GitHub: https://github.com/IceNightKing
"""

# ------------------------- Configuration Modification -------------------------
# Modify the repeat recognition interval (sec)
Interval_Time = 3.0
# Modify the program output language: 简体中文(zh), 繁體中文(cht), 日本語(jp), English(en)
Multi_Lang = ""
# Modify the output moe status
Moe_Mode = False
# ------------------------------------------------------------------------------

import colorama
from colorama import Fore, Style
import locale
import time
import subprocess

def output_message(key, lang, Moe_Mode = False):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
        },
        "program_information": {
            "zh": "欢迎使用建筑猜猜宝 v3.2-OCR ",
            "cht": "歡迎使用建築猜猜寶 v3.2-OCR ",
            "jp": "GTB-Solver v3.2-OCR へようこそ",
            "en": "Welcome to GTB-Solver v3.2-OCR"
        },
        "program_note": {
            "zh": "温馨提示: 本程序默认重复运行, 按下 Ctrl+C 以退出程序",
            "cht": "溫馨提示: 本程式預設重複運行, 按下 Ctrl+C 以退出程式",
            "jp": "注: このプログラムはデフォルトで繰り返し実行されます、「Ctrl+C」を押してプログラムを終了します",
            "en": "Note: GTB-Solver runs repeatedly by default, press Ctrl+C to exit the program"
        },
        "error_exception": {
            "zh": "错误:",
            "cht": "錯誤:",
            "jp": "エラー:",
            "en": "Error:"
        },
    }

    moe_suffixes = {
        "zh": "喵~",
        "cht": "喵~",
        "jp": "ニャー~",
        "en": " meow~"
    }

    message = messages.get(key, {}).get(lang, messages["unsupported_language"]["en"])
    message += f'{moe_suffixes.get(lang, moe_suffixes["en"])}' if Moe_Mode else ""
    return message

colorama.init(autoreset = True)
GTB_Solver_OCR = r"GTB-Solver-OCR_main.py"

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

while True:
    try:
        subprocess.run(["python", GTB_Solver_OCR], check = True)
        time.sleep(Interval_Time)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(Fore.YELLOW + output_message("error_exception", lang, Moe_Mode) + Style.RESET_ALL, e)
        continue

colorama.deinit()