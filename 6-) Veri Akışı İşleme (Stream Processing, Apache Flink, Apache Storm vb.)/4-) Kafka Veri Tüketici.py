from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'hava_durumu',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='hava_takip'
)

for mesaj in consumer:
    print(f"[ALINDI] {mesaj.value.decode('utf-8')}")

