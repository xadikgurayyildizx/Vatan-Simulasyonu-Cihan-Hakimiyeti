import os, time, random, sys

KIRMIZI = "\033[1;31m"; YESIL = "\033[1;32m"; MAVI = "\033[1;34m"
ALTIN = "\033[1;33m"; BEYAZ = "\033[1;37m"; SIFIR = "\033[0m"

def temizle(): os.system('clear')

def reis_mesaji():
    temizle()
    print(f"{KIRMIZI}╔══════════════════════════════════════════════════════════╗")
    print(f"║     T.C. CUMHURBAŞKANI RECEP TAYYİP ERDOĞAN MESAJI       ║")
    print(f"╚══════════════════════════════════════════════════════════╝{SIFIR}")
    mesaj = ["\n'Aziz milletim...'", "\n'Türkiye Yüzyılı hedeflerimize siber dünyada da yürüyoruz.'", "\n'Durmak yok, yola devam!'"]
    for satir in mesaj: print(f"{BEYAZ}{satir}{SIFIR}"); time.sleep(0.7)
    input(f"\n{ALTIN}Vatan sağ olsun! Devam...{SIFIR}")

def ana_menu():
    while True:
        temizle()
        print(f"{KIRMIZI}🇹🇷 VATAN SİMÜLASYONU PANELİ 🇹🇷{SIFIR}")
        print(f"\n1) Reis'in Mesajı\n2) Ata'nın Mesajı\n3) Savunma Durumu\n4) Çıkış")
        secim = input(f"\n{ALTIN}Seçiminiz --> {SIFIR}")
        if secim == '1': reis_mesaji()
        elif secim == '4': break

if __name__ == "__main__": ana_menu()
