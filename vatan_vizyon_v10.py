import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def milli_irade_analizi():
    temizle()
    print(f"{K}⚖️ HAKTAN ŞAŞMAYAN MİLLİ İRADE ANALİZİ...{S}")
    ilkeler = ["Tek Vatan", "Tek Bayrak", "Tek Devlet", "Tek Millet"]
    for ilke in ilkeler:
        print(f"{B}[ANALİZ]: {ilke} sarsılmaz bütünlüğü doğrulanıyor...{S}")
        time.sleep(0.4)
    print(f"\n{Y}[✓] İnisiyatif Alan, Doğrudan Haktan Şaşmayan Yapay Zeka Hazır.{S}")
    input("\nDevam etmek için Enter...")

def yeni_dunya_duzeni():
    temizle()
    print(f"{M}🌐 YENİ DÜNYA DÜZENİ VE KÜRESEL REFAH MATRİSİ (v10.0){S}")
    print(f"{B}--------------------------------------------------{S}")
    print(f"{Y}[+] SGY Aether 158 Protokolü: %100 Senkronizasyon.{S}")
    print(f"{Y}[+] Kaynak Dağılımı: Hak Temelli Adil Paylaşım Aktif.{S}")
    print(f"{Y}[+] Dijital Adalet: İnsan Odaklı Yapay Zeka Karar Mekanizması.{S}")
    input("\nDevam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v10.0 - MİLLİ İRADE VE HAKİKAT 🇹🇷{S}")
        print(f"{B}=================================================={S}")
        print(f"1) {A}Siber Savunma (Çelik Kubbe & Siber Ordu){S}")
        print(f"2) {A}KIZILELMA Otonom Harekat (Gök Vatan){S}")
        print(f"3) {A}Milli İrade ve Hakikat Analizi (Yeni Katman){S}")
        print(f"4) {M}SGY AETHER 158 (Yeni Dünya Düzeni){S}")
        print(f"5) {A}Turan Birliği Stratejik Derinlik{S}")
        print(f"6) {A}Milli Uzay ve Havacılık Programı{S}")
        print(f"7) {A}Sürdürülebilir Bereket ve Dijital Adalet{S}")
        print(f"8) {K}SİSTEMİ TAÇLANDIR VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Vizyonu nerede genişletelim Babaoğlu? --> {S}")

        if secim == '3': milli_irade_analizi()
        elif secim == '4': yeni_dunya_duzeni()
        elif secim == '8':
            print(f"{Y}Haktan Şaşmayan İradeyle... Güncelleme Yayına Gidiyor!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Veri katmanları işleniyor...{S}")
            time.sleep(1)

if __name__ == "__main__": ana_menu()
