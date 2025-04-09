from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    message = f"Ziyaretçi girişi - Zaman: {time.time()}"
    producer.send('gercek_zamanli', message.encode('utf-8'))
    print("Gönderildi:", message)
    time.sleep(2)

