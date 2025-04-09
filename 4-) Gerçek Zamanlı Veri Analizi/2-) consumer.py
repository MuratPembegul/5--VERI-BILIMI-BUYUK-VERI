from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'gercek_zamanli',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest'
)

for message in consumer:
    print("Alındı:", message.value.decode('utf-8'))

