import os

akun_user = [
    ['admin', 'admin123', 'admin'],
    ['nur', '018', 'user']
]

data_donor = [
    [1, 'Fred Brailey', 93, 71, 'O+', '081258016876', 135],
    [2, 'Cristiano Ronaldo', 40, 83, 'AB+', '081987654321', 34],
    [3, 'Hrithik Roshan', 51, 77, 'B-', '081987654321', 41],
    [4, 'Michael Octaviano', 50, 88, 'O+', '081987654321', 11],
    [5, 'Diko Saputra', 22, 55, 'B+', '081987654321', 4],
]
id_terakhir = 5
user_login = ''
role_user = ''

while True:
    while user_login == '':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=========================================')
        print('         SISTEM CEK DONOR DARAH          ')
        print('=========================================')
        print('1. Login')
        print('2. Register')
        print('3. Keluar')
        print('-----------------------------------------')
        pilihan_awal = input('Pilih Opsi (1/2/3): ')

        if pilihan_awal == '3':
            print('Anda telah keluar')
            exit()
        elif pilihan_awal == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- HALAMAN REGISTER ---')
            username_baru = input('Masukkan Username Baru : ')
            password_baru = input('Masukkan Password Baru : ')
            username_ada = False
            for akun in akun_user:
                if akun[0] == username_baru:
                    username_ada = True
                    break
            if username_ada:
                print('\nUsername sudah terdaftar! Silahkan coba lagi.')
            else:
                akun_user.append([username_baru, password_baru, 'pengguna'])
                print('\nAkun berhasil dibuat! Silahkan login.')

        elif pilihan_awal == '1':
            coba_login = 0
            login_berhasil = False
            while coba_login < 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- HALAMAN LOGIN ---')
                print(f'Percobaan ke-{coba_login + 1} dari 3')
                username = input('Username : ')
                password = input('Password : ')
                
                for akun in akun_user:
                    if akun[0] == username:
                        if akun[1] == password:
                            user_login = akun[0]
                            role_user = akun[2]
                            login_berhasil = True
                            break
                
                if login_berhasil:
                    print('\nLogin berhasil!')
                    break
                else:
                    coba_login += 1
                    sisa_coba = 3 - coba_login
                    if sisa_coba > 0:
                        print(f'\ Username atau Password salah! Sisa percobaan: {sisa_coba}')
            
            if login_berhasil == False:
                print('\ Anda telah gagal login 3 kali. Coba lagi nanti.')

        else:
            print('\ Pilihan tidak valid!')

    while user_login != '':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'=========================================')
        print(f'       Login sebagai {user_login} ({role_user})')
        print(f'=========================================')

        if role_user == 'admin':
            print('1. Tambah Data Pendonor')
            print('2. Lihat Data Pendonor')
            print('3. Ubah Data Pendonor')
            print('4. Hapus Data Pendonor')
            print('5. Catat Riwayat Donor')
            print('6. Logout')
            print('-----------------------------------------')
            pilihan_menu = input('Pilih Menu (1-6): ')

#c
            if pilihan_menu == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- TAMBAH DATA PENDONOR BARU ---')  #tambah data nur bru mau donor
                nama = input('Nama Lengkap        : ')
                umur_str = input('Umur                : ') 
                bb_str = input('Berat Badan (kg)    : ')
                goldar = input('Golongan Darah      : ')
                telepon = input('Nomor Telepon       : ')
                id_terakhir += 1
                donor_baru = [id_terakhir, nama, int(umur_str), int(bb_str), goldar, telepon, 0]
                data_donor.append(donor_baru)
                print('\n Data berhasil ditambahkan!')
                input('< kembali(0)')

#r
            elif pilihan_menu == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- DAFTAR SEMUA PENDONOR ---')
                if data_donor == []:
                    print('Belum ada data pendonor yang tersimpan.')
                else:
                    print('-' * 105)
                    print(f'{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}')
                    print('-' * 105)
                    for donor in data_donor:
                        jumlah_donor = donor[6]
                        penghargaan = '-'
                        if jumlah_donor >= 10:
                            penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5:
                            penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1:
                            penghargaan = "Sertifikat"
                        
                        print(f'{donor[0]:<4} | {donor[1]:<20} | {donor[2]:<5} | {donor[3]:<6} | {donor[4]:<8} | {donor[5]:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}')
                    print('-' * 105)
                input('< kembali(0)')

