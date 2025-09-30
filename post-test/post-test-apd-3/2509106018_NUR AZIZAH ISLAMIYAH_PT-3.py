print("==============================================")
print("      SELAMAT DATANG DI BRAINROT COFFEE      ")
print("==============================================")

login_berhasil = False
diskon = 0.0
total_harga = 0
total_bayar = 0
jumlah_diskon = 0

#login member
status_member = input('Apakah anda member? (ya/tidak) : ')
if status_member == 'ya':
    print('\n--- Silakan Login Terlebih Dahulu ---')
    input_user = input('Masukkan Username: ')
    input_pass = input('Masukkan Password: ')
    username_valid = 'nur'
    password_valid = '018'
    login_berhasil = True if (input_user == username_valid and input_pass == password_valid) else False
    if login_berhasil:
        print('Login Berhasil, Selamat Datang Member Brainrot Coffee')
        diskon = 0.15
    else:
        print('Login Gagal, Coba Lagi!')

else:
    print('\n--- Anda memesan sebagai non member ---')
    login_berhasil = True
    diskon = 0.0

#menu
if login_berhasil:
    print('Menu Brainrot Coffee : ')
    print('1. Cappucino Assasino - Rp. 20.000 ')
    print('2. Ballerina Cappucina - Rp. 18.000 ')
    print('3. Espresso Signora - Rp. 15.000 ')
    pilihan = input('Masukkan kode menu pesanan : (1/2/3)')
    
    #pemesanan
    if pilihan == '1':
        nama_pesanan = 'Cappucino Assasino'
        harga_pesanan = 20000
    elif pilihan == '2':
        nama_pesanan = 'Ballerina Cappucina'
        harga_pesanan = 18000
    elif pilihan == '3':
        nama_pesanan = 'Espresso Signora'
        harga_pesanan = 15000
    else:
        print('\nPilihan tidak valid.')

    if harga_pesanan > 0:
        #quantity
        quantity = int(input(f'Berapa cup {nama_pesanan} yang ingin kamu beli? :'))
        if quantity < 1:
            quantity = 1

        total_harga = harga_pesanan *quantity
        jumlah_diskon = total_harga *diskon
        total_bayar = total_harga - jumlah_diskon

        print('\n========================================')
        print('             BRAINROT COFFEE             ')
        print('========================================')
        print(f'Pesanan            : {nama_pesanan}')
        print(f'Jumlah             : {quantity} Cup')
        print(f'Total Harga        : Rp{total_harga}')
        if diskon > 0:
            print(f'Diskon Member 15%  : Rp{jumlah_diskon}')
            print('---------------------------------------')
        print(f'Total Bayar        : Rp {total_bayar}')
        print('Terima kasih telah membeli!')