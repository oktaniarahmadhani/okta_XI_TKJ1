#nama: okta nia rahmadhani
#kelas: 11 tkj1
#no absen: 20
#soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.
def tentukan_status_lulus(tugas, ujian):
    if tugas > 70 and ujian > 60:
        return "Lulus"
    else:
        return "Gagal"

def main():
    # Nilai tugas dan nilai ujian yang diberikan
    nilai_tugas = 80
    nilai_ujian = 75
    
    # Menentukan status siswa menggunakan fungsi tentukan_status_lulus
    status_lulus = tentukan_status_lulus(nilai_tugas, nilai_ujian)

    # Mencetak status siswa
    print("Status siswa:", status_lulus)

if __name__ == "__main__":
    main()

