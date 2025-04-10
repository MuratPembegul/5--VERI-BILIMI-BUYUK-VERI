import time
import random
from queue import Queue
from threading import Thread

# 🎈 Küçük bir veri kuyruğumuz var
veri_kuyrugu = Queue()

# 🧃 Veri Üretici (Producer)
def veri_uretici():
    while True:
        veri = random.randint(1, 100)  # Rastgele sayı üret
        print(f"[ÜRETİCİ] Veri üretildi: {veri}")
        veri_kuyrugu.put(veri)         # Kuyruğa veriyi koy
        time.sleep(1)                  # 1 saniyede bir üret

# 🍽️ Veri Tüketici (Consumer)
def veri_tuketici():
    while True:
        veri = veri_kuyrugu.get()     # Kuyruktan veri al
        print(f"👉 [TÜKETİCİ] Veri alındı: {veri}")
        time.sleep(2)                 # 2 saniyede bir tüket

# 🎮 Thread'leri başlatalım
uretici_thread = Thread(target=veri_uretici)
tuketici_thread = Thread(target=veri_tuketici)

uretici_thread.start()
tuketici_thread.start()

