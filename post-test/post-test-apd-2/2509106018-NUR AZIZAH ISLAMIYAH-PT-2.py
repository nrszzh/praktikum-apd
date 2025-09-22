#input
nama_pasien = str (input('Nama Pasien : '))
tinggi_badan = int (input('Tinggi Badan (cm) : '))
berat_badan = int (input('Berat Badan (kg) : '))

#rumus
berat_ideal = tinggi_badan - 100
is_kelebihan = berat_badan > berat_ideal

#status
status_list = ['Berat Badan Ideal', 'Berat Badan Kelebihan']
status = status_list[int(is_kelebihan)]

#output
print('\n--------------------------------------------------')
print('|             HASIIL CEK BERAT BADAN             |')
print('--------------------------------------------------')
print(f'|  Nama Pasien  : {nama_pasien:<27}    |')
print(f'|  Tinggi Badan : {tinggi_badan} cm{' ' :<25}|')
print(f'|  Berat Badan  : {berat_badan} kg{' ':<26}|')
print(f'|  Berat Ideal  : {berat_ideal} kg{' ':<26}| ')
print(f'|  Status       : {status:<31}|')
print('--------------------------------------------------')