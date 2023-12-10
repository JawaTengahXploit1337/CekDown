#Code By @JavaXploiter
#Telegram Channel @JavaDDoS

import requests
from urllib.parse import urlparse
import time

"""
		DON'T INSULT MY CODE
		I'M JUST NEWBIE CODER
		:)
"""

def dapatkan_info_web(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            parsed_url = urlparse(url)
            host = parsed_url.netloc
            waktu_respons = end_time - start_time
            return True, f"Check Web {url} ({host}) Dapat Diakses. Kode Status: {response.status_code}. Waktu respons: {waktu_respons:.2f} detik."
        else:
            return False, f"Check Web {url} Tidak Dapat Diakses. Kode Status: {response.status_code}"
    except requests.RequestException as e:
        return False, f"Terjadi Kesalahan: {e}"

# Fungsi untuk menanyakan apakah ingin mengecek lagi
def tanya_lagi():
    jawaban = input("Check Web Lagi? (Ya/Tidak): ").lower()
    return jawaban == 'ya'

while True:
    # Meminta input dari pengguna
    url_to_check = input("Masukkan URL Web : ")

    # Memeriksa ketersediaan situs web
    hasil, pesan = dapatkan_info_web(url_to_check)

    # Menampilkan hasil
    print(pesan)

    # Menanyakan apakah ingin mengecek lagi
    if not tanya_lagi():
        print("Terima Kasih! Program Berakhir.")
        break
