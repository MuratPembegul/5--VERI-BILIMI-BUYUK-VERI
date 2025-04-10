from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'veri_akisi',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    veri = message.value
    print(f"Alınan veri: {veri}")
    # burada ML modeliyle işleyebilirsin

