import util_function, load_only

name_folders = load_only.nama_folder # Mengambil nama folder yang di load pada module load_only.py

'''------------------------------------------------------------ DATA USER ------------------------------------------------------------'''

'''-------------------- Membaca Data --------------------'''
datauser, len_user = util_function.read_csv("user.csv", name_folders) # Membaca data user dan panjang data dari file 'user.csv'
'''-------------------- Membaca Data --------------------'''


'''-------------------- Membuat Matriks Data --------------------'''
# TODO: Membuat Matriks Data User
data_user = [[] for i in range(len_user)] # Membuat list data sepanjang data user
for i in range(len_user):   # Loop untuk mengisi matriks dengan data user
    data_user[i] = util_function.split_koma(datauser[i], 3) # Memisahkan string menjadi list dengan jumlah kolom sebanyak 3
'''-------------------- Membuat Matriks Data --------------------'''

'''------------------------------------------------------------ DATA USER ------------------------------------------------------------'''




'''------------------------------------------------------------ DATA CANDI ------------------------------------------------------------'''

'''-------------------- Membaca Data --------------------'''
datacandi, len_candi = util_function.read_csv("candi.csv", name_folders) # Membaca data candi dan panjang data dari file 'candi.csv'
'''-------------------- Membaca Data --------------------'''


'''-------------------- Membuat Matriks Data --------------------'''
# TODO: Membuat Matriks Data Candi
data_candi = [[] for i in range(len_candi)] # Membuat list data sepanjang data candi
for i in range(len_candi):  # Loop untuk mengisi matriks dengan data candi
    data_candi[i] = util_function.split_koma(datacandi[i], 6) # Memisahkan string menjadi list dengan jumlah kolom sebanyak 6
'''-------------------- Membuat Matriks Data --------------------'''


'''-------------------- Menambahkan Harga Candi --------------------'''
for i in range(len_candi): # Loop untuk mengisi list temporary dengan data lama
    if data_candi[i] != []: # Saat data yang mau diisikan tidak kosong
        data_candi[i][5] = 10000 * int(data_candi[i][2]) + 15000 * int(data_candi[i][3]) + 7500 * int(data_candi[i][4]) # Men-Assign harga ke index terakhir
'''-------------------- Menambahkan Harga Candi --------------------'''

'''------------------------------------------------------------ DATA CANDI ------------------------------------------------------------'''




'''------------------------------------------------------------ DATA BAHAN BANGUNAN ------------------------------------------------------------'''

'''-------------------- Membaca Data --------------------'''
databahanbangunan = util_function.read_csv("bahan_bangunan.csv", name_folders)[0] # Membaca data bahan bangunan dari file 'bahan_bangunan.csv'
'''-------------------- Membaca Data --------------------'''


'''-------------------- Membuat Matriks Data --------------------'''
data_bahan_bangunan = [[]]
data_bahan_bangunan[0] = util_function.split_koma(databahanbangunan[1],3) # Memisahkan string menjadi list dengan jumlah kolom sebanyak 3
'''-------------------- Membuat Matriks Data --------------------'''

'''------------------------------------------------------------ DATA BAHAN BANGUNAN ------------------------------------------------------------'''




'''------------------------------------------------------------ DATA CANDI YANG DIHANCURKAN ------------------------------------------------------------'''

'''-------------------- Inisialisasi Awal --------------------'''
jumlah_candi_yang_dihancurkan = 0 # Inisialisasi awal untuk jumlah candi yang dihancurkan
'''-------------------- Inisialisasi Awal --------------------'''


'''-------------------- Cek Jumlah Data Kosong --------------------'''
for i in range(len_candi): # Loop untuk mengecek apakah ada data kosong atau tidak pada data candi (Apabila ada data kosong berarti candi tersebut telah dihancurkan)
    if data_candi[i] == []: # Saat ditemukan data kosong
        jumlah_candi_yang_dihancurkan += 1
'''-------------------- Cek Jumlah Data Kosong --------------------'''


'''-------------------- Mengisi Data Candi Yang Dihancurkan --------------------'''
index = 0 # Inisialisasi awal index pencacah list candi yang dihancurkan
id_candi_yang_dihancurkan = [0 for i in range(jumlah_candi_yang_dihancurkan)] # List untuk tempat menampung id candi yang telah dihancurkan pada baris kosong di data candi

for i in range(len_candi): # Loop untuk mengisi list id candi yang dihancurkan
    if data_candi[i] == []: # Apabila ditemukan baris kosong di data candi (data candi yang telah dihancurkan)
        id_candi_yang_dihancurkan[index] = i + 1 # Mengisi id candi yang dihancurkan
        index += 1
'''-------------------- Mengisi Data Candi Yang Dihancurkan --------------------'''

'''------------------------------------------------------------ DATA CANDI YANG DIHANCURKAN ------------------------------------------------------------'''




