import os, time, random

# Renkler
K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def otonom_harekat():
    temizle()
    print(f"{K}🚀 KIZILELMA OTONOM HAREKAT SİSTEMİ DEVREDE...{S}")
    birimler = ["ANKA-3", "KIZILELMA", "TB-3", "HÜRJET"]
    for birim in birimler:
        print(f"{B}[SİSTEM]: {birim} otonom uçuş verileri senkronize ediliyor...{S}")
        time.sleep(0.4)
    print(f"\n{Y}[✓] Gök Vatan ve Mavi Vatan 7/24 Koruma Altında.{S}")
    input("\nDevam etmek için Enter...")

def aether_158_gelismis():
    temizle()
    print(f"{M}🌐 SGY AETHER 158 - KÜRESEL REFAH VE DENGE MATRİSİ{S}")
    print(f"{B}--------------------------------------------------{S}")
    protokoller = ["Adil Paylaşım", "Sürdürülebilir Barış", "Dijital Eşitlik", "Teknolojik Etik"]
    for p in protokoller:
        print(f"{Y}[+] {p} Protokolü 158 madde ile harmanlanıyor...{S}")
        time.sleep(0.5)
    print(f"\n{A}>>> Küresel Refah SGY Aether v9.0 ile Güvence Altında. <<<{S}")
    input("\nDevam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v9.0 - KIZILELMA & AETHER 🇹🇷{S}")
        print(f"{B}=================================================={S}")
        print(f"1) {A}Siber Savunma & Çelik Kubbe{S}")
        print(f"2) {A}KIZILELMA Otonom Harekat (Gök Vatan){S}")
        print(f"3) {A}Turan Birliği Stratejik Derinlik{S}")
        print(f"4) {M}SGY AETHER 158 (Küresel Refah Protokolü){S}")
        print(f"5) {A}Nükleer Güç & Enerji Bağımsızlığı{S}")
        print(f"6) {A}Milli Uzay Programı (Ay Misyonu){S}")
        print(f"7) {A}Dijital Adalet & Toplumsal Bereket{S}")
        print(f"8) {K}SİSTEMİ GÜNCELLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Hangi vizyonu genişletelim Babaoğlu? --> {S}")

        if secim == '2': otonom_harekat()
        elif secim == '4': aether_158_gelismis()
        elif secim == '8':
            print(f"{Y}Devlet Ebed Müddet! Güncelleme GitHub'a uçuyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Veri katmanları işleniyor...{S}")
            time.sleep(1)

if __name__ == "__main__": ana_menu()
