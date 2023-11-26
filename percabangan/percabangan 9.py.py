#nama: okta nia rahmadhani
#kelas: 11 tkj1
#no absen: 20
#soal: Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.
def cek_status_persiapan():
    # Meminta input pengguna tentang status persiapan proyek
    status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ").capitalize()

    # Menentukan apakah proyek dapat diluncurkan berdasarkan status persiapan
    if status_persiapan == "Siap":
        print("Proyek diluncurkan.")
    elif status_persiapan == "Tunda":
        print("Proyek ditunda.")
    else:
        print("Input tidak valid. Harap masukkan 'Siap' atau 'Tunda'.")

if __name__ == "__main__":
    cek_status_persiapan()
