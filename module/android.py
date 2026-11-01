#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developer by MergenCoreSystem
# Не стал обращатся прямо в adb server, сделал код максимально простым и читаемым для новичков в python,
# вдруг это поможет в развитии скила по началу.
from module.utils import COLORS
from module.utils.banner import show_banner
import requests
import time as t
import subprocess
import webbrowser

WHSL = C = "\033[39m"
ENDL = W = "\033[0m"
REDL = R = "\033[0;31m"
GNSL = G = "\033[1;34m"
GRNL = U = "\033[32;1m"
OKNL = O = "\033[96m"
FIOL = H = "\033[95m"
OKBL = Y = "\033[93m"

page_1 = f'''
        
 {REDL}[ {GNSL}1{REDL} ] {WHSL}  Подключенные устройства            {REDL}[ {GNSL}16{REDL} ] {WHSL} Открываем геолокацию на Google Планета Земля 
 {REDL}[ {GNSL}2{REDL} ] {WHSL}  Отключить все устройства           {REDL}[ {GNSL}17{REDL} ] {WHSL} Просмотр информации об устройстве 💾 
 {REDL}[ {GNSL}3{REDL} ] {WHSL}  Подключите новое устройство        {REDL}[ {GNSL}18{REDL} ] {GNSL} Show Mac/Inet
 {REDL}[ {GNSL}4{REDL} ] {WHSL}  Доступ через {GNSL}shell                 {REDL}[ {GNSL}19{REDL} ] {WHSL} Извлечь apk из приложения
 {REDL}[ {GNSL}5{REDL} ] {WHSL}  Установка{GNSL} apk{WHSL}                      {REDL}[ {GNSL}20{REDL} ] {GNSL} Get Battery Status
 {REDL}[ {GNSL}6{REDL} ] {WHSL}  Записать видео с экрана            {REDL}[ {GNSL}21{REDL} ] {GNSL} Get Network Status
 {REDL}[ {GNSL}7{REDL} ] {WHSL}  Получить {GNSL}screenshot 💾             {REDL}[ {GNSL}22{REDL} ] {WHSL} Включение / выключение {GNSL}Wi-Fi
 {REDL}[ {GNSL}8{REDL} ] {WHSL}  Перезапуск вашего сервера          {REDL}[ {GNSL}23{REDL} ] {WHSL} Удалить пароль устройства
 {REDL}[ {GNSL}9{REDL} ] {WHSL}  Выгрузка файлов                    {REDL}[ {GNSL}24{REDL} ] {WHSL} Эмуляция нажатия клавиш
 {REDL}[ {GNSL}10{REDL} ] {WHSL} Перезагрузка устройства            {REDL}[ {GNSL}25{REDL} ] {WHSL} Получить текущую активность (Логи) 💾
 {REDL}[ {GNSL}11{REDL} ] {WHSL} Удалить приложение                 {REDL}[ {GNSL}26{REDL} ] {WHSL} Массовое подключение устройств 💾
 {REDL}[ {GNSL}12{REDL} ] {WHSL} Показать журнал устройства 💾      {REDL}[ {GNSL}27{REDL} ] {WHSL} Открыть инструкции по adb
 {REDL}[ {GNSL}13{REDL} ] {WHSL} Dump {GNSL}System Info 💾                {REDL}[ {GNSL}28{REDL} ] {GNSL} Grab wpa_supplicant
 {REDL}[ {GNSL}14{REDL} ] {WHSL} Список всех приложений             {REDL}[ {GNSL}29{REDL} ] {WHSL} Port Forwarding
 {REDL}[ {GNSL}15{REDL} ] {WHSL} Запустить приложение               {REDL}[ {GNSL}30{REDL} ] {WHSL} Получить фотографию
 
 
 {REDL}[ {GNSL}99{REDL} ] {WHSL} Обратно в меню{GNSL}            {REDL}[ {GNSL}66{REDL} ]{WHSL} Очистить консоль            {REDL}[ {GNSL}77{REDL} ]{WHSL} Отключить сервер

'''


