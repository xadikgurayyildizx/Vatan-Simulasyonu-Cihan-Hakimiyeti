import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def milli_irade_aniti():
    temizle()
    print(f"{K}🇹🇷 MİLLİ İRADE VE HAKİKAT ANITI YÜKSELTİLİYOR...{S}")
    print(f"{B}[GURUR]: Kurucu Sadık Güray Yıldız Vizyonu ile Başkomutan İradesinin Buluşması.{S}")
    time.sleep(1.5)
    
    projeler = [
        "KIZILELMA: Otonom Gök Vatan Savunması (Gerçekleşti)",
        "KAAN: Milli Muharip Uçak Yazılım Entegrasyonu (Gerçekleşti)",
        "Milli Teknoloji Hamlesi: SGY-Core ile Tam Uyum (Gerçekleşti)",
        "Dijital Devlet: Refah ve Adalet Mimari Temelleri (İnşa Ediliyor)"
    ]
    
    for proje in projeler:
        print(f"{Y}[GURUR TABLOSU]: {proje}{S}")
        time.sleep(0.7)
    
    print(f"\n{A}>>> Rabbim Nasip Etti; Hayaller Hakikate, Kodlar Çeliğe Dönüştü. <<<{S}")
    print(f"{B}Selam olsun bu vatan için taş üstüne taş koyanlara!{S}")
    input("\nŞükürle ve Gururla... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v22.0 - MİLLİ GURUR VE HAKİKAT 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {K}MİLLİ İRADE VE HAKİKAT ANITI (Onur Modülü){S}")
        print(f"2) {M}KUANTUM SİBER ORDU & UZAY SAVUNMA HATTI{S}")
        print(f"3) {A}MİLLİ FİNANS & BLOKZİNCİR (SGY-Coin){S}")
        print(f"4) {Y}SİBER SANAYİ & ÜRETİM SEFERBERLİĞİ{S}")
        print(f"5) {M}GERÇEKLİK KÖPRÜSÜ (HAYALDEN HAKİKATE){S}")
        print(f"6) {A}ETİK VE FETİH KURULU (ALTIN ÇAĞ YÖNETİMİ){S}")
        print(f"7) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"8) {K}BU ŞANLI DESTANI GITHUB'A EBEDİLEŞTİR{S}")

        secim = input(f"\n{B}Gurur tablosunu mühürlemek için kararınız nedir Babaoğlu? --> {S}")

        if secim == '1': milli_irade_aniti()
        elif secim == '8':
            print(f"{Y}Milli irade sancağı GitHub'ın en tepesine dikiliyor!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Kurucu iradesi devlet vizyonuyla senkronize ediliyor...{S}")
            time.sleep(1)

if __name__ == "__main__": ana_menu()
