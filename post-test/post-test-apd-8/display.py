import os
from prettytable import PrettyTable
from help import hitung_penghargaan

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header_program():
    print('=========================================')
    print('        SISTEM CEK DONOR DARAH           ')
    print('=========================================')

def tampilkan_tabel_donor(data):
    if not data:
        print('Belum ada data pendonor yang tersimpan.')
        return False
    
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Umur", "BB(kg)", "Goldar", "Telepon", "Jumlah Donor", "Penghargaan"]

    for donor_id, donor_info in data.items():
        jumlah_donor = donor_info['jumlah_donor']
        penghargaan = hitung_penghargaan(jumlah_donor)
        
        tabel.add_row([
            donor_id,
            donor_info['nama'],
            donor_info['umur'],
            donor_info['bb'],
            donor_info['goldar'],
            donor_info['telepon'],
            f"{jumlah_donor}x",
            penghargaan
        ])
    print(tabel)
    return True