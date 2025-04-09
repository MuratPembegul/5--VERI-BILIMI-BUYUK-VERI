import json
from pymongo import MongoClient

with open('veri.json', 'r', encoding='utf-8') as dosya:
    veri = json.load(dosya)

client = MongoClient('mongodb://localhost:27017/')
db = client['bocusu_db']
col = db['json_aktarim']
col.insert_one(veri)

print("JSON verisi MongoDB'ye aktarıldı.")

