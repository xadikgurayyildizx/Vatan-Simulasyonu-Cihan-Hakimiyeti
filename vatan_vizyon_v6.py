import os, time, random

# Renkler
K = "\033[1;31m"; Y = "\033[1;32m"; M = "\033[1;34m"
A = "\033[1;33m"; B = "\033[1;37m"; S = "\033[0m"

def temizle(): os.system('clear')

def katman_analizi(katman_adi):
    temizle()
    print(f"{A}--- {katman_adi} Analiz Ediliyor ---{S}\n")
    for i in range(1, 4):
        print(f"{B}[SİSTEM]: Veri bloğu {i} doğrulanıyor...{S}")
        time.sleep(0.4)
    print(f"\n{Y}[✓] {katman_adi} Verileri Güncellendi.{S}")
    time.sleep(1)

def ana_menu():
    while True:
        temizle()
        print(f"{K}🇹🇷 VATAN SİMÜLASYONU VE KÜRESEL REFAH V6.0 🇹🇷{S}")
        print(f"{B}--------------------------------------------{S}")
        print(f"1) {A}SİBER SAVUNMA KATMANI{S} (ASELSAN-HAVELSAN Entegre)")
        print(f"2) {A}ENERJİ BAĞIMSIZLIĞI{S} (Nükleer Füzyon & Doğalgaz)")
        print(f"3) {A}TURAN BİRLİĞİ EKONOMİSİ{S} (Ortak Pazar Analizi)")
        print(f"4) {A}DİJİTAL ADALET SİSTEMİ{S} (Küresel Refah Dağılımı)")
        print(f"5) {A}UZAY VE HAVACILIK{S} (Milli Uzay Programı)")
        print(f"6) {A}GIDA VE TARIM TEKNOLOJİSİ{S} (Sürdürülebilir Bereket)")
        print(f"7) {A}TOPLUMSAL SEVGİ VE BARIŞ{S} (Gönül Coğrafyası)")
        print(f"8) {K}SİSTEMDEN AYRIL{S}")

        secim = input(f"\n{B}Hangi katmana odaklanalım Babaoğlu? --> {S}")

        if secim == '1':
            katman_analizi("Siber Savunma")
            print(f"{Y}\n[+] Çelik Kubbe Aktif.\n[+] Yerli Kriptoloji Algoritmaları Devrede.{S}")
            input("\nDevam...")
        elif secim == '2':
            katman_analizi("Enerji")
            print(f"{Y}\n[+] Akkuyu Tam Kapasite.\n[+] Karadeniz Gazı Şebekede.{S}")
            input("\nDevam...")
        elif secim == '3':
            katman_analizi("Turan Birliği")
            print(f"{Y}\n[+] Ortak Para Birimi Hazırlıkları Başladı.\n[+] Zengezur Koridoru Lojistik Akışı Aktif.{S}")
            input("\nDevam...")
        elif secim == '4':
            katman_analizi("Dijital Adalet")
            print(f"{Y}\n[+] Dünya Beşten Büyüktür Algoritması Çalışıyor.\n[+] Gelir Dağılımı Dengeleme Modülü Aktif.{S}")
            input("\nDevam...")
        elif secim == '5':
            katman_analizi("Uzay")
            print(f"{Y}\n[+] Ay Misyonu İniş Aracı Hazır.\n[+] Milli Uydu Takımı Yörüngede.{S}")
            input("\nDevam...")
        elif secim == '6':
            katman_analizi("Tarım")
            print(f"{Y}\n[+] Akıllı Sulama Sistemleri Devrede.\n[+] Tohum Bankası Güvenlik Altında.{S}")
            input("\nDevam...")
        elif secim == '7':
            katman_analizi("Toplumsal Barış")
            print(f"{Y}\n[+] Gönül Köprüleri Kuruldu.\n[+] İnsani Yardım Koridorları Açık.{S}")
            input("\nDevam...")
        elif secim == '8':
            print(f"{K}Devlet Ebed Müddet!{S}")
            break

if __name__ == "__main__": ana_menu()
