"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on multi-language hints and regular expressions.
Version: 4.1
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

def output_message(key, lang, Moe_Mode = False, word_count = "", e = ""):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
        },
        "program_information": {
            "zh": "欢迎使用建筑猜猜宝 v4.1 ",
            "cht": "歡迎使用建築猜猜寶 v4.1 ",
            "jp": "GTB-Solver v4.1 へようこそ",
            "en": "Welcome to GTB-Solver v4.1"
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
            "zh": f'错误: {e} ',
            "cht": f'錯誤: {e} ',
            "jp": f'エラー: {e} ',
            "en": f'Error: {e}'
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
            "jp": f'テーマの英字数は {Fore.YELLOW}{word_count}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_count}{Fore.CYAN} characters long'
        },
        "output_zh_word_count": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_count}{Fore.CYAN} 个字',
            "cht": f'此主題簡體中文字數為 {Fore.YELLOW}{word_count}{Fore.CYAN} 個字',
            "jp": f'テーマの簡体字中国語の文字数は {Fore.YELLOW}{word_count}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_count}{Fore.CYAN} character(s) long in Simplified Chinese'
        },
        "output_cht_word_count": {
            "zh": f'该主题繁体中文字数为 {Fore.YELLOW}{word_count}{Fore.CYAN} 个字',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_count}{Fore.CYAN} 個字',
            "jp": f'テーマの繁体字中国語の文字数は {Fore.YELLOW}{word_count}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_count}{Fore.CYAN} character(s) long in Traditional Chinese'
        },
        "output_jp_word_count": {
            "zh": f'该主题日语字数为 {Fore.YELLOW}{word_count}{Fore.CYAN} 个字',
            "cht": f'此主題日文字數為 {Fore.YELLOW}{word_count}{Fore.CYAN} 個字',
            "jp": f'テーマの文字数は {Fore.YELLOW}{word_count}{Fore.CYAN} です',
            "en": f'The theme is {Fore.YELLOW}{word_count}{Fore.CYAN} character(s) long in Japanese'
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
                pattern += rf"[a-zA-Z\u4e00-\u9fff\u3040-\u30ff\uff66-\uff9f-.'《》]{{{num}}}"
                num = ""
            pattern += re.escape(char) if char in banned_chars else ("." if char == "_" else char)
    pattern += rf"[a-zA-Z\u4e00-\u9fff\u3040-\u30ff\uff66-\uff9f-.'《》]{{{num}}}" if num else ""
    return pattern, target_column

def input_thesaurus():
    global df

    try:
        df = pd.read_excel(GTB_Thesaurus, keep_default_na = False).replace("", "%")
    except FileNotFoundError:
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_file_not_found", lang, Moe_Mode)}{Style.RESET_ALL}')
        exit()

    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_starts", lang, Moe_Mode)} {"-" * 10}{Style.RESET_ALL}')
    for column in ["English", "简体中文", "繁體中文", "日本語", "Shortcut(s)", "Multiword(s)"]:
        print(f'{Fore.CYAN}{column}  \t\t\t{Fore.GREEN}●{Style.RESET_ALL}') if column in df.columns else print(f'{Fore.CYAN}{column}  \t\t\t{Fore.RED}●{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_completed", lang, Moe_Mode)} {"-" * 10}{Style.RESET_ALL}')

    if "English" not in df.columns:
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, Moe_Mode)}{Style.RESET_ALL}')
        exit()

