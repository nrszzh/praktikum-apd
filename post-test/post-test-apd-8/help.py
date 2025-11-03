def hitung_penghargaan(jumlah_donor):
    if jumlah_donor >= 10: return "Satya Lencana"
    elif jumlah_donor >= 5: return "Medali Emas"
    elif jumlah_donor >= 1: return "Sertifikat"
    else: return "-"

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
    jawaban = input(isi).strip().lower()
    if jawaban == 'y': return True
    elif jawaban == 'n': return False
    else:
        print("Pilihan tidak valid. Masukkan 'y' atau 'n'")
        return konfirmasi(isi)