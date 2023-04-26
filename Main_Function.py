import util_function, function_jin, time, function_candi, os.path
logins = False
access = ""
user = "asdf"
path_folder = ""
username_jin_summon = ""

'''-------------------------------------------------------------F01------------------------------------------------------------'''
def login():
    import tempdata, Visual
    global logins, access, user
    Visual.render_screen(["Login"],1) # Menampilkan screen 'login'
    time.sleep(0.5)

    '''-------------------- Input User --------------------'''
    # asumsi input username unik dan hanya mengandung huruf alphabet
    username = input("Username: ") # Input dari user
    password = input("Password: ")
    '''-------------------- Input User --------------------'''


    '''-------------------- Inisialisasi Awal --------------------'''
    datauser = tempdata.data_user # meng-assign data global ke variabel data user lokal
    index = 0   # sebagai tempat menyimpan index tempat username ditemukan
    cekuser = False     # sebagai tempat menyimpan cek apakah user ada pada data atau tidak
    cekpass = ""    # sebagai tempat untuk menyimpan password yang diambil dari data 
    '''-------------------- Inisialisasi Awal --------------------'''


    '''-------------------- Memeriksa User --------------------'''
    for i in range(tempdata.len_user):  # loop untuk memeriksa apakah username yang diinput ada pada data atau tidak
        # Kondisional untuk mengecek apakah username terdapat pada data atau tidak
        if datauser[i][0] == username: # datauser[i](akun pada baris ke brp pada data)[0](username)
            # {Username terdapat pada data}
            cekuser = True # cek benar, berarti username ada pada data
            index = i # menyimpan index tempat username ditemukan
            cekpass = datauser[i][1] # menyimpan password pada data dengan index yang sama dengan index ditemukannya username
    '''-------------------- Memeriksa User --------------------'''

    
    '''-------------------- Validasi Login --------------------'''
    # Kondisional untuk memvalidasi login
    if not cekuser: # Saat user tidak ditemukan pada data
        Visual.render_screen(["Username tidak terdaftar!"],1) # Menampilkan pesan
        time.sleep(2.5)
        login() # Mengulangi fungsi login
    else: # Saat user ditemukan pada data
        if password == cekpass: # ketika password yang diinput benar
            logins = True # Merubah variabel logins global menjadi benar (sudah login)
            access = datauser[index][2] # Merubah variabel access global menjadi role dari user
            user = datauser[index][0] # Merubah variabel user global menjadi username
            Visual.printascii(access,access) # Menampilkan animasi karakter
            
        else: # ketika password yang diinput salah
            Visual.render_screen(["Password salah!"],1) # Menampilkan pesan
            time.sleep(2.5)
            login() # Mengulang fungsi login
    '''-------------------- Validasi Login --------------------'''

'''-------------------------------------------------------------F01------------------------------------------------------------'''



'''-------------------------------------------------------------F02------------------------------------------------------------'''
def logout():
    import Visual
    global logins, access, user

    '''-------------------- Inisialisasi Variabel Global --------------------'''
    logins = False # Merubah variabel logins global menjadi salah (belum login)
    access = "" # Merubah variabel access global menjadi tidak ada
    user = "" # Merubah variabel user global menjadi tidak ada
    '''-------------------- Inisialisasi Variabel Global --------------------'''

    
    Visual.printascii("logout",None) # Menampilkan animasi logout
'''-------------------------------------------------------------F02------------------------------------------------------------'''



'''------------------------------------------------------------F03------------------------------------------------------------'''
def summonJin():
    global username_jin_summon # Username dari jin yang akan disummon
    import tempdata, Visual
    Visual.render_screen(["Summon Jin"],1) # Menampilkan animasi summon jin
    time.sleep(0.5)

    '''-------------------- Mengecek Jumlah Jin --------------------'''
    if tempdata.len_user < 102: # Jika total jin masih di bawah 100 (< 102 dikarenakan ada user Bondowoso dan Roro yang bukan merupakan jin tetapi terdapat pada data user)

        '''-------------------- Input Jenis Jin --------------------'''
        Visual.render_screen(["Jenis jin yang dapat dipanggil: ", # Animasi opsi jenis jin
        "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
        "(2) Pembangun - Bertugas membangun candi"], 3)

        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ")) # Menerima input jenis jin yang akan dipanggil

        # TODO: Validasi input
        while jin != 2 and jin != 1: # Loop untuk validasi input
            Visual.render_screen([f'Tidak ada jenis jin bernomor "{jin}"!'], 1) # Jika input di luar dari opsi
            time.sleep(2.5)
            Visual.render_screen(["Jenis jin yang dapat dipanggil: ",
            "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
            "(2) Pembangun - Bertugas membangun candi"], 3)
            jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ")) # Looping meminta input jenis jin
        '''-------------------- Input Jenis Jin --------------------'''


        '''-------------------- Input Username Jin --------------------'''
        if jin == 1: # Ketika user menginput opsi 1
            role = "Pengumpul"
            Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
            username = input("Masukkan username jin: ") # Memasukkan username jin yang akan dipanggil

            # TODO: Validasi username
            while function_jin.Cek_User(username): # Jika username sudah terdaftar akan looping meminta input
                Visual.render_screen([f'Username "{username}" sudah diambil!'],1) 
                time.sleep(2)
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
                username = input("Masukkan username jin: ")
        else: # Ketika user menginput opsi 2
            role = "Pembangun"
            Visual.render_screen(['Memilih jin "Pembangun".'], 1)
            username = input("Masukkan username jin: ") # Memasukkan username jin yang akan dipanggil

            # TODO: Validasi username
            while function_jin.Cek_User(username): # Jika username sudah terdaftar akan looping meminta input
                Visual.render_screen([f'Username "{username}" sudah diambil!'],1)  
                time.sleep(2)
                Visual.render_screen(['Memilih jin "Pembangun".'], 1)
                username = input("Masukkan username jin: ")

        username_jin_summon = username # Username jin yang di summon akan disave pada variabel global yang diperuntukkan animasi
        '''-------------------- Input Username Jin --------------------'''


        '''-------------------- Input Password Jin --------------------'''
        password = input("Masukkan password jin: ") # Meminta data password untuk username jin yang akan disummon

        # TODO: Validasi panjang password
        while not 5 <= util_function.length(password + '.', '.') <= 25: # Jika password panjangnya tidak dari 5 sampai 25 huruf
            Visual.render_screen(["Password panjangnya harus 5-25 karakter!"],1) # Menampilkan pesan kesalahan
            time.sleep(2.5)
            if role == "Pengumpul": # Sesuai opsi jenis jin yang dipilih di atas
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1) # Menampilkan animasi
            elif role == "Pembangun": # Sesuai opsi jenis jin yang dipilih di atas
                Visual.render_screen(['Memilih jin "Pembangun".'], 1) # Menampilkan animasi
            password = input("Masukkan password jin: ") 
        '''-------------------- Input Password Jin --------------------'''


        '''-------------------- Update Data User --------------------'''
        datas = [username,password,role] # Mengubah inputan data menjadi bentuk list bernama datas

        # TODO: Mengupdate data user
        tempdatas = [[] for i in range(tempdata.len_user + 1)] # Menambahkan list datas ke ke datas temporary untuk disave sementara
        for i in range(tempdata.len_user): # Loop untuk mengisi tempdatas (datas temporary) dengan data sebelumnya
            tempdatas[i] = tempdata.data_user[i]
        tempdatas[tempdata.len_user] = datas # Menambahkan list bernama datas ke tempdatas (datas temporary)

        tempdata.len_user += 1 # Mengupdate jumlah user setelah melakukan summon jin
        tempdata.data_user = tempdatas # Memasukkan tempdatas (datas temporary) ke data user
        '''-------------------- Update Data User --------------------'''


        '''-------------------- Tampilan Animasi --------------------'''
        time.sleep(1)
        if role == "Pengumpul":
            Visual.printascii("summon_pengumpul",access) # Menampilkan animasi summon jin pengumpul
        elif role == "Pembangun":
            Visual.printascii("summon_pembangun",access) # Menampilkan animasi summon jin pembangun
        '''-------------------- Tampilan Animasi --------------------'''

        
    else: # Jika jin yang terdaftar sudah 100

        '''-------------------- Tampilan Animasi --------------------'''
        Visual.render_screen(["Jumlah Jin telah maksimal! (100 jin).",f"{user} tidak dapat men-summon lebih dari itu."],2)
        time.sleep(2)
        '''-------------------- Tampilan Animasi --------------------'''

    '''-------------------- Mengecek Jumlah Jin --------------------'''

