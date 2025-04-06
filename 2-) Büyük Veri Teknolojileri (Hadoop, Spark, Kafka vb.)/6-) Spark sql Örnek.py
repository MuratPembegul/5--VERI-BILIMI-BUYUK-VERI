# Spark SQL örneği (Python benzeri mantıkla)

veriler = [
    {"isim": "Ahmet", "yas": 30},
    {"isim": "Ayşe", "yas": 25},
    {"isim": "Mehmet", "yas": 35}
]

print("30 yaşından büyükleri filtrele:")
filtreli = list(filter(lambda kisi: kisi["yas"] > 30, veriler))

for kisi in filtreli:
    print(kisi["isim"], "-", kisi["yas"], "yaşında")

