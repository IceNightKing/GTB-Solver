# 欢迎使用 GTB_Solver_EN, 本程序由 IceNight 编写, 请在有限范围内合理使用, 作者对因滥用本程序而导致的封禁问题概不负责
# 当前版本为: Demo_202401

import colorama
from colorama import Fore, Style
import pandas as pd
import re
import pyperclip

# 请在下方提供词库文件路径
GTB_Thesaurus = r"GTB_Thesaurus_Demo.xlsx"
# 本程序现已支持: 简体中文(zh)、繁體中文(cht)、日本語(jp)、English(en)
Multi_Lang = "zh"
# 首个匹配结果自动复制开关
Auto_Copy = False

colorama.init(autoreset = True)
if Multi_Lang == "zh":
    print(Fore.CYAN + "温馨提示: 本程序默认重复运行, 输入 0 以退出程序" + Style.RESET_ALL)
elif Multi_Lang == "cht":
    print(Fore.CYAN + "溫馨提示: 本程式默認重複運行, 輸入 0 以退出程式" + Style.RESET_ALL)
elif Multi_Lang == "jp":
    print(Fore.CYAN + "注: このプログラムはデフォルトで繰り返し実行されます、プログラムを終了するには「0」を入力します" + Style.RESET_ALL)
else:
    print(Fore.CYAN + "Note: This program runs repeatedly by default, enter 0 to exit the program" + Style.RESET_ALL)

try:
    df = pd.read_excel(GTB_Thesaurus)
except FileNotFoundError:
    if Multi_Lang == "zh":
        print(Fore.YELLOW + "错误: 未找到词库文件, 请检查文件路径是否配置正确" + Style.RESET_ALL)
    elif Multi_Lang == "cht":
        print(Fore.YELLOW + "錯誤: 未找到詞庫檔案, 請檢查檔案路徑是否配寘正確" + Style.RESET_ALL)
    elif Multi_Lang == "jp":
        print(Fore.YELLOW + "エラー: シソーラスファイルが見つかりません、ファイルパスが正しく設定されているか確認してください" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Error: Thesaurus file not found, please check if the file path is configured correctly" + Style.RESET_ALL)
    exit()

if Auto_Copy:
    copy_to_clipboard = True
else:
    copy_to_clipboard = False

def pattern_from_input(user_input):
    pattern = ""
    num = ""
    for char in user_input:
        if char.isdigit():
            num += char
        else:
            if num:
                pattern += r"[a-zA-Z]{" + num + r"}"
                num = ""
            pattern += char
    if num:
        pattern += r"[a-zA-Z]{" + num + r"}"
    return pattern

while True:
    if Multi_Lang == "zh":
        user_input = input(Fore.RED + "请输入部分英语: " + Style.RESET_ALL).lower()
    elif Multi_Lang == "cht":
        user_input = input(Fore.RED + "請輸入部分英文: " + Style.RESET_ALL).lower()
    elif Multi_Lang == "jp":
        user_input = input(Fore.RED + "英語の一部を入力してください: " + Style.RESET_ALL).lower()
    else:
        user_input = input(Fore.RED + "Please enter a portion of English: " + Style.RESET_ALL).lower()

    if user_input == "0":
        if Multi_Lang == "zh":
            print(Fore.MAGENTA + "您已退出程序" + Style.RESET_ALL)
        elif Multi_Lang == "cht":
            print(Fore.MAGENTA + "您已退出程式" + Style.RESET_ALL)
        elif Multi_Lang == "jp":
            print(Fore.MAGENTA + "プログラムを終了しました" + Style.RESET_ALL)
        else:
            print(Fore.MAGENTA + "You have exited the program" + Style.RESET_ALL)
        break

    input_pattern = pattern_from_input(user_input)
    matching_rows = df[df["English"].str.lower().str.contains("^" + input_pattern + "$")]

    if not matching_rows.empty:
        color_count = 0
        for index, row in matching_rows.iterrows():
            if color_count%2 == 0:
                if row["Shortcut(s)"] == "-" and row["Multiword(s)"] == "-":
                    print(row["English"], "-", row["简体中文"])
                elif row["Shortcut(s)"] == "-":
                    print(row["English"], "-", row["简体中文"], "-", row["Multiword(s)"])
                elif row["Multiword(s)"] == "-":
                    print(row["English"], "-", row["简体中文"], "-", row["Shortcut(s)"])
                else:
                    print(row["English"], "-", row["简体中文"], "-", row["Shortcut(s)"], "-", row["Multiword(s)"])
            else:
                if row["Shortcut(s)"] == "-" and row["Multiword(s)"] == "-":
                    print(Fore.GREEN + row["English"] + Style.RESET_ALL, "-", Fore.GREEN + row["简体中文"] + Style.RESET_ALL)
                elif row["Shortcut(s)"] == "-":
                    print(Fore.GREEN + row["English"] + Style.RESET_ALL, "-", Fore.GREEN + row["简体中文"] + Style.RESET_ALL, "-", Fore.GREEN + row["Multiword(s)"] + Style.RESET_ALL)
                elif row["Multiword(s)"] == "-":
                    print(Fore.GREEN + row["English"] + Style.RESET_ALL, "-", Fore.GREEN + row["简体中文"] + Style.RESET_ALL, "-", Fore.GREEN + row["Shortcut(s)"] + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + row["English"] + Style.RESET_ALL, "-", Fore.GREEN + row["简体中文"] + Style.RESET_ALL, "-", Fore.GREEN + row["Shortcut(s)"] + Style.RESET_ALL, "-", Fore.GREEN + row["Multiword(s)"] + Style.RESET_ALL)
            color_count += 1

            if copy_to_clipboard:
                if row["Shortcut(s)"] == "-" and row["Multiword(s)"] == "-":
                    pyperclip.copy(row["简体中文"])
                elif row["Shortcut(s)"] == "-":
                    multiwords = row["Multiword(s)"].split(" & ")
                    pyperclip.copy(multiwords[0])
                else:
                    shortcuts = row["Shortcut(s)"].split(" & ")
                    pyperclip.copy(shortcuts[0])
                copy_to_clipboard = False

        if Auto_Copy:
            copy_to_clipboard = True
        print(Fore.YELLOW + "------------------------------" + Style.RESET_ALL)
    else:
        if Multi_Lang == "zh":
            print(Fore.YELLOW + "匹配失败, 未在当前词库中找到匹配条目" + Style.RESET_ALL)
        elif Multi_Lang == "cht":
            print(Fore.YELLOW + "匹配失敗, 未在當前詞庫中找到匹配條目" + Style.RESET_ALL)
        elif Multi_Lang == "jp":
            print(Fore.YELLOW + "マッチに失敗しました、現在のシソーラスに一致するものが見つかりませんでした" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Match failed, no matching entry found in the current thesaurus" + Style.RESET_ALL)

colorama.deinit()