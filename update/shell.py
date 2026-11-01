# -*- coding: utf-8 -*-
import sys
import json
import os
import readline
from config.localization import Localizer
from core.completer import MergenCompleter

R = '\033[31m'
G = '\033[32m'
B = '\033[34m'
M = '\033[35m'
C = '\033[36m'
W = '\033[0m'

class MergenShell:
    def __init__(self):
        self.loc = Localizer('TR')
        self.active_module = None
        
        self.global_api_registry = {
            "SHODAN": "",
            "GMAP_G": "",
            "IP_API": "",
            "NGROK_AUTH": "",
            "VIRUSTOTAL_API": "",
            "CMS_DETECT_API": "",
            "PHONE_APIS": "80fd4720becad81c5d608c7d4b2f"
        }

        self.modules = {
            'osint/ip_whois': {'TARGET_IP': ''},
            'osint/domain_analyzer': {'DOMAIN': '', 'USE_VIRUSTOTAL': 'FALSE'},
            'osint/phone_lookup': {'PHONE_NUMBER': ''},
            'social/big_brother': {'TEMPLATE': 'telegram', 'TUNNEL_PORT': '8080'},
            'osint/username_crawler': {'USERNAME': ''},
            'osint/shodan_scanner': {'QUERY': ''}
        }

    def print_banner(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        banner = f"""
{M}    ,_,   {C} __  __                                   {R}  ____                  
{M}   (o,o)  {C}|  \/  | ___ _ __ __ _  ___ _ __          {R} / ___|___  _ __ ___ 
{M}   {{` '}}  {C}| |\/| |/ _ \ '__/ _` |/ _ \ '_ \  _____  {R}| |   / _ \| '__/ _ \\
{M}   "-"    {C}| |  | |  __/ | | (_| |  __/ | | ||_____| {R}| |__| (_) | | |  __/
{M}          {C}|_|  |_|\___|_|  \__, |\___|_| |_|        {R} \____\___/|_|  \___|
{C}                           |___/                    {W} Framework v1.0.0
        """
        print(banner)
        print(f"[{G}+{W}] {self.loc.translate('license_ok')}")
        print(f"[{B}*{W}] {self.loc.translate('welcome')}\n")

    def execute_command(self, cmd_line):
        tokens = cmd_line.strip().split()
        if not tokens:
            return True

        base_cmd = tokens[0].lower()

        if base_cmd in ['exit', 'quit']:
            return False

        elif base_cmd == 'help':
            print(f"\n{M}{self.loc.translate('help_title')}{W}")
            print("-" * 60)
            commands = [
                ('help', 'Yardım menüsünü gösterir.'),
                ('lang <TR/EN/RU>', self.loc.translate('help_lang')),
                ('show modules', 'Modülleri listeler.'),
                ('show options', 'Seçenekleri listeler.'),
                ('use <modül>', self.loc.translate('help_use')),
                ('set <param> <val>', self.loc.translate('help_set')),
                ('run', self.loc.translate('help_run')),
                ('back', self.loc.translate('help_back'))
            ]
            for c, d in commands:
                print(f"  {G}{c:<20}{W} : {d}")
            print()

        elif base_cmd == 'lang' and len(tokens) > 1:
            if self.loc.set_language(tokens[1]):
                print(f"[{G}+{W}] {self.loc.translate('lang_changed')}")

        elif base_cmd == 'show' and len(tokens) > 1:
            sub = tokens[1].lower()
            if sub == 'modules':
                for m in self.modules: print(f"  {G}{m}{W}")
            elif sub == 'options':
                print(f"\n{C}Global API Credentials:{W}")
                for k, v in self.global_api_registry.items():
                    print(f"  {k:<18} -> {G if v else R}{v if v else '[NOT SET]'}{W}")
                if self.active_module:
                    print(f"\n{C}Module Options ({self.active_module}):{W}")
                    for p, v in self.modules[self.active_module].items():
                        print(f"  {p:<18} -> {G if v else W}{v if v else '[REQUIRED]'}{W}")
                print()

        elif base_cmd == 'use' and len(tokens) > 1:
            if tokens[1] in self.modules:
                self.active_module = tokens[1]
                print(f"[{G}+{W}] {self.loc.translate('mod_activated', name=tokens[1])}")
            else:
                print(f"[{R}-{W}] {self.loc.translate('mod_not_found')}")

        elif base_cmd == 'set' and len(tokens) > 2:
            param = tokens[1].upper()
            val = " ".join(tokens[2:])
            if param in self.global_api_registry:
                self.global_api_registry[param] = val
                print(f"[{G}+{W}] {self.loc.translate('param_set', param=param, val=val)}")
            elif self.active_module and param in self.modules[self.active_module]:
                self.modules[self.active_module][param] = val
                print(f"[{G}+{W}] {self.loc.translate('param_set', param=param, val=val)}")

        elif base_cmd in ['run', 'exploit']:
            if not self.active_module:
                print(f"[{R}-{W}] {self.loc.translate('no_active_mod')}")
            else:
                missing = [p for p, v in self.modules[self.active_module].items() if v == '']
                if missing:
                    for m in missing: print(f"[{R}-{W}] {self.loc.translate('missing_param', param=m)}")
                else:
                    print(f"[{B}*{W}] {self.loc.translate('running_mod', mod=self.active_module)}")

        elif base_cmd == 'back':
            self.active_module = None

        return True

    def start_loop(self):
        # Readline kütüphanesine tab tamamlama motorunu bağlıyoruz
        completer = MergenCompleter(self)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        
        self.print_banner()
        running = True
        while running:
            try:
                prompt = f"mergen ({R}{self.active_module}{W}) > " if self.active_module else "mergen > "
                cmd_line = input(prompt)
                running = self.execute_command(cmd_line)
            except (KeyboardInterrupt, EOFError):
                break
