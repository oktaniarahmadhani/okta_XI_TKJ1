#nama: okta nia rahmadhani
#kelas: 11 tkj1
#no absen: 20
#soal: Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman.
# Menerima input durasi peminjaman buku dalam hari
durasi_peminjaman = int(input("Masukkan durasi peminjaman buku (7): "))

# Menentukan jenis peminjaman berdasarkan durasi
if durasi_peminjaman <= 7:
    jenis_peminjaman = "Peminjaman Pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_peminjaman = "Peminjaman Menengah"
else:
    jenis_peminjaman = "Peminjaman Panjang"

# Mencetak jenis peminjaman
print ("jenis peminjaman":", peminjaman_pendek")