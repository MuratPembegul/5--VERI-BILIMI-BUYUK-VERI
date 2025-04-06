# HDFS dosya bloklama simülasyonu

dosya_boyutu_mb = 512  # örnek veri dosyası boyutu
blok_boyutu_mb = 128  # varsayılan HDFS blok boyutu

blok_sayisi = dosya_boyutu_mb // blok_boyutu_mb
kalan = dosya_boyutu_mb % blok_boyutu_mb

print(f"Toplam blok sayısı: {blok_sayisi + (1 if kalan > 0 else 0)}")

