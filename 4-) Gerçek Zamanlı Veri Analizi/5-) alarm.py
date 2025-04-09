from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('gercek_zamanli', bootstrap_servers='localhost:9092')
count = 0
start_time = time.time()

for msg in consumer:
    count += 1
    elapsed = time.time() - start_time
    print(f"[{count}] Ziyaretçi: {msg.value.decode('utf-8')}")

    if elapsed > 10:
        print("Son 10 saniyede ziyaretçi sayısı:", count)
        if count > 5:
            print("🚨 ALARM: Yoğun giriş tespit edildi!")
        count = 0
        start_time = time.time()

