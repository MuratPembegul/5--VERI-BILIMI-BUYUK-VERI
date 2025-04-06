import dask.array as da

# 1 milyondan fazla sayıdan oluşan büyük bir array oluşturalım
böcüş_array = da.random.random(size=(10000, 10000), chunks=(1000, 1000))

# Ortalama hesapla (dask bunu parça parça işler!)
ortalama = böcüş_array.mean()

# Hesaplamayı başlat
print("Ortalama:", ortalama.compute())

