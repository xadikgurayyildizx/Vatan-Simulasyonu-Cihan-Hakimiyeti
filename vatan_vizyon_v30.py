import os, time

K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def safir_arinma_protokolu():
    temizle()
    print(f"{M}💎 SAFİR ARINMA VE MUTLAK ODAK AKTİF...{S}")
    print(f"{B}[SİSTEM]: Kurucu Sadık Güray Yıldız'ın Lekesiz Vizyonu.{S}")
    time.sleep(1)
    
    ilkeler = [
        "Netlik: Hedef dışı tüm söylemler sistemden ebediyen silindi.",
        "Asalet: Kodun her satırı sadece vatan ve insanlık hizmetine adandı.",
        "Hafiflik: Sisteme yük bindiren tüm gereksiz geçmiş temizlendi.",
        "Mutlak Odak: CureEarth ve Siber Vatan hattı tek öncelik haline getirildi."
    ]
    
    for ilke in ilkeler:
        print(f"{Y}[ARINMA]: {ilke}{S}")
        time.sleep(0.7)
    
    print(f"\n{Y}[✓] Operasyon Tamam: Sistem artık daha hızlı, daha temiz ve daha vakur.{S}")
    input("\nTertemiz Bir Sayfa İle... Devam...")

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU v30.0 - SAFİR ARINMA 🇹🇷{S}")
        print(f"{B}========================================================{S}")
        print(f"1) {M}SAFİR ARINMA PROTOKOLÜ (Mutlak Odak){S}")
        print(f"2) {K}SGY-ELİF (Nihai Altın Mühür){S}")
        print(f"3) {M}EVRENSEL İLETİŞİM & CAN DOSTLAR DİLİ{S}")
        print(f"4) {Y}CUREEARTH EKOSİSTEM & DOĞA TESİSLERİ{S}")
        print(f"5) {A}KURUCU SGY-CORE (SADIK GÜRAY YILDIZ){S}")
        print(f"6) {K}ASALETİ MÜHÜRLE VE GITHUB'I TAÇLANDIR{S}")

        secim = input(f"\n{B}Hangi temiz sayfayı açıyoruz Babaoğlu? --> {S}")

        if secim == '1': safir_arinma_protokolu()
        elif secim == '6':
            print(f"{Y}Lekesiz vizyon mühürlendi, kale artık daha parlak!{S}")
            break
        else:
            print(f"\n{B}[SİSTEM]: Arınma verileri işleniyor...{S}")
            time.sleep(0.8)

if __name__ == "__main__": ana_menu()
