# Kafka’nın çalışması için arka planda Kafka sunucusu (broker) çalışmalı.
# Apache Kafka kurulu olmalı. Aşağıdaki gibi başlatman gerekiyor:

# Zookeeper başlat
bin/zookeeper-server-start.sh config/zookeeper.properties

# Kafka Broker başlat
bin/kafka-server-start.sh config/server.properties



