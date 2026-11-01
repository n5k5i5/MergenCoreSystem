# -*- coding: utf-8 -*-

LANGUAGES = {
    'TR': {
        'welcome': 'MergenCoreSystem - Gelişmiş OSINT Konsoluna Hoş Geldiniz!',
        'license_ok': 'Lisans durumu: AKTİF (Doğrulandı).',
        'license_fail': 'Hata: Geçersiz lisans anahtarı veya licence.json bulunamadı!',
        'help_title': 'Kullanılabilir Global Komutlar:',
        'help_use': 'Belirtilen istihbarat modülünü aktif eder.',
        'help_set': 'Aktif modüle ait parametre/API değerlerini atar.',
        'help_show': 'Modülleri (`show modules`) veya parametreleri (`show options`) listeler.',
        'help_run': 'Ayarlanan parametrelerle modülü tetikler.',
        'help_back': 'Mevcut modül bağlamından çıkıp küresel alana döner.',
        'help_lang': 'Arayüz dilini değiştirir (Seçenekler: TR, EN, RU).',
        'help_exit': 'Konsolu güvenli bir şekilde kapatır.',
        'unknown_cmd': 'Bilinmeyen komut: "{cmd}". Yardım için "help" yazın.',
        'no_active_mod': 'Aktif modül seçilmedi. Önce "use <modül>" komutunu çalıştırın.',
        'mod_activated': 'Modül bağlamına geçildi: {name}',
        'mod_not_found': 'Belirtilen isimde bir OSINT modülü bulunamadı!',
        'param_set': '[+] {param} parametresi -> "{val}" olarak güncellendi.',
        'missing_param': 'Başarısız: Gerekli zorunlu parametre eksik: {param}',
        'running_mod': '[*] {mod} modülü toplanan API ve hedef verileriyle başlatılıyor...',
        'lang_changed': 'Sistem dili başarıyla Türkçe olarak ayarlandı.'
    },
    'EN': {
        'welcome': 'Welcome to MergenCoreSystem - Advanced OSINT Console!',
        'license_ok': 'License status: ACTIVE (Verified).',
        'license_fail': 'Error: Invalid license key or licence.json missing!',
        'help_title': 'Available Global Commands:',
        'help_use': 'Activates the specified intelligence module.',
        'help_set': 'Assigns parameter or API key values to the active module.',
        'help_show': 'Lists modules (`show modules`) or configuration (`show options`).',
        'help_run': 'Triggers the active module with configured options.',
        'help_back': 'Exits the current module context and returns to global prompt.',
        'help_lang': 'Changes the console language (Options: TR, EN, RU).',
        'help_exit': 'Exits the platform securely.',
        'unknown_cmd': 'Unknown command: "{cmd}". Type "help" for assistance.',
        'no_active_mod': 'No active module context. Use "use <module>" first.',
        'mod_activated': 'Switched to module context: {name}',
        'mod_not_found': 'Specified OSINT module could not be found!',
        'param_set': '[+] Parameter {param} updated to -> "{val}".',
        'missing_param': 'Failed: Required missing parameter: {param}',
        'running_mod': '[*] Launching module {mod} with collected target details...',
        'lang_changed': 'System language successfully changed to English.'
    },
    'RU': {
        'welcome': 'Добро пожаловать в MergenCoreSystem - Расширенную Консоль OSINT!',
        'license_ok': 'Статус лицензии: АКТИВЕН (Подтверждено).',
        'license_fail': 'Ошибка: Неверный лицензионный ключ или отсутствует licence.json!',
        'help_title': 'Доступные глобальные команды:',
        'help_use': 'Активирует указанный модуль разведки.',
        'help_set': 'Назначает значения параметров или API-ключей для модуля.',
        'help_show': 'Выводит список модулей (`show modules`) или опций (`show options`).',
        'help_run': 'Запускает активный модуль с настроенными параметрами.',
        'help_back': 'Выходит из контекста текущего модуля в глобальное меню.',
        'help_lang': 'Изменяет язык интерфейса консоли (Доступно: TR, EN, RU).',
        'help_exit': 'Безопасно завершает работу платформы.',
        'unknown_cmd': 'Неизвестная команда: "{cmd}". Введите "help" для справки.',
        'no_active_mod': 'Нет активного модуля. Сначала выполните команду "use <модуль>".',
        'mod_activated': 'Переключено на контекст модуля: {name}',
        'mod_not_found': 'Указанный модуль OSINT не найден!',
        'param_set': '[+] Параметр {param} обновлен на -> "{val}".',
        'missing_param': 'Ошибка: Отсутствует обязательный параметр: {param}',
        'running_mod': '[*] Запуск модуля {mod} с собранными данными цели...',
        'lang_changed': 'Язык системы успешно изменен на Русский.'
    }
}

class Localizer:
    def __init__(self, default_lang='TR'):
        self.current_lang = default_lang if default_lang in LANGUAGES else 'TR'

    def set_language(self, lang_code):
        if lang_code.upper() in LANGUAGES:
            self.current_lang = lang_code.upper()
            return True
        return False

    def translate(self, key, **kwargs):
        text = LANGUAGES[self.current_lang].get(key, f"[{key}]")
        if kwargs:
            return text.format(**kwargs)
        return text
