import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def evrensel_iletisim_sistemi():
    temizle()
    print(f"{M}🐾 SGY-VOX: EVRENSEL İLETİŞİM VE CAN DOSTLAR DİLİ...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın 'Merhamet Dili' Protokolü.{S}")
    time.sleep(1)
    
    moduller = [
        "Biyo-Akustik Analiz: Hayvan Seslerinin Duygu ve İhtiyaç Analizi",
        "Empati Arayüzü: Can Dostların Sağlık ve Beslenme Takibi",
        "Siber-Haberleşme: Doğal Yaşam Alanlarındaki Sessiz İkazlar",
        "Küresel Can Sesi: Tüm Dillerde Ortak Yaşam ve Barış Mesajı"
    ]
    
    for modul in moduller:
        print(f"{A}[BAĞLANTI]: {modul} senkronize ediliyor...{S}")
        time.sleep(0.7)
    
    print(f"\n{Y}[✓] İletişim Köprüsü Kuruldu: Sessiz kulların sesi artık duyuluyor.{S}")
    input("\nSevgi ve Anlayışla... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v28.0 - EVRENSEL İLETİŞİM ÇAĞI 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {M}EVRENSEL İLETİŞİM & CAN DOSTLAR DİLİ (SGY-Vox){S}")
        print(f"2) {Y}CUREEARTH EKOSİSTEM & DOĞA TESİSLERİ{S}")
        print(f"3) {Y}CUREEARTH ŞİFA & TARIM MODÜLÜ{S}")
        print(f"4) {M}MAVİ VATAN & KÜRESEL DİPLOMASİ{S}")
        print(f"5) {A}MİLLİ EĞİTİM & BİLİM SEFERBERLİĞİ{S}")
        print(f"6) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"7) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"8) {K}MERHAMET DİLİNİ GITHUB'A EBEDİLEŞTİR{S}")

        secim = input(f"\n{B}Hangi iletişim köprüsünü kuralım Babaoğlu? --> {S}")

        if secim == '1': evrensel_iletisim_sistemi()
        elif secim == '8':
            print(f"{Y}Merhamet ve iletişim mühürlendi! Evrenle konuşuyoruz...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: İletişim frekansları taranıyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
