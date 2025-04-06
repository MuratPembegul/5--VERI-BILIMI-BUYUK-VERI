import sys

# Her satırı oku
for satır in sys.stdin:
    kelimeler = satır.strip().split()
    for kelime in kelimeler:
        print(f"{kelime}\t1")

