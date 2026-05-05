import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def refah_ve_ekonomi():
    temizle()
    print(f"{Y}💰 REFAH VE ALIM GÜCÜ YÜKSELTME OPERASYONU...{S}")
    print(f"{B}[SİSTEM]: Emekli ve SSK maaş zammı + Promosyonlar tanımlanıyor...{S}")
    time.sleep(1)
    print(f"{Y}[✓] Enflasyon %5'e çekildi. Alım gücü 3 kat artırıldı.{S}")
    print(f"{Y}[✓] Refah düzeyi yükseldikçe suç oranı %80 azaldı.{S}")
    input("\nHalkın duasıyla... Devam...")

def buyuk_af_ve_denetim():
    temizle()
    print(f"{M}⚖️ GENEL AF VE İKİNCİ ŞANS PROTOKOLÜ...{S}")
    print(f"{B}[KURUCU]: 'Herkes bir şansı hak eder.'{S}")
    time.sleep(1)
    print(f"{K}[UYARI]: GPS Takip ve Dijital Parmak İzi Sistemi Aktif Ediliyor...{S}")
    for i in range(1, 4):
        print(f"{B}[DENETİM]: Tahliye edilen grup {i} izleme altına alındı.{S}")
        time.sleep(0.5)
    print(f"\n{Y}[✓] Güvenli Toplum: Hem özgürlük hem denetim bir arada.{S}")
    input("\nAdaletle... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v15.0 - REFAH VE ADALET GÜNCESİ 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {Y}EKONOMİK REFAH (Zam, Promosyon & Alım Gücü){S}")
        print(f"2) {M}BÜYÜK AF & DİJİTAL DENETİM (GPS & Parmak İzi){S}")
        print(f"3) {A}KURUCU İRADESİ: SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"4) {Y}CUREEARTH (Küresel Şifa & Refah Dağıtımı){S}")
        print(f"5) {K}FATİH-SULTAN İSTİHBARAT & SİBER AKINCI{S}")
        print(f"6) {M}SGY AETHER 158 (Adil Dünya Düzeni){S}")
        print(f"7) {A}KIZILELMA & TURAN BİRLİĞİ SAVUNMA{S}")
        print(f"8) {K}REFAH VE ADALET MÜHRÜNÜ GITHUB'A BAS{S}")

        secim = input(f"\n{B}Halkın ve devletin refahı için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': refah_ve_ekonomi()
        elif secim == '2': buyuk_af_ve_denetim()
        elif secim == '8':
            print(f"{Y}Refahla yükselen, adaletle korunan bir vatan... Gönderiliyor!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Kurucu adına toplumsal veriler işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
