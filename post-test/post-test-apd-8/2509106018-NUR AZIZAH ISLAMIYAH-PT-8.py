import time
import data
from display import clear_screen, header_program
from log import register_user, login_valid
from crud import (
    menu_tambah_donor, menu_lihat_donor, menu_ubah_donor, 
    menu_hapus_donor, menu_catat_riwayat
)

user_login = ''
role_user = ''

#login
while True:
    while user_login == '':
        clear_screen()
        header_program()
        print('1. Login')
        print('2. Register')
        print('3. Keluar')
        print('-----------------------------------------')
        pilihan_awal = input('Pilih Opsi (1/2/3): ').strip()

        if pilihan_awal == '3':
            print('Anda telah keluar. Terima kasih!')
            exit()
        elif pilihan_awal == '2':
            register_user(data.akun_user)
        elif pilihan_awal == '1':
            coba_login = 0
            login_berhasil = False
            while coba_login < 3:
                clear_screen()
                print('--- LOGIN ---')
                print(f'Percobaan ke-{coba_login + 1} dari 3')
                username = input('Username : ').strip()
                password = input('Password : ').strip()

                if not username or not password:
                    print('Username dan Password tidak boleh kosong!')
                    time.sleep(1)
                    coba_login += 1
                    continue
                
                berhasil, role_hasil = login_valid(username, password, data.akun_user)
                
                if berhasil:
                    user_login = username
                    role_user = role_hasil
                    login_berhasil = True
                    print('Login berhasil')
                    time.sleep(1)
                    break
                else:
                    coba_login += 1
                    sisa_coba = 3 - coba_login
                    if sisa_coba > 0:
                        print(f'Username atau Password salah! Sisa percobaan: {sisa_coba}')
                        time.sleep(1)

            if not login_berhasil:
                print('Login Gagal, kembali ke menu awal...')
                time.sleep(1)
        else:
            print('Pilihan tidak valid!')
            time.sleep(1)

    #menu utama
    while user_login != '':
        clear_screen()
        header_program()
        print(f'      Login sebagai {user_login} ({role_user.upper()})')
        print(f'=========================================')

        if role_user == 'admin':
            print('1. Tambah Data Pendonor')
            print('2. Lihat Data Pendonor')
            print('3. Ubah Data Pendonor')
            print('4. Hapus Data Pendonor')
            print('5. Catat Riwayat Donor')
            print('6. Logout')
            print('-----------------------------------------')
            pilihan_menu = input('Pilih Menu (1-6): ').strip()

            if pilihan_menu == '1': menu_tambah_donor()
            elif pilihan_menu == '2': menu_lihat_donor()
            elif pilihan_menu == '3': menu_ubah_donor()
            elif pilihan_menu == '4': menu_hapus_donor()
            elif pilihan_menu == '5': menu_catat_riwayat()
            elif pilihan_menu == '6':
                user_login = ''
                role_user = ''
                print('Anda telah logout.')
                time.sleep(1)
            else:
                print('Pilihan tidak valid!')
                time.sleep(1)

        else: #user biasa
            print('1. Lihat Data Pendonor')
            print('2. Logout')
            print('-----------------------------------------')
            pilihan_menu = input('Pilih Menu (1/2): ').strip()

            if pilihan_menu == '1': menu_lihat_donor()
            elif pilihan_menu == '2':
                user_login = ''
                role_user = ''
                print('Anda telah logout.')
                time.sleep(1)
            else:
                print('Pilihan tidak valid!')
                time.sleep(1)