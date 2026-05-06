import requests
import time

def fiyat_cek():
    print('--- SGY KRİPTO NÖBETİ BAŞLADI ---')
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,pi-network&vs_currencies=usd'
    try:
        data = requests.get(url).json()
        print(f'BTC: {data["bitcoin"]["usd"]}$ ')
        print(f'ETH: {data["ethereum"]["usd"]}$ ')
        print(f'PI (Market): {data["pi-network"]["usd"]}$ ')
        print('[OK] SGY-Aether Veri Akışı Stabil.')
    except:
        print('[!] Veri Çekilemedi, Bağlantıyı Kontrol Et.')

fiyat_cek()