'''------------------------------------------------------------F03------------------------------------------------------------'''
    


'''------------------------------------------------------------F04------------------------------------------------------------'''
def hapusJin():
    import tempdata, Visual

    '''-------------------- Tampilan Awal --------------------'''
    Visual.render_screen(["Hapus Jin"],1) # Menampilkan animasi tampilan opsi penghapusan jin
    time.sleep(0.5)
    '''-------------------- Tampilan Awal --------------------'''
    

    '''-------------------- Input Username --------------------'''
    username = input("Masukkan username jin : ") # Meminta input username jin yang akan dihapus
    '''-------------------- Input Username --------------------'''


    '''-------------------- Cek Username --------------------'''
    if not function_jin.Cek_User(username): # Jika username yang diinput tidak memiliki kesamaan dengan data yang ada

        '''-------------------- Validasi Kesalahan --------------------'''
        Visual.render_screen(["Tidak ada jin dengan username tersebut."],1) # Menampilkan pesan kesalahan
        time.sleep(2)
        '''-------------------- Validasi Kesalahan --------------------'''


    elif function_jin.Cek_User(username): # Jika username terdaftar di dalam data

        '''-------------------- Konfirmasi --------------------'''
        option = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ") # Input user terkait konfirmasi penghapusan jin
        '''-------------------- Konfirmasi --------------------'''


        '''-------------------- Validasi Konfirmasi --------------------'''
        while option != "Y" and option != "N":
            Visual.render_screen(["Input tidak sesuai!","Silakan masukan (Y/N)!"],2) # Pesan kesalahan
            option = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ") # Input user terkait konfirmasi penghapusan jin
        '''-------------------- Validasi Konfirmasi --------------------'''


        '''-------------------- Penghapusan Jin --------------------'''
        if option == "Y": # Jika input user adalah Ya

            '''-------------------- Inisialisasi Awal Data --------------------'''
            data_user = tempdata.data_user # Mengambil data user
            datacandi = tempdata.data_candi # Mengambil data candi
            '''-------------------- Inisialisasi Awal Data --------------------'''


            '''-------------------- Mencari Indeks Username --------------------'''
            for i in range(tempdata.len_user): # Loop untuk mencari indeks data yang usernamenya sesuai dengan input user
                if data_user[i][0] == username: 
                    index = i
            '''-------------------- Mencari Indeks Username --------------------'''


            '''-------------------- Menghapus Username Dari Data --------------------'''
            for i in range(index,tempdata.len_user-1): # Loop untuk menghapus data jin lalu menaikkan semua data di bawahnya 1 indeks ke atas
                tempdata.data_user[i] = tempdata.data_user[i+1] 
            '''-------------------- Menghapus Username Dari Data --------------------'''


            '''-------------------- Mengupdate Data User --------------------'''
            tempdata.len_user -= 1 # mengupdate panjang data user menjadi berkurang 1

            # TODO: Mengupdate data user
            tempdatas = [[] for i in range(tempdata.len_user)] # Membuat ulang tempdata yang baru dengan jumlah elemen yang sesuai dengan panjang data (sehingga list tidak ada elemen kosong)
            for i in range(tempdata.len_user): # Loop untuk memasukan data lama ke list baru
                tempdatas[i] = tempdata.data_user[i]

            tempdata.data_user = tempdatas # Meng-assign kembali tempdatas untuk data user
            '''-------------------- Mengupdate Data User --------------------'''


            '''-------------------- Mengupdate Data Candi yang Dihancurkan--------------------'''

            # TODO: Menghitung banyak candi yang telah dibangun jin yang akan dihapus 
            count = 0 # Banyak candi yang telah dibangun oleh jin yang akan dihapus
            for i in range(tempdata.len_candi): # Menghitung banyak candi yang dibangun oleh jin yang akan dihapus
                if datacandi[i][1] == username:
                    count+=1

            # TODO: Inisialisasi Awal 
            j = 0
            tempdatas = [[] for i in range(tempdata.len_candi - count)] # Membuat list tempdatas baru untuk data candi
            
            # TODO: Mengupdate data candi yang dihancurkan
            for i in range(tempdata.len_candi): # Loop untuk mengisi tempdatas 
                if datacandi[i][1] != username: # Jika candi tidak dibangun oleh jin yang akan dihapus
                    tempdatas[j] = datacandi[i] # Candi tersebut akan di-assign ke tempdatas
                    j+=1
                else: # Jika candi dibuat oleh jin yang akan dihapus
                    tempdata.len_candi-=1 # Panjang data candi berkurang 1
                    id = datacandi[i][0] # ID Candi akan masuk ke variabel id

                    temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan + 1)] # List sementara candi yang dihancurkan
                    for i in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk mengisi list sementara dengan data yang sudah ada sebelum ditambahkan id baru
                        temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]
                    temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id # Meng-assign id candi yang dohancurkan
                    tempdata.jumlah_candi_yang_dihancurkan += 1 # Jumlah candi yang dihancurkan bertambah 1
                    tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<") # Mengurutkan data id candi yang dihancurkan dari yang terkecil

            tempdata.data_candi = tempdatas # Data candi terbaru dari tempdatas
            '''-------------------- Mengupdate Data Candi yang Dihancurkan--------------------'''


            '''-------------------- Tampilan Animasi --------------------'''
            if data_user[index][2] == "Pembangun": # Jika role jin yang dihapus adalah pembangun
                Visual.printascii("hapus_jin_bangun",access) # Menampilkan animasi jin dihapus
            elif data_user[index][2] == "Pengumpul": # Jika role jin yang dihapus adalah pembangun
                Visual.printascii("hapus_jin_kumpul",access) # Menampilkan animasi jin dihapus
            '''-------------------- Tampilan Animasi --------------------'''

        '''-------------------- Penghapusan Jin --------------------'''

    '''-------------------- Cek Username --------------------'''

