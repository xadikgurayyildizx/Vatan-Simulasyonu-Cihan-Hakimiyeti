import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def uydu_haberlesme_agi():
    temizle()
    print(f"{M}📡 SGY-NET: UYDU TABANLI VERİ EGEMENLİĞİ AKTİF...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın Kesintisiz Haberleşme Doktrini.{S}")
    time.sleep(1)
    
    katmanlar = [
        "Alçak Yörünge Veri Takım Yıldızları (SGY-Star)",
        "Kırılamaz Lazer Haberleşme Linkleri",
        "Küresel İnternet Bağımsızlığı: Milli Gateway",
        "Siber Vatan Siber-Uzay Kalkanı"
    ]
    
    for katman in katmanlar:
        print(f"{A}[BAĞLANTI]: {katman} kuruluyor...{S}")
        time.sleep(0.6)
    
    print(f"\n{Y}[✓] Veri Egemenliği Sağlandı: Hattımızı kimse kesemez!{S}")
    input("\nGöklerdeki İmzayla... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v23.0 - VERİ VE UYDU EGEMENLİĞİ 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {M}UYDU TABANLI HABERLEŞME (SGY-NET){S}")
        print(f"2) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"3) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA{S}")
        print(f"4) {A}MİLLİ FİNANS & BLOKZİNCİR ADALETİ{S}")
        print(f"5) {Y}SİBER SANAYİ & ÜRETİM SEFERBERLİĞİ{S}")
        print(f"6) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"7) {A}KIZILELMA & TURAN BİRLİĞİ VİZYONU{S}")
        print(f"8) {K}YENİ UFUKLARI MÜHÜRLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Hangi ufka nişan alıyoruz Babaoğlu? --> {S}")

        if secim == '1': uydu_haberlesme_agi()
        elif secim == '8':
            print(f"{Y}Uydu ağları örüldü, veri hakimiyeti sağlandı! Uçuşa geçiliyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Uzaydan gelen veriler işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
