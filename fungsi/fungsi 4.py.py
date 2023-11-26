def hitung_jumlah_digit(bilangan):
    # Mengkonversi bilangan menjadi string untuk memudahkan penghitungan jumlah digit
    bilangan_str = str(bilangan)
    
    # Menginisialisasi variabel jumlah_digit
    jumlah_digit = 0
    
    # Menghitung jumlah digit
    for digit in bilangan_str:
        if digit.isdigit():  # Memeriksa apakah karakter adalah digit
            jumlah_digit += int(digit)
    
    return jumlah_digit

# Mengambil input bilangan dari pengguna
bilangan = int(input("Masukkan bilangan: "))

# Memanggil fungsi dan mencetak hasilnya
hasil_jumlah_digit = hitung_jumlah_digit(bilangan)
print(f"Jumlah digit dari {bilangan} adalah {hasil_jumlah_digit}")