'''------------------------------------------------------------F04------------------------------------------------------------'''



'''------------------------------------------------------------F05------------------------------------------------------------'''
def ubahJin():
    import tempdata, Visual

    '''-------------------- Input Username --------------------'''
    username = input("Masukkan username jin : ") # Meminta input username yang akan dirubah tipenya
    '''-------------------- Input Username --------------------'''


    '''-------------------- Cek Username --------------------'''
    # Kondisional untuk mengecek username yang di input terdaftar pada data atau tidak
    if not function_jin.Cek_User(username): # Saat username tidak ditemukan pada data
        Visual.render_screen(["Tidak ada jin dengan username tersebut."],1)
        time.sleep(2)
        Visual.printascii(access,access)
    else: # Saat username ditemukan pada data

        '''-------------------- Inisialisasi Awal Data --------------------'''
        data_user = tempdata.data_user # Mengambil data user dan di assign ke variabel lokal
        index = 0 # Tempat menyimpan index username
        '''-------------------- Inisialisasi Awal Data --------------------'''


        '''-------------------- Mencari Index Username --------------------'''
        for i in range(tempdata.len_user): # Loop untuk mencari index username
            if data_user[i][0] == username: # Saat username ditemukan
                index = i
        '''-------------------- Mencari Index Username --------------------'''


        '''-------------------- Mengubah Tipe Username --------------------'''
        tempdata.data_user[index][2] = function_jin.ubah_role(tempdata.data_user[index][2]) # Memanggil fungsi ubah_role
        '''-------------------- Mengubah Tipe Username --------------------'''


        '''-------------------- Tampilan Animasi --------------------'''
        if tempdata.data_user[index][2] == "Pembangun": # Jika jin diubah menjadi tipe pembangun
            Visual.printascii("ubah_kumpul_bangun",access)
        elif tempdata.data_user[index][2] == "Pengumpul": # Jika jin diubah menjadi tipe pengumpul
            Visual.printascii("ubah_bangun_kumpul",access)
        '''-------------------- Tampilan Animasi --------------------'''

    '''-------------------- Cek Username --------------------'''
    
'''------------------------------------------------------------F05------------------------------------------------------------'''



