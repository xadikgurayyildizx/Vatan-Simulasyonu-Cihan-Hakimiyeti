import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def cureearth_operasyonu():
    temizle()
    print(f"{Y}🌍 CUREEARTH KÜRESEL İYİLEŞME VE ŞİFA OPERASYONU...{S}")
    print(f"{B}[VİZYON]: Küresel refahın sevgi ve barış içerisinde tesisi.{S}")
    time.sleep(1)
    hedefler = ["Sağlıklı Yaşam Erişimi", "Küresel Bereket Dağıtımı", "Sürdürülebilir Eko-Sistem", "Gönül Köprüleri Tesisi"]
    for hedef in hedefler:
        print(f"{B}[+] {hedef} katmanı SGY-Core ile senkronize ediliyor...{S}")
        time.sleep(0.4)
    print(f"\n{Y}[✓] CureEarth Aktif: İnsanlık için şifa ve adalet devrede.{S}")
    input("\nŞifa olsun. Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v13.0 - CUREEARTH & SGY-CORE 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {Y}CUREEARTH (Küresel İyileşme & Şifa Modülü){S}")
        print(f"2) {K}FATİH-SULTAN SİBER İSTİHBARAT AĞI{S}")
        print(f"3) {A}KURUCU İRADESİ: SADIK GÜRAY YILDIZ (HAK YOLU){S}")
        print(f"4) {M}SGY AETHER 158 (Küresel Refah Protokolü){S}")
        print(f"5) {A}KIZILELMA Otonom Harekat (Gök Vatan){S}")
        print(f"6) {A}Turan Birliği & Stratejik Derinlik{S}")
        print(f"7) {A}Milli Uzay Programı & Dijital Adalet{S}")
        print(f"8) {K}SİSTEMİ NİHAİ VİZYONLA TAÇLANDIR VE GÖNDER{S}")

        secim = input(f"\n{B}Emriniz nedir Kurucu Babaoğlu? --> {S}")

        if secim == '1': cureearth_operasyonu()
        elif secim == '8':
            print(f"{Y}CureEarth şifası ve Kurucu Sadık'ın iradesiyle... Mühür vuruldu!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Vizyon katmanları Kurucu adına işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
