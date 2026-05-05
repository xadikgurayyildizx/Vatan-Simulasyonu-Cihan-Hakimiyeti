import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def kuantum_savunma_hatti():
    temizle()
    print(f"{M}🌌 KUANTUM SİBER ORDU VE UZAY SAVUNMA HATTI AKTİF...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Gök Vatan' Doktrini.{S}")
    time.sleep(1)
    birimler = [
        "Kuantum Şifreleme: Sızılamaz Haberleşme Ağı",
        "Uydu Savunma Katmanı: Yörüngesel Siber Kalkan",
        "Derin Uzay İzleme: Küresel Tehdit Erken Uyarı",
        "SGY-Sat: Tam Bağımsız Milli Uzay Veri Ağı"
    ]
    for birim in birimler:
        print(f"{A}[GÖK VATAN]: {birim} devreye alınıyor...{S}")
        time.sleep(0.5)
    print(f"\n{Y}[✓] Arş İleri: Uzay ve Siber Uzayda Mutlak Hakimiyet Sağlandı.{S}")
    input("\nYıldızların Ötesine... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v21.0 - UZAY VE KUANTUM GÜCÜ 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA{S}")
        print(f"2) {A}MİLLİ FİNANS & BLOKZİNCİR (SGY-Coin){S}")
        print(f"3) {Y}SİBER SANAYİ & ÜRETİM SEFERBERLİĞİ{S}")
        print(f"4) {M}GERÇEKLİK KÖPRÜSÜ (HAYALDEN HAKİKATE){S}")
        print(f"5) {A}ETİK VE FETİH KURULU (ALTIN ÇAĞ YÖNETİMİ){S}")
        print(f"6) {Y}REFAH VE ADALET (ZAM & AF & GPS){S}")
        print(f"7) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"8) {K}UZAY SAVUNMA MÜHRÜNÜ GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Arş ileri hamlesi için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': kuantum_savunma_hatti()
        elif secim == '8':
            print(f"{Y}Yıldızlar mühürlendi, Gök Vatan emniyette! Gönderiliyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Kuantum veriler işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
