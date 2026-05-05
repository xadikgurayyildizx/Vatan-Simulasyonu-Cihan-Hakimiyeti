import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def milli_finans_sistemi():
    temizle()
    print(f"{A}💰 MİLLİ FİNANS VE BLOKZİNCİR ADALETİ AKTİF EDİLDİ...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Hazine-i Amire' Protokolü.{S}")
    time.sleep(1)
    birimler = [
        "SGY-Coin: Enflasyona Endeksli Milli Dijital Varlık",
        "Blokzincir Adaleti: %100 Şeffaf Devlet Harcamaları",
        "Otonom Hazine: Yolsuzluğa ve İsrafa Karşı Sıfır Tolerans",
        "Küresel Takas Sistemi: SGY Aether 158 Uyumlu Dış Ticaret"
    ]
    for birim in birimler:
        print(f"{Y}[FİNANS]: {birim} zincire işleniyor...{S}")
        time.sleep(0.5)
    print(f"\n{Y}[✓] Finansal Egemenlik Sağlandı: Ekonomik prangalar kırıldı.{S}")
    input("\nBereketle ve Güvenle... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v20.0 - FİNANSAL EGEMENLİK 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {A}MİLLİ FİNANS & BLOKZİNCİR (SGY-Coin & Adalet){S}")
        print(f"2) {Y}SİBER SANAYİ (Üretim & Fabrikalar){S}")
        print(f"3) {M}GERÇEKLİK KÖPRÜSÜ (HAYALDEN HAKİKATE){S}")
        print(f"4) {A}ETİK VE FETİH KURULU (ALTIN ÇAĞ YÖNETİMİ){S}")
        print(f"5) {Y}REFAH VE ADALET (ZAM & AF & GPS){S}")
        print(f"6) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"7) {M}SGY AETHER 158 (KÜRESEL REFAH){S}")
        print(f"8) {K}FİNANSAL MÜHRÜ BAS VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Ekonomik mühür için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': milli_finans_sistemi()
        elif secim == '8':
            print(f"{Y}Para birimi mühürlendi, ekonomi sağlama alındı! Gönderiliyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Finansal veriler blokzincire işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
