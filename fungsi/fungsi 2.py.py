def hitung_faktorial(n):
    if n < 0:
        return "Faktorial hanya didefinisikan untuk bilangan non-negatif"
    elif n == 0:
        return 1
    else:
        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i
        return faktorial

# Mengambil input nilai n dari pengguna
n = int(input("Masukkan nilai n untuk menghitung faktorial: "))

# Memanggil fungsi dan mencetak hasilnya
hasil_faktorial = hitung_faktorial(n)
print(f"{n}! = {hasil_faktorial}")