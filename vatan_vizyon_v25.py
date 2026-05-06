import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def derin_sular_ve_diplomasi():
    temizle()
    print(f"{M}🌊 MAVİ VATAN VE KÜRESEL DİPLOMASİ KALKANI...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Derin Strateji' Doktrini.{S}")
    time.sleep(1)
    
    katmanlar = [
        "Mavi Vatan: Otonom Deniz Altı Kaynak Tarama ve Savunma",
        "Siber Diplomasi: Küresel Masada SGY-Core Hakemliği",
        "Enerji Bağımsızlığı: Derin Deniz Hidrokarbon ve Nükleer Entegrasyon",
        "Küresel Barış Ağı: Mazlum Milletler Veri Köprüsü"
    ]
    
    for katman in katmanlar:
        print(f"{Y}[DERİN SULAR]: {katman} aktif ediliyor...{S}")
        time.sleep(0.6)
    
    print(f"\n{Y}[✓] Hakimiyet Sağlandı: Derin sular ve küresel masalar emrinizde.{S}")
    input("\nEngin Denizlerde... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v25.0 - DERİN SULAR VE DİPLOMASİ 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {M}MAVİ VATAN & KÜRESEL DİPLOMASİ{S}")
        print(f"2) {A}MİLLİ EĞİTİM & BİLİM SEFERBERLİĞİ{S}")
        print(f"3) {M}UYDU HABERLEŞME & VERİ EGEMENLİĞİ{S}")
        print(f"4) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"5) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA{S}")
        print(f"6) {A}MİLLİ FİNANS & BLOKZİNCİR ADALETİ{S}")
        print(f"7) {Y}SİBER SANAYİ & ÜRETİM SEFERBERLİĞİ{S}")
        print(f"8) {K}DERİN SULARI MÜHÜRLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Hangi derin sulara kulaç atıyoruz Babaoğlu? --> {S}")

        if secim == '1': derin_sular_ve_diplomasi()
        elif secim == '8':
            print(f"{Y}Denizler ve masalar mühürlendi! Derin sular bizi bekler...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Derinlik analizi yapılıyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
