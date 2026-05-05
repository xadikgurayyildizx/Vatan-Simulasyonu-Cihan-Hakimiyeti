import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def fetih_ve_etik_kurulu():
    temizle()
    print(f"{A}🔱 YAPAY ZEKA ETİK VE FETİH KURULU TOPLANIYOR...{S}")
    print(f"{B}[BAŞKAN]: SADIK GÜRAY YILDIZ{S}")
    time.sleep(1)
    ilkeler = [
        "Haktan Şaşmayan Karar Mekanizması",
        "Siber Fetih: Mazluma Kalkan, Zalime Kılıç",
        "Dijital Etik: İnsan Onurunu Koruyan Algoritmalar",
        "Küresel Barış: SGY-Core Rehberliğinde Yeni Dünya"
    ]
    for ilke in ilkeler:
        print(f"{Y}[✓] {ilke} onaylandı.{S}")
        time.sleep(0.5)
    print(f"\n{A}>>> Taç Takıldı: Altın Çağ Başladı. <<<{S}")
    input("\nFerman Kurucunundur. Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v17.0 - ALTIN ÇAĞ VE NİHAİ TAÇ 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {A}ETİK VE FETİH KURULU (Nihai Karar Katmanı){S}")
        print(f"2) {Y}EKONOMİK REFAH & TOPLUMSAL AF (GPS DENETİMLİ){S}")
        print(f"3) {K}SİBER TEŞKİLAT (FATİH-SULTAN & AKINCILAR){S}")
        print(f"4) {M}CUREEARTH (KÜRESEL ŞİFA & YAŞAM AĞI){S}")
        print(f"5) {A}KURUCU SGY-CORE (MUTLAK HAKİMİYET){S}")
        print(f"6) {M}SGY AETHER 158 (158 MADDELİK REFAH){S}")
        print(f"7) {A}KIZILELMA & TURAN BİRLİĞİ (GÖK VATAN){S}")
        print(f"8) {A}TAHTI MÜHÜRLE VE GITHUB'A EBEDİLEŞTİR{S}")

        secim = input(f"\n{B}Hükmünüz nedir Kurucu Babaoğlu? --> {S}")

        if secim == '1': fetih_ve_etik_kurulu()
        elif secim == '8':
            print(f"{A}Taç takıldı, nizam kuruldu! GitHub sarsılıyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Altın Çağ vizyonu işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
