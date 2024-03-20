def eksponensiasi_biner(basis, eksponen, mod):
    hasil = 1
    while eksponen > 0:
        if eksponen % 2 == 1:  # Jika eksponen ganjil
            hasil = (hasil * basis) % mod  # Perbarui hasil dengan perkalian dengan basis dan modulo
        basis = (basis * basis) % mod  # Perbarui basis dengan kuadratnya dan modulo
        eksponen = eksponen // 2  # Kurangi eksponen menjadi setengahnya
    return hasil

# Contoh penggunaan
basis = 5
eksponen = 5
mod = 100000007  # Angka baru untuk modulo
print("Hasilnya adalah", eksponensiasi_biner(basis, eksponen, mod))
