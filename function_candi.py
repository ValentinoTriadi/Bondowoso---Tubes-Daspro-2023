import util_function

'''---------------------------------------------------------- Process List ----------------------------------------------------------'''
def saveCandi(material: list, username: str) -> list:
    import tempdata

    '''-------------------- Mencari ID Candi --------------------'''
    if tempdata.jumlah_candi_yang_dihancurkan == 0: # Saat tidak ada candi yang dihancurkan
        
        '''-------------------- Menentukan ID Candi --------------------'''
        tempdata.len_candi +=1 # Menambahkan jumlah candi yang telah dibangun
        id = tempdata.len_candi # Mengambil id sebagai jumlah candi yang telah dibangun 
        '''-------------------- Menentukan ID Candi --------------------'''

    else: # Saat ada candi yang dihancurkan

        '''-------------------- Menentukan ID Candi --------------------'''
        id = tempdata.id_candi_yang_dihancurkan[0] # Mengambil id dari data id candi yang dihancurkan elemen pertama (karena data id candi yang dihancurkan sudah urut dari kecil ke besar sehingga elemen pertama merupakan id terkecil)
        '''-------------------- Menentukan ID Candi --------------------'''


        '''-------------------- Mengupdate data candi yang dihancurkan --------------------'''
        tempdatas = [ 0 for i in range(tempdata.jumlah_candi_yang_dihancurkan - 1)] # Membuat list baru tempdatas sebagai penyimpanan sementara data id candi yang dihancurkan
        for i in range(1,tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk memasukan data id candi yang lama dan menaikannya 1 index (elemen pertama pada data lama tidak dimasukan karena sudah digunakan sebagai ID candi yang akan dibangun)
            tempdatas[i-1] = tempdata.id_candi_yang_dihancurkan[i]
        
        tempdata.id_candi_yang_dihancurkan = tempdatas # Mengupdate data id candi yang dihancurkan dengan list tempdatas
        tempdata.jumlah_candi_yang_dihancurkan -= 1 # Mengupdate panjang data id candi yang dihancurkan
        '''-------------------- Mengupdate data candi yang dihancurkan --------------------'''

    '''-------------------- Mencari ID Candi --------------------'''


    '''-------------------- Menyiapkan Data Candi Yang Akan Dibangun --------------------'''
    harga = int(material[0]) * 10000 + int(material[1]) * 15000 + int(material[2]) * 7500 # Menghitung harga candi yang akan dibangun
    datas = [str(id), username, material[0], material[1], material[2], harga] # Memplotkan data-data candi sesuai dengan template data candi yang tersedia
    '''-------------------- Menyiapkan Data Candi Yang Akan Dibangun --------------------'''

    return datas # Mengembalikan data candi yang akan dibangun
    
'''---------------------------------------------------------- Process List ----------------------------------------------------------'''



'''---------------------------------------------------------- Hitung Jumlah Bahan Yang Terpakai ----------------------------------------------------------'''
def countbahan(bahan: str) -> int:
    import tempdata

    '''-------------------- Mengambil Data Candi --------------------'''
    data = tempdata.data_candi # Mengambil data candi dan menyimpannya pada variabel lokal
    '''-------------------- Mengambil Data Candi --------------------'''


    '''-------------------- Menentukan Index Bahan --------------------'''
    if bahan == "pasir":
        index = 2 # Index 2 pada data candi merupakan index bahan pasir
    elif bahan == "batu":
        index = 3 # Index 2 pada data candi merupakan index bahan batu
    elif bahan == "air":
        index = 4 # Index 2 pada data candi merupakan index bahan air
    '''-------------------- Menentukan Index Bahan --------------------'''


    '''-------------------- Menghitung Jumlah Bahan Yang Terpakai --------------------'''
    count = 0 # Inisialisasi awal jumlah bahan yang terpakai
    for i in range(tempdata.len_candi): # Loop untuk mencari jumlah bahan per candi dan menambahkan ke variabel count 
        if data[i] != []: # Saat data tidak kosong (karena saat candi dihancurkan, line candi yang dihancurkan tersebut merupakan data kosong)
            count += int(data[i][index])
    '''-------------------- Menghitung Jumlah Bahan Yang Terpakai --------------------'''
    
    return count # Mengembalikan jumlah bahan yang terpakai

'''---------------------------------------------------------- Hitung Jumlah Bahan Yang Terpakai ----------------------------------------------------------'''



'''---------------------------------------------------------- Cari Candi Termahal/Termurah ----------------------------------------------------------'''
def canditer(mahal: bool) -> tuple:
    import tempdata
    '''-------------------- Inisialisasi Awal --------------------'''
    data = tempdata. data_candi # Data candi dimasukan ke dalam variabel lokal
    lendata = tempdata.len_candi - tempdata.jumlah_candi_yang_dihancurkan # Panjang Data merupakan panjang data efisien dimana data kosong tidak dihitung (karena pada data candi, candi yang dihancurkan merupakan line kosong maka panjang data efisien adalah panjang data candi dikurangi oleh jumlah data kosongnya (jumlah candi yang dihancurkan))
    tempid = ['' for i in range(lendata)] # Inisialisasi awal untuk tempat id sementara 
    tempharga = [0 for i in range(lendata)] # Inisialisasi awal untuk tempat harga sementara
    index = 0 # Tempat untuk menyimpan index temporary data
    '''-------------------- Inisialisasi Awal --------------------'''


    '''-------------------- Mengisi Temporary List --------------------'''
    for i in range(tempdata.len_candi):
        if data[i] != []: # Saat data tidak kosong (karena saat candi dihancurkan, line candi yang dihancurkan tersebut merupakan data kosong)
            tempid[index] = data[i][0] # Memasukan id candi kedalam temporary list tempid
            tempharga[index] = int(data[i][5]) # Memasukan harga candi kedalam temporary list tempid dengan index yang sama dengan index id nya
            index += 1 # Menaikan index temporary data
    '''-------------------- Mengisi Temporary List --------------------'''


    '''-------------------- Mencari Harga Ekstrim --------------------'''
    if mahal: # Saat yang akan dicari merupakan data termahal

        '''-------------------- Mencari Harga Maksimum --------------------'''
        harga = util_function.maksimum(tempharga,lendata) # Mencari harga tertinggi dari list temporary harga
        '''-------------------- Mencari Harga Maksimum --------------------'''

        
        '''-------------------- Mengembalikan Data Candi Termahal --------------------'''
        for i in range(lendata): # Loop untuk mencari data candi dengan harga maksimum
            if tempharga[i] == harga: # Saat data candi merupakan data candi dengan harga maksimum
                return tempid[i],harga # Mengembalikan data id dan harga candi termahal
        '''-------------------- Mengembalikan Data Candi Termahal --------------------'''

    else: # Saat yang akan dicari merupakan data termurah

        '''-------------------- Mencari Harga Minimum --------------------'''
        harga = util_function.minimum(tempharga,lendata) # Mencari harga tertinggi dari list temporary harga
        '''-------------------- Mencari Harga Minimum --------------------'''


        '''-------------------- Mengembalikan Data Candi Termurah --------------------'''
        for i in range(lendata): # Loop untuk mencari data candi dengan harga minimum
            if tempharga[i] == harga: # Saat data candi merupakan data candi dengan harga minimum
                return tempid[i],harga  # Mengembalikan data id dan harga candi termurah
        '''-------------------- Mengembalikan Data Candi Termurah --------------------'''

    '''-------------------- Mencari Harga Ekstrim --------------------'''

'''---------------------------------------------------------- Cari Candi Termahal/Termurah ----------------------------------------------------------'''