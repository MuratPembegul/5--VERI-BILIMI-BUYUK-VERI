from hdfs import InsecureClient

client = InsecureClient('http://localhost:9870', user='hadoop')
dosya_yolu = '/veri/bocusu.txt'
icerik = "Minik Böcüşün ilk büyük veri denemesi 😍\n"

with client.write(dosya_yolu, encoding='utf-8') as yaz:
    yaz.write(icerik)

print("Veri başarıyla HDFS'ye yazıldı 🎉")

