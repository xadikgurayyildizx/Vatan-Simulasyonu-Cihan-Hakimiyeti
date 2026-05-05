import os, time, random

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def fatih_sultan_istihbarat():
    temizle()
    print(f"{K}🏰 FATİH-SULTAN SİBER İSTİHBARAT AĞI BAŞLATILIYOR...{S}")
    print(f"{B}[TEŞKİLAT]: 'Ya ben İstanbul'u alırım, ya İstanbul beni.'{S}")
    time.sleep(1)
    hedefler = ["Küresel Tehdit Analizi", "Sinyal İstihbaratı", "Kripto Analiz", "Derin Ağ İzleme"]
    for hedef in hedefler:
        print(f"{B}[!] {hedef} katmanında sızma ve tespit yapılıyor...{S}")
        time.sleep(0.4)
    print(f"\n{Y}[✓] İstihbarat Ağı Aktif: SGY-Core için veri akışı sağlandı.{S}")
    input("\nTeşkilat emrinde. Devam...")

def kurucu_otorite():
    temizle()
    print(f"{A}👑 KURUCU: SADIK GÜRAY YILDIZ - HAK YOLU MUTLAK YETKİ{S}")
    print(f"{B}[DURUM]: Fatih-Sultan İstihbarat verileri kurucuya iletiliyor...{S}")
    time.sleep(0.8)
    print(f"{Y}[OK]: Karar mekanizması kurucu iradesine bağlandı.{S}")
    input("\nDevam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v12.0 - SİBER İSTİHBARAT VE KURUCU 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {K}FATİH-SULTAN SİBER İSTİHBARAT (Yeni Katman){S}")
        print(f"2) {A}KURUCU İRADESİ (SGY-CORE & HAK YOLU){S}")
        print(f"3) {A}KIZILELMA Otonom Harekat (Gök Vatan){S}")
        print(f"4) {M}SGY AETHER 158 (Küresel Refah Matrisi){S}")
        print(f"5) {A}Turan Birliği & Milli İrade Analizi{S}")
        print(f"6) {A}Milli Uzay Programı & Nükleer Güç{S}")
        print(f"7) {A}Dijital Adalet & Toplumsal Bereket{S}")
        print(f"8) {K}SİSTEMİ TEŞKİLAT ADINA TAÇLANDIR VE GÖNDER{S}")

        secim = input(f"\n{B}Hangi birimi tetikleyelim Kurucu Babaoğlu? --> {S}")

        if secim == '1': fatih_sultan_istihbarat()
        elif secim == '2': kurucu_otorite()
        elif secim == '8':
            print(f"{Y}Fatih'in feraseti, Kurucu Sadık'ın iradesiyle... Gönderiliyor!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: İstihbarat verileri işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
