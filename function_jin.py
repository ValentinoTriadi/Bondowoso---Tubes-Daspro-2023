import util_function

'''------------------------------------------------------------ Cek User ------------------------------------------------------------'''
def Cek_User(username: str) -> bool:
    import tempdata

    '''-------------------- Inisialisasi Awal --------------------'''
    data = tempdata.data_user # Mengambil data user dan memasukan ke variabel lokal data
    sama = False # Inisialisasi awal (sama = False berarti tidak ada user pada data, sama = True berarti ada user pada data)
    '''-------------------- Inisialisasi Awal --------------------'''


    '''-------------------- Mengecek Username --------------------'''
    for i in range(2,tempdata.len_user): 
        if data[i][0] == username: # Saat user ditemukan pada data
            sama = True
    '''-------------------- Mengecek Username --------------------'''

    return sama # Mengembalikan informasi ada user pada data atau tidak

'''------------------------------------------------------------ Cek User ------------------------------------------------------------'''



'''------------------------------------------------------------ Ubah Role ------------------------------------------------------------'''
def ubah_role(role: str) -> str:
    import Visual

    '''-------------------- Mengecek Role --------------------'''
    if role == "Pengumpul": # Saat role jin awal adalah pengumpul

        '''-------------------- Input Opsi dan Validasi ------------------ --'''
        opsi = input(f'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ') # Meminta opsi atau konfirmasi user
        while opsi != "Y" and opsi != "N": # Validasi saat opsi yang diinputkan tidak sesuai dengan ketentuan
            Visual.render_screen(["Input salah! Masukan hanya (Y/N)"],1) # Pesan Kesalahan
            opsi = input(f'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ') # Meminta opsi atau konfirmasi user ulang
        '''-------------------- Input Opsi dan Validasi ------------------ --'''


        '''-------------------- Mengembalikan Tipe Jin Setelah Dirubah ------------------ --'''
        if opsi == "Y": # Saat user ingin merubah tipe jin
            return 'Pengumpul' # Mengembalikan tipe jin setelah dirubah
        else: # Saat user tidak jadi merubah tipe jin
            return 'Pembangun' # Mengembalikan tipe jin awal
        '''-------------------- Mengembalikan Tipe Jin Setelah Dirubah ------------------ --'''

    else: # Saat role jin awal adalah pembangun

        '''-------------------- Input Opsi dan Validasi ------------------ --'''
        opsi = input(f'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ') # Meminta opsi atau konfirmasi user
        while opsi != "Y" and opsi != "N": # Validasi saat opsi yang diinputkan tidak sesuai dengan ketentuan
            Visual.render_screen(["Input salah! Masukan hanya (Y/N)"],1) # Pesan Kesalahan
            opsi = input(f'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ') # Meminta opsi atau konfirmasi user ulang
        '''-------------------- Input Opsi dan Validasi ------------------ --'''


        '''-------------------- Mengembalikan Tipe Jin Setelah Dirubah ------------------ --'''
        if opsi == "Y": # Saat user ingin merubah tipe jin
            return 'Pengumpul' # Mengembalikan tipe jin setelah dirubah
        else: # Saat user tidak jadi merubah tipe jin
            return 'Pembangun' # Mengembalikan tipe jin awal
        '''-------------------- Mengembalikan Tipe Jin Setelah Dirubah ------------------ --'''

    '''-------------------- Mengecek Role --------------------'''

'''------------------------------------------------------------ Ubah Role ------------------------------------------------------------'''



'''------------------------------------------------------------ Hitung Jin ------------------------------------------------------------'''
def count_jin(jenis: str) -> int:
    import tempdata

    '''-------------------- Inisialisasi Awal --------------------'''
    data = tempdata.data_user # mengambil data user dan memasukan ke variabel lokal
    count = 0 # Jumlah awal jin dengan role tertentu
    '''-------------------- Inisialisasi Awal --------------------'''


    '''-------------------- Loop Untuk Menghitung Jumlah Jin Bertipe Tertentu --------------------'''
    for i in range(tempdata.len_user):
        if data[i][2] == jenis: # Saat jin memiliki role sesuai dengan yang dicari
            count += 1
    '''-------------------- Loop Untuk Menghitung Jumlah Jin Bertipe Tertentu --------------------'''

    return count # Mengembalikan jumlah jin yang bertipe tertentu

'''------------------------------------------------------------ Hitung Jin ------------------------------------------------------------'''



