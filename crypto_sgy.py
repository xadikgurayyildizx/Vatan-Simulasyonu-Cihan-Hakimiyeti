import requests
import os
def sgy_operasyon():
    print('--- SGY KRİPTO & SİSTEM NÖBETİ ---')
    try:
        data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,pi-network&vs_currencies=usd').json()
        print(f'BTC: {data["bitcoin"]["usd"]}$ | ETH: {data["ethereum"]["usd"]}$ | PI: {data["pi-network"]["usd"]}$')
    except: print('[!] Veri Çekilemedi.')
    print('--- Sistem Durumu ---')
    os.system('termux-battery-status | grep percentage')
    print('[OK] Ejderha Nöbette.')
sgy_operasyon()
