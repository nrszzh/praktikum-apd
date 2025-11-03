import time
from display import clear_screen

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
    time.sleep(1)

def login_valid(username, password, daftar_akun):
    if username in daftar_akun and daftar_akun[username]['password'] == password:
        return True, daftar_akun[username]['role']
    return False, None