def hitung_fibonacci(n):
    if n <= 0:
        return "Input harus lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return hitung_fibonacci(n - 1) + hitung_fibonacci(n - 2)

# Mengambil input nilai n dari pengguna
n = int(input("Masukkan nilai n untuk bilangan Fibonacci: "))

# Memanggil fungsi dan mencetak hasilnya
hasil_fibonacci = hitung_fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil_fibonacci}")