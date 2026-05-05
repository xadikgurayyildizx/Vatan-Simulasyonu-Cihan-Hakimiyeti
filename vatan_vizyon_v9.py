import os, time, random

# Renk Matrisi
K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def otonom_karar(birim):
    temizle()
    print(f"{K}🚀 KIZILELMA OTONOM KARAR MEKANİZMASI AKTİF...{S}")
    print(f"{B}[SİSTEM]: {birim} birimi için tehdit ve fırsat analizi yapılıyor...{S}")
    time.sleep(1)
    skor = random.randint(85, 100)
    print(f"{Y}[BAŞARILI]: Milli Karar Skoru: %{skor}{S}")
    print(f"{B}[KARAR]: Yerli ve milli algoritmalarla en uygun rota belirlendi.{S}")
    time.sleep(1.5)

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU & KIZILELMA v9.0 🇹🇷{S}")
        print(f"{M}🌀 SGY AETHER 158 PROTOKOLÜ ENTEGRE EDİLDİ{S}")
        print(f"{B}=================================================={S}")
        print(f"1) {A}Siber Savunma (Çelik Kubbe - Otonom){S}")
        print(f"2) {A}Kızılelma Stratejik Karar Destek{S}")
        print(f"3) {A}Turan Birliği & Dijital İpekyolu{S}")
        print(f"4) {M}SGY Aether 158: Küresel Refah Dağıtımı{S}")
        print(f"5) {A}Uzay ve Gök Vatan Savunması{S}")
        print(f"6) {A}Fail-Safe: Hata Önleyici Protokoller{S}")
        print(f"7) {A}Milli Enerji ve Füzyon Matrisi{S}")
        print(f"8) {K}SİSTEMİ GÜNCELLE VE GITHUB'A FIRLAT{S}")

        secim = input(f"\n{B}Hangi birimi yönetelim Babaoğlu? --> {S}")

        if secim == '1': otonom_karar("SİBER SAVUNMA")
        elif secim == '2': otonom_karar("STRATEJİK PLANLAMA")
        elif secim == '4':
            print(f"{M}\n[AETHER]: 158 madde üzerinden refah transferi yapılıyor...{S}")
            time.sleep(1); input("\nTamamlandı...")
        elif secim == '6':
            print(f"{Y}\n[HATA ÖNLEYİCİ]: Sistem kendi hatalarını denetliyor. Durum: Kusursuz.{S}")
            time.sleep(1); input("\nTamamlandı...")
        elif secim == '8':
            print(f"{Y}Milli teknoloji hamlesi güncelleniyor...{S}")
            break
        else:
            print(f"\n{B}[BİLGİ]: Bu katman otonom olarak çalışmaya devam ediyor.{S}")
            time.sleep(1)

if __name__ == "__main__": ana_menu()
