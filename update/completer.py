# -*- coding: utf-8 -*-
import readline

class MergenCompleter:
    def __init__(self, shell):
        self.shell = shell
        self.global_commands = ['help', 'show', 'use', 'set', 'run', 'back', 'lang', 'exit', 'quit']
        self.show_options = ['modules', 'options']
        self.languages = ['TR', 'EN', 'RU']

    def complete(self, text, state):
        buffer = readline.get_line_buffer()
        tokens = buffer.strip().split()
        
        if not buffer:
            return (self.global_commands + [None])[state]

        # İlk komut yazılıyorsa global komutları tamamla
        if len(tokens) == 0 or (len(tokens) == 1 and not buffer.endswith(' ')):
            results = [c for c in self.global_commands if c.startswith(text)]
            return (results + [None])[state]

        base_cmd = tokens[0].lower()

        # "use <tab>" -> Modülleri listele
        if base_cmd == 'use':
            mod_list = list(self.shell.modules.keys())
            results = [m for m in mod_list if m.startswith(text)]
            return (results + [None])[state]

        # "show <tab>" -> modules veya options tamamla
        if base_cmd == 'show':
            results = [s for s in self.show_options if s.startswith(text)]
            return (results + [None])[state]

        # "lang <tab>" -> Dilleri tamamla
        if base_cmd == 'lang':
            results = [l for l in self.languages if l.startswith(text.upper())]
            return (results + [None])[state]

        # "set <tab>" -> Aktif modül parametrelerini veya Global API'leri tamamla
        if base_cmd == 'set':
            possible_params = list(self.shell.global_api_registry.keys())
            if self.shell.active_module:
                possible_params += list(self.shell.modules[self.shell.active_module].keys())
            results = [p for p in possible_params if p.startswith(text.upper())]
            return (results + [None])[state]

        return None
