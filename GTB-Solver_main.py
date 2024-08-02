"""
GTB-Solver: Quickly guess the theme of "Guess The Build" game on Hypixel server based on multi-language hints and regular expressions.
Version: 5.0
Author: IceNight
GitHub: https://github.com/IceNightKing
"""

# ------------------------- Configuration Modification -------------------------
# Modify the path of the thesaurus file or replace the thesaurus file
GTB_THESAURUS = r"GTB_Thesaurus_Demo.xlsx"
# Modify the program output language: 简体中文(zh), 繁體中文(cht), 日本語(jp), 한국어(kor), Русский(ru), Deutsch(de), Français(fra), Español(spa), Português(pt), Italiano(it), English(en)
MULTI_LANG = ""
# Modify the output moe mode status
MOE_MODE = False
# Modify the automatic copying mode status
AUTO_COPY = False
# Modify the random copying mode status
RAC_MODE = False
# Modify the log assisted processing mode status
LAP_MODE = False
# Modify the path of the log file
LOG_FILE = r"C:\Minecraft\.minecraft\logs\latest.log"
# Modify the repeat reading interval of the log file (sec)
LAP_INTERVAL = 0.05
# Modify the custom copy content at the end of the game
CUSTOM_CONTENT = "Good Game"
# Modify the theme auxiliary recording mode status
TAR_MODE = False
# Modify the path of the theme auxiliary recording file
GTB_TAR_FILE = r"GTB_TAR_File.txt"
# Modify the semi-automatic sending mode status
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
import random

def output_language():
    global lang

    system_lang_dic = {
        "zh": {"zh", "chinese"},
        "cht": {"cht", "traditional", "hk", "hong-kong", "mo", "macao", "tw", "taiwan"},
        "jp": {"ja", "jp", "japanese"},
        "kor": {"ko", "kor", "korean"},
        "ru": {"ru", "russian"},
        "de": {"de", "german"},
        "fra": {"fr", "fra", "french"},
        "spa": {"es", "spa", "spanish"},
        "pt": {"pt", "portuguese"},
        "it": {"it", "italian"},
        "en": {"en", "english"}
    }

    if MULTI_LANG:
        lang = MULTI_LANG.lower()
    else:
        get_system_lang, _ = locale.getlocale()
        system_lang = get_system_lang.lower().replace("_", "-")

        for key, values in system_lang_dic.items():
            if any(re.search(r'\b{}\b'.format(system_lang_part), system_lang) for system_lang_part in values):
                lang = key
                break
        else:
            print(f'{Fore.YELLOW}{output_message("unsupported_language", get_system_lang.split("_")[0], moe)}{Style.RESET_ALL}')
            lang = "en"

    if lang == "zh" and any(re.search(r'\b{}\b'.format(system_lang_part), system_lang) for system_lang_part in system_lang_dic["cht"]):
        lang = "cht"

    if lang not in system_lang_dic:
        print(f'{Fore.YELLOW}{output_message("unsupported_language", lang, moe)}{Style.RESET_ALL}')
        lang = "en"

