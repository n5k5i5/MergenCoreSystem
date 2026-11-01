import os
import time
import webbrowser
from platform import system
from module.utils import COLORS

# banners
from module.utils.ban import (
    page_1, page_14, page_3, page_6, page_10,
    page_13, page_28,
    page_42, page_5,
)
from module.utils.banner import show_banner



def clear_screen():
    if system() == "Linux":
        os.system("clear")
    if system() == "Windows":
        os.system("cls")


def osint():
    import os
    os.system("printf '\033]2;OSAN 🇸🇮 \a'")
    global option
    while True:
        print(page_10)
        choice = None
        while True:
            try:
                user_input = input(
                    f"{COLORS.REDL} └──> {COLORS.FIOL}Bafomёd production ──>{COLORS.GNSL} Введите номер опции: {COLORS.WHSL}")
                print()
            except KeyboardInterrupt:
                return

            if len(user_input) == 0:
                break

            try:
                choice = int(user_input)
            except ValueError:
                print(f"{COLORS.REDL}Неверный ввод!{COLORS.ENDL}")
            else:
                break

        if choice is None:
            continue

        if choice == 1:
            import requests
            import os
            import json
            import os
            from ipwhois import IPWhois

            ip = input(f' Введите IP address: ')
            clear_screen()
            from ipwhois import IPWhois
            from pprint import pprint

            whois = IPWhois(ip)
            result = whois.lookup_whois()
            pprint(result)

            Agent = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/44.0.2403.157 Safari/537.36'}

            try:
                req = requests.get('https://sonar.omnisint.io/reverse/' + ip, headers=Agent).text
                parse = json.loads(req)
                print(f"[#] Reverse {ip} > [{str(len(parse))} Domain]")
                for sampah in parse:
                    hapus = sampah.replace("www.", "").replace('error:Invalid IPv4 address', '').replace('api.',
                                                                                                         '').replace(
                        'cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace(
                        'cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace(
                        'ns2.', '').replace('ns3.', '').replace('ns4.', '').replace('autodiscover.', '')

            except:
                print(f'[#] Reverse {ip} > Error')

        elif choice == 2:
            show_banner(clear=True)
            from module.domain import run
            run()

        elif choice == 3:
            from module.phonenumber import phone_number
            ph = input(f"{COLORS.REDL} └──>{COLORS.GNSL} 🔎 Введите номер телефона:{COLORS.WHSL} ")
            show_banner(clear=True)
            phone_number(ph)
            time.sleep(1)

        elif choice == 4:
            clear_screen()
            print(page_42)
            option = input(f"{COLORS.REDL} └──> {COLORS.WHSL} Введите номер опции: {COLORS.GNSL}")
            if option == "1":
                os.system(f'sudo apt install exif')
                filename = input(f" {COLORS.REDL}└──> {COLORS.WHSL} Укажите путь до файла: {COLORS.GNSL}")
                show_banner(clear=True)
                os.system(f'exif {filename}')

            elif option == "2":
                from module.metadata import pdf
                pdf_filename = input(f'\n {COLORS.WHSL}Укажите пожалуйста путь до фотографии:{COLORS.GNSL} ')
                print(f'')
                pdf(pdf_filename)

            elif option == "99":
                print(page_10)
                show_banner(clear=True)

        elif choice == 5:
            from module.reverseimagesearch import reverseimagesearch
            clear_screen()
            print(page_6)
            option = input(f" {COLORS.REDL} └──> {COLORS.WHSL} Введите номер опции: {COLORS.GNSL}")
            if option == "2":
                urls = [
                    "https://search4faces.com",
                    "https://findclone.ru",
                    "https://tineye.com",
                    "https://pimeyes.com/en",
                    "https://carnet.ai",
                ]
                for url in urls:
                    webbrowser.open(url)
                show_banner(clear=True)
                print(f'{COLORS.WHSL} Сайты открыты, приятного розыска')

            elif option == "1":
                print(f"\n {COLORS.GNSL} Пример пути: /home/mergencore/Desktop/deanon.png\n")
                img = input(f" {COLORS.REDL} └──> {COLORS.GNSL}Укажите путь до фотографии :")
                reverseimagesearch(img)
                print(f'{COLORS.WHSL} Выполнение запроса, ожидайте\n')
                show_banner(clear=True)
                print(f'{COLORS.WHSL} Данные открыты в браузере')

            elif option == "99":
                print(page_10)
                show_banner(clear=True)

        elif choice == 6:
            show_banner(clear=True)
            from module.macaddress import maclookup
            mac = input(f"\n{COLORS.REDL} └──>{COLORS.WHSL} Введите mac address: ")
            maclookup(mac)

        elif choice == 7:
            from module.host import location
            show_banner(clear=True)
            location()

        elif choice == 8:
            show_banner(clear=True)
            print(page_28)
            input1 = input(f"{COLORS.REDL} └──> {COLORS.WHSL} Введите номер опции: {COLORS.GNSL}")
            if input1 == "1":
                from module.host import wiki
                wiki()

            elif input1 == "2":
                from module.Information_services import information_menu
                information_menu()

            elif input1 == "3":
                show_banner(clear=True)
                print(f' Мини Wikipedia открыта')
                webbrowser.open('https://map.malfrats.industries')

            elif input1 == "4":
                show_banner(clear=True)
                print(f' Файл с закладками лежит в папке database,\n')
                print(f' импортируйте эти закладки в браузер, в настройках браузера')

            elif input1 == "99":
                show_banner(clear=True)

        elif choice == 9:
            show_banner(clear=True)
            from module.utils.identity import identity
            identity()
            print(f' Сайты для генерация фотографий для социальный сетей')
            option = input(f"\n{COLORS.FIOL} Открываем в браузере? y/n: ")
            print('')
            if option == "y":
                urls = [
                    "https://thispersondoesnotexist.com/",
                    "https://generated.photos/faces",
                ]
                for url in urls:
                    webbrowser.open(url)

        elif choice == 10:
            clear_screen()
            print(page_1)

        elif choice == 11:
            show_banner(clear=True)
            print(page_3)
            option = input(f"{COLORS.REDL} └──> {COLORS.WHSL} Введите номер опции: {COLORS.GNSL}")
            if option == "1":
                os.system("git clone https://github.com/MergenCoreSystem/osint-info")
                time.sleep(1)

            elif choice == "99":
                show_banner(clear=True)

        elif choice == 12:
            from module.wizard import userfull
            print(f'\n{COLORS.FIOL} By Soxoj')
            username = input(f'{COLORS.WHSL} Введите имя пользователя для поиска{COLORS.REDL}: ')
            userfull(username)

        elif choice == 13:
            clear_screen()          
            print(page_5)
            option = input(f"{COLORS.REDL} └──>{COLORS.WHSL} Выберите опцию: ")
            if option == "1":
                pass

            elif option == "2":
                urls = [
                    "https://btc.com/",
                    "https://www.blockchain.com/explorer",
                    "https://live.blockcypher.com/",
                    "https://tokenview.com/en/",
                    "https://www.walletexplorer.com/",
                    "https://bitinfocharts.com/",
                ]
                for url in urls:
                    webbrowser.open(url)
                show_banner(clear=True)
                print(f"\n Сайты открыты")
                
            elif option == "3":
                urls = [
                    "https://bitcoinwhoswho.com/",
                    "https://www.bitcoinabuse.com/",
                    "https://www.walletexplorer.com/",
                    "https://intelx.io/tools?tab=bitcoin",
                ]
                for url in urls:
                    webbrowser.open(url)
                show_banner(clear=True)
                print(f"\n Сайты открыты")
                
                
            elif option == "4":
                urls = [
                    "https://crystalblockchain.com/",
                    "https://www.chainalysis.com/",
                    "https://ciphertrace.com/",
                    "https://amlbot.com/",
                    "https://learnmeabitcoin.com/tools/path/",
                ]
                for url in urls:
                    webbrowser.open(url)
                show_banner(clear=True)
                print(f"\n Сайты открыты")
                
                
            elif option == "5":
                show_banner(clear=True)
                print(page_cryptocu)
                
                
            elif option == "6":
                urls = [
                    "https://blocks.wizb.it/",
                    "https://oxt.me/",
                ]
                for url in urls:
                    webbrowser.open(url)
                show_banner(clear=True)
                print(f"\n Сайты открыты")
                
            elif option == "7":
                urls = [
                    "https://vk.com/@tomhunter-pogovorim-ob-identifikacii-kriptovalutnyh-koshelkov",
                    "https://oxt.me/",
                ]
                for url in urls:
                    webbrowser.open(url)
                show_banner(clear=True)
                print(f"\n Сайты открыты")   
                
            elif option == "99":
                show_banner(clear=True)

        elif choice == 14:
            from module.chmodan import showdam
            show_banner(clear=True)
            print(page_14)
            option = input(f" {COLORS.REDL} └──> {COLORS.WHSL} Введите номер опции: {COLORS.GNSL}")
            if option == "1":
                showdam()
                osint()

            elif option == "2":
                from module.utils.information_services_data import page_shodan
                show_banner(clear=True)
                print(page_shodan)

            elif option == "99":
                print(page_10)
                show_banner(clear=True)

        elif choice == 16:
            from mergencore import api
            clear_screen()
            print(page_13)
            for i in api:
                if api[i]:
                    print(f' {COLORS.WHSL}Токен {i} :{COLORS.GNSL} Активирован ✅')
                else:
                    print(f' {COLORS.WHSL}Токен {i} :{COLORS.REDL} Добавьте API token ❌')

        elif choice == 99:
            show_banner(clear=True)
            from module.utils.killing import restart
            restart()

        elif choice == 88:
            show_banner(clear=True)
            print(page_40)

        elif choice == 66:
            show_banner(clear=True)
            print(
                f'\n{COLORS.WHSL}                             Рабочее окно программы очищено\n')

        elif choice == 00:
            from module.utils.killing import kill
            kill()


        elif choice == 16:
            from module.android import android_debug
            android_debug()
            
        else:
            show_banner(clear=True)
            print(f"{COLORS.WHSL} Неверный ввод опции, хотите больше опций ? Приобритайте PRO версию")


# if __name__ == '__main__':
#     try:
#         mytagigelik()
#     except KeyboardInterrupt:
#         os.system("clear")
#         print(f'{COLORS.WHSL} Неверный ввод')

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MODULES_PATH = os.path.join(PROJECT_PATH, 'module')
