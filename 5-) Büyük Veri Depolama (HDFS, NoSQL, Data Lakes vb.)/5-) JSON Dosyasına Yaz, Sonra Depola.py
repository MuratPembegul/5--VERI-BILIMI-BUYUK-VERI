import json

veri = {
    "id": 1,
    "kullanici": "Minik Böcücük",
    "zaman": "2025-04-09",
    "not": "Büyük veri JSON denemesi"
}

with open('veri.json', 'w', encoding='utf-8') as dosya:
    json.dump(veri, dosya, ensure_ascii=False, indent=2)

print("Veri JSON dosyasına yazıldı.")

