import os, time, random

# Renkler
K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def vizyon_yukle(metin):
    temizle()
    print(f"{M}🌀 {metin} AKTİF EDİLİYOR...{S}")
    for i in range(1, 6):
        print(f"{B}[ANALİZ]: Katman {i} senkronize ediliyor...{S}")
        time.sleep(0.3)
    print(f"\n{Y}[✓] İşlem Başarılı.{S}")
    time.sleep(1)

def aether_158():
    temizle()
    print(f"{M}🌐 SGY AETHER 158 PROTOKOLÜ - KÜRESEL REFAH MATRİSİ{S}")
    print(f"{B}--------------------------------------------------{S}")
    for i in range(1, 159):
        if i % 15 == 0:
            print(f"{Y}[+] Aether Madde {i}: Refah dengeleniyor...{S}")
            time.sleep(0.2)
    print(f"\n{A}>>> Dünya Beşten Büyüktür ve SGY Aether ile Daha Adildir. <<<{S}")
    input("\nDevam etmek için Enter...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU & SGY AETHER v8.0 - ELİT VİZYON 🇹🇷{S}")
        print(f"{B}=================================================={S}")
        print(f"1) {A}Siber Savunma & Çelik Kubbe{S}")
        print(f"2) {A}Enerji Bağımsızlığı & Nükleer Güç{S}")
        print(f"3) {A}Turan Birliği Ortak Pazarı{S}")
        print(f"4) {M}SGY AETHER 158 (Küresel İyileşme Protokolü){S}")
        print(f"5) {A}Dijital Adalet & Gönül Coğrafyası{S}")
        print(f"6) {A}Milli Uzay ve Havacılık Vizyonu{S}")
        print(f"7) {A}Sürdürülebilir Bereket & Akıllı Tarım{S}")
        print(f"8) {K}SİSTEMİ GÜNCELLE VE GÖNDER{S}")

        secim = input(f"\n{B}Hangi vizyonu tetikleyelim Babaoğlu? --> {S}")

        if secim == '1': vizyon_yukle("SİBER SAVUNMA"); print(f"{Y}[+] Savunma Hattı Kuruldu.{S}"); input("\nDevam...")
        elif secim == '4': aether_158()
        elif secim == '8':
            print(f"{Y}Devlet Ebed Müddet! Cihan Hakimiyeti Başlıyor...{S}")
            break
        else: vizyon_yukle("VERİ ANALİZİ"); input("\nDevam...")

if __name__ == "__main__": ana_menu()
