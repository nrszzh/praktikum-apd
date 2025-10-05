import os

print('==============================================')
print('     SELAMAT DATANG DI BRAINROT COFFEE      ')
print('==============================================')

status_member = input('Apakah Anda member? (y/n) : ')

username_valid = 'nur'
password_valid = '018'

while True:
    login_berhasil = False
    diskon_rate = 0.0
    total_harga = 0
    keranjang = ''

    #login member
    if status_member == 'y':
        print('\n--- Silakan Login Terlebih Dahulu ---')
        for percobaan in range(3):
            print(f'--- (Percobaan {percobaan + 1} dari 3) ---')
            input_username = input('Masukkan Username: ')
            input_password = input('Masukkan Password: ')

            if input_username == '' or input_password == '':
                print('Username atau Password tidak boleh kosong')
                if percobaan < 2:
                    print(f'Sisa percobaan: {2 - percobaan}')
                continue

            if input_username == username_valid and input_password == password_valid:
                login_berhasil = True
                diskon_rate = 0.15
                print('Login Berhasil! Selamat Datang Member Brainrot Coffee')
                break
            else:
                print('Username atau Password salah, Coba Lagi!')
                if percobaan < 2:
                    print(f'Sisa percobaan: {2 - percobaan}')
        
        if not login_berhasil:
            print('\nLogin Gagal, Transaksi Non Member')

    if not login_berhasil:
        print('\n--- Anda memesan sebagai non member ---')

    #pemesanan
    while True:
        print('\nMenu Brainrot Coffee')
        print('1. Cappucino Assasino - Rp. 20.000 ')
        print('2. Ballerina Cappucina - Rp. 18.000 ')
        print('3. Espresso Signora - Rp. 15.000 ')
        print('4. Checkout')
        print('---------------------------------')
        if total_harga > 0:
            print(f'Total Belanja Sementara: Rp {total_harga:,}')
        
        pilihan = input('\nMasukkan kode menu pesanan (1/2/3): ')

        if pilihan == '1':
            total_harga += 20000
            keranjang += '- Cappucino Assasino   Rp 20,000\n'
            print('-> "Cappucino Assasino" telah ditambahkan ke keranjang.')
        elif pilihan == '2':
            total_harga += 18000
            keranjang += '- Ballerina Cappucina  Rp 18,000\n'
            print('-> "Ballerina Cappucina" telah ditambahkan ke keranjang.')
        elif pilihan == '3':
            total_harga += 15000
            keranjang += '- Espresso Signora     Rp 15,000\n'
            print('-> "Espresso Signora" telah ditambahkan ke keranjang.')
        elif pilihan == '4':
            print('Pesanan selesai, siap untuk pembayaran')
            break
        else:
            print('Pilihan tidak valid, coba lagi')

    #struk
    os.system('cls')
    print('\n\n==============================================')
    print('              STRUK PEMBAYARAN              ')
    print('==============================================')
    
    if keranjang == "":
        print('Anda tidak membeli apa pun')
    else:
        print('Produk yang dibeli: ')
        print(keranjang)
        print('----------------------------------------------')

        jumlah_diskon = int(total_harga *diskon_rate)
        total_bayar = total_harga - jumlah_diskon

        if login_berhasil:
            print(f'Total Harga          : Rp {total_harga}')
            print(f'Diskon Member (15%)  : Rp {jumlah_diskon}')
            print('----------------------------------------------')
            print(f'Total yang Harus Dibayar : Rp {total_bayar}')
        else:
            print(f'Total yang Harus Dibayar : Rp {total_bayar}')

    print('==============================================')
    print('         Terima kasih telah membeli!        ')
    print('==============================================')

    #apakah ingin traksaksi
    transaksi_lagi = input('\nApakah Anda ingin memulai transaksi baru? (y/n): ')
    if transaksi_lagi != 'y':
        break

print('\nTerimakasih, Jangan lupa untuk berkunjung lagi!')