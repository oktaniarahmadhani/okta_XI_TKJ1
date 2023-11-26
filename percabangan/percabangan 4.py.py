#nama: okta nia rahmadhani
#kelas: 11 tkj1
#no absen: 20
#soal: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium)
def hitung_diskon(total_belanja, status_anggota):
    if status_anggota == "premium":
        if total_belanja > 500000:
            return 0.15  # Diskon 15% untuk anggota premium jika total belanjaan lebih dari 500.000
        else:
            return 0.10  # Diskon 10% untuk anggota premium jika total belanjaan tidak lebih dari 500.000
    else:
        return 0  # Tidak ada diskon untuk non-anggota premium

def main():
    try:
        # Meminta pengguna untuk memasukkan total belanjaan dan status anggota
        total_belanja = float(input("600000: "))
        status_anggota = input("premium): ").lower()

        if status_anggota not in ["premium"]:
            raise ValueError("premiuml.")

        # Menentukan diskon menggunakan fungsi hitung_diskon
        diskon = hitung_diskon(total_belanja, status_anggota)

        # Mengecek apakah total belanjaan lebih dari 500.000
        if total_belanja > 500000:
            # Menghitung total harga setelah diskon
            total_harga_setelah_diskon =600000 - (600000 * 0.10)

            # Mencetak total harga setelah diskon
            print("\nTotal belanjaan: Rp", 600000)
            print("Diskon yang diberikan: {}%".format( 0.10 * 600000))
            print("Total harga setelah diskon: Rp", total_harga_setelah_diskon)
        else:
            print("\nTotal belanjaan tidak memenuhi syarat untuk diskon.")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