'''------------------------------------------------------------ DATA JIN PEMBANGUN YANG PERNAH MEMBANGUN DAN TERDAFTAR SEBAGAI PEMBANGUN ------------------------------------------------------------'''
# Yang pernah membangun disini yang dimaksud adalah ketika jin pernah membangun candi namun role nya diubah menjadi pengumpul
# Terdaftar sebagai pembangun merupakan jin yang terdaftar sebagai jin pembangun pada data user

'''-------------------- Jumlah Pembangun Yang Terdaftar --------------------'''
len_pembangun = 0 # Inisialisasi awal jumlah jin yang pernah membangun 
for i in range(len_user): # Loop untuk mencari jin pembangun pada data user
    if data_user[i][2] == "Pembangun": # Ketika jin memiliki role Pembangun
        len_pembangun += 1 # Jumlah jin bertambah 1 ketika ditemukan jin dengan role Pembangun
'''-------------------- Jumlah Pembangun Yang Terdaftar --------------------'''


'''-------------------- Mengisi Data Jin Yang Pernah Membangun Dengan Data User --------------------'''
data_jin_yang_pernah_membangun = ["" for i in range(len_pembangun)] # List tempat data jin yang pernah membangun 
j = 0 # Inisialisasi index pencacah list data jin yang pernah membangun

for i in range(len_user): # Loop untuk mengisi data jin yang pernah membangun dengan data user yang memiliki role Pembangun
    if data_user[i][2] == "Pembangun": # Ketika user memiliki role Pembangun
        data_jin_yang_pernah_membangun[j] = data_user[i][0] # Menginputkan nama jin pembangun ke data jin yang pernah membangun
        j += 1 # Index pencacah bertambah 1
'''-------------------- Mengisi Data Jin Yang Pernah Membangun Dengan Data User --------------------'''


'''-------------------- Mengisi Data Jin Yang Pernah Membangun Dari Data Candi --------------------'''
for i in range(len_candi): # Loop untuk mengecek dan menambahkan data jin yang pernah membangun 
    if data_candi[i] != []: # Ketika data yang dicek tidak kosong
        cek = True # Inisialisasi awal kondisi pengecekan (True berarti jin yang membangun candi tidak ditemukan pada list data jin yang pernah membangun)

        for j in range(len_pembangun): # Loop untuk mengecek apakah jin yang membangun candi ada pada list data jin yang pernah membangun atau tidak
            if data_candi[i][1] == data_jin_yang_pernah_membangun[j]: # Kondisi saat jin yang membangun candi ditemukan pada list data jin yang pernah membangun
                cek = False # Kondisi pengecekan False berarti jin yang membangun candi ditemukan pada list data jin yang pernah membangun
        
        if cek: # Saat kondisi pengecekan True (saat jin yang membangun candi tidak ditemukan pada list data jin yang pernah membangun)
            len_pembangun += 1 # Jumlah jin yang pernah membangun bertambah 1
            temp_data_jin_yang_pernah_membangun = ["" for k in range(len_pembangun)] # Inisialisasi list sementara untuk mengisi data jin yang pernah membangun

            for k in range(len_pembangun-1): # Loop untuk mengisi list data jin yang pernah membangun dengan data lama
                temp_data_jin_yang_pernah_membangun[k] = data_jin_yang_pernah_membangun[k] # Mengisi list sementara dengan data lama

            temp_data_jin_yang_pernah_membangun[len_pembangun-1] = data_candi[i][1] # Mengisi list index terakhir dengan jin yang membangun candi 
            data_jin_yang_pernah_membangun = temp_data_jin_yang_pernah_membangun # Mengupdate data jin yang pernah membangun dengan data yang lebih baru (list temporary) 
'''-------------------- Mengisi Data Jin Yang Pernah Membangun Dari Data Candi --------------------'''

'''------------------------------------------------------------ DATA JIN PEMBANGUN YANG PERNAH MEMBANGUN DAN TERDAFTAR SEBAGAI PEMBANGUN ------------------------------------------------------------'''




'''------------------------------------------------------------ DATA STACK ------------------------------------------------------------'''
jumlah_stack = 1
undo_stack = [[data_candi, len_candi, data_user, len_user, data_jin_yang_pernah_membangun, len_pembangun, id_candi_yang_dihancurkan, jumlah_candi_yang_dihancurkan]] # Data awal stack

# Struktur stack
"""
undo_stack = [[data candi, panjang data candi, data user, panjang data user, data jin yang pernah membangun, panjang data jin yang pernah membangun, id candi yang hancur, jumlah id candi yang hancur],[...],...]
undo_stack[...][0] = Data candi
undo_stack[...][1] = Panjang data candi
undo_stack[...][2] = Data user
undo_stack[...][3] = Panjang data user
undo_stack[...][4] = Data jin yang pernah membangun
undo_stack[...][5] = Panjang data jin yang pernah membangun
undo_stack[...][6] = Id candi yang hancur (tidak ada pada data)
undo_stack[...][7] = Banyak id candi yang hancur
"""
'''------------------------------------------------------------ DATA STACK ------------------------------------------------------------'''