'''-------------------------------------------------------------F06------------------------------------------------------------'''
def bangun(username: str):
    import tempdata, Visual

    '''-------------------- Inisialisasi Awal Data --------------------'''
    candi = tempdata.data_candi #Mengambil data candi dan di assign ke variabel lokal
    bahan = tempdata.data_bahan_bangunan #Mengambil data bahan bangunan dalam bentuk csv dan di assign ke variabel lokal dalam bentuk matriks
    '''-------------------- Inisialisasi Awal Data --------------------'''


    '''-------------------- Penentuan Bahan Bangunan --------------------'''
    #Menentukan banyaknya bahan yang dibutuhkan untuk membangun candi secara acak
    pasir = util_function.randint(1,5) ; batu = util_function.randint(1,5) ; air = util_function.randint(1,5)
    '''-------------------- Penentuan Bahan Bangunan --------------------'''

        
    '''-------------------- Pembangunan Candi  --------------------'''
    #Kondisional untuk bahan bangunan pembuatan candi
    if pasir <= int(bahan[0][0]) and batu <= int(bahan[0][1]) and air <= int(bahan[0][2]): #Jika bahan bangunan mencukupi

        '''-------------------- Mengupdate Data Bahan Bangunan --------------------'''
        #Jumlah bahan bangunan yang dimiliki (pasir, batu, dan air) akan dikurangi sesuai bahan bangunan yang diperlukan 
        bahan[0][0] = str(int(bahan[0][0]) - pasir) ; bahan[0][1] = str(int(bahan[0][1]) - batu) ; bahan[0][2] = str(int(bahan[0][2]) - air )
        material = [str(pasir),str(batu),str(air)] #Membuat variabel lokal baru berisikan data bahan bangunan dengan bentuk list of string 
        tempdata.data_bahan_bangunan = bahan #Menyimpan kembali perubahan data bahan bangunan ke variabel global
        '''-------------------- Mengupdate Data Bahan Bangunan --------------------'''


        '''-------------------- Cek Jumlah Candi --------------------'''
        #Kondisional untuk memeriksa jumlah candi
        if tempdata.len_candi < 100: #Jika jumlah candi belum mencapai 100

            '''-------------------- Cek Apakah Candi Pernah Dihancurkan --------------------'''
            #Kondisional untuk memeriksa data candi
            if tempdata.jumlah_candi_yang_dihancurkan == 0: #Jika candi belum pernah dihancurkan 

                '''-------------------- Mengupdate Data Candi  --------------------'''
                #Apabila candi belum pernah dihancurkan, diperlukan data list baru untuk menyimpan candi dengan jumlah indeks yang bertambah satu
                tempdatacandi = [[] for i in range(tempdata.len_candi + 1)] #Variabel lokal list baru untuk menyimpan data candi yang baru dengan panjang list bertambah 1
                for i in range(tempdata.len_candi): #Loop untuk mengisi data candi yang lama dengan menyisakan satu indeks data kosong
                    tempdatacandi[i] = candi[i]

                #Indeks data yang kosong akan diisi dengan data candi yang baru dibangun
                tempdatacandi[tempdata.len_candi-1] = function_candi.saveCandi(material, username) 
                tempdata.data_candi = tempdatacandi #Menyimpan data baru candi ke variabel global
                '''-------------------- Mengupdate Data Candi --------------------'''

            else: #Jika candi pernah dihancurkan

                '''-------------------- Mengupdate Data Candi --------------------'''
                #Apabila candi pernah dihancurkan, akan menyisakan indeks kosong yang mungkin berada di tengah-tengah data
                tempdatacandi = [[] for i in range(tempdata.len_candi)] #Variabel lokal list baru untuk menyimpan data candi yang baru  
                cek = True
                for i in range(tempdata.len_candi): #Loop untuk mengisi data candi
                    #Kondisional pengisian data candi
                    if tempdata.data_candi[i] == [] and cek: #Jika terdapat data candi (indeks) yang kosong
                        tempdatacandi[i] = function_candi.saveCandi(material, username) #Data candi yang baru akan diisikan pada indeks yang kosong
                        cek = False #
                    else: #Jika tidak terdapat data candi (indeks) yang kosong
                        tempdatacandi[i] = candi[i] #Menyimpan data candi yang lama
                tempdata.data_candi = tempdatacandi #Menyimpan data candi baru ke variabel global
                '''-------------------- Mengupdate Data CAndi --------------------'''

            '''-------------------- Cek Apakah Candi Pernah Dihancurkan --------------------'''
            

            '''-------------------- Cek apakah username ada di list jin_yang_pernah_membangun atau tidak --------------------'''
            # Kalau ada, maka list jin_yang_pernah_membangun tidak ditambahkan username
            # Kalau tidak ada, maka list jin_yang_pernah_membangun ditambahkan username
            cek = True  # Kondisi awal apabila user tidak ditemukan dalam list jin_yang_pernah_membangun
            for i in range(tempdata.len_pembangun): # Loop untuk mengecek apakah user ada didalam list jin_yang_pernah_membangun atau tidak
                if tempdata.data_jin_yang_pernah_membangun[i] == username:   # Kondisi saat user ditemukan ada didalam list jin_yang_pernah_membangun
                    cek = False

            if cek: # Kondisi saat user tidak ditemukan dalam list jin_yang_pernah_membangun
                tempdata.len_pembangun += 1 # Panjang list jin_yang_pernah_membangun bertambah 1
                
                temp_jin_pembangun = ["" for i in range(tempdata.len_pembangun)]    # Inisialisasi awal list baru untuk menyimpan list jin_yang_pernah_membangun yang akan ditambah user baru
                for i in range(tempdata.len_pembangun): # Loop untuk mengisi list baru dengan list jin_yang_pernah_membangun dan user baru
                    #Kondisional untuk data jin
                    if i != tempdata.len_pembangun - 1: # Jika belum mencapai indeks terakhir dari list
                        temp_jin_pembangun[i] = tempdata.data_jin_yang_pernah_membangun # User jin yang pernah membangun sebelumnya diinputkan
                    else: # Jika telah mencapai indeks terakhir dari list
                        temp_jin_pembangun[i] = username # User Jin baru diinputkan
            '''-------------------- Cek apakah username ada di list jin_yang_pernah_membangun atau tidak --------------------'''


            '''-------------------- Tampilan Animasi Bangun Candi --------------------'''
            Visual.printascii("bangun_candi",access)
            Visual.render_screen([f"Sisa candi yang perlu dibangun: {100-tempdata.len_candi + tempdata.jumlah_candi_yang_dihancurkan}."],1)
            time.sleep(2.5)
            '''-------------------- Tampilan Animasi Bangun Candi --------------------'''

        else: #Jika jumlah candi telah mencapai 100

            '''-------------------- Tampilan Animasi Bangun Candi Berjumlah >= 100 --------------------'''
            Visual.printascii("bangun_candi",access)
            Visual.render_screen(["Sisa candi yang perlu dibangun: 0."],1)
            time.sleep(2.5)
            '''-------------------- Tampilan Animasi Bangun Candi Berjumlah >= 100--------------------'''

        '''-------------------- Cek Jumlah Candi --------------------'''

    else: #Jika bahan bangunan tidak tercukupi

        '''-------------------- Tampilan Animasi Bahan Bangunan Tidak Tercukupi --------------------'''
        Visual.render_screen(["Bahan bangunan tidak mencukupi","Candi tidak bisa dibangun!"],2)
        time.sleep(2.5)
        '''-------------------- Tampilan Animasi Bahan Bangunan Tidak Tecukupi --------------------'''

    '''-------------------- Pembangunan Candi --------------------'''

'''-------------------------------------------------------------F06------------------------------------------------------------'''



    
'''-------------------------------------------------------------F07------------------------------------------------------------'''
def kumpul(batch: bool):
    import tempdata, Visual

    '''-------------------- Inisialisasi Awal --------------------'''
    pasir = util_function.randint(0,5) ; batu = util_function.randint(0,5) ; air = util_function.randint(0,5) # Mengeluarkan angka random antara angka 0 sampai 5
    bahan = tempdata.data_bahan_bangunan # Mengambil data bahan bangunan dan memasukkan data ke variabel lokal
    bahan[0][0] = str(int(bahan[0][0]) + pasir) ; bahan[0][1] = str(int(bahan[0][1]) + batu) ; bahan[0][2] = str(int(bahan[0][2]) + air ) # Update data bahan setelah ditambah bahan yang dikumpulkan
    '''-------------------- Inisialisasi Awal --------------------'''

    if batch : # Saat fungsi kumpul dipanggil untuk melakukan batch kumpul
        return [pasir,batu,air] # Mengembalikan banyak bahan bangunan yang dikumpulkan
    else: # Saat fungsi kumpul dipanggil untuk melakukan satu kali kumpul bahan
        Visual.printascii("kumpul", access)
        Visual.render_screen([f"Jin menemukan {pasir} pasir, {batu} batu, {air} air."],1) 
        time.sleep(2.5)

