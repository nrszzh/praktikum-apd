# nilai = 70

# status = "Lulus" if nilai >= 60 else "Tidak Lulus"
# print(status)

# if nilai > 75:
#     print('Nilai A')
# elif nilai > 65:
#     print('Nilai B')
# else:
#     print('Nilai C')



# suhu = 35
# if suhu >= 35:
#     print('PANAS')
# if suhu > 30:
#     print('Sauna')
# elif suhu > 20:
#     print('normal')
# else:
#     print('dingin') 


# umur = int(input("Masukkan umur Anda: "))
# if umur < 13:
#     kategori = "Anak-anak"
# elif umur < 18:
#     kategori = "Remaja"
# elif umur < 60:
#     kategori = "Dewasa"
# else:
#     kategori = "Lansia"
# print("Umur:", umur, "Kategori:", kategori)

tinggi = float(input'Masukkan Tinggi Anda :')
if tinggi >=145:
    print('Boleh masuk wahana')
else:
    print('Tidak boleh masuk')

bisakah = 'silahkan masuk wahana' if tinggi >= 145 else 'tidak boleh'
print(bisakah)


belanja = float(input('Masukka total belanja Anda : '))

if belanja > 100000:
    diskon = belanja *0.2
    total_bayar = belanja - diskon
    print(f'total bayar anda adalah', {total_bayar})
elif belanja > 50000:
    diskon = belanja *0.1
    total_bayar = belanja - diskon
    print(f'total bayar anda adalah', {total_bayar})
else:
    diskon = 0
