import ray
import time

# Ray'i başlat
ray.init()

# Uzaktan çalışacak bir fonksiyon tanımla
@ray.remote
def uzun_işlem(saniye):
    time.sleep(saniye)
    return f"{saniye} saniye bekledi."

# Paralel olarak işlemleri başlat
görevler = [uzun_işlem.remote(s) for s in [2, 3, 1]]

# Tüm sonuçları al
sonuçlar = ray.get(görevler)

# Yazdır
for sonuç in sonuçlar:
    print(sonuç)

