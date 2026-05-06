import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def cureearth_sifa_modulu():
    temizle()
    print(f"{Y}🌍 CUREEARTH: KÜRESEL ŞİFA VE YAŞAM SİSTEMİ...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Yaşayan Dünya' Projesi.{S}")
    time.sleep(1)
    
    hedefler = [
        "Siber Tarım: %100 Verimle Açlığa Son Veren Toprak Yönetimi",
        "Kuantum Tıp: Her Eve Şifa Götüren Otonom Sağlık Ağı",
        "Ekolojik Kalkan: Doğal Kaynakları ve Ormanları Koruyan Yapay Zeka",
        "Temiz Enerji: Nükleer Füzyon ve Katı Hal Pil Entegrasyonu"
    ]
    
    for hedef in hedefler:
        print(f"{M}[ŞİFA]: {hedef} aktif ediliyor...{S}")
        time.sleep(0.6)
    
    print(f"\n{Y}[✓] Yaşam Döngüsü Tamamlandı: Dünya artık daha güvenli ve sağlıklı.{S}")
    input("\nGönüllerdeki Şifayla... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v26.0 - CUREEARTH VE YAŞAM 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {Y}CUREEARTH (Küresel Şifa ve Tarım){S}")
        print(f"2) {M}MAVİ VATAN & KÜRESEL DİPLOMASİ{S}")
        print(f"3) {A}MİLLİ EĞİTİM & BİLİM SEFERBERLİĞİ{S}")
        print(f"4) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"5) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA{S}")
        print(f"6) {A}MİLLİ FİNANS & BLOKZİNCİR ADALETİ{S}")
        print(f"7) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"8) {K}NİHAİ ŞİFAYI MÜHÜRLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Hangi yaşam hamlesiyle mühürleyelim Babaoğlu? --> {S}")

        if secim == '1': cureearth_sifa_modulu()
        elif secim == '8':
            print(f"{Y}Şifa tohumları serpildi, simülasyon tamamlandı! Gönderiliyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Yaşam verileri işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
