# 1. Proje ana dizinini ve alt kırılımları oluşturun
mkdir -p MergenCoreSystem/config MergenCoreSystem/core
cd MergenCoreSystem

# 2. __init__.py boş paket dosyalarını yerleştirin
touch config/__init__.py core/__init__.py

# 3. Yukarıdaki Parça A, B, C ve D kod bloklarını sırasıyla ilgili dosyalara kaydedin:
# (nano, vim veya tercih ettiğiniz bir editör ile dosyaları oluşturun)
# nano config/localization.py
# nano core/completer.py
# nano core/shell.py
# nano mergen.py

# 4. Ana çalıştırma dosyasına çalıştırma yetkisi verin
chmod +x mergen.py

# 5. Kendi sisteminizi Metasploit arayüzü ve Sekme Tamamlama (Tab) konforuyla başlatın!
python3 mergen.py
