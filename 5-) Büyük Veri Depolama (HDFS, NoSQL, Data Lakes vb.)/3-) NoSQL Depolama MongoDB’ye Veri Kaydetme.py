from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
veritabani = client['bocusu_db']
koleksiyon = veritabani['ziyaretciler']

veri = {"isim": "Murat", "tarih": "2025-04-09", "aciklama": "Böcüşün MongoDB kaydı"}

sonuc = koleksiyon.insert_one(veri)
print("Veri MongoDB'ye kaydedildi. ID:", sonuc.inserted_id)

