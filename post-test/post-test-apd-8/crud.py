import data
from view import clear_screen, tampilkan_tabel_donor
from help import input_id, konfirmasi

#c
def menu_tambah_donor():
    clear_screen()
    print('--- TAMBAH DATA PENDONOR BARU ---')
    print("\nData Saat Ini:")
    tampilkan_tabel_donor(data.data_donor) # Gunakan data.data_donor
    print("\nMasukkan data baru:")
    nama = input('Nama Lengkap      : ').strip()
    umur_str = input('Umur              : ').strip()
    bb_str = input('Berat Badan (kg)  : ').strip()
    goldar = input('Golongan Darah    : ').strip().upper()
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
                data.id_terakhir += 1 # Akses data.id_terakhir
                donor_baru_dict = {'nama': nama, 'umur': umur, 'bb': bb, 'goldar': goldar, 'telepon': telepon, 'jumlah_donor': 0}
                data.data_donor[data.id_terakhir] = donor_baru_dict # Akses data.data_donor
                print('Data berhasil ditambahkan!')
        except ValueError:
            print('Umur dan Berat Badan harus berupa angka!')

    input('< kembali(0)')

#r
def menu_lihat_donor():
    clear_screen()
    print('--- DAFTAR SEMUA PENDONOR ---')
    tampilkan_tabel_donor(data.data_donor)
    input('< kembali(0)')

#u
def menu_ubah_donor():
    clear_screen()
    print('--- UBAH DATA PENDONOR ---')
    if not tampilkan_tabel_donor(data.data_donor):
        input('< kembali(0)')
        return
    id_ubah = input_id('Masukkan ID data yang ingin diubah: ')
    if id_ubah not in data.data_donor:
        print(f'ID {id_ubah} tidak ditemukan.')
    else:
        pendonor_ditemukan = data.data_donor[id_ubah]
        print('(Kosongi jika tidak ingin diubah)')
        nama_baru = input(f'Nama baru ({pendonor_ditemukan['nama']}): ').strip()
        umur_baru_str = input(f'Umur baru ({pendonor_ditemukan['umur']}): ').strip()
        bb_baru_str = input(f'BB baru ({pendonor_ditemukan['bb']}): ').strip()
        goldar_baru = input(f'Goldar baru ({pendonor_ditemukan['goldar']}): ').strip().upper()
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
        if not pesan_error: 
            print('Data berhasil diubah')
        else:
            print('\nData diubah sebagian dengan error:')
            for msg in pesan_error: print(f" - {msg}")
            
    input('< kembali(0)')

#d
def menu_hapus_donor():
    clear_screen()
    print('--- HAPUS DATA PENDONOR ---')
    if not tampilkan_tabel_donor(data.data_donor):
        input('< kembali(0)')
        return

    id_hapus = input_id('Masukkan ID data yang ingin dihapus: ')
    if id_hapus not in data.data_donor:
        print(f'ID {id_hapus} tidak ditemukan.')
    else:
        nama_hapus = data.data_donor[id_hapus]['nama']
        if konfirmasi(f'Yakin ingin menghapus data {nama_hapus} (ID: {id_hapus})? (y/n): '):
            del data.data_donor[id_hapus]
            print('Data berhasil dihapus')
        else:
            print('Penghapusan dibatalkan')
    input('< kembali(0)')

#menu 5
def menu_catat_riwayat():
    clear_screen()
    print('--- CATAT RIWAYAT DONOR ---')
    if not tampilkan_tabel_donor(data.data_donor):
        input('< kembali(0)')
        return

    id_donor = input_id('Masukkan ID pendonor yg baru donor: ')
    if id_donor not in data.data_donor:
        print(f'ID {id_donor} tidak ditemukan.')
    else:
        data.data_donor[id_donor]['jumlah_donor'] += 1
        nama_pendonor = data.data_donor[id_donor]['nama']
        jumlah_baru = data.data_donor[id_donor]['jumlah_donor']
        print(f'Berhasil! Riwayat donor {nama_pendonor} sekarang adalah {jumlah_baru} kali.')
    input('< kembali(0)')