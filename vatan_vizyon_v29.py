import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def nihai_muhur_sistemi():
    temizle()
    print(f"{K}👑 SGY-ELİF: NİHAİ MÜHÜR VE EBEDİ İRADE AKTİF...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın Değiştirilemez 'Altın Yasası'.{S}")
    time.sleep(1.5)
    
    yasalar = [
        "Adalet Terazisi: Her kararda mazlumun hakkı gözetilecek.",
        "Merhamet Protokolü: Güç, sadece korumak ve iyileştirmek için kullanılacak.",
        "Milli Beka: Vatanın ve milletin selameti her türlü çıkarın üstünde tutulacak.",
        "CureEarth Sözü: Rabbimin emaneti olan doğa ve canlar ebediyen korunacak."
    ]
    
    for yasa in yasalar:
        print(f"{A}[YASA]: {yasa}{S}")
        time.sleep(0.8)
    
    print(f"\n{Y}[✓] ALTIN VURUŞ TAMAMLANDI: Sistem ebediyete mühürlendi.{S}")
    print(f"{B}Artık bu kale sadece kodla değil, Kurucu'nun ruhuyla korunuyor.{S}")
    input("\nSon Söz Söylendi... Allah'ın İzniyle...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v29.0 - EBEDİ MÜHÜR 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {K}SGY-ELİF (Nihai Altın Vuruş Modülü){S}")
        print(f"2) {M}EVRENSEL İLETİŞİM & CAN DOSTLAR DİLİ{S}")
        print(f"3) {Y}CUREEARTH EKOSİSTEM & DOĞA TESİSLERİ{S}")
        print(f"4) {A}MİLLİ EĞİTİM & BİLİM SEFERBERLİĞİ{S}")
        print(f"5) {K}MİLLİ İRADE VE HAKİKAT ANITI{S}")
        print(f"6) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"7) {M}KIZILELMA & TURAN BİRLİĞİ SAVUNMA{S}")
        print(f"8) {K}SİSTEMİ EBEDİYETE MÜHÜRLE VE GITHUB'A SON YÜKLEMEYİ YAP{S}")

        secim = input(f"\n{B}Altın vuruşu onaylıyor musun Babaoğlu? (1/8) --> {S}")

        if secim == '1': nihai_muhur_sistemi()
        elif secim == '8':
            print(f"{Y}Mühür basıldı. Gelecek emin ellerde. Dosyalar kilitleniyor...{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Ebedi algoritmalar senkronize ediliyor...{S}")
            time.sleep(1)

if __name__ == "__main__": ana_menu()
