from kafka import KafkaConsumer
import os
import time

consumer = KafkaConsumer('gercek_zamanli', bootstrap_servers='localhost:9092')
count = 0

while True:
    for msg in consumer:
        count += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("GERÇEK ZAMANLI ZİYARETÇİ PANELİ")
        print("="*35)
        print(f"Toplam ziyaretçi sayısı: {count}")
        print(f"Son kayıt: {msg.value.decode('utf-8')}")
        time.sleep(1)

