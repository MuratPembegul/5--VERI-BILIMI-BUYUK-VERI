from hdfs import InsecureClient

client = InsecureClient('http://localhost:9870', user='hadoop')
dosya_yolu = '/veri/bocusu.txt'

with client.read(dosya_yolu, encoding='utf-8') as oku:
    veri = oku.read()
    print("HDFS'den gelen veri:\n", veri)