def input_matching():
    global lang, copy_to_clipboard

    while True:
        lang_code_dic = {
            "en": "English",
            "zh": "简体中文",
            "cht": "繁體中文",
            "jp": "日本語"
        }
        lang_switch = matched_rows = False
        matching_rows = None

        user_input = input(f'{Fore.RED}{output_message("input_prompt", lang, Moe_Mode)}{Style.RESET_ALL}').lower()
        input_pattern, target_column = pattern_from_input(user_input)

        if user_input == "0":
            print(f'{Fore.MAGENTA}{output_message("exit_program", lang, Moe_Mode)}{Style.RESET_ALL}')
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
            print(f'{Fore.YELLOW}{output_message("match_failed", lang, Moe_Mode)}{Style.RESET_ALL}')
            continue
        except KeyError:
            print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, Moe_Mode)}{Style.RESET_ALL}')
            exit()

        if not matching_rows.empty:
            word_count_list = {
                "English": [],
                "简体中文": [],
                "繁體中文": [],
                "日本語": []
            }
            target_column_code = {v: k for k, v in lang_code_dic.items()}.get(target_column, None)
            output_word_count = False
            color_count = 0
            copy_to_clipboard = True if Auto_Copy else False

            def get_wf_color(wf_row):
                thresholds = [(1.00, Fore.BLUE), (4.00, Fore.WHITE), (7.00, Fore.GREEN), (10.00, Fore.YELLOW), (13.00, Fore.RED)]
                for threshold, color in thresholds:
                    if wf_row < threshold:
                        return color
                return Fore.MAGENTA

            def get_text_color(color_count):
                return Fore.GREEN if color_count%2 != 0 else ""

            def process_row(row):
                global copy_to_clipboard

                if "WF" in df.columns and row["WF"] != "%":
                    wf_row = "{:.2f}".format(row["WF"])
                    wf_color = get_wf_color(float(wf_row))
                    text_row = f'{wf_color}{wf_row}{Style.RESET_ALL} - '
                else:
                    text_row = ""

                text_color = get_text_color(color_count)
                text_row += f'{text_color}{row["English"]}{Style.RESET_ALL}' if row["English"] != "%" else f'{Fore.BLUE}NULL{Style.RESET_ALL}'

                for lang_code, full_lang in lang_code_dic.items():
                    if (lang_code == lang or target_column == full_lang) and full_lang in df.columns and full_lang != "English" and row[full_lang] != "%":
                        text_row += f' - {text_color}{row[full_lang]}{Style.RESET_ALL}'

                for column in ["Shortcut(s)", "Multiword(s)"]:
                    if column in df.columns and row[column] != "-":
                        text_row += f' - {text_color}{row[column]}{Style.RESET_ALL}'
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
                for word_count_lang in word_count_list:
                    if target_column in {i for i in word_count_list} and target_column != "English" and row[target_column] != "%":
                        word_count_list[target_column].append(len(str(row[target_column])))
                        break
                    if word_count_lang == lang_code_dic[lang] and word_count_lang in df.columns and word_count_lang != "English" and row[word_count_lang] != "%":
                        word_count_list[word_count_lang].append(len(str(row[word_count_lang])))
                        break
                word_count_list["English"].append(len(str(row["English"]))) if row["English"] != "%" else ""

            for word_count_lang in word_count_list:
                word_count_list[word_count_lang] = sorted(set(word_count_list[word_count_lang]))

            for lang_code, full_lang in lang_code_dic.items():
                if target_column in {i for i in word_count_list} and len(word_count_list[target_column]) == 1:
                    print(f'{Fore.CYAN}{output_message(f"output_{target_column_code}_word_count", lang, Moe_Mode, word_count_list[target_column][0])}{Style.RESET_ALL}')
                    output_word_count = True
                    break
                if lang_code == lang and len(word_count_list[full_lang]) == 1:
                    print(f'{Fore.CYAN}{output_message(f"output_{lang_code}_word_count", lang, Moe_Mode, word_count_list[full_lang][0])}{Style.RESET_ALL}')
                    output_word_count = True
                    break
            print(f'{Fore.CYAN}{output_message("output_en_word_count", lang, Moe_Mode, word_count_list["English"][0])}{Style.RESET_ALL}') if not output_word_count and len(word_count_list["English"]) == 1 else ""

            for _, row in matching_rows.iterrows():
                process_row(row)
                color_count += 1
            print(f'{Fore.YELLOW}{"-" * 30}{Style.RESET_ALL}')
        else:
            if lang_switch:
                print(f'{Fore.MAGENTA}{output_message("language_switched", lang, Moe_Mode)}{Style.RESET_ALL}')
            else:
                print(f'{Fore.YELLOW}{output_message("match_failed", lang, Moe_Mode)}{Style.RESET_ALL}')

def solver():
    try:
        output_language()
        print(f'{Fore.MAGENTA}{output_message("program_information", lang, Moe_Mode)}{Style.RESET_ALL}')
        print(f'{Fore.CYAN}{output_message("program_note", lang, Moe_Mode)}{Style.RESET_ALL}')
        input_thesaurus()
        input_matching()
    except KeyboardInterrupt:
        print(f'\n{Fore.MAGENTA}{output_message("exit_program", lang, Moe_Mode)}{Style.RESET_ALL}')
        exit()
    except Exception as e:
        print(f'{Fore.YELLOW}{output_message("error_exception", lang, Moe_Mode, e = e)}{Style.RESET_ALL}')
        exit()

colorama.init(autoreset = True)
solver()
colorama.deinit()