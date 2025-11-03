# import inquirer

# questions = [
#     inquirer.Editor('bio', 
#                     message = "Silahkan tulis bio anda ")
# ]

# import inquirer

# # Buat pertanyaan dengan pilihan yang bisa dipilih pakai panah
# pertanyaan = [
#     inquirer.List(
#         'bahasa',
#         message="Pilih bahasa pemrograman favoritmu:",
#         choices=['Python', 'JavaScript', 'Java', 'C++', 'Go']
#     )
# ]

# # Jalankan pertanyaan
# jawaban = inquirer.prompt(pertanyaan)

# # Tampilkan hasil
# print(f"\nKamu memilih: {jawaban['bahasa']} ")

# from prettytable import PrettyTable
# table = PrettyTable()

# table.field_names = ["NIM", "Nama", "Prodi"]
# table.add.row(['001', 'ucup', 'informatika'])
# table.add.row(['002', 'yoga', ' sepuh informatika'])
# table.add.row(['003', 'fauzi', 'ketua web'])
# print(table.get_string(sortby="Nama"))

# from datetime import datetime
# print(datetime.now())

# # import math
# # print(math.sqrt(16))

# # # # # # angka = min(1,5,8,132,451)       #round(3.49)
# # # # # # print(angka)

#  for i, v in enumerate(['a','b']):
#     print(i, v) # 0 a , 1 b
# len([10, 20, 30]) # 3
# list(map(str, [1,2,3])) # ['1', '2', '3']
# sorted([3, 1, 2]) # [1, 2, 3]
# list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

# x = 42
# def fungsi():
#      x = 10
#      y = 20
#      z = 30
#      print(globals()['x'])  
#      print(locals()['x'])  
#      print(locals()) # {'x': 10, 'y': 20, 'z': 30} #print local nya harus didalam fungsi, klo ga bakal error
# fungsi()

#  nama = input('Masukkan nama kalian')
#  print(nama.upper())

# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
# print(acak_kartu)