'''-------------------------------------------------------------F07------------------------------------------------------------'''


    
'''-------------------------------------------------------------F08------------------------------------------------------------'''

'''-------------------- 1 --------------------'''
def batchkumpul():
    import Visual

    '''-------------------- 2 --------------------'''
    jinPengumpul = function_jin.count_jin("Pengumpul")
    '''-------------------- 2 --------------------'''


    '''-------------------- 3 --------------------'''
    if jinPengumpul == 0:
        
        '''-------------------- 4 --------------------'''
        Visual.render_screen(["Kumpul gagal","Anda tidak punya jin pengumpul","Silahkan summon terlebih dahulu."],3)
        time.sleep(2)
        Visual.printascii(access,access)
        '''-------------------- 4 --------------------'''

    else:

        '''-------------------- 5 --------------------'''
        pasir = 0 ; batu = 0 ; air = 0
        for i in range(jinPengumpul):
            PBA = kumpul(True)
            pasir += PBA[0] ; batu += PBA[1] ; air += PBA[2]
        '''-------------------- 5 --------------------'''


        '''-------------------- 6 --------------------'''
        Visual.render_screen([f"Mengerahkan {jinPengumpul} jin untuk mengumpulkan bahan."],1)
        time.sleep(2.5)
        Visual.printascii("kumpul",access)
        Visual.render_screen([f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air."],1)
        time.sleep(2.5)
        '''-------------------- 6 --------------------'''

    '''-------------------- 3 --------------------'''

    
'''-------------------- 1 --------------------'''
def batchbangun():  
    import tempdata, Visual

    '''-------------------- 2 --------------------'''
    Jumlah_jin_Pembangun = function_jin.count_jin("Pembangun")
    '''-------------------- 2 --------------------'''


    if Jumlah_jin_Pembangun == 0:
        
        '''-------------------- 3 --------------------'''
        Visual.render_screen(["Bangun gagal","Anda tidak punya jin pembangun","Silahkan summon terlebih dahulu."],3)
        time.sleep(2)
        Visual.printascii(access,access)
        '''-------------------- 3 --------------------'''
        
    else:

        '''-------------------- 4 --------------------'''
        data_user = tempdata.data_user 
        '''-------------------- 4 --------------------'''


        '''-------------------- 5 --------------------'''
        if Jumlah_jin_Pembangun - tempdata.jumlah_candi_yang_dihancurkan > 0:
            lendata = tempdata.len_candi + Jumlah_jin_Pembangun - tempdata.jumlah_candi_yang_dihancurkan
        else:
            lendata = tempdata.len_candi
        '''-------------------- 5 --------------------'''


        '''-------------------- 6 --------------------'''
        temp_candi = [[] for i in range(lendata)]
        total_Material = [0,0,0]
        bahan = tempdata.data_bahan_bangunan
        jin = ["" for i in range(Jumlah_jin_Pembangun)]
        j = 0
        '''-------------------- 6 --------------------'''


        '''-------------------- 7 --------------------'''
        for i in range(tempdata.len_candi):
            temp_candi[i] = tempdata.data_candi[i]
        '''-------------------- 7 --------------------'''


        '''-------------------- 8 --------------------'''
        for i in range(tempdata.len_user):
            if data_user[i][2] == "Pembangun":
                jin[j] = data_user[i][0]
                j += 1
        '''-------------------- 8 --------------------'''


        '''-------------------- 9 --------------------'''
        temp_id_candi_yang_dihancurkan = tempdata.id_candi_yang_dihancurkan
        temp_jumlah_candi_yang_dihancurkan = tempdata.jumlah_candi_yang_dihancurkan
        '''-------------------- 9 --------------------'''


        '''-------------------- 10 --------------------'''
        j = 0
        for i in range(lendata):
            if temp_candi[i] == []:

                '''-------------------- 11 --------------------'''
                pasir = util_function.randint(1,5) ; batu = util_function.randint(1,5) ; air = util_function.randint(1,5)
                material = [str(pasir),str(batu),str(air)]
                '''-------------------- 11 --------------------'''
                

                '''-------------------- 12 --------------------'''
                if temp_jumlah_candi_yang_dihancurkan == 0: # Kondisi ketika tidak ada candi yg hancur
                    index = tempdata.len_candi+1
                    tempdata.len_candi+=1
                else:   # Kondisi ketika ada candi yg hancur
                    index = temp_id_candi_yang_dihancurkan[0]   # mengambil id dari candi yang telah dihancurkan

                    tempdatas = [ 0 for i in range(temp_jumlah_candi_yang_dihancurkan - 1)] # Inisialisasi awal list baru untuk menyimpan list temp_id_candi_yang_dihancurkan ketika diambil 1 id tekecil
                    for k in range(1,temp_jumlah_candi_yang_dihancurkan): # mengisi list baru dengan list temp_id_candi_yang_dihancurkan setelah diambil 1 id terkecil
                        tempdatas[k-1] = temp_id_candi_yang_dihancurkan[k]
                    
                    temp_id_candi_yang_dihancurkan = tempdatas # merubah list temp_id_candi_yang_dihancurkan menjadi list temp_id_candi_yang_dihancurkan yang telah diambil 1 id terkecil
                    temp_jumlah_candi_yang_dihancurkan -= 1 # mengurangi jumlah candi yang dihancurkan (karena akan dibangun kembali)
                '''-------------------- 12 --------------------'''


                '''-------------------- 13 --------------------'''
                harga = int(material[0]) * 10000 + int(material[1]) * 15000 + int(material[2]) * 7500
                temp_candi[i] = [index,jin[j],material[0],material[1],material[2],harga]
                j += 1
                total_Material[0] += pasir ; total_Material[1] += batu ; total_Material[2] += air
                '''-------------------- 13 --------------------'''

        '''-------------------- 10 --------------------'''


        '''-------------------- 14 --------------------'''
        Visual.render_screen([f"Mengerahkan {Jumlah_jin_Pembangun} jin untuk membangun candi dengan total bahan",
                              f"{total_Material[0]} pasir, {total_Material[1]} batu, dan {total_Material[2]} air."],2)
        time.sleep(2.5)
        '''-------------------- 14 --------------------'''


        '''-------------------- 15 --------------------'''
        if total_Material[0] <= int(bahan[0][0]) and total_Material[1] <= int(bahan[0][1]) and total_Material[2] <= int(bahan[0][2]):
            bahan[0][0] = str(int(bahan[0][0]) - total_Material[0]) ; bahan[0][1] = str(int(bahan[0][1]) - total_Material[1]) ; bahan[0][2] = str(int(bahan[0][2]) - total_Material[2] )

            '''-------------------- Cek apakah username ada di list jin_yang_pernah_membangun atau tidak --------------------'''
            # Kalau ada, maka list jin_yang_pernah_membangun tidak ditambahkan username
            # Kalau tidak ada, maka list jin_yang_pernah_membangun ditambahkan username
            for i in range(tempdata.len_user): # Cek semua user yang memiliki role "Pembangun"
                if data_user[i][2] == "Pembangun":
                    cek = True  # Kondisi awal apabila user tidak ditemukan dalam list jin_yang_pernah_membangun
                    for j in range(tempdata.len_pembangun): # Loop untuk mengecek apakah user ada didalam list jin_yang_pernah_membangun atau tidak
                        if tempdata.data_jin_yang_pernah_membangun[j] == data_user[i][0]:   # Kondisi saat user ditemukan ada didalam list jin_yang_pernah_membangun
                            cek = False

                    if cek: # Kondisi saat user tidak ditemukan dalam list jin_yang_pernah_membangun
                        tempdata.len_pembangun += 1 # Panjang list jin_yang_pernah_membangun bertambah 1
                        
                        temp_jin_pembangun = ["" for j in range(tempdata.len_pembangun)]    # Inisialisasi awal list baru untuk menyimpan list jin_yang_pernah_membangun yang akan ditambah user baru
                        for j in range(tempdata.len_pembangun): # Loop untuk mengisi list baru dengan list jin_yang_pernah_membangun dan user baru
                            if j != tempdata.len_pembangun - 1:
                                temp_jin_pembangun[j] = tempdata.data_jin_yang_pernah_membangun
                            else:
                                temp_jin_pembangun[j] = data_user[i][2]
            '''-------------------- Cek apakah username ada di list jin_yang_pernah_membangun atau tidak --------------------'''


            '''-------------------- 16 --------------------'''
            tempdata.data_bahan_bangunan = bahan

            if lendata > 100:
                temp_candi2 = [[] for i in range(100)]
                for i in range(100):
                    temp_candi2[i] = temp_candi[i]
                tempdata.data_candi = temp_candi 
                tempdata.len_candi = 100
            else:
                tempdata.data_candi = temp_candi
                tempdata.len_candi = lendata

            tempdata.id_candi_yang_dihancurkan = temp_id_candi_yang_dihancurkan
            tempdata.jumlah_candi_yang_dihancurkan = temp_jumlah_candi_yang_dihancurkan
            '''-------------------- 16 --------------------'''


            '''-------------------- 17 --------------------'''
            Visual.printascii("batch_bangun",access)
            Visual.render_screen([f"Jin berhasil membangun total {Jumlah_jin_Pembangun} candi."],1)
            time.sleep(2.5)
            '''-------------------- 17 --------------------'''

        else:

            '''-------------------- 18 --------------------'''
            sisa_pasir = total_Material[0] - int(bahan[0][0])
            sisa_batu = total_Material[1] - int(bahan[0][1])
            sisa_air = total_Material[2] - int(bahan[0][2])
            if sisa_pasir < 0:
                sisa_pasir = 0
            if sisa_batu < 0:
                sisa_batu = 0
            if sisa_air < 0:
                sisa_air = 0
            '''-------------------- 18 --------------------'''


            '''-------------------- 19 --------------------'''
            Visual.render_screen([f"Bangun gagal. Kurang {sisa_pasir} pasir, {sisa_batu} batu, dan {sisa_air} air."],1)
            time.sleep(2.5)
            '''-------------------- 19 --------------------'''

        '''-------------------- 15 --------------------'''

'''-------------------- 1 --------------------'''

'''-------------------------------------------------------------F08------------------------------------------------------------'''



'''-------------------------------------------------------------F09------------------------------------------------------------'''
def laporanjin ():
    import Visual
    # Komentar berikut merupakan algoritma dasar dalam output laporan jin
    
    # import tempdata
    # data_bahan = tempdata.data_bahan_bangunan

    # print("> Total Jin:", tempdata.len_user-2)
    # print("> Total Jin Pengumpul:", function_jin.count_jin("Pengumpul"))
    # print("> Total Jin Pembangun:", function_jin.count_jin("Pembangun"))
    # print("> Jin Terajin:", function_jin.jinter(True))
    # print("> Jin Termalas:", function_jin.jinter(False))
    # print("> Jumlah Pasir:", data_bahan[0][0], "unit")
    # print("> Jumlah Air:", data_bahan[0][2], "unit")
    # print("> Jumlah Batu:", data_bahan[0][1], "unit")

    # dalam kelompok kami, kami mengeluarkan output laporan jin yang dapat dilihat pada module laporan pada folder animasi
    Visual.printascii("laporan_jin", access)
    input()
'''-------------------------------------------------------------F09------------------------------------------------------------'''



'''-------------------------------------------------------------F10------------------------------------------------------------'''
def laporancandi():
    import Visual
    # Komentar berikut merupakan algoritma dasar dalam output laporan jin
    
    
    # import tempdata
    # print("> Total Candi:", tempdata.len_candi)
    # print("> Total Pasir yang digunakan:", function_candi.countbahan("pasir"))
    # print("> Total Batu yang digunakan:", function_candi.countbahan("batu"))
    # print("> Total Air yang digunakan:", function_candi.countbahan("air"))
    # ter_mahal, harga_mahal = function_candi.canditer(True)
    # print("> ID Candi Termahal:", ter_mahal, f"({harga_mahal})")
    # ter_murah, harga_murah = function_candi.canditer(False)
    # print("> ID Candi Termurah:", ter_murah, f"({harga_murah})")

    # dalam kelompok kami, kami mengeluarkan output laporan jin yang dapat dilihat pada module laporan pada folder animasi
    Visual.printascii("laporan_candi", access)
    input()
'''-------------------------------------------------------------F10------------------------------------------------------------'''



'''-------------------------------------------------------------F11------------------------------------------------------------'''

'''-------------------- Cek ID --------------------'''
# Fungsi cek id candi apakah ada atau tidak
def cekid(id: int) -> bool:
    import tempdata
    '''-------------------- Inisialisasi Awal Data --------------------'''
    data_candi = tempdata.data_candi # Mengambil data candi dan memasukkan ke variabel lokal
    '''-------------------- Inisialisasi Awal Data --------------------'''


    '''-------------------- Cek ID --------------------'''
    for i in range (tempdata.len_candi): # Loop untuk mencacah panjang candi
        cek = True # True berarti id tidak ada pada list id_candi_yang_dihancurkan

        for j in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk cek apakah id yang akan dihancurkan ada pada list id_candi_yang_dihancurkan
            if i + 1 == tempdata.id_candi_yang_dihancurkan[j]: # Kondisi saat id yang akan dihancurkan ada pada list id_candi_yang_dihancurkan
                cek = False # False berarti id ada pada list id_candi_yang_dihancurkan

        if cek: # Saat id yang akan dihancurkan tidak ada pada list id_candi_yang_dihancurkan 
            if data_candi[i] != [] and id == int(data_candi[i][0]): # Saat data candi yang sedang dicek tidak kosong dan id yang akan dihancurkan terdapat pada data candi
                return True # Mengembalikan True yang berarti id yang akan dihancurkan terdapat pada data candi
    '''-------------------- Cek ID --------------------'''

    return False # Mengembalikan False yang berarti id yang akan dihancurkan tidak terdapat pada data candi

'''-------------------- Cek ID --------------------'''


'''-------------------- Hapus ID --------------------'''
# Hapus id candi dari list
def remove_dataid(id: int):
    import tempdata

    '''-------------------- 2 --------------------'''
    for i in range(tempdata.len_candi):
        cek = True
        for j in range(tempdata.jumlah_candi_yang_dihancurkan):
            if i + 1 == tempdata.id_candi_yang_dihancurkan[j]:
                # id_candi_yang_dihancurkan merupakan kumpulan data berisi id candi yang telah dihapus
                # jadi jika id candi tersebut telah dihancurkan maka tidak "dihancurkan"
                cek = False
        if cek: 
            #jka candi belum dihancurkan
            #data candi digantikan dengan list kosong
            if int(tempdata.data_candi[i][0]) == id: # Asumsi id candi tidak ada yang sama
                tempdata.data_candi[i] =  []
    '''-------------------- 2 --------------------'''


    '''-------------------- 3 --------------------'''
    temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan+1)]
    #id candi yang telah dihancurkan disalin ke temphancur
    for i in range(tempdata.jumlah_candi_yang_dihancurkan):
        temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]

    #add data pada jumlah candi yang dihancurkan beserta dengan id nya
    temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id
    '''-------------------- 3 --------------------'''


    '''-------------------- 4 --------------------'''
    tempdata.jumlah_candi_yang_dihancurkan += 1 #Tracking jumlah candi yang telah dihancurkan
    tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<") #sort id yang telah dihancurkan secara descending
    '''-------------------- 4 --------------------'''

