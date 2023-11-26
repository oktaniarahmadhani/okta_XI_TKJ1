#nama: okta nia rahmadhani
#kelas: 11 tkj1
#no absen: 20
#soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya
def cek_keberadaan_file(nama_file, daftar_file):
    if nama_file in daftar_file:
        return "File sudah ada"
    else:
        return "File belum ada"

def main():
    OKTA_file = "data.txt"
    daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

    hasil_pemeriksaan = cek_keberadaan_file(OKTA_file, daftar_file_di_server)

    print(hasil_pemeriksaan)

if __name__ == "__main__":
    main()
