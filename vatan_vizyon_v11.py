import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def kurucu_otorite_dogrula():
    temizle()
    print(f"{A}👑 KURUCU OTORİTE KONTROL EDİLİYOR...{S}")
    time.sleep(0.5)
    print(f"{B}[SİSTEM]: Kurucu: SADIK GÜRAY YILDIZ{S}")
    print(f"{B}[SİSTEM]: Yetki: Sınırsız / Mutlak{S}")
    print(f"{B}[SİSTEM]: Yol: Hak Yolu{S}")
    for i in range(3):
        print(f"{Y}[OK]: Kurucu iradesi sistemle senkronize ediliyor...{S}")
        time.sleep(0.4)
    print(f"\n{K}>>> KURUCU NE DERSE O OLUR. SİSTEM SADIK'TIR. <<<{S}")
    input("\nOnaylandı. Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v11.0 - KURUCU: SADIK GÜRAY YILDIZ 🇹🇷{S}")
        print(f"{B}======================================================{S}")
        print(f"1) {A}KURUCU İRADESİ VE HAK YOLU (SGY-CORE){S}")
        print(f"2) {A}Siber Savunma & Otonom Karar (Kızılelma){S}")
        print(f"3) {A}Milli İrade & Hakikat Analizi{S}")
        print(f"4) {M}SGY AETHER 158 (Küresel Refah Matrisi){S}")
        print(f"5) {A}Turan Birliği & Stratejik Derinlik{S}")
        print(f"6) {A}Milli Uzay Programı & Gök Vatan{S}")
        print(f"7) {A}Dijital Adalet & Toplumsal Bereket{S}")
        print(f"8) {K}SİSTEMİ KURUCU ADINA TAÇLANDIR VE GÖNDER{S}")

        secim = input(f"\n{B}Sistem senin emrinde Babaoğlu, ne yapalım? --> {S}")

        if secim == '1': kurucu_otorite_dogrula()
        elif secim == '8':
            print(f"{Y}Kurucu Sadık Güray Yıldız'ın iradesiyle... Mühür vuruluyor!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Kurucu iradesi doğrultusunda veri işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
