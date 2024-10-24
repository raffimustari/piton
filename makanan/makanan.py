makanan = []
harga = []
total = 0  

while True:
    makanan_input = input("Masukkan nama makanan (ketik 's' untuk selesai): ")
    if makanan_input == 's':
        break
    else:
        harga_input = int(input("Masukkan harga (makanan): "))
        makanan.append(makanan_input)
        harga.append(harga_input)

print("data makanan dan harganya:")
for i in range(len(makanan)):
    print(makanan[i], end=" ")
    total += harga[i]
print(f"\ntotal belanjan anda: Rp.{total}")