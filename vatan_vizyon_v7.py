import os, time, random

# Renkler
K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def aether_protokol_yukle():
    temizle()
    print(f"{M}🌐 SGY AETHER 158 PROTOKOLÜ BAŞLATILIYOR...{S}")
    for i in range(1, 159):
        if i % 20 == 0:
            print(f"{B}[AETHER]: Madde {i} sisteme entegre edildi...{S}")
            time.sleep(0.2)
    print(f"\n{Y}[✓] 158 Madde Aktif: Küresel Refah Matrisi Tamamlandı.{S}")
    time.sleep(1)

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU & SGY AETHER v7.0 🇹🇷{S}")
        print(f"{B}--------------------------------------------{S}")
        print(f"1) {A}SİBER SAVUNMA VE ÇELİK KUBBE{S}")
        print(f"2) {A}ENERJİ VE NÜKLEER GÜÇ{S}")
        print(f"3) {A}TURAN BİRLİĞİ VE ORTAK PAZAR{S}")
        print(f"4) {M}SGY AETHER 158 (KÜRESEL REFAH){S}")
        print(f"5) {A}DİJİTAL ADALET VE ETİK{S}")
        print(f"6) {A}UZAY VE HAVACILIK{S}")
        print(f"7) {A}GÖNÜL COĞRAFYASI VE BARIŞ{S}")
        print(f"8) {K}SİSTEMİ KAPAT VE GÖNDER{S}")

        secim = input(f"\n{B}Hangi vizyonu tetikleyelim Babaoğlu? --> {S}")

        if secim == '4':
            aether_protokol_yukle()
            print(f"{Y}\n[+] Kaynaklar adil dağıtılıyor...\n[+] SGY Aether: 'Dünya Herkese Yeter' Modu Aktif.{S}")
            input("\nDevam...")
        elif secim == '8':
            print(f"{K}Devlet Ebed Müddet!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Veri katmanı işleniyor...{S}")
            time.sleep(1)

if __name__ == "__main__": ana_menu()