def android_debug():
    show_banner(clear=True)
    print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
    print(f"\n{COLORS.WHSL}                             Start Android Debug Bridge server\n")
    print(f'\n{COLORS.WHSL} Внимание, обязательно отключайте adb сервер, \n используйте proxy и меняйте mac address при подключении к устройствам.\n')
    print(page_1)
    import datetime
    global path_to_file

    ip = None
    while True:
        try:
            option = input(
                f"{REDL} └──> {FIOL}Bafomёd production ──>{GNSL} Введите номер опции: {WHSL}")
        except KeyboardInterrupt:
            return

        if option == '1':
            if not ip:
                subprocess.call("adb devices -l", shell=True)
            else:
                subprocess.call("adb devices -l", shell=True)

        elif option == '2':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                subprocess.call("adb disconnect", shell=True)

        elif option == '3':
            print(f"\n Введите IP address.\n")
            try:
                ip = input(f" Android Debug Bridge {GNSL}[{REDL} connect_device {GNSL}]{ENDL}: ")
                port_device = input(f" Введите порт {GNSL}[{REDL} connect_device {GNSL}]{ENDL}: ")
                subprocess.call(f"adb tcpip '{port_device}' >> /dev/null", shell=True)
                subprocess.call(f"adb connect {ip}:{port_device}", shell=True)

            except KeyboardInterrupt:
                continue

        elif option == '4':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                subprocess.call(f"adb -s {ip} shell", shell=True)

        elif option == '5':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                 
                print(f" Введите путь к apk файлу. Пример /home/Apashe/Desktop/test.apk.\n")
                apk_location = input(f" Android Debug Bridge{GNSL}[{REDL} apk_install {GNSL}]{ENDL}:")
                subprocess.call("adb -s  " + ip + " install " + apk_location, shell=True)
                print(f" {GNSL}Apk был установлен.")

        elif option == '6':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                try:
                    print(f" Запись видео началась.")
                    print(f" Нажми ctrl+c для остановки записи.\n")
                    subprocess.call(f"adb -s {ip} shell screenrecord /sdcard/demo.mp4", shell=True)
                    print(f"\n Укажите, где вы хотите сохранить видео.\n Пример: /home/apashe/Desktop/sc.mp4\n")
                    place_location = input(f" Android Debug Bridge {GNSL}[{REDL}screen_record{GNSL}]{ENDL}:")
                    subprocess.call(f"adb -s {ip} pull /sdcard/screen.mp4 {place_location}", shell=True)
                    print(f" Видео успешно загружено.")
                    t.sleep(4)
                    print(page_1)

                except KeyboardInterrupt:
                    show_banner(clear=True)
                    print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
                    print(page_1)
                    continue  # /home/apashe/Desktop/sc.mp4

        elif option == '7':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                try:

                    save_data = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
                    filename = f'screenshot__{ip}__{save_data}'
                    path_to_file = 'report/' + filename
                    subprocess.call(f"adb -s {ip} shell screencap /sdcard/screen.png", shell=True)
                    print(f" Ожидайте происходит загрузка скриншота в папку report\n")
                    subprocess.call(f"adb -s {ip} pull /sdcard/screen.png {path_to_file}", shell=True)
                    print(f" {GNSL} Скриншот {WHSL}успешно загружен.")
                    t.sleep(4)
                    print(page_1)

                except KeyboardInterrupt:
                    show_banner(clear=True)
                    print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
                    print(page_1)
                    continue

        elif option == '8':
            print(f"\n Перезапуск сервера ADB...\n")
            subprocess.call("adb kill-server >> /dev/null", shell=True)
            subprocess.call("adb start-server >> /dev/null", shell=True)
            print(f" Сервер успешно перезагружен")
            t.sleep(4)
            print(page_1)

        elif option == '9':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                print(f" Введите местоположение файла на устройстве.\n Пример: /sdcard/DCIM/demo.mp4 \n")
                file_location = input(f" Android Debug Bridge {GNSL}[{REDL} file_pull {GNSL}]{ENDL}:")
                 
                print(f" Пример: /home/apashe/Desktop\n Введите, где вы хотите сохранить файл.\n")
                place_location = input(f" Android Debug Bridge {GNSL}[{REDL} file_pull {GNSL}]{ENDL}:")
                subprocess.call(f"adb -s {ip} pull {file_location} {place_location}", shell=True)
                print(page_1)

        elif option == '10':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                subprocess.call(f"adb -s {ip} reboot ", shell=True)
                print(f" Устройство будет перезагруженно, ожидайте 1 минуту ")
                t.sleep(4)
                print(page_1)

        elif option == '11':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                print(f" Введите название pack_name \n")
                package_name = input(f" Android Debug Bridge {GNSL}[{REDL} app_delete {GNSL}]{ENDL}:")
                subprocess.call(f"adb -s {ip} unistall {package_name}", shell=True)

        elif option == '12':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                try:
                    print(f"\n Нажми ctrl+c для остановки.\n")
                    t.sleep(4)
                    subprocess.call(f'adb -s {ip} logcat ', shell=True)

                except KeyboardInterrupt:
                    show_banner(clear=True)
                    print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
                    print(page_1)
                    continue

        elif option == '13':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                try:
                    print(f"\n{COLORS.REDL}  Нажми ctrl+c для остановки.\n")
                    t.sleep(4)
                    subprocess.call(f"adb -s {ip} shell dumpsys", shell=True)

                except KeyboardInterrupt:
                    show_banner(clear=True)
                    print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
                    print(page_1)
                    continue

        elif option == '14':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            subprocess.call(f"adb -s {ip} shell pm list packages -f", shell=True)

        elif option == '15':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
             
            print(f"  Введите название приложения.\n")
            package_name = input(f" Android Debug Bridge {GNSL}[{REDL} Запуск приложения {GNSL}]{ENDL}:")
            subprocess.call(f"adb -s {ip} shell monkey -p " + package_name + " -v 500", shell=True)

        elif option == '16':
            option = input(f"\n{COLORS.FIOL} Открываем геолокацию на карте (y/n)?:{COLORS.REDL} ")
            show_banner(clear=True)
            if option == "y":
                data = requests.get(
                    "http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
                resp = data.json()
                if resp["status"] == "fail":
                    print(f'{COLORS.WHSL} Дополнительная информация\n')

                print(f"{COLORS.WHSL} Latitude:{COLORS.FIOL} " + str(resp["lat"]))
                print(f"{COLORS.WHSL} Longitude:{COLORS.FIOL} " + str(resp["lon"]))
                print(f"{COLORS.WHSL} Принадлежность к мобильному оператору:{COLORS.FIOL} " + str(resp["mobile"]))
                print(f"{COLORS.GNSL} Прокси:{COLORS.FIOL} " + str(resp["proxy"]))
                webbrowser.open(f"https://earth.google.com/web/search/{resp['lat']}+{resp['lon']}")
                print(f"\n{COLORS.REDL} Status: " + resp["status"])

            elif option == "n":
                return

        elif option == '17':
            show_banner(clear=True)
            subprocess.call(f'adb shell getprop | grep -e"model\|version.sdk\|manufacturer\|hardware\|platform\|revision\|serialno\|product.name\|brand"', shell=True)
            print(page_1)

        elif option == '18':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                subprocess.call(f"adb -s {ip} shell ip address show wlan0", shell=True)

        elif option == '19':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
             
            print(f" Введите название apk.\n")
            package_name = input(f" Package_name - Android Debug Bridge: ")
            subprocess.call(f"adb -s {ip} shell pm path " + package_name, shell=True)
             
            print(f" Введите путь к apk на устойстве.\n")
            path = input(" Android Debug Bridge: ")
             
            print(f" Введите место хранения apk.\n")
            location = input(f" Android Debug Bridge pull_apk:")
            subprocess.call(f"adb -s {ip} pull {path} {location}", shell=True)
            t.sleep(5)
            print(page_1)

        elif option == '20':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                subprocess.call(f"adb -s {ip} shell dumpsys battery", shell=True)

        elif option == '21':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                subprocess.call(f"adb -s {ip} shell netstat", shell=True)

        elif option == '22':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                print(f" Чтобы снова включить WiFi, устройство должно быть подключено.")
                 
                on_off = input(f"{GNSL}   [{REDL} + {GNSL}]{WHSL} Хотите включить/выключить WiFi on/off{REDL} :")
                if on_off == 'off':
                    command = " shell svc wifi disable"
                else:
                    command = " shell svc wifi enable"
                subprocess.call(f"adb -s {ip} {command}", shell=True)

        elif option == '23':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                 
                print(f"****************** REMOVING PASSWORD ******************")
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/gesture.key'", shell=True)
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/locksettings.db'", shell=True)
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/locksettings.db-wal'", shell=True)
                subprocess.call(f"adb -s {ip} shell su 0 'rm /data/system/locksettings.db-shm'", shell=True)
                print(f"****************** REMOVING PASSWORD ******************")

        elif option == '24':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")

            print(f'''
 {GNSL}[ {REDL}0{GNSL} ]  {WHSL}Кнопка_UNKNOWN       {GNSL}[ {REDL}21{GNSL} ]{WHSL}  Кнопка_DPAD_LEFT      {GNSL}[ {REDL}42{GNSL} ]{WHSL}  Кнопка_N            {GNSL}[ {REDL}63{GNSL} ]{WHSL}  Кнопка_SYM 
 {GNSL}[ {REDL}1{GNSL} ]  {WHSL}Кнопка_MENU          {GNSL}[ {REDL}22{GNSL} ]{WHSL}  Кнопка_DPAD_RIGHT     {GNSL}[ {REDL}43{GNSL} ]{WHSL}  Кнопка_O            {GNSL}[ {REDL}64{GNSL} ]{WHSL}  Кнопка_EXPLORER
 {GNSL}[ {REDL}2{GNSL} ]  {WHSL}Кнопка_SOFT_RIGHT    {GNSL}[ {REDL}23{GNSL} ]{WHSL}  Кнопка_DPAD_CENTER    {GNSL}[ {REDL}44{GNSL} ]{WHSL}  Кнопка_P            {GNSL}[ {REDL}65{GNSL} ]{WHSL}  Кнопка_ENVELOPE
 {GNSL}[ {REDL}3{GNSL} ]  {WHSL}Кнопка_HOME          {GNSL}[ {REDL}24{GNSL} ]{WHSL}  Кнопка_VOLUME_UP      {GNSL}[ {REDL}45{GNSL} ]{WHSL}  Кнопка_Q            {GNSL}[ {REDL}66{GNSL} ]{WHSL}  Кнопка_ENTER
 {GNSL}[ {REDL}4{GNSL} ]  {WHSL}Кнопка_BACK          {GNSL}[ {REDL}25{GNSL} ]{WHSL}  Кнопка_VOLUME_DOWN    {GNSL}[ {REDL}46{GNSL} ]{WHSL}  Кнопка_R            {GNSL}[ {REDL}67{GNSL} ]{WHSL}  Кнопка_DEL
 {GNSL}[ {REDL}5{GNSL} ]  {WHSL}Кнопка_CALL          {GNSL}[ {REDL}26{GNSL} ]{WHSL}  Кнопка_POWER          {GNSL}[ {REDL}47{GNSL} ]{WHSL}  Кнопка_S            {GNSL}[ {REDL}68{GNSL} ]{WHSL}  Кнопка_GRAVE
 {GNSL}[ {REDL}6{GNSL} ]  {WHSL}Кнопка_ENDCALL       {GNSL}[ {REDL}27{GNSL} ]{WHSL}  Кнопка_CAMERA         {GNSL}[ {REDL}48{GNSL} ]{WHSL}  Кнопка_T            {GNSL}[ {REDL}69{GNSL} ]{WHSL}  Кнопка_MINUS
 {GNSL}[ {REDL}7{GNSL} ]  {WHSL}Кнопка_0             {GNSL}[ {REDL}28{GNSL} ]{WHSL}  Кнопка_CLEAR          {GNSL}[ {REDL}49{GNSL} ]{WHSL}  Кнопка_U            {GNSL}[ {REDL}70{GNSL} ]{WHSL}  Кнопка_EQUALS
 {GNSL}[ {REDL}8{GNSL} ]  {WHSL}Кнопка_1             {GNSL}[ {REDL}29{GNSL} ]{WHSL}  Кнопка_A              {GNSL}[ {REDL}50{GNSL} ]{WHSL}  Кнопка_V            {GNSL}[ {REDL}71{GNSL} ]{WHSL}  Кнопка_LEFT_BRACKET
 {GNSL}[ {REDL}9{GNSL} ]  {WHSL}Кнопка_2             {GNSL}[ {REDL}30{GNSL} ]{WHSL}  Кнопка_B              {GNSL}[ {REDL}51{GNSL} ]{WHSL}  Кнопка_W            {GNSL}[ {REDL}72{GNSL} ]{WHSL}  Кнопка_RIGHT_BRACKET
 {GNSL}[ {REDL}10{GNSL} ] {WHSL}Кнопка_3             {GNSL}[ {REDL}31{GNSL} ]{WHSL}  Кнопка_C              {GNSL}[ {REDL}52{GNSL} ]{WHSL}  Кнопка_X            {GNSL}[ {REDL}73{GNSL} ]{WHSL}  Кнопка_BACKSLASH
 {GNSL}[ {REDL}11{GNSL} ] {WHSL}Кнопка_4             {GNSL}[ {REDL}32{GNSL} ]{WHSL}  Кнопка_D              {GNSL}[ {REDL}53{GNSL} ]{WHSL}  Кнопка_Y            {GNSL}[ {REDL}74{GNSL} ]{WHSL}  Кнопка_SEMICOLON
 {GNSL}[ {REDL}12{GNSL} ] {WHSL}Кнопка_5             {GNSL}[ {REDL}33{GNSL} ]{WHSL}  Кнопка_E              {GNSL}[ {REDL}54{GNSL} ]{WHSL}  Кнопка_Z            {GNSL}[ {REDL}75{GNSL} ]{WHSL}  Кнопка_APOSTROPHE
 {GNSL}[ {REDL}13{GNSL} ] {WHSL}Кнопка_6             {GNSL}[ {REDL}34{GNSL} ]{WHSL}  Кнопка_F              {GNSL}[ {REDL}55{GNSL} ]{WHSL}  Кнопка_COMMA        {GNSL}[ {REDL}76{GNSL} ]{WHSL}  Кнопка_SLASH
 {GNSL}[ {REDL}14{GNSL} ] {WHSL}Кнопка_7             {GNSL}[ {REDL}35{GNSL} ]{WHSL}  Кнопка_G              {GNSL}[ {REDL}56{GNSL} ]{WHSL}  Кнопка_PERIOD       {GNSL}[ {REDL}77{GNSL} ]{WHSL}  Кнопка_AT
 {GNSL}[ {REDL}15{GNSL} ] {WHSL}Кнопка_8             {GNSL}[ {REDL}36{GNSL} ]{WHSL}  Кнопка_H              {GNSL}[ {REDL}57{GNSL} ]{WHSL}  Кнопка_ALT_LEFT     {GNSL}[ {REDL}78{GNSL} ]{WHSL}  Кнопка_NUM
 {GNSL}[ {REDL}16{GNSL} ] {WHSL}Кнопка_9             {GNSL}[ {REDL}37{GNSL} ]{WHSL}  Кнопка_I              {GNSL}[ {REDL}58{GNSL} ]{WHSL}  Кнопка_ALT_RIGHT    {GNSL}[ {REDL}79{GNSL} ]{WHSL}  Кнопка_HEADSETHOOK
 {GNSL}[ {REDL}17{GNSL} ] {WHSL}Кнопка_STAR          {GNSL}[ {REDL}38{GNSL} ]{WHSL}  Кнопка_J              {GNSL}[ {REDL}59{GNSL} ]{WHSL}  Кнопка_SHIFT_LEFT   {GNSL}[ {REDL}80{GNSL} ]{WHSL}  Кнопка_FOCUS
 {GNSL}[ {REDL}18{GNSL} ] {WHSL}Кнопка_POUND         {GNSL}[ {REDL}39{GNSL} ]{WHSL}  Кнопка_K              {GNSL}[ {REDL}60{GNSL} ]{WHSL}  Кнопка_SHIFT_RIGHT  {GNSL}[ {REDL}81{GNSL} ]{WHSL}  Кнопка_PLUS
 {GNSL}[ {REDL}19{GNSL} ] {WHSL}Кнопка_DPAD_UP       {GNSL}[ {REDL}40{GNSL} ]{WHSL}  Кнопка_L              {GNSL}[ {REDL}61{GNSL} ]{WHSL}  Кнопка_TAB          {GNSL}[ {REDL}82{GNSL} ]{WHSL}  Кнопка_MENU
 {GNSL}[ {REDL}20{GNSL} ] {WHSL}Кнопка_DPAD_DOWN     {GNSL}[ {REDL}41{GNSL} ]{WHSL}  Кнопка_M              {GNSL}[ {REDL}62{GNSL} ]{WHSL}  Кнопка_SPACE        {GNSL}[ {REDL}83{GNSL} ]{WHSL}  Кнопка_NOTIFICATION
 ''')
            print(f" Введите номер кнопки.\n")
            num = input(f" Android Debug Bridge {GNSL}[{REDL} Кнопка {GNSL}]{ENDL}: ")
            subprocess.call(f"adb -s {ip} shell input keyevent {num}", shell=True)
            print(f" Вы активировали кнопку")
            t.sleep(4)
            print(page_1)

        elif option == '25':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:
                try:
                    print(f' Для остановки нажми ctrl + c')
                    t.sleep(4)
                    subprocess.call(f"adb -s {ip} shell dumpsys activity", shell=True)

                except KeyboardInterrupt:
                    show_banner(clear=True)
                    print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
                    print(page_1)
                    continue

        elif option == "26":
            try:
                print(f" Пример пути: /home/Apashe/Desktop/test.txt\n")
                path_to_ips = input(f" Введите путь к вашему txt файлу с IP адресами:")
            except KeyboardInterrupt:
                continue

            with open(path_to_ips, "r") as f:
                ip_adb_addresses = f.read().splitlines()

            for ip_address in ip_adb_addresses:
                subprocess.call(f" adb connect {ip_address}:{5555}", shell=True)

        elif option == '27':
            urls = [
                "http://android-tip.com/soveti_i_poleznoe/77-adb-dlya-chaynikov-chast-1.html",
                "https://irongamers.ru/forum/faq/izuchaem-android-desjat-osnovnyh-komand-adb-i-fastboot-kotorye-vy-dolzhny-znat-d",
                "https://docs.microsoft.com/ru-ru/dual-screen/android/emulator/adb",
                "https://softandroid.net/2020/01/05/adb-%D0%B8%D0%BB%D0%B8-android-debug-bridge-%D0%BE%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D1%8F%D1%8E-%D0%BD%D0%B0-%D0%BF%D0%B0%D0%BB%D1%8C%D1%86%D0%B0%D1%85-%D1%87%D1%82%D0%BE-%D1%8D%D1%82%D0%BE-%D0%B7/",
                "https://www.youtube.com/watch?v=QOXmNDXDWhM",
            ]
            for url in urls:
                webbrowser.open(url)
                print(page_1)

        elif option == '28':
            try:
                print(f" Введите, где вы хотите сохранить файл.\n")
                location = input(f" Android Debug Bridge {GNSL}[{REDL} wpa_grub {GNSL}]{ENDL}:")
                subprocess.call(f"adb -s {ip} shell su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'",
                                shell=True)
                subprocess.call(f"adb -s {ip} pull /sdcard/wpa_supplicant.conf {location}", shell=True)

            except KeyboardInterrupt:
                if not ip:
                    print(f"\n{REDL} Нет подключенных устройств к серверу.\n")

        elif option == '29':
            if not ip:
                print(f"\n{REDL} Нет подключенных устройств к серверу.\n")
            else:

                print(f" Введите порт на устройстве.\n")
                port_device = input(f" Android Debug Bridge port_device: ")

                print(f" Введите порт для пересылки.\n")
                forward_port = input(" Android Debug Bridge forward_port: ")
                subprocess.call(f"adb -s {ip} forward tcp:" + port_device + " tcp:" + forward_port, shell=True)

        elif option == '30':
            subprocess.call(f"adb -s {ip} shell input keyevent {27}", shell=True)
            save_data = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
            filename = f'photo__{ip}__{save_data}'
            path_to_file = 'report/' + filename
            subprocess.call(f"adb -s {ip} shell screencap /sdcard/screen.png", shell=True)
            print(f"\n Ожидайте происходит загрузка скриншота в папку report\n Может быть такое что на устройстве нет камеры,\n как у smartTV\n")
            subprocess.call(f"adb -s {ip} pull /sdcard/screen.png {path_to_file}", shell=True)

        elif option == '66':
            show_banner(clear=True)
            print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
            print(page_1)

        elif option == '77':
            subprocess.call("adb disconnect >> /dev/null", shell=True)
            subprocess.call("adb kill-server >> /dev/null", shell=True)
            show_banner(clear=True)
            print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
            print(f' Сервер android debug отключен')
            print(page_1)

        elif option == '99':
            show_banner(clear=True)
            print(f'\n{COLORS.WHSL}                             Рабочее окно консоли очищено\n')
            return

        else:
            print(page_1)
