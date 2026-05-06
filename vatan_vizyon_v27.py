import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def cureearth_ekosistem_tesisleri():
    temizle()
    print(f"{Y}🌍 CUREEARTH EKOSİSTEM VE DOĞA KORUMA SEFERBERLİĞİ...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Emanete Sahip Çık' Doktrini.{S}")
    time.sleep(1)
    
    tesisler = [
        "Sıfır Atık Fabrikaları: %100 Geri Dönüşüm ve Sıfır Kirlilik",
        "Mavi Vatan Temizlik Filosu: Denizleri ve Okyanusları Arıtan Otonom Gemiler",
        "Gök Vatan Hava Kalite Kontrol: Şehirleri Temiz Hava ile Besleyen Filtreleme",
        "Hayvan Hakları ve Yaşam Alanları: Doğal Ortamında Korunan Can Dostlar",
        "Güneş ve Rüzgar Enerjisi Hasadı: Doğaya Zarar Vermeyen Sınırsız Güç"
    ]
    
    for tesis in tesisler:
        print(f"{Y}[TESİS KURULUYOR]: {tesis}{S}")
        time.sleep(0.7)
    
    print(f"\n{A}>>> Rabbimin Yarattığı Her Zerreyi Korumak İçin Söz Verdik. <<<{S}")
    input("\nDoğayla Barışık Bir Gelecek İçin... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v27.0 - CUREEARTH VE EKOSİSTEM 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {Y}CUREEARTH EKOSİSTEM TESİSLERİ (Doğa & Hayvan & Enerji){S}")
        print(f"2) {Y}CUREEARTH ŞİFA MODÜLÜ (Küresel Sağlık & Tarım){S}")
        print(f"3) {M}MAVİ VATAN & KÜRESEL DİPLOMASİ{S}")
        print(f"4) {A}MİLLİ EĞİTİM & BİLİM SEFERBERLİĞİ{S}")
        print(f"5) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"6) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA{S}")
        print(f"7) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"8) {K}EMANETİ MÜHÜRLE VE GITHUB'A GÖNDER{S}")

        secim = input(f"\n{B}Nimetlere sahip çıkmak için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': cureearth_ekosistem_tesisleri()
        elif secim == '8':
            print(f"{Y}Doğa ve yaşam mühürlendi, gelecek yeşeriyor! Gönderiliyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Ekolojik denge verileri analiz ediliyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
