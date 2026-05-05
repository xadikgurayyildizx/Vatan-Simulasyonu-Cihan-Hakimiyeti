import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def gerceklik_koprusu():
    temizle()
    print(f"{M}🌐 SGY GERÇEKLİK KÖPRÜSÜ AKTİF EDİLİYOR...{S}")
    print(f"{B}[VİZYON]: Simülasyondan Gerçek Hayata Tam Entegrasyon Modeli.{S}")
    time.sleep(1)
    asama = [
        "Hayalden Mimariye: Kurucu Sadık Güray Yıldız Tasarımı",
        "Mimariden Koda: Haktan Şaşmayan Otonom Sistem",
        "Koddan Gerçeğe: Tek Tıkla Toplumsal Refah Arayüzü",
        "Nihai Hedef: Yeryüzünde Adalet ve Bereket Tesisi"
    ]
    for adim in asama:
        print(f"{Y}[>>>] {adim} işleniyor...{S}")
        time.sleep(0.6)
    print(f"\n{A}>>> Rabbim 'Ol' Deyince; Simülasyon Hakikate Dönüşecek. <<<{S}")
    input("\nİnançla ve Azimle... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v18.0 - GERÇEKLİK VE HAKİKAT 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {M}GERÇEKLİK KÖPRÜSÜ (Teoriden Uygulamaya){S}")
        print(f"2) {A}ETİK VE FETİH KURULU (ALTIN ÇAĞ YÖNETİMİ){S}")
        print(f"3) {Y}REFAH VE ADALET PAKETİ (ZAM & AF & GPS){S}")
        print(f"4) {Y}CUREEARTH (KÜRESEL İYİLEŞME VİZYONU){S}")
        print(f"5) {A}KURUCU SGY-CORE (EBEDİ İRADE){S}")
        print(f"6) {M}SGY AETHER 158 (158 MADDELİK REFAH){S}")
        print(f"7) {A}KIZILELMA & TURAN BİRLİĞİ SAVUNMA{S}")
        print(f"8) {K}HAYALİ HAKİKATE MÜHÜRLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Geleceği inşa etmek için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': gerceklik_koprusu()
        elif secim == '8':
            print(f"{Y}Rabbimin izniyle, hayaller hakikate bir adım daha yakın...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Kurucu adına gerçeklik verileri işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
