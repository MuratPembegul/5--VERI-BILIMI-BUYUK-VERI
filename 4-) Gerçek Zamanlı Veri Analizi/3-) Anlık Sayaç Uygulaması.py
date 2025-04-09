from kafka import KafkaConsumer
from collections import Counter

consumer = KafkaConsumer('gercek_zamanli', bootstrap_servers='localhost:9092')
sayac = Counter()

for msg in consumer:
    zaman = msg.value.decode('utf-8').split("- Zaman:")[1]
    print(f"Ziyaretçi kaydı alındı -> Zaman: {zaman}")
    sayac['ziyaretci'] += 1
    print("Toplam ziyaretçi sayısı:", sayac['ziyaretci'])

