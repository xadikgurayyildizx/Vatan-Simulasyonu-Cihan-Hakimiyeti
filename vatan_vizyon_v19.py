import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def siber_sanayi_seferberligi():
    temizle()
    print(f"{Y}🏭 SİBER SANAYİ VE MİLLİ ÜRETİM HAMLESİ...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Üretim Ordusu' Devrede.{S}")
    time.sleep(1)
    fabrikalar = [
        "Otonom Çelik Fabrikaları (Yapay Zeka Destekli)",
        "Milli Mikroçip Üretim Tesisleri (SGY-Logic)",
        "Yüksek Verimli Siber Tarım Havzaları",
        "Savunma Sanayi Siber-Fiziksel Entegrasyonu"
    ]
    for birim in fabrikalar:
        print(f"{B}[ÜRETİM]: {birim} tam kapasiteye alınıyor...{S}")
        time.sleep(0.5)
    print(f"\n{Y}[✓] Üretim Seferberliği Aktif: Dışa bağımlılık %0.1'e çekildi.{S}")
    input("\nBolluk ve Bereketle... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v19.0 - SANAYİ VE ÜRETİM GÜCÜ 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {Y}SİBER SANAYİ (Milli Üretim & Fabrikalar){S}")
        print(f"2) {M}GERÇEKLİK KÖPRÜSÜ (HAYALDEN HAKİKATE){S}")
        print(f"3) {A}ETİK VE FETİH KURULU (ALTIN ÇAĞ YÖNETİMİ){S}")
        print(f"4) {Y}REFAH VE ADALET PAKETİ (ZAM & AF & GPS){S}")
        print(f"5) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"6) {M}SGY AETHER 158 (KÜRESEL REFAH){S}")
        print(f"7) {A}KIZILELMA & TURAN BİRLİĞİ SAVUNMA{S}")
        print(f"8) {K}SANAYİ HAMLESİNİ MÜHÜRLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Üretim seferberliği için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': siber_sanayi_seferberligi()
        elif secim == '8':
            print(f"{Y}Fabrikalar çalışıyor, çarklar dönüyor! Mühür basıldı...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Üretim ve sanayi verileri işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
