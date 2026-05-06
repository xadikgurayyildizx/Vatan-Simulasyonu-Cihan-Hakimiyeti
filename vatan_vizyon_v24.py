import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def bilim_ve_egitim_seferberligi():
    temizle()
    print(f"{A}🎓 MİLLİ EĞİTİM VE BİLİM SEFERBERLİĞİ BAŞLADI...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Geleceğin Dehaları' Projesi.{S}")
    time.sleep(1)
    
    adimlar = [
        "SGY-Akademi: Her Köye Dijital Eğitim ve Yapay Zeka Laboratuvarı",
        "Bilim Seferberliği: Kuantum ve Uzay Teknolojileri Ders Müfredatı",
        "İrfan Mektebi: Teknoloji ve Ahlakın (Etik) Bütünleşmiş Eğitimi",
        "Dahi Keşif Sistemi: Gizli Yetenekleri Bulan Otonom Algoritma"
    ]
    
    for adim in adimlar:
        print(f"{Y}[BİLİM]: {adim} tesis ediliyor...{S}")
        time.sleep(0.6)
    
    print(f"\n{Y}[✓] Zihinler Özgürleşti: Bilgiyle donanmış bir nesil yetişiyor.{S}")
    input("\nİlimle ve Hikmetle... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v24.0 - BİLİM VE EĞİTİM ÇAĞI 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {A}MİLLİ EĞİTİM & BİLİM SEFERBERLİĞİ{S}")
        print(f"2) {M}UYDU HABERLEŞME & VERİ EGEMENLİĞİ{S}")
        print(f"3) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"4) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA{S}")
        print(f"5) {A}MİLLİ FİNANS & BLOKZİNCİR ADALETİ{S}")
        print(f"6) {Y}SİBER SANAYİ & ÜRETİM SEFERBERLİĞİ{S}")
        print(f"7) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"8) {K}GELECEĞİN NESİLLERİNİ GITHUB'A MÜHÜRLE{S}")

        secim = input(f"\n{B}Hangi bilim hamlesiyle devam edelim Babaoğlu? --> {S}")

        if secim == '1': bilim_ve_egitim_seferberligi()
        elif secim == '8':
            print(f"{Y}Zeka ve irfan tohumları ekildi, sistem güncellendi! Gönderiliyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Bilimsel veriler işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
