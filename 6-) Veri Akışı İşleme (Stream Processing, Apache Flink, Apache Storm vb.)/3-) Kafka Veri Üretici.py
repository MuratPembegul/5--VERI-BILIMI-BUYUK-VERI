from kafka import KafkaProducer
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    veri = f"Sıcaklık: {random.randint(20, 35)} °C"
    print(f"[ÜRETİLDİ] {veri}")
    producer.send('hava_durumu', veri.encode('utf-8'))
    time.sleep(1)

