import sys

son_kelime = None
toplam = 0

for satır in sys.stdin:
    kelime, sayı = satır.strip().split('\t')
    sayı = int(sayı)

    if son_kelime == kelime:
        toplam += sayı
    else:
        if son_kelime:
            print(f"{son_kelime}\t{toplam}")
        son_kelime = kelime
        toplam = sayı

if son_kelime == kelime:
    print(f"{son_kelime}\t{toplam}")

