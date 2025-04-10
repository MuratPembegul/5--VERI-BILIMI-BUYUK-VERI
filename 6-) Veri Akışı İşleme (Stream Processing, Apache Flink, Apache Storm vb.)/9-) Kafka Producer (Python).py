from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    timestamp = int(time.time() * 1000)
    message = f"data-{timestamp}"
    producer.send('flink-topic', message.encode())
    print(f"Gönderildi: {message}")
    time.sleep(1)

