import os

akun_user = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'nur': {'password': '018', 'role': 'user'}
}

data_donor = {
    1: {'nama': 'Fred Brailey', 'umur': 93, 'bb': 71, 'goldar': 'O+', 'telepon': '081258016876', 'jumlah_donor': 135},
    2: {'nama': 'Cristiano Ronaldo', 'umur': 40, 'bb': 83, 'goldar': 'AB+', 'telepon': '081987654321', 'jumlah_donor': 34},
    3: {'nama': 'Hrithik Roshan', 'umur': 51, 'bb': 77, 'goldar': 'B-', 'telepon': '081987654321', 'jumlah_donor': 41},
    4: {'nama': 'Michael Octaviano', 'umur': 50, 'bb': 88, 'goldar': 'O+', 'telepon': '081987654321', 'jumlah_donor': 11},
    5: {'nama': 'Diko Saputra', 'umur': 22, 'bb': 55, 'goldar': 'B+', 'telepon': '081987654321', 'jumlah_donor': 4},
}
id_terakhir = 5
user_login = ''
role_user = ''

while True:
    while user_login == '':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=========================================')
        print('        SISTEM CEK DONOR DARAH           ')
        print('=========================================')
        print('1. Login')
        print('2. Register')
        print('3. Keluar')
        print('-----------------------------------------')
        pilihan_awal = input('Pilih Opsi (1/2/3): ')

        if pilihan_awal == '3':
            print('\nAnda telah keluar')
            exit()

        elif pilihan_awal == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- REGISTER ---')
            username_baru = input('Masukkan Username Baru : ')
            password_baru = input('Masukkan Password Baru : ')
            if username_baru in akun_user:
                print('Username sudah terdaftar! Silahkan coba lagi.')
            elif username_baru == "" or password_baru == "":
                print('Username dan Password tidak boleh kosong')
            else:
                akun_user[username_baru] = {'password': password_baru, 'role': 'user'}
                print('Akun berhasil dibuat! Silahkan login.')

        elif pilihan_awal == '1':
            coba_login = 0
            login_berhasil = False
            while coba_login < 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- LOGIN ---')
                print(f'Percobaan ke-{coba_login + 1} dari 3')
                username = input('Username : ')
                password = input('Password : ')
                if username == "" or password == "":
                    print('Username dan Password tidak boleh kosong')
                    coba_login += 1
                    continue
                if username in akun_user:
                    if akun_user[username]['password'] == password:
                        user_login = username
                        role_user = akun_user[username]['role']
                        login_berhasil = True
                        print('Login berhasil!')
        
                        break
                coba_login += 1
                sisa_coba = 3 - coba_login
                if sisa_coba > 0:
                    print(f'Username atau Password salah! Sisa percobaan: {sisa_coba}')
            if login_berhasil == False:
                print('Login Gagal, kembali ke menu awal...')

        else:
            print('Pilihan tidak valid!')

    while user_login != '':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'=========================================')
        print(f'      Login sebagai {user_login} ({role_user})')
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
                print('--- TAMBAH DATA PENDONOR BARU ---') #misal tambah data nur bru mau donor
                nama = input('Nama Lengkap      : ')
                umur_str = input('Umur              : ')
                bb_str = input('Berat Badan (kg)  : ')
                goldar = input('Golongan Darah    : ')
                telepon = input('Nomor Telepon     : ')
                id_terakhir += 1
                donor_baru_dict = {
                    'nama': nama,
                    'umur': int(umur_str),
                    'bb': int(bb_str),
                    'goldar': goldar,
                    'telepon': telepon,
                    'jumlah_donor': 0 
                }
                data_donor[id_terakhir] = donor_baru_dict
                print('Data berhasil ditambahkan')
                input('< kembali(0)')

#r
            elif pilihan_menu == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- DAFTAR SEMUA PENDONOR ---')
                if data_donor == {}:
                    print('Belum ada data pendonor yang tersimpan.')
                else:
                    print('-' * 105)
                    print(f"{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}")
                    print('-' * 105)
                    for donor_id, donor_info in data_donor.items():
                        jumlah_donor = donor_info['jumlah_donor']
                        penghargaan = '-'
                        if jumlah_donor >= 10: penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5: penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1: penghargaan = "Sertifikat"
                        print(f"{donor_id:<4} | {donor_info['nama']:<20} | {donor_info['umur']:<5} | {donor_info['bb']:<6} | {donor_info['goldar']:<8} | {donor_info['telepon']:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}")
                    print('-' * 105)
                input('< kembali(0)')

