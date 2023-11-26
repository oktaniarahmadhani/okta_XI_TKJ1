#nama: okta nia rahmadhani
#kelas: 11 tkj1
#no absen: 20
#soal: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.
def cek_perlu_restart():
    # Meminta input pengguna apakah ada pembaruan perangkat lunak
    ada_pembaruan = input("Apakah ada pembaruan perangkat lunak? ya: ").lower()

    if ada_pembaruan == "ya":
        # Jika ada pembaruan, meminta input pengguna apakah pembaruan memerlukan restart
        perlu_restart = input("Apakah pembaruan memerlukan restart? ya: ").lower()

        if perlu_restart == "ya":
            print("ya.")
        else:
            print("ya.")
    else:
        print("ya.")

if __name__ == "__main__":
    cek_perlu_restart()