'''-------------------- 1 --------------------'''


'''-------------------- 1 --------------------'''
def hancurkancandi():
    import Visual

    '''-------------------- 2 --------------------'''
    id = int(input("Masukkan ID candi: ")) #Input id candi yang akan dihancurkan
    '''-------------------- 2 --------------------'''


    '''-------------------- 3 --------------------'''
    #cek candi apakah ada atau tidak
    if cekid(id):

        '''-------------------- 4 --------------------'''
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")#confirmasi untuk hancurkan candi
        '''-------------------- 4 --------------------'''


        '''-------------------- 5 --------------------'''
        while confirm != 'Y' and confirm != 'N': # Saat input user tidak sesuai dengan ketentuan
            Visual.render_screen(["EXIT", "", "", "Silakan masukan input sesuai dengan ketentuan"],4) # Pesan Kesalahan 
        '''-------------------- 5 --------------------'''

        '''-------------------- 6 --------------------'''
        if confirm == "Y":
            remove_dataid(id) # Menghapus id candi
            #visual hancurkan candi
            Visual.printascii("hancur_candi",access)
            Visual.printascii(access,access)
        '''-------------------- 6 --------------------'''

    else:

        '''-------------------- 7 --------------------'''
        Visual.render_screen(["Tidak ada candi dengan ID tersebut."],1)
        time.sleep(2)
        '''-------------------- 7 --------------------'''

    '''-------------------- 3 --------------------'''