def output_message(key, lang, moe=False, word_chars=None, e=None, output_del_elem=None, correct_theme=None, LAP_guess_cnt=None):
    messages = {
        "unsupported_language": {
            "en": f'Warn: Language code "{lang}" is not yet supported, GTB-Solver will output in English'
        },
        "program_info": {
            "zh": "欢迎使用建筑猜猜宝 v5.0 ",
            "cht": "歡迎使用建築猜猜寶 v5.0 ",
            "jp": "GTB-Solver v5.0 へようこそ",
            "kor": "GTB-Solver v5.0 에 오신 것을 환영합니다",
            "ru": "Добро пожаловать в GTB-Solver v5.0",
            "de": "Willkommen bei GTB-Solver v5.0",
            "fra": "Bienvenue dans GTB-Solver v5.0",
            "spa": "Bienvenido a GTB-Solver v5.0",
            "pt": "Bem-vindo ao GTB-Solver v5.0",
            "it": "Benvenuti nel GTB Solver v5.0",
            "en": "Welcome to GTB-Solver v5.0"
        },
        "program_note": {
            "zh": "温馨提示：建筑猜猜宝默认重复运行，输入 0 或按下 Ctrl+C 以退出程序",
            "cht": "溫馨提示：建築猜猜寶預設重複運行，輸入 0 或按下 Ctrl+C 以退出程式",
            "jp": "注：GTB-Solver はデフォルトで繰り返し実行されます。「0」を入力するか、「Ctrl」+「C」を押してプログラムを終了します",
            "kor": "참고: GTB-Solver 는 기본적으로 반복적으로 실행됩니다. 0 을 입력하거나 Ctrl+C 를 눌러 프로그램을 종료합니다",
            "ru": "Примечание: GTB-Solver по умолчанию запускается повторно. Введите 0 или нажмите Ctrl+C, чтобы выйти из программы",
            "de": "Hinweis: GTB-Solver wird standardmäßig wiederholt ausgeführt. Geben Sie 0 ein oder drücken Sie Strg+C, um das Programm zu beenden",
            "fra": "Remarque: GTB-Solver s'exécute à plusieurs reprises par défaut, entrez 0 ou appuyez sur Ctrl+C pour quitter le programme",
            "spa": "Nota: GTB-Solver se ejecuta repetidamente de forma predeterminada, ingrese 0 o presione Ctrl+C para salir del programa",
            "pt": "Nota: GTB-Solver é executado repetidamente por padrão, digite 0 ou pressione Ctrl+C para sair do programa",
            "it": "Nota: GTB-Solver viene eseguito ripetutamente per impostazione predefinita, inserisci 0 o premi Ctrl+C per uscire dal programma",
            "en": "Note: GTB-Solver runs repeatedly by default, enter 0 or press Ctrl+C to exit the program"
        },
        "thesaurus_self_check_starts": {
            "zh": "词库状态自检",
            "cht": "詞庫狀態自檢",
            "jp": "シソーラス・セルフチェック開始",
            "kor": "동의어 사전 자체 점검 시작",
            "ru": "Самопроверка Тезауруса",
            "de": "Thesaurus Selbsttest Start",
            "fra": "Auto-Vérification du Thésaurus",
            "spa": "Autocomprobación del Tesauro",
            "pt": "Autoverificação do Thesaurus",
            "it": "Autocontrollo del Thesaurus",
            "en": "Thesaurus Self-Check"
        },
        "thesaurus_self_check_completed": {
            "zh": "词库自检完成",
            "cht": "詞庫自檢完成",
            "jp": "シソーラス・セルフチェック完了",
            "kor": "동의어 사전 자체 점검 완료",
            "ru": "Самопроверка Завершена",
            "de": " Selbsttest Abgeschlossen ",
            "fra": "  Auto-Vérification Terminée  ",
            "spa": " Autocomprobación Completada",
            "pt": " Autoverificação  Concluída ",
            "it": " Autocontrollo  Completato ",
            "en": "Self-Check Completed"
        },
        "program_self_check_starts": {
            "zh": "程序状态自检",
            "cht": "程式狀態自檢",
            "jp": "プログラム・セルフチェック開始",
            "kor": "프로그램 자체 점검 시작",
            "ru": "Самопроверка Программы",
            "de": "Programm Selbsttest Start",
            "fra": "Auto-Vérification du Programme",
            "spa": "Autocomprobación del Programa",
            "pt": "Autoverificação do Programa",
            "it": "Autocontrollo del Programma",
            "en": " Program Self-Check "
        },
        "program_self_check_completed": {
            "zh": "程序自检完成",
            "cht": "程式自檢完成",
            "jp": "プログラム・セルフチェック完了",
            "kor": "프로그램 자체 점검 완료",
            "ru": "Самопроверка Завершена",
            "de": " Selbsttest Abgeschlossen",
            "fra": "  Auto-Vérification Terminée  ",
            "spa": " Autocomprobación Completada ",
            "pt": " Autoverificação Concluída ",
            "it": " Autocontrollo  Completato ",
            "en": "Self-Check Completed"
        },
        "program_MOE_STD_name": {
            "zh": "输出萌化模式\t\t\t",
            "cht": "輸出萌化模式\t\t\t",
            "jp": "出力萌えモード\t\t\t\t\t",
            "kor": "출력 모에 모드\t\t\t",
            "ru": "Режим Выхода Моэ\t\t\t",
            "de": "Ausgabe Moe Modus\t\t\t\t",
            "fra": "Mode de Sortie Moe\t\t\t\t",
            "spa": "Modo de Salida Moe\t\t\t\t",
            "pt": "Modo de Saída Moe\t\t\t\t",
            "it": "Modalità di Uscita Moe\t\t\t\t",
            "en": "Output Moe Mode\t\t\t\t"
        },
        "program_AC_STD_name": {
            "zh": "自动复制模式\t\t\t",
            "cht": "自動複製模式\t\t\t",
            "jp": "自動コピーモード\t\t\t\t",
            "kor": "자동 복사 모드\t\t\t",
            "ru": "Режим Автоматического Копирования\t",
            "de": "Automatischer Kopiermodus\t\t\t",
            "fra": "Mode de Copie Automatique\t\t\t",
            "spa": "Modo de Copia Automática\t\t\t",
            "pt": "Modo de Cópia Automática\t\t\t",
            "it": "Modalità di Copia Automatica\t\t\t",
            "en": "Automatic Copying Mode\t\t\t"
        },
        "program_RAC_STD_name": {
            "zh": "随机复制模式\t\t\t",
            "cht": "隨機複製模式\t\t\t",
            "jp": "ランダムコピーモード\t\t\t\t",
            "kor": "랜덤 복사 모드\t\t\t",
            "ru": "Режим Случайного Копирования\t\t",
            "de": "Zufälliger Kopiermodus\t\t\t\t",
            "fra": "Mode de Copie Aléatoire\t\t\t\t",
            "spa": "Modo de Copia Aleatoria\t\t\t\t",
            "pt": "Modo de Cópia Aleatória\t\t\t\t",
            "it": "Modalità di Copia Casuale\t\t\t",
            "en": "Random Copying Mode\t\t\t"
        },
        "program_LAP_STD_name": {
            "zh": "日志辅助处理模式\t\t",
            "cht": "日誌輔助處理模式\t\t",
            "jp": "ログアシスト処理モード\t\t\t\t",
            "kor": "로그 지원 처리 모드\t\t",
            "ru": "Режим Вспомогательной Обработки Журнала\t",
            "de": "Protokollunterstützter Verarbeitungsmodus\t",
            "fra": "Mode de Traitement Assisté par Journal\t\t",
            "spa": "Modo de Procesamiento Asistido por Registro\t",
            "pt": "Modo de Processamento Assistido por Log\t\t",
            "it": "Modalità di Elaborazione Assistita dal Registro\t",
            "en": "Log Assisted Processing Mode\t\t"
        },
        "program_TAR_STD_name": {
            "zh": "主题辅助记录模式\t\t",
            "cht": "主題輔助記錄模式\t\t",
            "jp": "テーマ補助記録モード\t\t\t\t",
            "kor": "테마 보조녹화 모드\t\t",
            "ru": "Режим Вспомогательной Записи Темы\t",
            "de": "Thema Hilfsaufnahmemodus\t\t\t",
            "fra": "Mode d'Enregistrement Auxiliaire du Thème\t",
            "spa": "Modo de Grabación Auxiliar de Tema\t\t",
            "pt": "Modo de Gravação Auxiliar do Tema\t\t",
            "it": "Modalità di Registrazione Ausiliaria del Tema\t",
            "en": "Theme Auxiliary Recording Mode\t\t"
        },
        "program_SAS_STD_name": {
            "zh": "半自动发送模式\t\t\t",
            "cht": "半自動發送模式\t\t\t",
            "jp": "半自動送信モード\t\t\t\t",
            "kor": "반자동 전송 모드\t\t",
            "ru": "Режим Полуавтоматической Отправки\t",
            "de": "Halbautomatischer Sendemodus\t\t\t",
            "fra": "Mode d'Envoi Semi-Automatique\t\t\t",
            "spa": "Modo de Envío Semiautomático\t\t\t",
            "pt": "Modo de Envio Semiautomático\t\t\t",
            "it": "Modalità di Invio Semi-Automatico\t\t",
            "en": "Semi-Automatic Sending Mode\t\t"
        },
        "error_thesaurus_file_not_found": {
            "zh": "错误：未找到词库文件，请检查文件路径是否设置正确",
            "cht": "錯誤：未找到詞庫檔案，請檢查檔案路徑是否設定正確",
            "jp": "エラー：シソーラス・ファイルが見つかりません、ファイルのパスが正しく設定されているか確認してください",
            "kor": "오류: 동의어 사전 파일을 찾을 수 없습니다. 파일 경로가 올바르게 구성되었는지 확인하십시오",
            "ru": "Ошибка: Файл тезауруса не найден, проверьте, правильно ли настроен путь к файлу",
            "de": "Fehler: Thesaurus-Datei nicht gefunden. Bitte überprüfen Sie, ob der Dateipfad richtig konfiguriert ist",
            "fra": "Erreur: Fichier thésaurus non trouvé, veuillez vérifier si le chemin du fichier est correctement configuré",
            "spa": "Error: No se encontró el archivo de tesauro, verifique si la ruta del archivo está configurada correctamente",
            "pt": "Erro: Arquivo do thesaurus não encontrado, verifique se o caminho do arquivo está configurado corretamente",
            "it": "Errore: File del thesaurus non trovato, verificare che il percorso del file sia configurato correttamente",
            "en": "Error: Thesaurus file not found, please check if the file path is configured correctly"
        },
        "error_thesaurus_column_not_found": {
            "zh": "错误：未找到 English 列，请检查词库列名是否设置正确",
            "cht": "錯誤：未找到 English 欄，請檢查詞庫欄名是否設定正確",
            "jp": "エラー：「English」カラムが見つかりません、シソーラス・カラム名が正しく設定されているか確認してください",
            "kor": '오류: "English" 열을 찾을 수 없습니다. 동의어 사전 열 이름이 올바르게 구성되었는지 확인하십시오',
            "ru": 'Ошибка: Колонка «English» не найдена, проверьте, правильно ли настроено имя колонки тезауруса',
            "de": 'Fehler: Spalte „English“ nicht gefunden. Bitte überprüfen Sie, ob der Thesaurus-Spaltenname richtig konfiguriert ist',
            "fra": 'Erreur: Colonne «English» non trouvée, veuillez vérifier si le nom de la colonne du thésaurus est correctement configuré',
            "spa": 'Error: No se encontró la columna "English", verifique si el nombre de la columna del tesauro está configurado correctamente',
            "pt": 'Erro: Coluna "English" não encontrada, verifique se o nome da coluna do thesaurus está configurado corretamente',
            "it": 'Errore: Colonna "English" non trovata, controllare che il nome della colonna del thesaurus sia configurato correttamente',
            "en": 'Error: "English" column not found, please check if the the thesaurus column name is configured correctly'
        },
        "error_log_file_not_found": {
            "zh": "错误：未找到日志文件，日志辅助处理模式启动失败，请检查文件路径是否设置正确",
            "cht": "錯誤：未找到日誌檔案，日誌輔助處理模式啟動失敗，請檢查檔案路徑是否設定正確",
            "jp": "エラー：ログファイルが見つからなかったため、ログアシスト処理モードを開始できませんでした。ファイルのパスが正しく設定されているか確認してください",
            "kor": "오류: 로그 파일을 찾을 수 없어 로그 지원 처리 모드를 시작하지 못했습니다. 파일 경로가 올바르게 구성되었는지 확인하십시오",
            "ru": "Ошибка: Режим обработки журнала не удалось запустить, поскольку файл журнала не был найден, проверьте правильность пути к файлу",
            "de": "Fehler: Der protokollgestützte Verarbeitungsmodus konnte nicht gestartet werden, da die Protokolldatei nicht gefunden wurde. Überprüfen Sie bitte, ob der Dateipfad richtig konfiguriert ist",
            "fra": "Erreur: Le mode de traitement assisté par journal n'a pas pu démarrer car le fichier journal n'a pas été trouvé, veuillez vérifier si le chemin du fichier est correctement configuré",
            "spa": "Error: El modo de procesamiento asistido por registro no pudo iniciarse porque no se encontró el archivo de registro, verifique si la ruta del archivo está configurada correctamente",
            "pt": "Erro: O modo de processamento assistido por log falhou ao iniciar porque o arquivo de log não foi encontrado, verifique se o caminho do arquivo está configurado corretamente",
            "it": "Errore: La modalità di elaborazione assistita dal registro non è riuscita ad avviarsi perché il file di registro non è stato trovato, controllare che il percorso del file sia configurato correttamente",
            "en": "Error: The log assisted processing mode failed to start because the log file was not found, please check if the file path is configured correctly"
        },
        "error_log_decoding_failed": {
            "zh": "错误：未能成功解码日志文件，日志辅助处理模式启动失败，请删除日志文件后重新开始游戏",
            "cht": "錯誤：未能成功解碼日誌檔案，日誌輔助處理模式啟動失敗，請刪除日誌檔案後重新開始遊戲",
            "jp": "エラー：ログファイルが正常にデコードできなかったため、ログアシスト処理モードを開始できませんでした。ログファイルを削除してゲームを再起動してください",
            "kor": "오류: 로그 파일을 성공적으로 디코딩할 수 없어 로그 지원 처리 모드를 시작하지 못했습니다. 로그 파일을 삭제하고 게임을 다시 시작해주세요",
            "ru": "Ошибка: Не удалось запустить режим обработки журнала, поскольку файл журнала не удалось успешно декодировать. Пожалуйста, удалите файл журнала и перезапустите игру",
            "de": "Fehler: Der Protokoll-unterstützte Verarbeitungsmodus konnte nicht gestartet werden, da die Protokolldatei nicht erfolgreich dekodiert werden konnte. Bitte löschen Sie die Protokolldatei und starten Sie das Spiel neu",
            "fra": "Erreur: Le mode de traitement assisté par journal n'a pas pu démarrer car le fichier journal n'a pas pu être décodé correctement. Veuillez supprimer le fichier journal et redémarrer le jeu",
            "spa": "Error: El modo de procesamiento asistido por registro no se pudo iniciar porque no se pudo decodificar correctamente el archivo de registro. Borre el archivo de registro y reinicie el juego",
            "pt": "Erro: O modo de processamento assistido por log falhou ao iniciar porque o arquivo de log não pôde ser decodificado com sucesso. Exclua o arquivo de log e reinicie o jogo",
            "it": "Errore: La modalità di elaborazione assistita dal registro non è riuscita ad avviarsi perché il file di registro non è stato decodificato correttamente. Elimina il file di registro e riavvia il gioco",
            "en": "Error: The log assisted processing mode failed to start because the log file could not be decoded successfully. Please delete the log file and restart the game"
        },
        "error_TAR_file_decoding_failed": {
            "zh": "错误：未能成功解码主题辅助记录文件，主题辅助记录模式启动失败，请删除辅助记录文件后重新开始游戏",
            "cht": "錯誤：未能成功解碼主題輔助記錄檔案，主題輔助記錄模式啟動失敗，請刪除輔助記錄檔案後重新開始遊戲",
            "jp": "エラー：テーマ補助記録ファイルが正常にデコードできなかったため、テーマ補助記録モードを開始できませんでした。補助記録ファイルを削除してゲームを再起動してください",
            "kor": "오류: 테마 보조녹음 파일을 성공적으로 디코딩하지 못해 테마 보조녹화 모드를 시작하지 못했습니다. 보조녹화 파일을 삭제하고 게임을 다시 시작해주세요",
            "ru": "Ошибка: Не удалось запустить режим вспомогательной записи темы, поскольку файл вспомогательной записи темы не удалось успешно декодировать. Пожалуйста, удалите файл вспомогательной записи и перезапустите игру",
            "de": "Fehler: Der Modus „Hilfsaufnahme des Themas“ konnte nicht gestartet werden, da die Hilfsaufnahmedatei des Themas nicht erfolgreich dekodiert werden konnte. Bitte löschen Sie die Hilfsaufnahmedatei und starten Sie das Spiel neu",
            "fra": "Erreur: Le mode d'enregistrement auxiliaire du thème n'a pas pu démarrer car le fichier d'enregistrement auxiliaire du thème n'a pas pu être décodé correctement. Veuillez supprimer le fichier d'enregistrement auxiliaire et redémarrer le jeu",
            "spa": "Error: El modo de grabación auxiliar del tema no se pudo iniciar porque no se pudo decodificar correctamente el archivo de grabación auxiliar del tema. Elimina el archivo de grabación auxiliar y reinicia el juego",
            "pt": "Erro: O modo de gravação auxiliar do tema falhou ao iniciar porque o arquivo de gravação auxiliar do tema não pôde ser decodificado com sucesso. Exclua o arquivo de gravação auxiliar e reinicie o jogo",
            "it": "Errore: La modalità di registrazione ausiliaria del tema non è riuscita ad avviarsi perché il file di registrazione ausiliaria del tema non è stato decodificato correttamente. Elimina il file di registrazione ausiliaria e riavvia il gioco",
            "en": "Error: The theme auxiliary recording mode failed to start because the theme auxiliary recording file could not be decoded successfully. Please delete the auxiliary recording file and restart the game"
        },
        "error_RAC_disabled_autocopy": {
            "zh": "错误：随机复制模式启动失败，因为前置的自动复制模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：隨機複製模式啟動失敗，因為前置的自動複製模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回の自動コピーモードが有効になっていないため、ランダムコピーモードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "kor": "오류: 이전 자동 복사 모드가 활성화되지 않았기 때문에 임의 복사 모드를 시작할 수 없습니다. 프로그램 구성이 올바른지 확인하세요",
            "ru": "Ошибка: Не удалось запустить режим произвольного копирования, поскольку не был включен предыдущий автоматический режим копирования. Проверьте, пожалуйста, правильность конфигурации программы",
            "de": "Fehler: Der Zufallskopiermodus konnte nicht gestartet werden, da der vorherige automatische Kopiermodus nicht aktiviert wurde. Bitte überprüfen Sie, ob die Programmkonfiguration korrekt ist",
            "fra": "Erreur: Le mode de copie aléatoire n'a pas pu démarrer car le mode de copie automatique précédent n'a pas été activé. Veuillez vérifier si la configuration du programme est correcte",
            "spa": "Error: El modo de copia aleatoria no se pudo iniciar porque no se había habilitado el modo de copia automática anterior. Verifique si la configuración del programa es correcta",
            "pt": "Erro: O modo de cópia aleatória falhou ao iniciar porque o modo de cópia automática anterior não foi habilitado. Verifique se a configuração do programa está correta",
            "it": "Errore: La modalità di copia casuale non è riuscita ad avviarsi perché la precedente modalità di copia automatica non è stata abilitata. Controllare se la configurazione del programma è corretta",
            "en": "Error: The random copying mode failed to start because the previous automatic copying mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_TAR_disabled_LAP": {
            "zh": "错误：主题辅助记录模式启动失败，因为前置的日志辅助处理模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：主題輔助記錄模式啟動失敗，因為前置的日誌輔助處理模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回のログアシスト処理モードが有効になっていないため、テーマ補助記録モードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "kor": "오류: 이전 로그 지원 처리 모드가 활성화되지 않았기 때문에 테마 보조 녹음 모드를 시작하지 못했습니다. 프로그램 구성이 올바른지 확인해주세요",
            "ru": "Ошибка: Не удалось запустить вспомогательный режим записи темы, поскольку не был включен предыдущий вспомогательный режим обработки журнала. Проверьте, пожалуйста, правильность конфигурации программы",
            "de": "Fehler: Der Themen-Hilfsaufzeichnungsmodus konnte nicht gestartet werden, da der vorherige Protokoll-unterstützte Verarbeitungsmodus nicht aktiviert wurde. Bitte überprüfen Sie, ob die Programmkonfiguration korrekt ist",
            "fra": "Erreur: Le mode d'enregistrement auxiliaire du thème n'a pas pu démarrer car le mode de traitement assisté par journal précédent n'a pas été activé. Veuillez vérifier si la configuration du programme est correcte",
            "spa": "Error: El modo de grabación auxiliar del tema no se pudo iniciar porque no se habilitó el modo de procesamiento asistido por registro anterior. Verifique si la configuración del programa es correcta",
            "pt": "Erro: O modo de gravação auxiliar do tema falhou ao iniciar porque o modo de processamento assistido de log anterior não foi habilitado. Verifique se a configuração do programa está correta",
            "it": "Errore: La modalità di registrazione ausiliaria del tema non è riuscita ad avviarsi perché la precedente modalità di elaborazione assistita dal registro non è stata abilitata. Controllare se la configurazione del programma è corretta",
            "en": "Error: The theme auxiliary recording mode failed to start because the previous log assisted processing mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_SAS_disabled_autocopy": {
            "zh": "错误：半自动发送模式启动失败，因为前置的自动复制模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：半自動發送模式啟動失敗，因為前置的自動複製模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回の自動コピーモードが有効になっていないため、半自動送信モードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "kor": "오류: 이전 자동 복사 모드가 활성화되지 않았기 때문에 반자동 전송 모드를 시작하지 못했습니다. 프로그램 구성이 올바른지 확인해주세요",
            "ru": "Ошибка: Не удалось запустить полуавтоматический режим отправки, поскольку не был включен предыдущий автоматический режим копирования. Проверьте, пожалуйста, правильность конфигурации программы",
            "de": "Fehler: Der halbautomatische Sendemodus konnte nicht gestartet werden, da der vorherige automatische Kopiermodus nicht aktiviert wurde. Bitte überprüfen Sie, ob die Programmkonfiguration korrekt ist",
            "fra": "Erreur: Le mode d'envoi semi-automatique n'a pas pu démarrer car le mode de copie automatique précédent n'a pas été activé. Veuillez vérifier si la configuration du programme est correcte",
            "spa": "Error: El modo de envío semiautomático no se pudo iniciar porque no se había habilitado el modo de copia automática anterior. Verifique si la configuración del programa es correcta",
            "pt": "Erro: O modo de envio semiautomático falhou ao iniciar porque o modo de cópia automática anterior não foi habilitado. Verifique se a configuração do programa está correta",
            "it": "Errore: La modalità di invio semi-automatico non è riuscita ad avviarsi perché la precedente modalità di copia automatica non è stata abilitata. Controllare se la configurazione del programma è corretta",
            "en": "Error: The semi-automatic sending mode failed to start because the previous automatic copying mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_SAS_disabled_LAP": {
            "zh": "错误：半自动发送模式启动失败，因为前置的日志辅助处理模式尚未开启，请检查程序配置是否正确",
            "cht": "錯誤：半自動發送模式啟動失敗，因為前置的日誌輔助處理模式尚未開啟，請檢查程式配置是否正確",
            "jp": "エラー：前回のログアシスト処理モードが有効になっていないため、半自動送信モードを開始できませんでした。プログラムの設定が正しいか確認してください",
            "kor": "오류: 이전 로그 지원 처리 모드가 활성화되지 않았기 때문에 반자동 전송 모드를 시작하지 못했습니다. 프로그램 구성이 올바른지 확인해주세요",
            "ru": "Ошибка: Не удалось запустить полуавтоматический режим отправки, так как не был включен предыдущий режим обработки с помощью журнала. Проверьте, пожалуйста, правильность конфигурации программы",
            "de": "Fehler: Der halbautomatische Sendemodus konnte nicht gestartet werden, da der vorherige protokollgestützte Verarbeitungsmodus nicht aktiviert wurde. Bitte überprüfen Sie, ob die Programmkonfiguration korrekt ist",
            "fra": "Erreur: Le mode d'envoi semi-automatique n'a pas pu démarrer car le mode de traitement assisté par journal précédent n'a pas été activé. Veuillez vérifier si la configuration du programme est correcte",
            "spa": "Error: El modo de envío semiautomático no se pudo iniciar porque no se había habilitado el modo de procesamiento asistido por registro anterior. Verifique si la configuración del programa es correcta",
            "pt": "Erro: O modo de envio semiautomático falhou ao iniciar porque o modo de processamento assistido por log anterior não foi habilitado. Verifique se a configuração do programa está correta",
            "it": "Errore: La modalità di invio semi-automatico non è riuscita ad avviarsi perché la precedente modalità di elaborazione assistita dal log non è stata abilitata. Controllare se la configurazione del programma è corretta",
            "en": "Error: The semi-automatic sending mode failed to start because the previous log assisted processing mode has not been enabled. Please check if the program configuration is correct"
        },
        "error_SAS_window_not_found": {
            "zh": "错误：未找到游戏窗口，当前内容半自动发送失败，请检查游戏窗口名称是否设置正确",
            "cht": "錯誤：未找到遊戲窗口，本次內容半自動發送失敗，請檢查遊戲窗口名稱是否設定正確",
            "jp": "エラー：ゲームウィンドウが見つからなかったため、現在のコンテンツの半自動送信に失敗しました。ゲームウィンドウのタイトルが正しく設定されているか確認してください",
            "kor": "오류: 게임창을 찾을 수 없어 현재 콘텐츠 반자동 전송에 실패했습니다. 게임 창 제목이 올바르게 설정되어 있는지 확인해주세요",
            "ru": "Ошибка: Полуавтоматическая отправка текущего контента не удалась, так как игровое окно не найдено. Пожалуйста, проверьте, правильно ли задан заголовок игрового окна",
            "de": "Fehler: Das halbautomatische Senden des aktuellen Inhalts ist fehlgeschlagen, da das Spielfenster nicht gefunden wurde. Bitte überprüfen Sie, ob der Titel des Spielfensters richtig eingestellt ist",
            "fra": "Erreur: L'envoi semi-automatique du contenu actuel a échoué car la fenêtre de jeu n'a pas été trouvée. Veuillez vérifier si le titre de la fenêtre de jeu est correctement défini",
            "spa": "Error: El envío semiautomático del contenido actual falló porque no se encontró la ventana del juego. Verifique si el título de la ventana del juego está configurado correctamente",
            "pt": "Erro: O envio semiautomático do conteúdo atual falhou porque a janela do jogo não foi encontrada. Verifique se o título da janela do jogo está definido corretamente",
            "it": "Errore: L'invio semi-automatico del contenuto corrente non è riuscito perché la finestra di gioco non è stata trovata. Controlla se il titolo della finestra di gioco è impostato correttamente",
            "en": "Error: The current content semi-automatic sending failed because the game window was not found. Please check if the game window title is set correctly"
        },
        "error_exception": {
            "zh": f'错误：{e} ',
            "cht": f'錯誤：{e} ',
            "jp": f'エラー：{e} ',
            "kor": f'오류: {e}',
            "ru": f'Ошибка: {e}',
            "de": f'Fehler: {e}',
            "fra": f'Erreur: {e}',
            "spa": f'Error: {e}',
            "pt": f'Erro: {e}',
            "it": f'Errore: {e}',
            "en": f'Error: {e}'
        },
        "input_prompt": {
            "zh": "请输入匹配式：",
            "cht": "請輸入匹配式：",
            "jp": "マッチする式を入力してください：",
            "kor": "일치하는 표현식을 입력하세요: ",
            "ru": "Введите подходящее выражение: ",
            "de": "Bitte geben Sie den passenden Ausdruck ein: ",
            "fra": "Veuillez saisir l'expression correspondante: ",
            "spa": "Introduzca la expresión coincidente: ",
            "pt": "Insira a expressão correspondente: ",
            "it": "Inserisci l'espressione corrispondente: ",
            "en": "Please enter the matching expression: "
        },
        "exit_program": {
            "zh": "您已退出程序",
            "cht": "您已退出程式",
            "jp": "プログラムを終了しました",
            "kor": "프로그램을 종료했습니다",
            "ru": "Вы вышли из программы",
            "de": "Sie haben das Programm beendet",
            "fra": "Vous avez quitté le programme",
            "spa": "Has salido del programa",
            "pt": "Você saiu do programa",
            "it": "Hai abbandonato il programma",
            "en": "You have exited the program"
        },
        "output_en_word_chars": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマの英字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 영어로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов на Английском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang und auf Englisch',
            "fra": f'Le thème mesure {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères en Anglais',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres de longitud en Inglés',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres em Inglês',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri in Inglese',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long'
        },
        "output_zh_word_chars": {
            "zh": f'该主题字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題簡體中文字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの簡体字中国語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 중국어 간체로 된 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} иероглифа(ов) в Упрощенном Китайском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang in Vereinfachtem Chinesisch',
            "fra": f'Le thème est {Fore.YELLOW}{word_chars}{Fore.CYAN} caractère(s) de long en Chinois Simplifié',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} carácter(es) de longitud en Chino Simplificado',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caractere(s) de comprimento em Chinês Simplificado',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} carattere/i in Cinese Semplificato',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Simplified Chinese'
        },
        "output_cht_word_chars": {
            "zh": f'该主题繁体中文字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの繁体字中国語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 중국어 번체로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} иероглифа(ов) на Традиционном Китайском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang in Traditionellem Chinesisch',
            "fra": f'Le thème est {Fore.YELLOW}{word_chars}{Fore.CYAN} caractère(s) de long en Chinois Traditionnel',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} carácter(es) de longitud en Chino Tradicional',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caractere(s) de comprimento em Chinês Tradicional',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} carattere/i in Cinese Tradizionale',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Traditional Chinese'
        },
        "output_jp_word_chars": {
            "zh": f'该主题日语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題日語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 일본어로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} иероглифа(ов) на Японском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang auf Japanisch',
            "fra": f'Le thème est long de {Fore.YELLOW}{word_chars}{Fore.CYAN} caractère(s) en Japonais',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} carácter(es) de longitud en Japonés',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caractere(s) de comprimento em Japonês',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} carattere/i in Giapponese',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Japanese'
        },
        "output_kor_word_chars": {
            "zh": f'该主题韩语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字',
            "cht": f'此主題韓語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字',
            "jp": f'テーマの韓国語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마의 길이는 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} иероглифа(ов) на Корейском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang auf Koreanisch',
            "fra": f'Le thème est {Fore.YELLOW}{word_chars}{Fore.CYAN} caractère(s) de long en Coréen',
            "spa": f'El tema tiene una longitud de {Fore.YELLOW}{word_chars}{Fore.CYAN} carácter(es) en Coreano',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caractere(s) em Coreano',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} carattere/i in Coreano',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} character(s) long in Korean'
        },
        "output_ru_word_chars": {
            "zh": f'该主题俄语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題俄語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマのロシア語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마의 길이는 러시아어로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang auf Russisch',
            "fra": f'Le thème mesure {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères de long en Russe',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres de longitud en Ruso',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres em Russo',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri in Russo',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long in Russian'
        },
        "output_de_word_chars": {
            "zh": f'该主题德语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題德語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマのドイツ語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마의 길이는 독일어로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов на Немецком языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang',
            "fra": f'Le thème mesure {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères en Allemand',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres en Alemán',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres em Alemão',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri in Tedesco',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long in German'
        },
        "output_fra_word_chars": {
            "zh": f'该主题法语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題法語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマのフランス語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 프랑스어로 된 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов на Французском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang und auf Französisch',
            "fra": f'Le thème fait {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères de long',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres de longitud en Francés',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres em Francês',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri in Francese',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long in French'
        },
        "output_spa_word_chars": {
            "zh": f'该主题西班牙语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題西班牙語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマのスペイン語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 스페인어로 된 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов на Испанском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang auf Spanisch',
            "fra": f'Le thème mesure {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères en Espagnol',
            "spa": f'El tema tiene una longitud de {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres em Espanhol',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri in Spagnolo',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long in Spanish'
        },
        "output_pt_word_chars": {
            "zh": f'该主题葡萄牙语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題葡萄牙語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマのポルトガル語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마의 길이는 포르투갈어로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов на Португальском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang auf Portugiesisch',
            "fra": f'Le thème mesure {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères en Portugais',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres de longitud en Portugués',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri in Portoghese',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long in Portuguese'
        },
        "output_it_word_chars": {
            "zh": f'该主题意大利语字数为 {Fore.YELLOW}{word_chars}{Fore.CYAN} 个字母',
            "cht": f'此主題義大利語字數為 {Fore.YELLOW}{word_chars}{Fore.CYAN} 個字母',
            "jp": f'テーマのイタリア語の文字数は {Fore.YELLOW}{word_chars}{Fore.CYAN} です',
            "kor": f'테마는 이탈리아어로 {Fore.YELLOW}{word_chars}{Fore.CYAN} 자 길이입니다',
            "ru": f'Тема имеет длину {Fore.YELLOW}{word_chars}{Fore.CYAN} символов на Итальянском языке',
            "de": f'Das Thema ist {Fore.YELLOW}{word_chars}{Fore.CYAN} Zeichen lang und auf Italienisch',
            "fra": f'Le thème mesure {Fore.YELLOW}{word_chars}{Fore.CYAN} caractères en Italien',
            "spa": f'El tema tiene {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres de longitud en Italiano',
            "pt": f'O tema tem {Fore.YELLOW}{word_chars}{Fore.CYAN} caracteres em Italiano',
            "it": f'Il tema è lungo {Fore.YELLOW}{word_chars}{Fore.CYAN} caratteri',
            "en": f'The theme is {Fore.YELLOW}{word_chars}{Fore.CYAN} characters long in Italian'
        },
        "language_switched": {
            "zh": "已将语言设置为简体中文",
            "cht": "已將語言設定為繁體中文",
            "jp": "言語を日本語に設定しました",
            "kor": "언어를 한국어로 설정하셨습니다",
            "ru": "Вы устанавливаете Русский язык",
            "de": "Sie haben Ihre Sprache auf Deutsch eingestellt",
            "fra": "Vous définissez votre langue sur le Français",
            "spa": "Configuraste tu idioma en Español",
            "pt": "Você definiu seu idioma para Português",
            "it": "Hai impostato la tua lingua su Italiano",
            "en": "You set your language to English"
        },
        "match_failed": {
            "zh": "匹配失败，未在当前词库中找到匹配条目",
            "cht": "匹配失敗，未在當前詞庫中找到匹配條目",
            "jp": "マッチに失敗しました、現在のシソーラスに一致するものが見つかりませんでした",
            "kor": "일치에 실패했습니다. 현재 동의어 사전에 일치하는 항목이 없습니다",
            "ru": "Не удалось установить соответствие, в текущем тезаурусе не найдено ни одной подходящей записи",
            "de": "Übereinstimmung fehlgeschlagen, kein passender Eintrag im aktuellen Thesaurus gefunden",
            "fra": "La correspondance a échoué, aucune entrée correspondante n'a été trouvée dans le thésaurus actuel",
            "spa": "Coincidencia fallida, no se encontró ninguna entrada coincidente en el tesauro actual",
            "pt": "Falha na correspondência, nenhuma entrada correspondente foi encontrada no thesaurus atual",
            "it": "Corrispondenza fallita, nessuna voce corrispondente trovata nel thesaurus corrente",
            "en": "Match failed, no matching entry found in the current thesaurus"
        },
        "output_LAP_builder_left": {
            "zh": "本回合的建筑师离开了游戏！跳过",
            "cht": "當前回合的建築師離開了遊戲！跳過",
            "jp": "このラウンドの建築家がゲームから退出しました。スキップ中",
            "kor": "플롯 소유자가 게임을 나갔습니다! 건너 뛰는 중",
            "ru": "Владелец участка покинул игру! Пропуск",
            "de": "Der Bauplatzbesitzer hat das Spiel verlassen! Überspringe",
            "fra": "Le propriétaire du terrain a quitté la partie! Au suivant",
            "spa": "¡El dueño de la parcela ha abandonado el juego! Pasando al siguiente",
            "pt": "O dono desta construção saiu da partida! Pulando",
            "it": "Il proprietario del lotto è uscito! Saltando",
            "en": "The builder of this round has left the game! Skipping"
        },
        "output_LAP_builder_AFK": {
            "zh": "本回合的建筑师处于挂机状态！跳过",
            "cht": "當前回合的建築師處於掛網狀態！跳過",
            "jp": "このラウンドの建築家が無操作状態です。スキップ中",
            "kor": "해당 플롯의 플레이어가 자리를 비웠습니다! 건너 뛰는 중",
            "ru": "Хозяин участка отошёл! Пропуск",
            "de": "Der Bauplatzbesitzer ist AFK! Überspringen",
            "fra": "Le propriétaire du plot est AFK! Au suivant",
            "spa": "¡El dueño de la parcela está AFK! Pasando al siguiente",
            "pt": "O construtor está ausente! Pulando",
            "it": "Il proprietario del lotto è AFK! Saltando",
            "en": "The builder of this round is AFK! Skipping"
        },
        "output_LAP_builder_unplaced": {
            "zh": "本回合的建筑师尚未放置任何方块！跳过",
            "cht": "當前回合的建築師沒有放置任何方塊！跳過",
            "jp": "このラウンドの建築家がブロックを設置していません。スキップ中",
            "kor": "플롯 소유자가 아무런 블록도 설치를 하지 않았네요! 건너 뛰는 중",
            "ru": "Хозяин участка не поставил ни одного блока! Пропуск",
            "de": "Der Bauplatzbesitzer hat keine Blöcke platziert! Überspringen",
            "fra": "Le propriétaire du plot n'a placé aucun bloc! Au suivant",
            "spa": "¡El dueño de esta parcela no ha puesto ningún bloque! Saltando",
            "pt": "O construtor não colocou blocos! Pulando",
            "it": "Il proprietario del lotto non ha piazzato blocchi! Saltando",
            "en": "The builder of this round hasn't placed any blocks! Skipping"
        },
        "output_LAP_guess_info": {
            "zh": f'检测到有玩家猜测了主题 {Fore.YELLOW}{output_del_elem}{Fore.RED} 但未猜对，即将据此输出筛选后的匹配条目',
            "cht": f'偵測到有玩家猜測了主題 {Fore.YELLOW}{output_del_elem}{Fore.RED} 但未猜對，即將據此輸出篩選後的匹配條目',
            "jp": f'プレイヤーがテーマ {Fore.YELLOW}{output_del_elem}{Fore.RED} を推測したが正しく推測しなかったことを検出し、それに応じてフィルタリングされたマッチするエントリが出力されます',
            "kor": f'플레이어가 테마 {Fore.YELLOW}{output_del_elem}{Fore.RED} 를 추측했지만 올바르게 추측하지 않았음을 감지하고 필터링된 일치 항목이 그에 따라 출력됩니다',
            "ru": f'Определяет, что игрок угадал тему(ы) {Fore.YELLOW}{output_del_elem}{Fore.RED}, но не угадал правильно, и отфильтрованные совпадающие записи будут выведены соответствующим образом',
            "de": f'Erkennt, dass der Spieler Thema(n) {Fore.YELLOW}{output_del_elem}{Fore.RED} erraten hat, aber nicht richtig, und die gefilterten übereinstimmenden Einträge werden entsprechend ausgegeben',
            "fra": f"Détecte que le joueur a deviné le(s) thème(s) {Fore.YELLOW}{output_del_elem}{Fore.RED} mais n'a pas deviné correctement, et les entrées correspondantes filtrées seront affichées en conséquence",
            "spa": f'Detecta que el jugador adivinó el tema(s) {Fore.YELLOW}{output_del_elem}{Fore.RED} pero no lo hizo correctamente, y las entradas coincidentes filtradas se mostrarán en consecuencia',
            "pt": f'Detecta que o jogador adivinhou o(s) tema(s) {Fore.YELLOW}{output_del_elem}{Fore.RED}, mas não adivinhou corretamente, e as entradas correspondentes filtradas serão geradas adequadamente',
            "it": f'Rileva che il giocatore ha indovinato il tema(i) {Fore.YELLOW}{output_del_elem}{Fore.RED} ma non ha indovinato correttamente, e le voci corrispondenti filtrate verranno visualizzate di conseguenza',
            "en": f'Detects that the player guessed theme(s) {Fore.YELLOW}{output_del_elem}{Fore.RED} but did not guess correctly, and the filtered matching entries will be output accordingly'
        },
        "output_LAP_correct_guess": {
            "zh": f'检测到您正确猜出主题！本回合辅助猜测已暂停',
            "cht": f'偵測到您正確猜出主題！當前回合輔助猜測已暫停',
            "jp": f'テーマを正しく推測したことが検出されました。このラウンドでは、アシストによる推測は一時停止されています',
            "kor": f'테마를 정확하게 추측했음을 감지합니다! 이번 라운드에서는 보조 추측이 일시중지되었습니다',
            "ru": f'Обнаруживает, что вы правильно угадали тему! В этом раунде вспомогательное угадывание приостановлено',
            "de": f'Erkennt, dass Sie das Thema richtig erraten haben! Das unterstützte Raten wurde für diese Runde pausiert',
            "fra": f'Détecte que vous avez correctement deviné le thème! La devinette assistée a été interrompue pour ce tour',
            "spa": f'¡Detecta que has adivinado correctamente el tema! La adivinación asistida se ha pausado para esta ronda',
            "pt": f'Detecta que você adivinhou corretamente o tema! A adivinhação assistida foi pausada para esta rodada',
            "it": f"Rileva che hai indovinato correttamente il tema! L'indovinello assistito è stato sospeso per questo round",
            "en": f'Detects that you have correctly guessed the theme! Assisted guessing has been paused for this round'
        },
        "output_LAP_correct_theme": {
            "zh": f'本回合的主题是 {Fore.YELLOW}{correct_theme}{Fore.CYAN} ',
            "cht": f'當前回合的主題是 {Fore.YELLOW}{correct_theme}{Fore.CYAN} ',
            "jp": f'このラウンドのテーマは {Fore.YELLOW}{correct_theme}{Fore.CYAN} でした',
            "kor": f'이번 라운드의 주제는 {Fore.YELLOW}{correct_theme}{Fore.CYAN} 이었습니다',
            "ru": f'Тема этого раунда была {Fore.YELLOW}{correct_theme}{Fore.CYAN}',
            "de": f'Das Thema dieser Runde war {Fore.YELLOW}{correct_theme}{Fore.CYAN}',
            "fra": f'Le thème de ce tour était {Fore.YELLOW}{correct_theme}{Fore.CYAN}',
            "spa": f'El tema de esta ronda fue {Fore.YELLOW}{correct_theme}{Fore.CYAN}',
            "pt": f'O tema desta rodada foi {Fore.YELLOW}{correct_theme}{Fore.CYAN}',
            "it": f'Il tema di questo round era {Fore.YELLOW}{correct_theme}{Fore.CYAN}',
            "en": f'The theme of this round was {Fore.YELLOW}{correct_theme}{Fore.CYAN}'
        },
        "output_TAR_theme_added": {
            "zh": f'已将主题 {Fore.YELLOW}{correct_theme}{Fore.GREEN} 添加至辅助记录文件',
            "cht": f'已將主題 {Fore.YELLOW}{correct_theme}{Fore.GREEN} 新增至輔助記錄檔案',
            "jp": f'テーマ {Fore.YELLOW}{correct_theme}{Fore.GREEN} が補助記録ファイルに追加されました',
            "kor": f'보조녹화 파일에 {Fore.YELLOW}{correct_theme}{Fore.GREEN} 테마가 추가되었습니다',
            "ru": f'Тема {Fore.YELLOW}{correct_theme}{Fore.GREEN} была добавлена во вспомогательный файл записи',
            "de": f'Das Thema {Fore.YELLOW}{correct_theme}{Fore.GREEN} wurde der zusätzlichen Aufnahmedatei hinzugefügt',
            "fra": f"Le thème {Fore.YELLOW}{correct_theme}{Fore.GREEN} a été ajouté au fichier d'enregistrement auxiliaire",
            "spa": f'Se ha agregado el tema {Fore.YELLOW}{correct_theme}{Fore.GREEN} al archivo de grabación auxiliar',
            "pt": f'O tema {Fore.YELLOW}{correct_theme}{Fore.GREEN} foi adicionado ao arquivo de gravação auxiliar',
            "it": f'Il tema {Fore.YELLOW}{correct_theme}{Fore.GREEN} è stato aggiunto al file di registrazione ausiliario',
            "en": f'Theme {Fore.YELLOW}{correct_theme}{Fore.GREEN} has been added to the auxiliary recording file'
        },
        "output_LAP_game_over": {
            "zh": f'本场游戏结束，日志辅助处理模式共计帮助您猜测了 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 次',
            "cht": f'本場遊戲結束，日誌輔助處理模式總計幫助您猜測了 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 次',
            "jp": f'ゲームは終了しました。ログアシスト処理モードにより、合計 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 回推測できました',
            "kor": f'게임이 끝났고, 로그 지원 처리 모드를 통해 총 {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} 번 추측하는 데 도움이 되었습니다',
            "ru": f'Игра окончена, и режим обработки логов помог вам угадать {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} раз(а) в сумме',
            "de": f'Das Spiel ist vorbei und der protokollgestützte Verarbeitungsmodus hat Ihnen geholfen, insgesamt {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} Mal zu erraten',
            "fra": f'Le jeu est terminé et le mode de traitement assisté par journal vous a aidé à deviner {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} fois au total',
            "spa": f'El juego ha terminado y el modo de procesamiento asistido por registro te ha ayudado a adivinar {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} veces en total',
            "pt": f'O jogo acabou, e o modo de processamento assistido por log ajudou você a adivinhar {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} vez(es) no total',
            "it": f'La partita è terminata e la modalità di elaborazione assistita dal registro ti ha aiutato a indovinare {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} tempo/i in totale',
            "en": f'The game is over, and the log assisted processing mode has helped you guess {Fore.YELLOW}{LAP_guess_cnt}{Fore.MAGENTA} time(s) in total'
        },
        "output_SAS_content_sent": {
            "zh": f'已发送剪贴板内容 {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} 至游戏内',
            "cht": f'已發送剪貼簿內容 {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} 至遊戲內',
            "jp": f'クリップボードのコンテンツ {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} をゲームに送信しました',
            "kor": f'클립보드 콘텐츠 {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} 을 게임에 보냈습니다',
            "ru": f'Отправил содержимое буфера обмена {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} в игру',
            "de": f'Zwischenablageinhalt {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} an das Spiel gesendet',
            "fra": f'Contenu du presse-papiers envoyé {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} au jeu',
            "spa": f'Se envió el contenido del portapapeles {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} al juego',
            "pt": f'Conteúdo da área de transferência {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} enviado para o jogo',
            "it": f'Inviato il contenuto degli appunti {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} al gioco',
            "en": f'Sent clipboard content {Fore.YELLOW}{pyperclip.paste()}{Fore.GREEN} to the game'
        }
    }

    moe_suffix = {
        "zh": "喵~",
        "cht": "喵~",
        "jp": "ニャー~",
        "kor": " 야옹~",
        "ru": " мяу~",
        "de": " miau~",
        "fra": " miaou~",
        "spa": " miau~",
        "pt": " miau~",
        "it": " miagolio~",
        "en": " meow~"
    }

    if key == "input_prompt" and moe:
        input_prompt_moe = {
            "zh": "请输入奇妙咒语：",
            "cht": "請輸入奇妙咒語：",
            "jp": "魔法の呪文を入力してください：",
            "kor": "놀라운 주문을 입력하세요: ",
            "ru": "Введите чудесное заклинание: ",
            "de": "Bitte geben Sie den wunderbaren Zauber ein: ",
            "fra": "Veuillez saisir le sort merveilleux: ",
            "spa": "Introduzca el maravilloso hechizo: ",
            "pt": "Insira o feitiço maravilhoso: ",
            "it": "Inserisci l'incantesimo meraviglioso: ",
            "en": "Please enter the marvelous spell: "
        }
        return input_prompt_moe.get(lang, input_prompt_moe["en"])

    if key == "output_LAP_builder_left" and moe:
        output_LAP_builder_left_moe = {
            "zh": "本回合的建筑师回到快乐老家了！跳过喵~",
            "cht": "當前回合的建築師回到快樂老家了！跳過喵~",
            "jp": "このラウンドの建築家は幸せな故郷に戻ってきました。スキップ中ニャー~",
            "kor": "이번 라운드의 제작자가 행복한 고향으로 돌아왔습니다! 건너 뛰는 중야옹~",
            "ru": "Строитель этого раунда вернулся в счастливый родной город! Пропуск мяу~",
            "de": "Der Erbauer dieser Runde ist in die glückliche Heimatstadt zurückgekehrt! Überspringe miau~",
            "fra": "Le constructeur de cette ronde est de retour dans sa ville natale heureuse! Au suivant miaou~",
            "spa": "¡El constructor de esta ronda ha regresado a su feliz ciudad natal! Pasando al siguiente miau~",
            "pt": "O construtor desta rodada retornou à feliz cidade natal! Pulando miau~",
            "it": "Il costruttore di questo round è tornato nella sua felice città natale! Saltando miagolio~",
            "en": "The builder of this round has returned to the happy hometown! Skipping meow~"
        }
        return output_LAP_builder_left_moe.get(lang, output_LAP_builder_left_moe["en"])

    if key == "output_LAP_builder_AFK" and moe:
        output_LAP_builder_AFK_moe = {
            "zh": "本回合的建筑师沉浸在了幻想乡之中！跳过喵~",
            "cht": "當前回合的建築師沉浸在了幻想鄉之中！跳過喵~",
            "jp": "このラウンドの建築家は幻想郷に浸っています。スキップ中ニャー~",
            "kor": "이번 라운드의 제작자는 환상향에 빠져 있습니다! 건너 뛰는 중야옹~",
            "ru": "Строитель этого раунда погружается в Генсокё! Пропуск мяу~",
            "de": "Der Erbauer dieser Runde ist in Gensokyo vertieft! Überspringe miau~",
            "fra": "Le constructeur de ce tour est immergé dans Gensokyo! Au suivant miaou~",
            "spa": "¡El constructor de esta ronda está inmerso en Gensokyo! Pasando al siguiente miau~",
            "pt": "O construtor desta rodada está imerso em Gensokyo! Pulando miau~",
            "it": "Il costruttore di questo round è immerso in Gensokyo! Saltando miagolio~",
            "en": "The builder of this round is immersed in Gensokyo! Skipping meow~"
        }
        return output_LAP_builder_AFK_moe.get(lang, output_LAP_builder_AFK_moe["en"])

    if key == "output_LAP_builder_unplaced" and moe:
        output_LAP_builder_unplaced_moe = {
            "zh": "本回合建筑师的智商尚未占领高地！跳过喵~",
            "cht": "當前回合建築師的智商尚未佔領高地！跳過喵~",
            "jp": "このラウンドの建築家はあまり賢く見えません。スキップ中ニャー~",
            "kor": "이번 라운드의 작성자는 그다지 똑똑해 보이지 않습니다! 건너 뛰는 중야옹~",
            "ru": "Строитель этого раунда не выглядит слишком умным! Пропуск мяу~",
            "de": "Der Erbauer dieser Runde sieht nicht besonders schlau aus! Überspringe miau~",
            "fra": "Le constructeur de ce tour n'a pas l'air très intelligent! Au suivant miaou~",
            "spa": "¡El constructor de esta ronda no parece muy inteligente! Pasando al siguiente miau~",
            "pt": "O construtor desta rodada não parece muito inteligente! Pulando miau~",
            "it": "Il costruttore di questo round non sembra molto intelligente! Saltando miagolio~",
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
        "@kor": "한국어",
        "@ru": "Русский",
        "@de": "Deutsch",
        "@fra": "Français",
        "@spa": "Español",
        "@pt": "Português",
        "@it": "Italiano",
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
                pattern += rf"[a-zA-Z\u4E00-\u9FFF\u3040-\u30FF\uFF66-\uFF9F\uAC00-\uD7AF\u0400-\u052F\u00C0-\u00FF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF-.'/~()《》]{{{num}}}"
                num = ""
            pattern += re.escape(char) if char in banned_chars else ("." if char == "_" else char)
    pattern += rf"[a-zA-Z\u4E00-\u9FFF\u3040-\u30FF\uFF66-\uFF9F\uAC00-\uD7AF\u0400-\u052F\u00C0-\u00FF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF-.'/~()《》]{{{num}}}" if num else ""
    return pattern, target_column

def input_thesaurus():
    global df

    print(f'{Fore.MAGENTA}{output_message("program_info", lang, moe)}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}{output_message("program_note", lang, moe)}{Style.RESET_ALL}')

    if not os.path.exists(GTB_THESAURUS):
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_file_not_found", lang, moe)}{Style.RESET_ALL}')
        exit()
    else:
        df = pd.read_excel(GTB_THESAURUS, keep_default_na=False).replace("", "%")

    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_starts", lang, moe)} {"-" * 10}{Style.RESET_ALL}')
    for column in ["English", "简体中文", "繁體中文", "日本語", "한국어", "Русский", "Deutsch", "Français", "Español", "Português", "Italiano", "Shortcut(s)", "Multiword(s)"]:
        print(f'{Fore.CYAN}{column}  \t\t\t{Fore.GREEN}●{Style.RESET_ALL}') if column in df.columns else print(f'{Fore.CYAN}{column}  \t\t\t{Fore.RED}●{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}{"-" * 10} {output_message("thesaurus_self_check_completed", lang, moe)} {"-" * 10}{Style.RESET_ALL}')

    if "English" not in df.columns:
        print(f'{Fore.YELLOW}{output_message("error_thesaurus_column_not_found", lang, moe)}{Style.RESET_ALL}')
        exit()

def program_self_check():
    MOE_color = Fore.GREEN if MOE_MODE else Fore.RED
    AC_color = Fore.GREEN if AUTO_COPY else Fore.RED
    RAC_color = Fore.GREEN if RAC_MODE and AUTO_COPY else (Fore.YELLOW if RAC_MODE else Fore.RED)
    LAP_color = Fore.GREEN if LAP_MODE and os.path.exists(LOG_FILE) else (Fore.YELLOW if LAP_MODE else Fore.RED)
    TAR_color = Fore.GREEN if TAR_MODE and LAP_MODE else (Fore.YELLOW if TAR_MODE else Fore.RED)
    SAS_color = Fore.GREEN if SAS_MODE and AUTO_COPY and LAP_MODE else (Fore.YELLOW if SAS_MODE else Fore.RED)
    mode_color_dic = {
            "MOE": MOE_color,
            "AC": AC_color,
            "RAC": RAC_color,
            "LAP": LAP_color,
            "TAR": TAR_color,
            "SAS": SAS_color
        }

    print(f'{Fore.MAGENTA}{"-" * 10} {output_message("program_self_check_starts", lang, moe)} {"-" * 10}{Style.RESET_ALL}')
    for mode, mode_color in mode_color_dic.items():
        print(f'{Fore.CYAN}{output_message(f"program_{mode}_STD_name", lang, moe=False)}{mode_color}●{Style.RESET_ALL}')
    print(f'{Fore.MAGENTA}{"-" * 10} {output_message("program_self_check_completed", lang, moe)} {"-" * 10}{Style.RESET_ALL}')

    if LAP_MODE:
        LAP_thread = threading.Thread(target=LAP_main)
        LAP_thread.daemon = True
        LAP_thread.start()
    if RAC_MODE and not AUTO_COPY:
        print(f'{Fore.YELLOW}{output_message("error_RAC_disabled_autocopy", lang, moe)}{Style.RESET_ALL}')
    if TAR_MODE and not LAP_MODE:
        print(f'{Fore.YELLOW}{output_message("error_TAR_disabled_LAP", lang, moe)}{Style.RESET_ALL}')
    if SAS_MODE:
        if not AUTO_COPY:
            print(f'{Fore.YELLOW}{output_message("error_SAS_disabled_autocopy", lang, moe)}{Style.RESET_ALL}')
        if not LAP_MODE:
            print(f'{Fore.YELLOW}{output_message("error_SAS_disabled_LAP", lang, moe)}{Style.RESET_ALL}')

def input_matching():
    global lang_code_dic, LAP_match_lst_dic
    global lang, copy_to_clipboard
    global retry_flag, LAP_retry_flag

    while True:
        lang_code_dic = {
            "en": "English",
            "zh": "简体中文",
            "cht": "繁體中文",
            "jp": "日本語",
            "kor": "한국어",
            "ru": "Русский",
            "de": "Deutsch",
            "fra": "Français",
            "spa": "Español",
            "pt": "Português",
            "it": "Italiano"
        }
        matching_rows = None
        lang_switch = False
        copy_to_clipboard = AUTO_COPY

        user_input = input(f'\r\x1b[K{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}').lower()
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
                matching_rows = df[df[target_column].astype(str).str.lower().str.contains(f'^{input_pattern}$', na=False)]
            else:
                for lang_code, full_lang in lang_code_dic.items():
                    if lang_code == lang and full_lang in df.columns:
                        if lang in {"zh", "cht", "jp", "kor"}:
                            matching_rows = df[df[["English", full_lang]].apply(lambda x: x.astype(str).str.lower().str.contains(f'^{input_pattern}$', na=False)).any(axis=1)]
                            break
                        else:
                            matching_rows = df[df[full_lang].astype(str).str.lower().str.contains(f'^{input_pattern}$', na=False)]
                            break
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
                "日本語": [],
                "한국어": [],
                "Русский": [],
                "Deutsch": [],
                "Français": [],
                "Español": [],
                "Português": [],
                "Italiano": []
            }
            LAP_match_lst_dic = {
                "WF": [],
                "English": [],
                "简体中文": [],
                "繁體中文": [],
                "日本語": [],
                "한국어": [],
                "Русский": [],
                "Deutsch": [],
                "Français": [],
                "Español": [],
                "Português": [],
                "Italiano": [],
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
                global copy_to_clipboard

                if "WF" in df.columns:
                    if row["WF"] != "%":
                        wf_row = "{:.2f}".format(row["WF"])
                        wf_color = get_wf_color(float(wf_row))
                        LAP_match_lst_dic["WF"].append(f'{wf_color}{wf_row}')
                        text_row = f'{wf_color}{wf_row}{Style.RESET_ALL} - '
                    else:
                        LAP_match_lst_dic["WF"].append(row["WF"])
                        text_row = ""
                else:
                    LAP_match_lst_dic["WF"].append("%")
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
                    elif full_lang not in df.columns:
                        LAP_match_lst_dic[full_lang].append("%")

                for column in ["Shortcut(s)", "Multiword(s)"]:
                    if column in df.columns:
                        LAP_match_lst_dic[column].append(row[column])
                        if row[column] not in {"%", "-"}:
                            text_row += f' - {text_color}{row[column]}{Style.RESET_ALL}'
                    else:
                        LAP_match_lst_dic[column].append("-")

                print(text_row)

                if copy_to_clipboard:
                    for column in ["Shortcut(s)", "Multiword(s)"]:
                        if column in df.columns and row[column] not in {"%", "-"}:
                            pyperclip.copy(row[column].split(" & ")[0].lower())
                            copy_to_clipboard = False
                            break
                    if copy_to_clipboard:
                        random_AC_lang = random.choice(["简体中文", "繁體中文", "日本語", "한국어", "Русский", "Deutsch", "Français", "Español", "Português", "Italiano"])
                        for lang_code, full_lang in lang_code_dic.items():
                            if RAC_MODE and random_AC_lang in df.columns and row[random_AC_lang] != "%":
                                pyperclip.copy(row[random_AC_lang].lower())
                                copy_to_clipboard = False
                                break
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
            retry_flag = LAP_retry_flag = True
            print(f'{Fore.YELLOW}{"-" * 30}{Style.RESET_ALL}')

        else:
            if lang_switch:
                print(f'{Fore.MAGENTA}{output_message("language_switched", lang, moe)}{Style.RESET_ALL}')
            else:
                print(f'{Fore.YELLOW}{output_message("match_failed", lang, moe)}{Style.RESET_ALL}')

def LAP_main():
    global LAP_match_lst_dic
    global retry_flag, LAP_retry_flag, cooldown_time_flag, SAS_flag
    global current_cooldown_time

    LAP_match_lst_dic = {
        "WF": [],
        "English": [],
        "简体中文": [],
        "繁體中文": [],
        "日本語": [],
        "한국어": [],
        "Русский": [],
        "Deutsch": [],
        "Français": [],
        "Español": [],
        "Português": [],
        "Italiano": [],
        "Shortcut(s)": [],
        "Multiword(s)": []
    }
    player_guess_lst = []
    current_player_guess_lst = []
    del_elem_lst = []
    current_game_round = current_builder_name = current_theme_chars = current_player_guess = current_correct_theme = ""
    game_round = total_round = builder_name = theme_chars = f"{Fore.BLUE}NA"
    retry_flag = LAP_retry_flag = builder_left_flag = builder_AFK_flag = builder_unplaced_flag = correct_guess_flag = game_over_flag = False
    cooldown_time_flag = SAS_flag = False
    current_cooldown_time = 0.0
    LAP_guess_cnt = 0

    def LAP_game_info():
        game_round_color = Fore.YELLOW if game_round != total_round else Fore.RED
        print(f'\r\x1b[K{Fore.CYAN}[{game_round_color}{game_round}{Fore.CYAN}/{Fore.YELLOW}{total_round}{Fore.CYAN}] {Fore.YELLOW}{builder_name}{Fore.CYAN}({Fore.GREEN}{theme_chars}{Fore.CYAN}){Style.RESET_ALL}')
        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end="")

    try:
        while True:
            if not os.path.exists(LOG_FILE):
                print(f'{Fore.YELLOW}{output_message("error_log_file_not_found", lang, moe)}{Style.RESET_ALL}')
                break
            else:
                with open(LOG_FILE, "r", encoding="GB18030") as latest_log:
                    try:
                        log_last_lines = deque(latest_log, maxlen=2)
                        log_prev_line = log_last_lines[0]
                        log_last_line = log_last_lines[1]
                    except IndexError:
                        pass

                    COMMON_FORMAT_PREFIX = r'\[(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)\] \[Render thread/INFO\]: \[System\] \[CHAT\] '

                    search_game_round = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:Round: |回合：|ラウンド：|라운드: |Раунд: |Runde: |Manche: |Ronda: |Rodada: )(.+)/(.+)',
                        log_last_line
                    )
                    search_builder_name = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:Builder: |建筑师：|建築師：|建築家：|건축가: |Строитель: |Erbauer: |Constructeur: |Constructor: |Construtor: |Costruttore: )(.+)',
                        log_last_line
                    )
                    search_builder_left = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The owner left|The plot owner has left the game|该领地的主人离开了|領地主人已離線|領地的主人離開遊戲了|所有者が退出しました|プロットの所有者がゲームから退出しました|소유자가 나갔네요|플롯 소유자가 게임을 나갔습니다|Строитель вышел|Владелец участка покинул игру|Der Besitzer ist weg|Der Bauplatzbesitzer hat das Spiel verlassen|Le propriétaire a quitté|Le propriétaire du terrain a quitté la partie|¡El dueño salió|¡El dueño de la parcela ha abandonado el juego|O construtor saiu|O dono desta construção saiu da partida|Il proprietario è uscito|Il proprietario del lotto è uscito)',
                        log_last_line
                    )
                    search_builder_AFK = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The plot owner is AFK|该领地的主人暂时离开了|領地的主人在掛網|プロットの所有者が無操作状態です|해당 플롯의 플레이어가 자리를 비웠습니다|Хозяин участка отошёл|Der Bauplatzbesitzer ist AFK|Le propriétaire du plot est AFK|¡El dueño de la parcela está AFK|O construtor está ausente|Il proprietario del lotto è AFK)',
                        log_last_line
                    )
                    search_builder_unplaced = re.search(
                        rf"{COMMON_FORMAT_PREFIX}(?:The plot owner hasn't placed any blocks|该领地的主人尚未放置任何方块|領地的主人沒有放置任何方塊|プロットの所有者がブロックを設置していません|플롯 소유자가 아무런 블록도 설치를 하지 않았네요|Хозяин участка не поставил ни одного блока|Der Bauplatzbesitzer hat keine Blöcke platziert|Le propriétaire du plot n'a placé aucun bloc|¡El dueño de esta parcela no ha puesto ningún bloque|O construtor não colocou blocos|Il proprietario del lotto non ha piazzato blocchi)",
                        log_last_line
                    )
                    search_theme_chars = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The theme is |该主题字数为|主題為 |テーマの文字数は |이 주제는 |Количество символов в теме: |Das Thema ist |Le thème est composé de |El tema es |O tema tem |Il tema è lungo )(\d+)',
                        log_last_line
                    )
                    search_player_guess = re.search(
                        rf'{COMMON_FORMAT_PREFIX}.*?(?:Rookie|Untrained|Amateur|Apprentice|Experienced|Seasoned|Trained|Skilled|Talented|Professional|Expert|Master|#10 Builder|#[1-9] Builder|初来乍到|未经雕琢|初窥门径|学有所成|驾轻就熟|历练老成|技艺精湛|炉火纯青|技惊四座|巧夺天工|闻名于世|建筑大师|#10建筑师|#[1-9]建筑师|初來乍到|技藝生疏|初窺門徑|學徒|駕輕就熟|識途老馬|技藝精湛|爐火純青|技驚四座|巧奪天工|聞名於世|大師|#10 建築師|#[2-9] 建築師|冠絕當世|新人|一般人|アマチュア|見習|経験者|熟達者|ベテラン|熟練者|人材|職業人|専門家|マスター|#10 建築家|#[1-9] 建築家|풋내기|일반인|아마추어|견습기|경험자|숙달자|베테랑|숙련자|인재|직업인|전문가|마스터|#10 건축가|#[1-9] 건축가|Новичок|Необученный|Любитель|Ученик|Опытный|Бывалый|Обученный|Умелый|Талантливый|Профессионал|Эксперт|Мастер|Строитель #10|Строитель #[1-9]|Anfänger|Untrainiert|Lehrling|Erfahren|Trainiert|Bewandt|Talentiert|Professionell|Experte|Meister|#10 Baumeister|#[2-9] Baumeister|#1 Erbauer|Débutant|Novice|Apprenti|Expérimenté|Saisonnier|Entraîné|Compétent|Talentueux|Professionnel|Maitre|Constructeur #1|Novato|Iniciado|Aficionado|Aprendiz|Experimentado|Habilidoso|Entrenado|Talentoso|Profesional|Experto|Maestro|Constructor #10|Constructor #[1-9]|Amador|Dedicado|Veterano|Inteligente|Perito|Profissional|Experiente|Mestre|Colocação|1º colocado|Novellino|Non Allenato|Dilettante|Apprendista|Esperto|Allenato|Abile|Talentuoso|Professionista|10° Costruttore|[1-9]° Costruttore).*?: (.+)',
                        log_last_line
                    )
                    search_correct_guess = re.search(
                        rf'{COMMON_FORMAT_PREFIX}\+.*?\((?:Correct Guess|正确的猜测|正確的猜測|正確な推測|올바른 추측|Правильный ответ|Richtig erraten|Supposition Correcte|Adivinado correctamente|Palpite correto|Ipotesi Corretta)\)',
                        log_prev_line
                    )
                    search_correct_theme = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:The theme was: |主题是：|主題是：|お題は：|주제는 |Темой являлась: |Das Thema war: |Le thème était: |¡El tema fue: |O tema era |Il tema era: )(.+?)(?:!|！|이었습니다)',
                        log_last_line
                    )
                    search_game_over = re.search(
                        rf'{COMMON_FORMAT_PREFIX}(?:Want to play again|想再来一局吗|想再玩一次嗎|もう一度プレイしますか|다시 플레이하겠습니까|Хотите сыграть ещё раз|Nochmal spielen|Voulez-vous jouer à nouveau|¿Quieres jugar otra vez|Deseja jogar novamente|Vuoi giocare ancora)',
                        log_last_line
                    )
                    search_cooldown_time = re.search(
                        rf"{COMMON_FORMAT_PREFIX}(?:You must wait [1-3] seconds? in between guesses|你必须等待[1-3]秒才能再次猜测|你必須等待 [1-3] 秒後才能再次猜題|推測の間は [1-3] 秒間開ける必要があります|추측 후 [1-3]초를 기다려야 합니다|Вы должны подождать [1-3] секунд[аы] между угадываниями|Du musst [1-3] Sekunden? zwischen den Versuchen warten|Vous devez attendre [1-3] secondes? entre chaque supposition|Debes esperar [1-3] segundos? entre suposiciones|Aguarde [1-3] segundos? para dar outro palpite|Devi aspettare [1-3] second[oi] per mandare un'altra ipotesi)",
                        log_last_line
                    )

                    if LAP_retry_flag:
                        LAP_game_info()
                        LAP_retry_flag = False

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
                                "한국어": [],
                                "Русский": [],
                                "Deutsch": [],
                                "Français": [],
                                "Español": [],
                                "Português": [],
                                "Italiano": [],
                                "Shortcut(s)": [],
                                "Multiword(s)": []
                            }
                            current_theme_chars = ""
                            player_guess_lst = []
                            current_player_guess_lst = []
                            del_elem_lst = []
                            retry_flag = LAP_retry_flag = builder_left_flag = builder_AFK_flag = builder_unplaced_flag = correct_guess_flag = game_over_flag = False
                            SAS_flag = False
                            LAP_guess_cnt = 0 if game_round == 1 else LAP_guess_cnt
                            LAP_game_info()

                    if search_builder_name:
                        current_theme_chars = ""
                        game_round = total_round = builder_name = theme_chars = f"{Fore.BLUE}NA"
                        builder_name = search_builder_name.group(1)
                        if current_builder_name != builder_name:
                            current_builder_name = builder_name
                            LAP_game_info()

                    if search_builder_left and not builder_left_flag:
                        builder_left_flag = True
                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_builder_left", lang, moe)}{Style.RESET_ALL}')
                        LAP_game_info()

                    if search_builder_AFK and not builder_AFK_flag:
                        builder_AFK_flag = True
                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_builder_AFK", lang, moe)}{Style.RESET_ALL}')
                        LAP_game_info()

                    if search_builder_unplaced and not builder_unplaced_flag:
                        builder_unplaced_flag = True
                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_builder_unplaced", lang, moe)}{Style.RESET_ALL}')
                        LAP_game_info()

                    if search_theme_chars:
                        theme_chars = search_theme_chars.group(1)
                        if current_theme_chars != theme_chars:
                            current_theme_chars = theme_chars
                            LAP_game_info()

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
                                            for index, val in enumerate(normalized_value):
                                                if player_answer == val and index not in indices_to_remove:
                                                    indices_to_remove.append(index)

                                if indices_to_remove:
                                    for index in sorted(indices_to_remove, reverse=True):
                                        for key in LAP_match_lst_dic.keys():
                                            if index < len(LAP_match_lst_dic[key]):
                                                for lang_code, full_lang in lang_code_dic.items():
                                                    if lang_code == lang and key == full_lang:
                                                        if LAP_match_lst_dic[full_lang][index] not in {"%", "-"}:
                                                            del_elem_lst.append(LAP_match_lst_dic[full_lang][index])
                                                        elif index < len(LAP_match_lst_dic["English"]):
                                                            del_elem_lst.append(LAP_match_lst_dic["English"][index])

                                    del_elem_lst_seen = set()
                                    del_elem_lst_dedup = []

                                    for i in del_elem_lst:
                                        if i not in del_elem_lst_seen:
                                            del_elem_lst_seen.add(i)
                                            del_elem_lst_dedup.append(i)
                                    del_elem_lst = del_elem_lst_dedup

                                    for key in LAP_match_lst_dic.keys():
                                        LAP_match_lst_dic[key] = [elem for i, elem in enumerate(LAP_match_lst_dic[key]) if i not in indices_to_remove]

                                    separator_dic = {
                                        "zh": "、",
                                        "cht": "、",
                                        "jp": "・",
                                        "kor": ", ",
                                        "ru": ", ",
                                        "de": ", ",
                                        "fra": ", ",
                                        "spa": ", ",
                                        "pt": ", ",
                                        "it": ", ",
                                        "en": ", "
                                    }
                                    output_del_elem = separator_dic.get(lang, ", ").join(del_elem_lst)
                                    print(f'\r\x1b[K{Fore.RED}{output_message("output_LAP_guess_info", lang, moe, output_del_elem=output_del_elem)}{Style.RESET_ALL}')

                                    for i in range(len(LAP_match_lst_dic["English"])):
                                        elem_color = Fore.GREEN if elem_color_cnt%2 != 0 else ""

                                        for lang_code, full_lang in lang_code_dic.items():
                                            if lang_code == lang and full_lang != "English":
                                                elements_row = " - ".join(
                                                    f'{elem_color}{LAP_match_lst_dic[key][i]}{Style.RESET_ALL}'
                                                    for key in ["WF", "English", full_lang, "Shortcut(s)", "Multiword(s)"]
                                                    if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}
                                                )
                                                if AUTO_COPY and i == 0:
                                                    if RAC_MODE:
                                                        random_AC_lang = random.choice(["简体中文", "繁體中文", "日本語", "한국어", "Русский", "Deutsch", "Français", "Español", "Português", "Italiano"])
                                                        for key in ["Shortcut(s)", "Multiword(s)", random_AC_lang, "English"]:
                                                            if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}:
                                                                pyperclip.copy(LAP_match_lst_dic[key][i].split(" & ")[0].lower())
                                                                break
                                                    else:
                                                        for key in ["Shortcut(s)", "Multiword(s)", full_lang, "English"]:
                                                            if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}:
                                                                pyperclip.copy(LAP_match_lst_dic[key][i].split(" & ")[0].lower())
                                                                break
                                                elem_matched = True
                                                break
                                        if not elem_matched:
                                            elements_row = " - ".join(
                                                f'{elem_color}{LAP_match_lst_dic[key][i]}{Style.RESET_ALL}'
                                                for key in ["WF", "English", "Shortcut(s)", "Multiword(s)"]
                                                if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}
                                            )
                                            if AUTO_COPY and i == 0:
                                                if RAC_MODE:
                                                    random_AC_lang = random.choice(["简体中文", "繁體中文", "日本語", "한국어", "Русский", "Deutsch", "Français", "Español", "Português", "Italiano"])
                                                    for key in ["Shortcut(s)", "Multiword(s)", random_AC_lang, "English"]:
                                                        if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}:
                                                            pyperclip.copy(LAP_match_lst_dic[key][i].split(" & ")[0].lower())
                                                            break
                                                else:
                                                    for key in ["Shortcut(s)", "Multiword(s)", "English"]:
                                                        if key in df.columns and LAP_match_lst_dic[key][i] not in {"%", "-"}:
                                                            pyperclip.copy(LAP_match_lst_dic[key][i].split(" & ")[0].lower())
                                                            break

                                        elem_color_cnt += 1
                                        print(elements_row)

                                    if LAP_match_lst_dic["English"]:
                                        SAS_flag = True
                                        LAP_guess_cnt += 1
                                    else:
                                        print(f'{Fore.YELLOW}{output_message("match_failed", lang, moe)}{Style.RESET_ALL}')
                                    print(f'{Fore.YELLOW}{"-" * 30}{Style.RESET_ALL}')
                                    LAP_game_info()

                    if search_correct_guess and not correct_guess_flag:
                        correct_guess_flag = True
                        SAS_flag = False
                        print(f'\r\x1b[K{Fore.GREEN}{output_message("output_LAP_correct_guess", lang, moe)}{Style.RESET_ALL}')
                        LAP_game_info()

                    if search_correct_theme:
                        correct_theme = search_correct_theme.group(1)
                        if current_correct_theme != correct_theme:
                            current_correct_theme = correct_theme
                            correct_guess_flag = True
                            SAS_flag = False

                            print(f'\r\x1b[K{Fore.CYAN}{output_message("output_LAP_correct_theme", lang, moe, correct_theme=correct_theme)}{Style.RESET_ALL}')
                            if TAR_MODE:
                                try:
                                    if not os.path.exists(GTB_TAR_FILE):
                                        with open(GTB_TAR_FILE, "w", encoding="GB18030") as TAR_file:
                                            TAR_file.write(f'{correct_theme}\n')
                                    else:
                                        with open(GTB_TAR_FILE, "a", encoding="GB18030") as TAR_file:
                                            TAR_file.write(f'{correct_theme}\n')
                                    print(f'{Fore.GREEN}{output_message("output_TAR_theme_added", lang, moe, correct_theme=correct_theme)}{Style.RESET_ALL}')
                                except UnicodeDecodeError:
                                    print(f'{Fore.YELLOW}{output_message("error_TAR_file_decoding_failed", lang, moe)}{Style.RESET_ALL}')
                            LAP_game_info()

                    if search_game_over and not game_over_flag:
                        game_over_flag = True

                        pyperclip.copy(CUSTOM_CONTENT)
                        SAS_flag = True

                        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("output_LAP_game_over", lang, moe, LAP_guess_cnt=LAP_guess_cnt)}{Style.RESET_ALL}')
                        print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end="")

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

        time.sleep(3 - SAS_sleep_time) if cooldown_time_flag and SAS_sleep_time < 3 else ""
        time.sleep(SAS_INTERVAL)

        MC_windows[0].activate()
        pyautogui.press("t")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("delete")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        print(f'\r\x1b[K{Fore.GREEN}{output_message("output_SAS_content_sent", lang, moe)}{Style.RESET_ALL}')
    else:
        print(f'\r\x1b[K{Fore.YELLOW}{output_message("error_SAS_window_not_found", lang, moe)}{Style.RESET_ALL}')

    cooldown_time_flag = SAS_flag = False
    print(f'{Fore.RED}{output_message("input_prompt", lang, moe)}{Style.RESET_ALL}', end="")

def solver():
    global moe

    moe = MOE_MODE if MOE_MODE else False

    try:
        output_language()
        input_thesaurus()
        program_self_check()
        input_matching()
    except KeyboardInterrupt:
        print(f'\r\x1b[K{Fore.MAGENTA}{output_message("exit_program", lang, moe)}{Style.RESET_ALL}')
        exit()
    except Exception as e:
        print(f'\r\x1b[K{Fore.YELLOW}{output_message("error_exception", lang, moe, e=e)}{Style.RESET_ALL}')
        exit()

if __name__ == "__main__":
    colorama.init(autoreset=True)
    solver()
    colorama.deinit()