'''------------------------------------------------------------ Cari Jin Terajin/Termalas ------------------------------------------------------------'''
def jinter(rajin: bool) -> str:
    import tempdata

    '''-------------------- Inisialisasi Awal --------------------'''
    datacandi = tempdata.data_candi # Mengisi variabel lokal dengan data candi
    listpembangun = tempdata.data_jin_yang_pernah_membangun # Mengisi variabel lokal dengan data jin yang pernah membangun
    '''-------------------- Inisialisasi Awal --------------------'''


    '''-------------------- Menghitung Jumlah Candi Yang Dibangun --------------------'''
    jumlah_yg_dibangun_jin = [0 for i in range(tempdata.len_pembangun)] # Inisialisasi list baru sebagai tempat penyimpanan jumlah candi yang dibangun oleh jin
    
    for i in range(tempdata.len_candi): # Loop untuk mencacah data candi
        for j in range(tempdata.len_pembangun): # Loop untuk mencacah user yg bangun candi
            if datacandi[i] != []: # Saat data candi tidak kosong (Ada data candi yang kosong saat candi tersebut dihancurkan)
                if datacandi[i][1] == listpembangun[j]: # Saat jin yang membangun candi sesuai dengan data jin pada list user yang membangun candi
                    jumlah_yg_dibangun_jin[j]+=1 # Menambah jumlah candi yang dibangun jin tersebut
    '''-------------------- Menghitung Jumlah Candi Yang Dibangun --------------------'''


    '''-------------------- Jin Terajin/Termalas --------------------'''
    
    if rajin: # Saat ingin mengembalikan jin terajin

        '''-------------------- Inisialisasi Awal --------------------'''
        maks = util_function.maksimum(jumlah_yg_dibangun_jin, tempdata.len_pembangun) # Mencari jumlah candi terbanyak yang dibangun oleh jin
        jumlah_jin_terajin = 0 # Inisialisasi awal sebagai tempat jumlah jin dengan jumlah candi yang dibangun sama dan terbanyak
        '''-------------------- Inisialisasi Awal --------------------'''


        '''-------------------- Mencari Jumlah Jin Terajin --------------------'''
        for i in range(tempdata.len_pembangun):
            if jumlah_yg_dibangun_jin[i] == maks: # Saat jumlah candi yang dibangun jin merupakan jumah candi terbanyak
                jumlah_jin_terajin +=1
        '''-------------------- Mencari Jumlah Jin Terajin --------------------'''


        '''-------------------- Membuat List Jin Terajin --------------------'''
        list_terajin = ['' for i in range(jumlah_jin_terajin)] # Inisialisasi awal list dengan jumlah elemen sebanyak jumlah jin terajin
        index = 0 # Index untuk elemen list jin terajin
        for i in range(tempdata.len_pembangun): # Loop untuk mengisi list jin terajin
            if jumlah_yg_dibangun_jin[i] == maks: # Jika jumlah candi yang dibangun oleh jin merupakan jumlah candi terbanyak
                list_terajin[index] = listpembangun[i] # Memasukan nama jin ke dalam data jin terajin
                index += 1
        '''-------------------- Membuat List Jin Terajin --------------------'''

                
        '''-------------------- Mengembalikan Jin Terajin--------------------'''
        if jumlah_jin_terajin == 0: # Saat tidak ditemukan jin terajin (Dalam kasus ini bisa terjadi apabila tidak ada jin pembangun dan data candi kosong)
            return '-'
        elif jumlah_jin_terajin == 1: # Saat ditemukan hanya 1 jin terajin
            return list_terajin[0] # Mengembalikan data pertama list jin terajin (Karena list jin terajin hanya berisi 1 data)
        else: # Saat ditemukan lebih dari 1 jin terajin
            return util_function.leksikal(list_terajin,jumlah_jin_terajin, False)[0] # Mengembalikan data pertama list jin terajin setelah diurutkan dengan leksikografi terbesar ke kecil
        '''-------------------- Mengembalikan Jin Terajin--------------------'''
        
    else: # Saat ingin mengembalikan jin terajin

        '''-------------------- Inisialisasi Awal --------------------'''
        mins = util_function.maksimum(jumlah_yg_dibangun_jin, tempdata.len_pembangun) # Mencari jumlah candi terdikit yang dibangun oleh jin
        jumlah_jin_termalas = 0 # Inisialisasi awal sebagai tempat jumlah jin dengan jumlah candi yang dibangun sama dan terdikit
        '''-------------------- Inisialisasi Awal --------------------'''


        '''-------------------- Mencari Jumlah Jin Termalas --------------------'''
        for i in range(tempdata.len_pembangun):
            if jumlah_yg_dibangun_jin[i] == mins: # Saat jumlah candi yang dibangun jin merupakan jumah candi terdikit
                jumlah_jin_termalas +=1
        '''-------------------- Mencari Jumlah Jin Termalas --------------------'''


        '''-------------------- Membuat List Jin Termalas --------------------'''
        list_termalas = ['' for i in range(jumlah_jin_termalas)] # Inisialisasi awal list dengan jumlah elemen sebanyak jumlah jin termalas
        index = 0 # Index untuk elemen list jin termalas
        for i in range(tempdata.len_pembangun): # Loop untuk mengisi list jin termalas
            if jumlah_yg_dibangun_jin[i] == mins: # Jika jumlah candi yang dibangun oleh jin merupakan jumlah candi terdikit
                list_termalas[index] = listpembangun[i] # Memasukan nama jin ke dalam data jin termalas
                index += 1
        '''-------------------- Membuat List Jin Termalas --------------------'''
    

        '''-------------------- Mengembalikan Jin Termalas--------------------'''
        if jumlah_jin_termalas == 0: # Saat tidak ditemukan jin termalas (Dalam kasus ini bisa terjadi apabila tidak ada jin pembangun dan data candi kosong)
            return '-'
        elif jumlah_jin_termalas == 1: # Saat ditemukan hanya 1 jin termalas
            return list_termalas[0] # Mengembalikan data pertama list jin termalas (Karena list jin termalas hanya berisi 1 data)
        else: # Saat ditemukan lebih dari 1 jin termalas
            return util_function.leksikal(list_termalas,jumlah_jin_termalas, True)[0] # Mengembalikan data pertama list jin termalas setelah diurutkan dengan leksikografi terkecil ke besar
        '''-------------------- Mengembalikan Jin Termalas--------------------'''

    '''-------------------- Jin Terajin/Termalas --------------------'''

'''------------------------------------------------------------ Cari Jin Terajin/Termalas ------------------------------------------------------------'''