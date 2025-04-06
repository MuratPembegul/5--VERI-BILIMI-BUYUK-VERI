# Spark RDD (Resilient Distributed Dataset) örneği (teorik)

veriler = [1, 2, 3, 4, 5]

def karesini_al(x):
    return x * x

rdd = map(karesini_al, veriler)

print("Verilerin kareleri:")
print(list(rdd))

