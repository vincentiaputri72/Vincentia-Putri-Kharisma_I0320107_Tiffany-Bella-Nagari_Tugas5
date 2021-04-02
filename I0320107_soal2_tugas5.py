"Selamat datang di Program Grading Nilai"

nama = input("Nama: ")
nilai = int(input("Nilai skala 0-100: "))


if nilai >= 85 and nilai <=100:
    hasil = 'A'
elif nilai >= 80 and nilai < 85:
    hasil = 'A-'
elif nilai >= 75 and nilai < 80:
    hasil = 'B+'
elif nilai >= 70 and nilai < 75:
    hasil = 'B'
elif nilai >= 65 and nilai < 70:
    hasil = 'C+'
elif nilai >= 60 and nilai < 65:
    hasil = 'C'
elif nilai < 60 and nilai >= 0:
    hasil = 'E'
else:
    print("Nilai Anda tidak valid.")

print("Halo, ", nama, "! Nilai Anda setelah dikonversi adalah ", hasil)