#u
            elif pilihan_menu == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- UBAH DATA PENDONOR ---')  #data michael salah bb nya
                if data_donor == []:
                    print('Belum ada data untuk diubah.')
                else:
                    print('-' * 105)
                    print(f'{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}')
                    print('-' * 105)
                    for donor in data_donor:
                        jumlah_donor = donor[6]
                        penghargaan = '-'
                        if jumlah_donor >= 10:
                            penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5:
                            penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1:
                            penghargaan = "Sertifikat"
                        
                        print(f'{donor[0]:<4} | {donor[1]:<20} | {donor[2]:<5} | {donor[3]:<6} | {donor[4]:<8} | {donor[5]:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}')
                    print('-' * 105)
                    id_input = input('\nMasukkan ID data yang ingin diubah: ')
                    id_edit = int(id_input)
                    pendonor_ditemukan = []
                    for donor in data_donor:
                        if donor[0] == id_edit:
                            pendonor_ditemukan = donor
                            break

                    if pendonor_ditemukan != []:
                        print('\n(Kosongi jika tidak ingin diubah)')
                        
                        input_nama = input(f'Nama baru ({pendonor_ditemukan[1]}): ')
                        if input_nama == '':
                            nama_baru = pendonor_ditemukan[1]
                        else:
                            nama_baru = input_nama
                        
                        input_umur = input(f'Umur baru ({pendonor_ditemukan[2]}): ')
                        if input_umur == '':
                            umur_baru = (pendonor_ditemukan[2])
                        else:
                            umur_baru = input_umur
                        
                        input_bb = input(f'BB baru ({pendonor_ditemukan[3]}): ')
                        if input_bb == '':
                            bb_baru = (pendonor_ditemukan[3])
                        else:
                            bb_baru = input_bb

                        input_goldar = input(f'Goldar baru ({pendonor_ditemukan[4]}): ')
                        if input_goldar == '':
                            goldar_baru = pendonor_ditemukan[4]
                        else:
                            goldar_baru = input_goldar
                        
                        input_telepon = input(f'Telepon baru ({pendonor_ditemukan[5]}): ')
                        if input_telepon == '':
                            telepon_baru = pendonor_ditemukan[5]
                        else:
                            telepon_baru = input_telepon
                        
                        pendonor_ditemukan[1] = nama_baru
                        pendonor_ditemukan[2] = int(umur_baru)
                        pendonor_ditemukan[3] = int(bb_baru)  
                        pendonor_ditemukan[4] = goldar_baru
                        pendonor_ditemukan[5] = telepon_baru
                        print('\n Data berhasil diubah!')
                    else:
                        print(f'\n Data dengan ID {id_edit} tidak ditemukan.')
                input('< kembali(0)')

#d
            elif pilihan_menu == '4':
                print('--- HAPUS DATA PENDONOR ---') #hapus fred karna sdh meninggal (pendonor non aktif)
                if data_donor == []:
                    print('Belum ada data untuk dihapus.')
                else:
                    print('-' * 105)
                    print(f'{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}')
                    print('-' * 105)
                    for donor in data_donor:
                        jumlah_donor = donor[6]
                        penghargaan = '-'
                        if jumlah_donor >= 10:
                            penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5:
                            penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1:
                            penghargaan = "Sertifikat"
                        print(f'{donor[0]:<4} | {donor[1]:<20} | {donor[2]:<5} | {donor[3]:<6} | {donor[4]:<8} | {donor[5]:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}')
                    print('-' * 105)
                    id_input = input('\nMasukkan ID data yang ingin dihapus: ')

                    if id_input:
                        id_hapus = int(id_input)
                        pendonor_ditemukan = []
                        for donor in data_donor:
                            if donor[0] == id_hapus:
                                pendonor_ditemukan = donor
                                break
                        if pendonor_ditemukan != []:
                            konfirmasi = input(f'Yakin ingin menghapus {pendonor_ditemukan[1]}? (y/n): ')
                            if konfirmasi == 'y':
                                data_donor.remove(pendonor_ditemukan)
                                print('\n Data berhasil dihapus!')
                            else:
                                print('\nPenghapusan dibatalkan.')
                        else:
                            print(f'\n Data dengan ID {id_hapus} tidak ditemukan.')
                    else:
                        print('\n ID harus berupa angka!')
                input('< kembali(0)')

            elif pilihan_menu == '5': #riwayat
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- CATAT RIWAYAT DONOR ---')
                if data_donor == []:
                    print('Belum ada data pendonor.')
                else:
                    print(f"{'ID':<4} | {'Nama':<20} | {'Jumlah Donor Saat Ini':<25}")
                    print('-' * 55)
                    for donor in data_donor:
                        print(f"{donor[0]:<4} | {donor[1]:<20} | {donor[6]}x")
                    print('-' * 55)
                    id_input = input('\nID pendonor: ')
                    id_donor = int(id_input)
                    pendonor_ditemukan = []
                    for donor in data_donor:
                        if donor[0] == id_donor:
                            pendonor_ditemukan = donor
                            break
                    
                    if pendonor_ditemukan != []:
                        pendonor_ditemukan[6] += 1
                        print(f"\nBerhasil! Riwayat donor {pendonor_ditemukan[1]} kini menjadi {pendonor_ditemukan[6]} kali.")
                    else:
                        print(f"\nData dengan ID {id_donor} tidak ditemukan.")
                input('< kembali(0)')

            elif pilihan_menu == '6': #logout
                user_login = ''
                role_user = ''
                print('\nAnda telah logout.')
            
            else:
                print('\n Pilihan tidak valid!')

#bukan admin
        else:
            print('1. Lihat Data Pendonor')
            print('2. Logout')
            print('-----------------------------------------')
            pilihan_menu = input('Pilih Menu (1/2): ')

            if pilihan_menu == '1': #r user
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- DAFTAR SEMUA PENDONOR ---')
                if data_donor == []:
                    print('Belum ada data pendonor yang tersimpan.')
                else:
                    print(f'{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}')
                    print('-' * 105)
                    for donor in data_donor:
                        jumlah_donor = donor[6]
                        penghargaan = "-"
                        if jumlah_donor >= 10:
                            penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5:
                            penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1:
                            penghargaan = "Sertifikat"
                        
                        print(f'{donor[0]:<4} | {donor[1]:<20} | {donor[2]:<5} | {donor[3]:<6} | {donor[4]:<8} | {donor[5]:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}')
                    print('-' * 105)
                input('< kembali(0)')

            elif pilihan_menu == '2': #logout user
                user_login = ''
                role_user = ''
                print('\nAnda telah logout.')
            
            else:
                print('\n Pilihan tidak valid!')