'''-------------------- 1 --------------------'''

'''-------------------------------------------------------------F11------------------------------------------------------------'''



'''-------------------------------------------------------------F12------------------------------------------------------------'''
def ayamberkokok():
    import tempdata, Visual

    '''-------------------- Tampilan Animasi --------------------'''
    if tempdata.len_candi<100: # Saat jumlah candi kurang dari 100
        Visual.printascii("roro_menang",access)
        time.sleep(10)
    else: # Saat jumlah candi adalah 100
        Visual.printascii("bondo_menang",access)
        time.sleep(10)
    '''-------------------- Tampilan Animasi --------------------'''

'''-------------------------------------------------------------F12------------------------------------------------------------'''



'''------------------------------------------------------------F13------------------------------------------------------------'''
# Ada pada module load_only
'''------------------------------------------------------------F13------------------------------------------------------------'''



'''------------------------------------------------------------F14------------------------------------------------------------'''
def save():
    global path_folder
    import Visual

    '''-------------------- Tampilan Awal --------------------'''
    Visual.render_screen(["Save"],1)
    time.sleep(0.5)
    '''-------------------- Tampilan Awal --------------------'''


    '''-------------------- Input Nama Folder --------------------'''
    name_folder = input("Masukkan nama folder: ") # Meminta input nama folder tempat file akan disave
    path_folder = f"save/{name_folder}" # Membuat path directory untuk folder yang telah diinput
    '''-------------------- Input Nama Folder --------------------'''
    
    
    '''-------------------- Save File --------------------'''
    if not os.path.isdir(f"./{path_folder}"): # Saat folder belum ada namun folder parent 'save' sudah ada

        '''-------------------- Membuat Folder --------------------'''
        os.mkdir(f"./{path_folder}") # Membuat folder sesuai nama folder yang diinput
        '''-------------------- Membuat Folder --------------------'''

        '''-------------------- Menyimpan file CSV dalam folder --------------------'''
        util_function.write_csv("candi.csv", path_folder) # Menulis File candi.csv
        util_function.write_csv("user.csv", path_folder) # Menulis File user.csv
        util_function.write_csv("bahan_bangunan.csv", path_folder) # Menulis File bahan_bangunan.csv
        '''-------------------- Menyimpan file CSV dalam folder --------------------'''

        '''-------------------- Tampilan Animasi --------------------'''
        Visual.printascii("save1", access)
        '''-------------------- Tampilan Animasi --------------------'''

    elif not os.path.isdir("./save"): # Saat parent folder 'save' belum ada

        '''-------------------- Membuat Folder --------------------'''
        os.mkdir(f"./save") # Membuat folder parent 'save'
        os.mkdir(f"./{path_folder}") # Membuat folder sesuai nama folder yang diinput
        '''-------------------- Membuat Folder --------------------'''

        '''-------------------- Menyimpan file CSV dalam folder --------------------'''
        util_function.write_csv("candi.csv", path_folder) # Menulis File candi.csv
        util_function.write_csv("user.csv", path_folder) # Menulis File user.csv
        util_function.write_csv("bahan_bangunan.csv", path_folder) # Menulis File bahan_bangunan.csv
        '''-------------------- Menyimpan file CSV dalam folder --------------------'''

        '''-------------------- Tampilan Animasi --------------------'''
        Visual.printascii("save2",access)        
        '''-------------------- Tampilan Animasi --------------------'''

    elif os.path.isdir(f"./{path_folder}"): # Saat folder sudah ada dan folder parent 'save' sudah ada

        '''-------------------- Menyimpan file CSV dalam folder --------------------'''
        util_function.write_csv("candi.csv", path_folder) # Menulis File candi.csv
        util_function.write_csv("user.csv", path_folder) # Menulis File user.csv
        util_function.write_csv("bahan_bangunan.csv", path_folder) # Menulis File bahan_bangunan.csv
        '''-------------------- Menyimpan file CSV dalam folder --------------------'''

        '''-------------------- Tampilan Animasi --------------------'''
        Visual.printascii("save3",access)
        '''-------------------- Tampilan Animasi --------------------'''

    '''-------------------- Save File --------------------'''

