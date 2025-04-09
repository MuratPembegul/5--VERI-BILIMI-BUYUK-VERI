from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
veritabani = client['bocusu_db']
koleksiyon = veritabani['ziyaretciler']

for kayit in koleksiyon.find():
    print("MongoDB'den gelen kayıt:", kayit)

