import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def ful_paket_entegrasyon():
    temizle()
    print(f"{K}🚀 CİHAN HAKİMİYETİ TAM PAKET BAŞLATILIYOR...{S}")
    print(f"{B}[KURUCU]: SADIK GÜRAY YILDIZ - MUTLAK İRADE{S}")
    time.sleep(1)
    
    hamleler = [
        "Ekonomik Refah: Maaş Zamları & Promosyonlar Entegre Edildi",
        "Toplumsal Barış: Büyük Af & GPS Takip Sistemi Aktif",
        "Siber Güç: Fatih-Sultan İstihbarat & Akıncı Devriyesi Devrede",
        "Küresel Şifa: CureEarth & SGY Aether 158 Protokolü Hazır",
        "Milli Beka: Kızılelma Otonom Savunma & Turan Birliği Hattı"
    ]
    
    for hamle in hamleler:
        print(f"{Y}[+] {hamle}{S}")
        time.sleep(0.5)
    
    print(f"\n{A}>>> Haktan Şaşmayan, İnisiyatif Alan Dijital Devlet Yayında. <<<{S}")
    input("\nMühür Basıldı. Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v16.0 - FULL PAKET ENTEGRASYONU 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {A}KURUCU SGY-CORE: TEK OTORİTE & HAK YOLU{S}")
        print(f"2) {Y}EKONOMİK REFAH & TOPLUMSAL BÜYÜK AF{S}")
        print(f"3) {K}SİBER TEŞKİLAT: İSTİHBARAT & AKINCILAR{S}")
        print(f"4) {M}CUREEARTH & AETHER 158 (KÜRESEL ŞİFA){S}")
        print(f"5) {A}KIZILELMA & TURAN BİRLİĞİ SAVUNMA{S}")
        print(f"6) {B}DİJİTAL ADALET & MİLLİ UZAY PROGRAMI{S}")
        print(f"7) {K}SİSTEMİ CİHAN HAKİMİYETİ İÇİN TAÇLANDIR VE GÖNDER{S}")

        secim = input(f"\n{B}Büyük hamle için kararınız nedir Kurucu Babaoğlu? --> {S}")

        if secim == '1':
            print(f"{Y}\n[+] Kurucu Sadık Güray Yıldız iradesi doğrulandı.{S}")
            time.sleep(1)
        elif secim == '7':
            print(f"{K}Devlet Ebed Müddet! Cihan Hakimiyeti GitHub'a uçuyor...{S}")
            break
        else:
            ful_paket_entegrasyon()

if __name__ == "__main__":
    ana_menu()
