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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header_program():
    print('=========================================')
    print('        SISTEM CEK DONOR DARAH           ')
    print('=========================================')

def hitung_penghargaan(jumlah_donor):
    if jumlah_donor >= 10: return "Satya Lencana"
    elif jumlah_donor >= 5: return "Medali Emas"
    elif jumlah_donor >= 1: return "Sertifikat"
    else: return "-"

def tampilkan_tabel_donor(data):
    if not data:
        print('Belum ada data pendonor yang tersimpan.')
        return False
    print('-' * 105)
    print(f"{'ID':<4} | {'Nama':<20} | {'Umur':<5} | {'BB(kg)':<6} | {'Goldar':<8} | {'Telepon':<15} | {'Jumlah Donor':<13} | {'Penghargaan':<15}")
    print('-' * 105)
    for donor_id, donor_info in data.items():
        jumlah_donor = donor_info['jumlah_donor']
        penghargaan = hitung_penghargaan(jumlah_donor)
        print(f"{donor_id:<4} | {donor_info['nama']:<20} | {donor_info['umur']:<5} | {donor_info['bb']:<6} | {donor_info['goldar']:<8} | {donor_info['telepon']:<15} | {str(jumlah_donor) + 'x':<13} | {penghargaan:<15}")
    print('-' * 105)
    return True

def register_user(daftar_akun):
    clear_screen()
    print('--- REGISTER ---')
    username_baru = input('Masukkan Username Baru : ').strip()
    password_baru = input('Masukkan Password Baru : ').strip()
    if not username_baru or not password_baru:
        print('Username dan Password tidak boleh kosong')
    elif username_baru in daftar_akun:
        print('Username sudah terdaftar! Silahkan coba lagi.')
    else:
        daftar_akun[username_baru] = {'password': password_baru, 'role': 'user'}
        print('Akun berhasil dibuat! Silahkan login.')

def login_valid(username, password, daftar_akun):
    if username in daftar_akun and daftar_akun[username]['password'] == password:
        return True, daftar_akun[username]['role']
    return False, None

def input_id(isi):
    while True:
        id_str = input(isi).strip()
        if not id_str:
            print('ID tidak boleh kosong')
            continue
        try:
            id_int = int(id_str)
            if id_int > 0: return id_int
            else: print('ID harus berupa angka positif')
        except ValueError: print('ID harus berupa angka')

def apakah_data_kosong(data):
    return data == {}

def konfirmasi(isi):
    jawaban = input(isi).strip()
    if jawaban == 'y': return True
    elif jawaban == 'n': return False
    else:
        print("Pilihan tidak valid. Masukkan 'y' atau 'n'")
        return konfirmasi(isi)

#c
def menu_tambah_donor():
    global id_terakhir
    clear_screen()
    print('--- TAMBAH DATA PENDONOR BARU ---') #tambah si nur bru mau donor
    tampilkan_tabel_donor(data_donor)
    nama = input('Nama Lengkap      : ').strip()
    umur_str = input('Umur              : ').strip()
    bb_str = input('Berat Badan (kg)  : ').strip()
    goldar = input('Golongan Darah    : ').strip()
    telepon = input('Nomor Telepon     : ').strip()
    if not nama or not umur_str or not bb_str or not goldar or not telepon:
        print('Semua harus diisi!')
    else:
        try:
            umur = int(umur_str)
            bb = int(bb_str)
            if umur <= 0 or bb <= 0:
                print('Umur dan Berat Badan harus angka positif')
            else:
                id_terakhir += 1
                donor_baru_dict = {'nama': nama, 'umur': umur, 'bb': bb, 'goldar': goldar, 'telepon': telepon, 'jumlah_donor': 0}
                data_donor[id_terakhir] = donor_baru_dict
                print('Data berhasil ditambahkan!')
        except ValueError:
            print('Umur dan Berat Badan harus berupa angka!')

    input('< kembali(0)')

#r
def menu_lihat_donor():
    clear_screen()
    print('--- DAFTAR SEMUA PENDONOR ---')
    tampilkan_tabel_donor(data_donor)
    input('< kembali(0)')