#u
            elif pilihan_menu == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- UBAH DATA PENDONOR ---') #misal data michael bb nya salah
                if data_donor == {}:
                    print('Belum ada data untuk diubah.')
                else:
                    print('-' * 105)
                    print(f"{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}")
                    print('-' * 105)
                    for donor_id, donor_info in data_donor.items():
                        jumlah_donor = donor_info['jumlah_donor']
                        penghargaan = '-'
                        if jumlah_donor >= 10: penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5: penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1: penghargaan = "Sertifikat"
                        print(f"{donor_id:<4} | {donor_info['nama']:<20} | {donor_info['umur']:<5} | {donor_info['bb']:<6} | {donor_info['goldar']:<8} | {donor_info['telepon']:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}")
                    print('-' * 105)
                    id_input = input('\nMasukkan ID data yang ingin diubah: ')
                    if not id_input.isdigit():
                        print('ID harus berupa angka')
                    else:
                        id_edit = int(id_input)
                        if id_edit not in data_donor:
                            print(f'ID {id_edit} tidak ditemukan.')
                        else:
                            pendonor_ditemukan = data_donor[id_edit]
                            print('(Kosongi jika tidak ingin diubah)')

                            nama_baru = input(f"Nama baru ({pendonor_ditemukan['nama']}): ")
                            umur_baru_str = input(f"Umur baru ({pendonor_ditemukan['umur']}): ")
                            bb_baru_str = input(f"BB baru ({pendonor_ditemukan['bb']}): ")
                            goldar_baru = input(f"Goldar baru ({pendonor_ditemukan['goldar']}): ")
                            telepon_baru = input(f"Telepon baru ({pendonor_ditemukan['telepon']}): ")

                            update_berhasil = True
                            if update_berhasil:
                                print('Data berhasil diubah!')
                input('< kembali(0)')

#d
            elif pilihan_menu == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- HAPUS DATA PENDONOR ---')  #misal hapus fred karna sdh meninggal (pendonor non aktif)
                if data_donor == {}:
                    print('Belum ada data untuk dihapus.')
                else:
                    print('-' * 105)
                    print(f'{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}')
                    print('-' * 105)
                    for donor_id, donor_info in data_donor.items():
                        jumlah_donor = donor_info['jumlah_donor']
                        penghargaan = '-'
                        if jumlah_donor >= 10: penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5: penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1: penghargaan = "Sertifikat"
                        print(f"{donor_id:<4} | {donor_info['nama']:<20} | {donor_info['umur']:<5} | {donor_info['bb']:<6} | {donor_info['goldar']:<8} | {donor_info['telepon']:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}")
                    id_input = input('\nMasukkan ID data yang ingin dihapus: ')
                    if not id_input.isdigit():
                        print('ID harus berupa angka!')
                    else:
                        id_hapus = int(id_input)
                        if id_hapus not in data_donor:
                            print(f'ID {id_hapus} tidak ditemukan.')
                        else:
                            nama_hapus = data_donor[id_hapus]['nama']
                            konfirmasi = input(f'Yakin ingin menghapus data {nama_hapus} (ID: {id_hapus})? (y/n): ')
                            if konfirmasi == 'y':
                                del data_donor[id_hapus]
                                print('Data berhasil dihapus')
                            else:
                                print('Penghapusan dibatalkan.')
                input('< kembali(0)')

#menu 5
            elif pilihan_menu == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- CATAT RIWAYAT DONOR ---')
                if data_donor == {}:
                    print('Belum ada data pendonor.')
                else:
                    print('-' * 55)
                    print(f"{'ID':<4} | {'Nama':<20} | {'Jumlah Donor Saat Ini':<25}")
                    print('-' * 55)
                    for donor_id, donor_info in data_donor.items():
                        print(f"{donor_id:<4} | {donor_info['nama']:<20} | {donor_info['jumlah_donor']}x")
                    print('-' * 55)

                    id_input = input('ID pendonor yg baru donor: ')
                    if not id_input.isdigit():
                        print('ID harus berupa angka!')
                    else:
                        id_donor = int(id_input)
                        if id_donor not in data_donor:
                            print(f"ID {id_donor} tidak ditemukan.")
                        else:
                            data_donor[id_donor]['jumlah_donor'] += 1
                            nama_pendonor = data_donor[id_donor]['nama']
                            jumlah_baru = data_donor[id_donor]['jumlah_donor']
                            print(f"Berhasil! Riwayat donor {nama_pendonor} sekarang adalah {jumlah_baru} kali.")
                input('< kembali(0)')

#menu 6
            elif pilihan_menu == '6':
                user_login = ''
                role_user = ''
                print('\nAnda telah logout.')
            else:
                print('Pilihan menu tidak valid!')


#bukan admin
        else:
            print('1. Lihat Data Pendonor')
            print('2. Logout')
            print('-----------------------------------------')
            pilihan_menu = input('Pilih Menu (1/2): ')

#read user
            if pilihan_menu == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- DAFTAR SEMUA PENDONOR ---')
                if data_donor == {}:
                    print('Belum ada data pendonor yang tersimpan.')
                else:
                    print('-' * 105)
                    print(f"{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}")
                    print('-' * 105)
                    for donor_id, donor_info in data_donor.items():
                        jumlah_donor = donor_info['jumlah_donor']
                        penghargaan = "-"
                        if jumlah_donor >= 10: penghargaan = "Satya Lencana"
                        elif jumlah_donor >= 5: penghargaan = "Medali Emas"
                        elif jumlah_donor >= 1: penghargaan = "Sertifikat"
                        print(f"{donor_id:<4} | {donor_info['nama']:<20} | {donor_info['umur']:<5} | {donor_info['bb']:<6} | {donor_info['goldar']:<8} | {donor_info['telepon']:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}")
                    print('-' * 105)
                input('< kembali (0)')

#logout usr
            elif pilihan_menu == '2':
                user_login = ''
                role_user = ''
                print('Anda telah logout.')
            else:
                print('Pilihan tidak valid!')