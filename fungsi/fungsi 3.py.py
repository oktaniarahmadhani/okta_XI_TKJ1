def hitung_pangkat(bilangan, eksponen):
    hasil = bilangan ** eksponen
    return hasil

# Mengambil input bilangan dan eksponen dari pengguna
bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))

# Memanggil fungsi dan mencetak hasilnya
hasil_pangkat = hitung_pangkat(bilangan, eksponen)
print(f"{bilangan}^{eksponen} = {hasil_pangkat}")