#u
def menu_ubah_donor():
    clear_screen()
    print('--- UBAH DATA PENDONOR ---') #misal data michael(4) bb nya salah
    if not tampilkan_tabel_donor(data_donor):
        input('< kembali(0)')
        return
    id_ubah = input_id('Masukkan ID data yang ingin diubah: ')
    if id_ubah not in data_donor:
        print(f'ID {id_ubah} tidak ditemukan.')
    else:
        pendonor_ditemukan = data_donor[id_ubah]
        print('(Kosongi jika tidak ingin diubah)')
        nama_baru = input(f'Nama baru ({pendonor_ditemukan['nama']}): ').strip()
        umur_baru_str = input(f'Umur baru ({pendonor_ditemukan['umur']}): ').strip()
        bb_baru_str = input(f'BB baru ({pendonor_ditemukan['bb']}): ').strip()
        goldar_baru = input(f'Goldar baru ({pendonor_ditemukan['goldar']}): ').strip()
        telepon_baru = input(f'Telepon baru ({pendonor_ditemukan['telepon']}): ').strip()
        pesan_error = []
        if nama_baru: pendonor_ditemukan['nama'] = nama_baru
        if umur_baru_str:
            try:
                umur_baru = int(umur_baru_str)
                if umur_baru > 0: pendonor_ditemukan['umur'] = umur_baru
                else: pesan_error.append('Umur harus positif')
            except ValueError: pesan_error.append('Input umur tidak valid (harus angka)')
        if bb_baru_str:
            try:
                bb_baru = int(bb_baru_str)
                if bb_baru > 0: pendonor_ditemukan['bb'] = bb_baru
                else: pesan_error.append('Berat badan harus positif')
            except ValueError: pesan_error.append('Input berat badan tidak valid (harus angka)')
        if goldar_baru: pendonor_ditemukan['goldar'] = goldar_baru
        if telepon_baru: pendonor_ditemukan['telepon'] = telepon_baru
        if not pesan_error: print('Data berhasil diubah')
    input('< kembali(0)')

#d
def menu_hapus_donor():
    clear_screen()
    print('--- HAPUS DATA PENDONOR ---') #misal hapus fred karna sdh meninggal (pendonor non aktif)
    if not tampilkan_tabel_donor(data_donor):
        input('< kembali(0)')
        return

    id_hapus = input_id('Masukkan ID data yang ingin dihapus: ')
    if id_hapus not in data_donor:
        print(f'ID {id_hapus} tidak ditemukan.')
    else:
        nama_hapus = data_donor[id_hapus]['nama']
        if konfirmasi(f'Yakin ingin menghapus data {nama_hapus} (ID: {id_hapus})? (y/n): '):
            del data_donor[id_hapus]
            print('Data berhasil dihapus')
        else:
            print('Penghapusan dibatalkan')
    input('< kembali(0)')

#menu 5
def menu_catat_riwayat():
    clear_screen()
    print('--- CATAT RIWAYAT DONOR ---')
    if not tampilkan_tabel_donor(data_donor):
        input('< kembali(0)')
        return

    id_donor = input_id('Masukkan ID pendonor yg baru donor: ')
    if id_donor not in data_donor:
        print(f'ID {id_donor} tidak ditemukan.')
    else:
        data_donor[id_donor]['jumlah_donor'] += 1
        nama_pendonor = data_donor[id_donor]['nama']
        jumlah_baru = data_donor[id_donor]['jumlah_donor']
        print(f'Berhasil! Riwayat donor {nama_pendonor} sekarang adalah {jumlah_baru} kali.')
    input('< kembali(0)')

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
            register_user(akun_user)
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
                    coba_login += 1
                    continue
                berhasil, role_hasil = login_valid(username, password, akun_user)
                if berhasil:
                    user_login = username
                    role_user = role_hasil
                    login_berhasil = True
                    print('Login berhasil')
                    break
                else:
                    coba_login += 1
                    sisa_coba = 3 - coba_login
                    if sisa_coba > 0:
                        print(f'Username atau Password salah! Sisa percobaan: {sisa_coba}')

            if not login_berhasil:
                print('Login Gagal, kembali ke menu awal...')
        else:
            print('Pilihan tidak valid!')

    #menu utama
    while user_login != '':
        clear_screen()
        header_program()
        print(f'      Login sebagai {user_login} ({role_user.upper()})')
        print(f'-----------------------------------------')

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
            else:
                print('Pilihan tidak valid!')

#user biasa
        else:
            print('1. Lihat Data Pendonor')
            print('2. Logout')
            print('-----------------------------------------')
            pilihan_menu = input('Pilih Menu (1/2): ').strip()

            if pilihan_menu == '1': menu_lihat_donor()
            elif pilihan_menu == '2':
                user_login = ''
                role_user = ''
                print('Anda telah logout.')
            else:
                print('Pilihan tidak valid!')