'''------------------------------------------------------------F14------------------------------------------------------------'''

    

'''------------------------------------------------------------F15------------------------------------------------------------'''
def help():
    import Visual
    '''-------------------- Tampilan Help --------------------'''
    if logins: # Saat sudah login

        if access == "bandung_bondowoso": # Saat role user adalah bandung_bondowoso
            
            '''-------------------- Tampilan Help Bondowoso --------------------'''
            Visual.render_screen([" HELP ".center(28,"="), "", "1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. summonjin".ljust(80," "),"   Untuk memanggil jin dari dunia lain".ljust(80," "),
            "3. hapusjin".ljust(80," "),"   Untuk menghapus jin".ljust(80," "),
            "4. ubahjin".ljust(80," "),"   Untuk mengubah tipe jin".ljust(80," "),
            "5. batchkumpul".ljust(80," "),"   Untuk mengerahkan seluruh jin untuk mengumpulkan bahan".ljust(80," "),
            "6. batchbangun".ljust(80," "),"   Untuk mengerahkan seluruh jin untuk membangun".ljust(80," "),
            "7. laporanjin".ljust(80," "),"   Untuk mengambil laporan jin yang berisi kinerja para jin".ljust(80," "),
            "8. laporancandi".ljust(80," "),"   Untuk mengambil laporan candi yang berisi progress pembangunan candi".ljust(80," "),
            "9. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "10. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")], 22)
            '''-------------------- Tampilan Help Bondowoso --------------------'''

        elif access == "roro_jonggrang": # Saat role user adalah roro_jonggrang

            '''-------------------- Tampilan Help Roro --------------------'''
            Visual.render_screen([" HELP ".center(28,"="),"","1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. hancurkancandi".ljust(80," "),"   Untuk menghancurkan candi yang tersedia".ljust(80," "),
            "3. ayamberkokok".ljust(80," "),"   Untuk menyelesaikan permainan".ljust(80," "),
            "4. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "5. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],12)
            '''-------------------- Tampilan Help Roro --------------------'''

        elif access == "Pembangun": # Saat role user adalah Pembangun

            '''-------------------- Tampilan Help Jin Pembangun --------------------'''
            Visual.render_screen([" HELP ".center(28,"="),"","1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. bangun".ljust(80," "),"   Untuk membangun candi".ljust(80," "),
            "3. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "4. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],10)
            '''-------------------- Tampilan Help Jin Pembangun --------------------'''

        elif access == "Pengumpul": # Saat role user adalah Pengumpul

            '''-------------------- Tampilan Help Jin Pengumpul --------------------'''
            Visual.render_screen([" HELP ".center(28,"="),"","1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. kumpul".ljust(80," "),"   Untuk mengumpulkan resource candi".ljust(80," "),
            "3. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "4. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],10)
            '''-------------------- Tampilan Help Jin Pengumpul --------------------'''

    else: # Saat belum login

        '''-------------------- Tampilan Help Saat Belum Login --------------------'''
        Visual.render_screen([" HELP ".center(28,"="),"","1. login".ljust(80," "),"   Untuk masuk menggunakan akun".ljust(80," "),
        "2. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
        "3. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],8)
        '''-------------------- Tampilan Help Saat Belum Login --------------------'''

    '''-------------------- Tampilan Help --------------------'''

'''------------------------------------------------------------F15------------------------------------------------------------'''


    
'''------------------------------------------------------------F16------------------------------------------------------------'''
def keluar():
    import Visual

    '''-------------------- Tampilan Awal --------------------'''
    Visual.render_screen(["EXIT"],1)
    '''-------------------- Tampilan Awal --------------------'''


    '''-------------------- Konfirmasi Save File --------------------'''
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    # TODO: Validasi Konfirmasi
    while confirm != 'y' and confirm != 'n': # Saat input user tidak sesuai dengan ketentuan
        Visual.render_screen(["EXIT", "", "", "Silakan masukan input sesuai dengan ketentuan"],4) # Pesan Kesalahan 
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    '''-------------------- Konfirmasi Save File --------------------'''

    if confirm == 'y':
        save()
    Visual.printascii("exit",access)
'''------------------------------------------------------------F16------------------------------------------------------------'''
    
    
