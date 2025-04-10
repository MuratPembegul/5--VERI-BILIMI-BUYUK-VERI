from kafka.admin import KafkaAdminClient, NewTopic

admin = KafkaAdminClient(bootstrap_servers="localhost:9092")

topic = NewTopic(name="hava_durumu", num_partitions=1, replication_factor=1)

try:
    admin.create_topics([topic])
    print("Topic başarıyla oluşturuldu.")
except Exception as e:
    print("Topic zaten var veya hata oluştu:", e)

