# ulangi = 10
# for i in range (ulangi):
#     print(f'perulangan ke -{i}')

# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)

# for i in range (0,10,2):
#     print(i)

# for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 7):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
#     print(f"Total perulangan: {hitung}")

# tinggi = 6
# for i in range(tinggi):
#     print('*'*i)

# for i in range(6):
#     for j in range(i):
#         print('*', end='')
#     print('')

# angka = [2, 5, 8, 12, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
#     print("Program selesai.")

# for i in range(1, 11):
#     if i % 2 != 0:
#         continue
#     print(f"Angka ditemukan: {i}")
#     print("\nProgram selesai.")

h = 5
for i in range(1, h):
    bKiri = '*' * i
    tes = 'x'*((h-i)*2)
    bKanan = '*' *  i
    print(bKiri + tes + bKanan)