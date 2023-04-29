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

        '''~~~~~~~~~~~~~~~~~~~~ Rekursif ~~~~~~~~~~~~~~~~~~~~'''
        login() # Mengulangi fungsi login 
        '''~~~~~~~~~~~~~~~~~~~~ Rekursif ~~~~~~~~~~~~~~~~~~~~'''

    else: # Saat user ditemukan pada data
        if password == cekpass: # ketika password yang diinput benar
            logins = True # Merubah variabel logins global menjadi benar (sudah login)
            access = datauser[index][2] # Merubah variabel access global menjadi role dari user
            user = datauser[index][0] # Merubah variabel user global menjadi username
            Visual.printascii(access,access) # Menampilkan animasi karakter
            
        else: # ketika password yang diinput salah
            Visual.render_screen(["Password salah!"],1) # Menampilkan pesan
            time.sleep(2.5)

            '''~~~~~~~~~~~~~~~~~~~~ Rekursif ~~~~~~~~~~~~~~~~~~~~'''
            login() # Mengulang fungsi login
            '''~~~~~~~~~~~~~~~~~~~~ Rekursif ~~~~~~~~~~~~~~~~~~~~'''
                        
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

        '''~~~~~~~~~~~~~~~~~~~~~    Rekursif    ~~~~~~~~~~~~~~~~~~~~~'''
        '''-------------------- Input Jenis Jin --------------------'''
        def minta_Jenis_Jin():   
            Visual.render_screen(["Jenis jin yang dapat dipanggil: ", # Animasi opsi jenis jin
            "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
            "(2) Pembangun - Bertugas membangun candi"], 3)

            jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ") # Menerima input jenis jin yang akan dipanggil

            # TODO: Validasi input
            if jin != "2" and jin != "1": # Loop untuk validasi input
                Visual.render_screen([f'Tidak ada jenis jin bernomor "{jin}"!'], 1) # Jika input di luar dari opsi
                time.sleep(2.5)
                return minta_Jenis_Jin() # Looping meminta input jenis jin jika masih tidak sesuai
            else:
                return int(jin) # Mengembalikan jenis jin jika sudah sesuai dengan pilihan yang tersedia
            
        jin = minta_Jenis_Jin() # Assign jenis jin dari fungsi rekursif mintaJenisJin
        '''-------------------- Input Jenis Jin --------------------'''
        '''~~~~~~~~~~~~~~~~~~~~    Rekursif     ~~~~~~~~~~~~~~~~~~~~'''


        '''~~~~~~~~~~~~~~~~~~~~      Rekursif      ~~~~~~~~~~~~~~~~~~~~'''
        '''-------------------- Input Username Jin --------------------'''
        def minta_User_Jin(jin):   
            # TODO: Meminta input sesuai tipe jin yang diinput sebelumnya
            if jin == 1: # Ketika user menginput opsi 1
                role = "Pengumpul"
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
                # Diasumsikan username jin semuanya berupa huruf alphabet tanpa tanda baca ataupun karakter lainnya
                username = input("Masukkan username jin: ") # Memasukkan username jin yang akan dipanggil 

                # TODO: Validasi username
                if function_jin.Cek_User(username): # Jika username sudah terdaftar akan looping meminta input
                    Visual.render_screen([f'Username "{username}" sudah diambil!'],1) 
                    time.sleep(2)
                    Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
                    return minta_User_Jin(jin)
                else:
                    return username, role
                
            else: # Ketika user menginput opsi 2
                role = "Pembangun"
                Visual.render_screen(['Memilih jin "Pembangun".'], 1)
                username = input("Masukkan username jin: ") # Memasukkan username jin yang akan dipanggil

                # TODO: Validasi username
                if function_jin.Cek_User(username): # Jika username sudah terdaftar akan looping meminta input
                    Visual.render_screen([f'Username "{username}" sudah diambil!'],1)  
                    time.sleep(2)
                    Visual.render_screen(['Memilih jin "Pembangun".'], 1)
                    return minta_User_Jin(jin) # Looping rekursif fungsi meminta username Jin
                else:
                    return username, role # Mengembalikan username dan role jin ketika sudah benar

        username, role = minta_User_Jin(jin) # Username dan role jin yang disummon akan disave pada variabel global untuk animasi
        '''-------------------- Input Username Jin --------------------'''
        '''~~~~~~~~~~~~~~~~~~~~      Rekursif      ~~~~~~~~~~~~~~~~~~~~'''


        '''~~~~~~~~~~~~~~~~~~~~      Rekursif      ~~~~~~~~~~~~~~~~~~~~'''
        '''-------------------- Input Password Jin --------------------'''
        def minta_Pass():
            # TODO: Meminta password dari user
            password = input("Masukkan password jin: ") # Meminta data password untuk username jin yang akan disummon

            # TODO: Validasi panjang password
            if 5 <= util_function.length(password + '.', '.') <= 25: # Jika password panjangnya tidak dari 5 sampai 25 huruf
                if role == "Pengumpul": # Sesuai opsi jenis jin yang dipilih di atas
                    Visual.render_screen(['Memilih jin "Pengumpul".'], 1) 
                    return password
                elif role == "Pembangun": # Sesuai opsi jenis jin yang dipilih di atas
                    Visual.render_screen(['Memilih jin "Pembangun".'], 1)
                    return password
            else:
                Visual.render_screen(["Password panjangnya harus 5-25 karakter!"],1) # Menampilkan pesan kesalahan
                time.sleep(2.5)
                return minta_Pass() # Looping rekursif fungsi meminta password
            
        password = minta_Pass() # Assign password berdasarkan input user dari fungsi rekursif mintaPass
        '''-------------------- Input Password Jin --------------------'''
        '''~~~~~~~~~~~~~~~~~~~~      Rekursif      ~~~~~~~~~~~~~~~~~~~~'''


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


        '''-------------------- Update Data Jin Yang Pernah Membangun Jika Role Jin Adalah Pembangun --------------------'''
        if role == "Pembangun":
            tempdata.len_pembangun += 1 # Panjang data bertambah 1 (ditambahkan jin yang baru disummon)

            temp_jin_yang_pernah_membangun = ['' for i in range(tempdata.len_pembangun)] # List sebagai tempat untuk menyimpan data baru
            for i in range(tempdata.len_pembangun-1): # Loop untuk mengisi data baru dengan data lama
                temp_jin_yang_pernah_membangun[i] = tempdata.data_jin_yang_pernah_membangun[i]

            temp_jin_yang_pernah_membangun[tempdata.len_pembangun-1] = username # Mengisi elemen terakhir list dengan jin pembangun yang baru di summon

            tempdata.data_jin_yang_pernah_membangun = temp_jin_yang_pernah_membangun # Mengupdate data global
        '''-------------------- Update Data Jin Yang Pernah Membangun Jika Role Jin Adalah Pembangun --------------------'''


        '''-------------------- Tampilan Animasi --------------------'''
        time.sleep(1)
        tempdata.data_user = tempdatas
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

        '''~~~~~~~~~~~~~~~~~~~~      Rekursif      ~~~~~~~~~~~~~~~~~~~~'''
        def konfirmasi_Nama_Jin():

            '''-------------------- Konfirmasi --------------------'''
            opsi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ") # Input user terkait konfirmasi penghapusan jin
            '''-------------------- Konfirmasi --------------------'''


            '''-------------------- Validasi Konfirmasi --------------------'''
            if opsi != "Y" and opsi != "N":
                Visual.render_screen(["Input tidak sesuai!","Silakan masukan (Y/N)!"],2) # Pesan kesalahan
                return konfirmasi_Nama_Jin()
            else:
                return opsi
            '''-------------------- Validasi Konfirmasi --------------------'''
        
        opsi = konfirmasi_Nama_Jin() # Assign variabel opsi dengan input dari fungsi rekursif konfirmasi_Nama_Jin
        '''~~~~~~~~~~~~~~~~~~~~      Rekursif      ~~~~~~~~~~~~~~~~~~~~'''

        '''-------------------- Penghapusan Jin --------------------'''
        if opsi == "Y": # Jika input user adalah Ya

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
            temp_data_user = [[] for i in range(tempdata.len_user - 1)] # list baru sebagai tempat untuk data user setelah jin dihilangkan
            j = 0 # Index untuk mencacah temp_data_user 
            for i in range(tempdata.len_user): # Loop untuk menghapus data jin lalu menaikkan semua data di bawahnya 1 indeks ke atas
                if i != index: # Ketika index pencacah data user tidak sama dengan index jin yang ingin dihapus
                    temp_data_user[j] = tempdata.data_user[i] 
                    j += 1 # Index pencacah bertambah 1
            '''-------------------- Menghapus Username Dari Data --------------------'''


            '''-------------------- Mengupdate Data User --------------------'''
            tempdata.len_user -= 1 # mengupdate panjang data user menjadi berkurang 1
            tempdata.data_user = temp_data_user # Meng-assign kembali tempdatas untuk data user
            '''-------------------- Mengupdate Data User --------------------'''


            '''-------------------- Mengupdate Data Candi yang Dihancurkan --------------------'''
            # TODO: Menghitung banyak candi yang telah dibangun jin yang akan dihapus 
            count = 0 # Banyak candi yang telah dibangun oleh jin yang akan dihapus
            for i in range(tempdata.len_candi): # Menghitung banyak candi yang dibangun oleh jin yang akan dihapus
                if datacandi[i] != []:  
                    if datacandi[i][1] == username:
                        count += 1

            # TODO: Inisialisasi Awal 
            tempdatas = [[] for i in range(tempdata.len_candi)] # Membuat list tempdatas baru untuk data candi
            
            # TODO: Mengupdate data candi yang dihancurkan
            for i in range(tempdata.len_candi): # Loop untuk mengisi tempdatas 
                if datacandi[i] != []: # Ketika data candi yang dicacah tidak kosong

                    if datacandi[i][1] != username: # Jika candi tidak dibangun oleh jin yang akan dihapus
                        tempdatas[i] = datacandi[i] # Candi tersebut akan di-assign ke tempdatas

                    else: # Jika candi dibuat oleh jin yang akan dihapus (tidak akan ditambahkan ke tempdatas)
                        id = datacandi[i][0] # ID Candi akan masuk ke variabel id

                        temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan + 1)] # List sementara candi yang dihancurkan
                        for i in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk mengisi list sementara dengan data yang sudah ada sebelum ditambahkan id baru
                            temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]

                        temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id # Meng-assign id candi yang dohancurkan

                        tempdata.jumlah_candi_yang_dihancurkan += 1 # Jumlah candi yang dihancurkan bertambah 1
                        tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<") # Mengurutkan data id candi yang dihancurkan dari yang terkecil

            tempdata.data_candi = tempdatas # Data candi terbaru dari tempdatas
            '''-------------------- Mengupdate Data Candi yang Dihancurkan --------------------'''


            '''-------------------- Mengupdate Data Jin Yang Pernah Membangun --------------------'''
            for i in range(tempdata.len_pembangun): # Loop untuk mencari username di data jin yang pernah membangun
                if tempdata.data_jin_yang_pernah_membangun[i] == username: # Ketika username ditemukan pada data jin yang pernah membangun
                    cek = True # Mengembalikan True yang berarti jin yang ingin dihapus ditemukan di data jin yang pernah membangun 

            if cek: # Kondisi saat jin yang ingin dihapus ditemukan di data jin yang pernah membangun
                tempdata.len_pembangun -= 1 # Panjang data kurang 1 karena jin yang akan dihapus akan dihapus dari data
                temp_data_jin_yang_pernah_membangun = ['' for i in range(tempdata.len_pembangun)] # List sebagai tempat untuk menyimpan data baru setelah jin dihapus
                j = 0 # Index untuk mencacah list temp_data_jin_yang_pernah_membangun 
                for i in range(tempdata.len_pembangun): # Loop untuk mengisi list baru
                    if tempdata.data_jin_yang_pernah_membangun[i] != username: # Ketika data lama yang akan dimasukan ke list baru bukan merupakan user jin yang ingin dihapus
                        temp_data_jin_yang_pernah_membangun[j] = tempdata.data_jin_yang_pernah_membangun[i] # Memasukan data lama ke list baru
                        j += 1 # Index list bertamabah 1
            '''-------------------- Mengupdate Data Jin Yang Pernah Membangun --------------------'''


            '''-------------------- Tampilan Animasi --------------------'''
            if data_user[index][2] == "Pembangun": # Jika role jin yang dihapus adalah pembangun
                Visual.printascii("hapus_jin_bangun",access) # Menampilkan animasi jin dihapus
                Visual.render_screen(["Jin telah berhasil dihapus dari alam gaib."],1)
                time.sleep(2)
            elif data_user[index][2] == "Pengumpul": # Jika role jin yang dihapus adalah pembangun
                Visual.printascii("hapus_jin_kumpul",access) # Menampilkan animasi jin dihapus
                Visual.render_screen(["Jin telah berhasil dihapus dari alam gaib."],1)
                time.sleep(2)
            '''-------------------- Tampilan Animasi --------------------'''

        '''-------------------- Penghapusan Jin --------------------'''

    '''-------------------- Cek Username --------------------'''

'''------------------------------------------------------------F04------------------------------------------------------------'''



'''------------------------------------------------------------F05------------------------------------------------------------'''
def ubahJin():
    import tempdata, Visual

    '''-------------------- Tampilan Awal --------------------'''
    Visual.render_screen(["Ubah Jin"],1) # Menampilkan screen 'Ubah Jin'
    time.sleep(0.5)
    '''-------------------- Tampilan Awal --------------------'''


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
        temp_role = function_jin.ubah_role(tempdata.data_user[index][2]) # Memanggil fungsi ubah_role
        '''-------------------- Mengubah Tipe Username --------------------'''

        if temp_role != "Tidak Jadi": # Ketika user jadi mengubah jin (return dari fungsi ubah_role bukan "Tidak Jadi" melainkan role jin yang telah diubah)
            tempdata.data_user[index][2] = temp_role 

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

'''-------------------- Batch Kumpul --------------------'''
def batchkumpul():
    import Visual

    '''-------------------- Menghitung Jumlah Jin Pengumpul --------------------'''
    jumlah_jin_Pengumpul = function_jin.count_jin("Pengumpul")
    '''-------------------- Menghitung Jumlah Jin Pengumpul --------------------'''


    if jumlah_jin_Pengumpul == 0: # Ketika tidak ada jin pengumpul
        
        '''-------------------- Tampilan Kesalahan --------------------'''
        Visual.render_screen(["Kumpul gagal","Anda tidak punya jin pengumpul","Silahkan summon terlebih dahulu."],3) # Pesan Kesalahan
        time.sleep(2)
        '''-------------------- Tampilan Kesalahan --------------------'''

    else: # Ketika ada jin pengumpul

        '''-------------------- Mengumpulkan Bahan --------------------'''
        pasir = 0 ; batu = 0 ; air = 0 # Hasil Kumpul Semua Jin
        for i in range(jumlah_jin_Pengumpul): # Loop untuk melakukan kumpul sebanyak jin pengumpul
            PBA = kumpul(True) # Melakukan kumpul per jin
            pasir += PBA[0] ; batu += PBA[1] ; air += PBA[2] # Menjumlahkan hasil kumpul semua jin
        '''-------------------- Mengumpulkan Bahan --------------------'''


        '''-------------------- Tampilan Informasi Kumpul --------------------'''
        Visual.render_screen([f"Mengerahkan {jumlah_jin_Pengumpul} jin untuk mengumpulkan bahan."],1)
        time.sleep(2.5)
        Visual.printascii("kumpul",access)
        Visual.render_screen([f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air."],1)
        time.sleep(2.5)
        '''-------------------- Tampilan Informasi Kumpul --------------------'''


    
'''-------------------- Batch Bangun --------------------'''
def batchbangun():  
    import tempdata, Visual

    '''-------------------- Menghitung Jumlah Jin Pembangun --------------------'''
    Jumlah_jin_Pembangun = function_jin.count_jin("Pembangun")
    '''-------------------- Menghitung Jumlah Jin Pembangun --------------------'''


    if Jumlah_jin_Pembangun == 0: # Ketika tidak ada jin pembangun
        
        '''-------------------- Tampilan Kesalahan --------------------'''
        Visual.render_screen(["Bangun gagal","Anda tidak punya jin pembangun","Silahkan summon terlebih dahulu."],3) # Pesan Kesalahan
        time.sleep(2)
        Visual.printascii(access,access)
        '''-------------------- Tampilan Kesalahan --------------------'''
        
    else: # Ketika ada jin pembangun

        '''-------------------- Mengambil Data --------------------'''
        data_user = tempdata.data_user # Memasukan data user ke variabel lokal
        '''-------------------- Mengambil Data --------------------'''


        '''-------------------- Menentukan Panjang Data --------------------'''
        if Jumlah_jin_Pembangun - tempdata.jumlah_candi_yang_dihancurkan > 0: # Ketika jumlah candi yang dihancurkan lebih sedikit daripada jumlah candi yang akan dibangun atau jumlah jin pembangunnya (akan menambah line baru pada data candi)
            lendata = tempdata.len_candi + Jumlah_jin_Pembangun - tempdata.jumlah_candi_yang_dihancurkan # Panjang data merupakan panjang data candi saat ini ditambah jumlah jin pembangun lalu dikurangi oleh data candi yang kosong atau data candi yang dihancurkan
        else: # Ketika jumlah candi yang akan dibangun lebih sedikit daripada jumlah candi yang dihancurkan
            lendata = tempdata.len_candi # Panjang data candi akan tetap (karena candi yang akan dibangun akan mengisi tempat yang kosong pada data candi terlebih dahulu)
        '''-------------------- Menentukan Panjang Data --------------------'''


        '''-------------------- Inisialisasi Awal --------------------'''
        temp_candi = [[] for i in range(lendata)] # Tempat untuk menyimpan data candi terbaru
        panjang_data_candi = tempdata.len_candi # Mengambil panjang data candi

        bahan = tempdata.data_bahan_bangunan # Mengambil data bahan bangunan dan memasukan ke variabel lokal
        total_Material = [0,0,0] # Tempat untuk menyimpan total material yang digunakan

        jin = ["" for i in range(Jumlah_jin_Pembangun)] # Tempat untuk menuliskan para jin pembangun
        j = 0 # Index untuk mencacah list jin

        temp_id_candi_yang_dihancurkan = tempdata.id_candi_yang_dihancurkan # Mengambil data id candi yang dihancurkan
        temp_jumlah_candi_yang_dihancurkan = tempdata.jumlah_candi_yang_dihancurkan # Mengambil data jumlah candi yang dihancurkan
        '''-------------------- Inisialisasi Awal --------------------'''


        '''-------------------- Menyalin Data ke Variabel Lokal --------------------'''
        for i in range(tempdata.len_candi): # Loop untuk mengisikan data global ke list lokal
            temp_candi[i] = tempdata.data_candi[i]
        '''-------------------- Menyalin Data ke Variabel Lokal --------------------'''


        '''-------------------- Mencari Jin Pembangun --------------------'''
        for i in range(tempdata.len_user): # Loop untuk mencari semua jin pembangun
            if data_user[i][2] == "Pembangun": # Ketika jin memiliki role Pembangun maka jin akan masuk ke list jin
                jin[j] = data_user[i][0] # Memasukan nama jin ke list jin
                j += 1 # Index bertambah 1
        '''-------------------- Mencari Jin Pembangun --------------------'''


        '''-------------------- Menentukan Data Candi yang Dibangun --------------------'''
        j = 0 # index untuk mencacah list jin
        for i in range(lendata): # Loop untuk mengisi data kosong pada temp_candi 
            if temp_candi[i] == []: # Ketika data kosong

                '''-------------------- Bahan yang Digunakan --------------------'''
                pasir = util_function.randint(1,5) ; batu = util_function.randint(1,5) ; air = util_function.randint(1,5) # Melakukan randomisasi pada bahan yang akan digunakan
                '''-------------------- Bahan yang Digunakan --------------------'''
                

                '''-------------------- Menentukan ID Candi --------------------'''
                if temp_jumlah_candi_yang_dihancurkan == 0: # Kondisi ketika tidak ada candi yg hancur
                    index = panjang_data_candi + 1 # ID Candi merupakan ID setelah ID terakhir pada data candi
                    panjang_data_candi+=1 # Panjang data akan bertambah 1
                else: # Kondisi ketika ada candi yg hancur
                    index = temp_id_candi_yang_dihancurkan[0] # mengambil id dari candi yang telah dihancurkan dan terkecil (mengambil index pertama karena data id candi yang dihancurkan sudah diurutkan)

                    tempdatas = [ 0 for i in range(temp_jumlah_candi_yang_dihancurkan - 1)] # Inisialisasi awal list baru untuk menyimpan list temp_id_candi_yang_dihancurkan ketika diambil 1 id tekecil
                    for k in range(1,temp_jumlah_candi_yang_dihancurkan): # mengisi list baru dengan list temp_id_candi_yang_dihancurkan setelah diambil 1 id terkecil
                        tempdatas[k-1] = temp_id_candi_yang_dihancurkan[k]
                    
                    temp_id_candi_yang_dihancurkan = tempdatas # merubah list temp_id_candi_yang_dihancurkan menjadi list temp_id_candi_yang_dihancurkan yang telah diambil 1 id terkecil
                    temp_jumlah_candi_yang_dihancurkan -= 1 # mengurangi jumlah candi yang dihancurkan (karena akan dibangun kembali)
                '''-------------------- Menentukan ID Candi --------------------'''


                '''-------------------- Melengkapi Data Candi --------------------'''
                harga = int(pasir) * 10000 + int(batu) * 15000 + int(air) * 7500 # Menentukan Harga Candi
                temp_candi[i] = [str(index),jin[j],str(pasir),str(batu),str(air),str(harga)] # Memplotkan data candi sesuai struktur
                j += 1 # Index jin yang membangun bertambah 1
                total_Material[0] += pasir ; total_Material[1] += batu ; total_Material[2] += air # Menjumlahkan total material yang digunakan
                '''-------------------- Melengkapi Data Candi --------------------'''

        '''-------------------- Menentukan Data Candi yang Dibangun --------------------'''


        '''-------------------- Tampilan Informasi --------------------'''
        Visual.render_screen([f"Mengerahkan {Jumlah_jin_Pembangun} jin untuk membangun candi dengan total bahan",
                              f"{total_Material[0]} pasir, {total_Material[1]} batu, dan {total_Material[2]} air."],2)
        time.sleep(2.5)
        '''-------------------- Tampilan Informasi --------------------'''


        '''-------------------- Cek Bahan --------------------'''
        if total_Material[0] <= int(bahan[0][0]) and total_Material[1] <= int(bahan[0][1]) and total_Material[2] <= int(bahan[0][2]): # Ketika bahan yang tersedia cukup untuk membangun

            bahan[0][0] = str(int(bahan[0][0]) - total_Material[0]) ; bahan[0][1] = str(int(bahan[0][1]) - total_Material[1]) ; bahan[0][2] = str(int(bahan[0][2]) - total_Material[2] ) # Bahan yang tersedia akan dikurangi dengan bahan yang diperlukan untuk membangun

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


            '''-------------------- Update Data --------------------'''
            tempdata.data_bahan_bangunan = bahan # Mengupdate data bahan setelah digunakan
            tempdata.len_candi = panjang_data_candi

            if lendata > 100: # Ketika jumlah candi yang terbangun lebih dari 100 maka data akan dipotong hanya 100 data
                temp_candi2 = [[] for i in range(100)] # tempat untuk menyimpan 100 data candi
                for i in range(100): # Mengisi list dengan 100 data candi
                    temp_candi2[i] = temp_candi[i]
                tempdata.data_candi = temp_candi2 # Update data candi dengan data yang sudah dipotong
                tempdata.len_candi = 100 # Update panjang candi
            else: # Ketika jumlah candi yang terbangun kurang dari 100
                tempdata.data_candi = temp_candi # Update data candi
                tempdata.len_candi = lendata # Update panjang candi

            tempdata.id_candi_yang_dihancurkan = temp_id_candi_yang_dihancurkan # Update id candi yang dihancurkan
            tempdata.jumlah_candi_yang_dihancurkan = temp_jumlah_candi_yang_dihancurkan # Update jumlah candi yang dihancurkan
            '''-------------------- Update Data --------------------'''


            '''-------------------- Tampilan Animasi --------------------'''
            Visual.printascii("batch_bangun",access)
            Visual.render_screen([f"Jin berhasil membangun total {Jumlah_jin_Pembangun} candi."],1)
            time.sleep(2.5)
            '''-------------------- Tampilan Animasi --------------------'''

        else:

            '''-------------------- Kekurangan Bahan --------------------'''
            kurang_pasir = total_Material[0] - int(bahan[0][0]) ;kurang_batu = total_Material[1] - int(bahan[0][1]); kurang_air = total_Material[2] - int(bahan[0][2]) # Menghitung kekurangan bahan

            if kurang_pasir < 0: # Ketika Pasir tidak kurang
                kurang_pasir = 0
            if kurang_batu < 0: # Ketika batu tidak kurang
                kurang_batu = 0
            if kurang_air < 0: # Ketika air tidak kurang
                kurang_air = 0
            '''-------------------- Kekurangan Bahan --------------------'''


            '''-------------------- Tampilan Informasi --------------------'''
            Visual.render_screen([f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air."],1)
            time.sleep(2.5)
            '''-------------------- Tampilan Informasi --------------------'''

        '''-------------------- Cek Bahan --------------------'''

'''-------------------- Batch Bangun --------------------'''

'''-------------------------------------------------------------F08------------------------------------------------------------'''



'''-------------------------------------------------------------F09------------------------------------------------------------'''
def laporanjin ():
    import Visual
    # Komentar berikut merupakan algoritma dasar dalam output laporan jin
    
    """
    import tempdata
    data_bahan = tempdata.data_bahan_bangunan

    print("> Total Jin:", tempdata.len_user-2)
    print("> Total Jin Pengumpul:", function_jin.count_jin("Pengumpul"))
    print("> Total Jin Pembangun:", function_jin.count_jin("Pembangun"))
    print("> Jin Terajin:", function_jin.jinter(True))
    print("> Jin Termalas:", function_jin.jinter(False))
    print("> Jumlah Pasir:", data_bahan[0][0], "unit")
    print("> Jumlah Air:", data_bahan[0][2], "unit")
    print("> Jumlah Batu:", data_bahan[0][1], "unit")
    """

    # dalam kelompok kami, kami mengeluarkan output laporan jin yang dapat dilihat pada module laporan
    Visual.printascii("laporan_jin", access)
    input()
'''-------------------------------------------------------------F09------------------------------------------------------------'''



'''-------------------------------------------------------------F10------------------------------------------------------------'''
def laporancandi():
    import Visual
    # Komentar berikut merupakan algoritma dasar dalam output laporan jin
    
    """
    import tempdata
    print("> Total Candi:", tempdata.len_candi)
    print("> Total Pasir yang digunakan:", function_candi.countbahan("pasir"))
    print("> Total Batu yang digunakan:", function_candi.countbahan("batu"))
    print("> Total Air yang digunakan:", function_candi.countbahan("air"))
    ter_mahal, harga_mahal = function_candi.canditer(True)
    print("> ID Candi Termahal:", ter_mahal, f"({harga_mahal})")
    ter_murah, harga_murah = function_candi.canditer(False)
    print("> ID Candi Termurah:", ter_murah, f"({harga_murah})")
    """
    
    # dalam kelompok kami, kami mengeluarkan output laporan jin yang dapat dilihat pada module laporan
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

    for i in range (tempdata.len_candi): # Loop untuk mencacah panjang candi (id candi)
        cek = True # True berarti id tidak ada pada list id_candi_yang_dihancurkan

        for j in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk cek apakah id yang akan dihancurkan ada pada list id_candi_yang_dihancurkan
            if i + 1 == tempdata.id_candi_yang_dihancurkan[j]: # Kondisi saat id yang akan dihancurkan ada pada list id_candi_yang_dihancurkan
                cek = False # False berarti id ada pada list id_candi_yang_dihancurkan

        if cek: # Saat id yang akan dihancurkan tidak ada pada list id_candi_yang_dihancurkan 
            if data_candi[i] != [] and id == int(data_candi[i][0]): # Saat data candi yang sedang dicek tidak kosong dan id yang akan dihancurkan terdapat pada data candi
                return True # Mengembalikan True yang berarti id yang akan dihancurkan terdapat pada data candi

    return False # Mengembalikan False yang berarti id yang akan dihancurkan tidak terdapat pada data candi

'''-------------------- Cek ID --------------------'''


'''-------------------- Hapus ID --------------------'''
# Hapus id candi dari list
def remove_dataid(id: int):
    import tempdata

    for i in range(tempdata.len_candi): # Loop untuk mencacah seluruh id candi
        cek = True # Kondisi saat id candi yang ingin dihancurkan tidak ada pada list id_candi_yang_dihancurkan
        for j in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk mencacah elemen pada list id_candi_yang_dihancurkan
            if i + 1 == tempdata.id_candi_yang_dihancurkan[j]:
                # id_candi_yang_dihancurkan merupakan kumpulan data berisi id candi yang telah dihapus
                # jadi jika id candi tersebut telah dihancurkan maka tidak dapat "dihancurkan" lagi
                cek = False
        if cek: 
            # jika candi belum dihancurkan data candi digantikan dengan list kosong
            if int(tempdata.data_candi[i][0]) == id: # Asumsi id candi tidak ada yang sama
                tempdata.data_candi[i] =  []

    '''-------------------- Update Data Candi Yang Dihancurkan --------------------'''
    temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan + 1)] # Tempat untuk menyimpan data id candi yang telah dihancurkan setelah ditambah 1 id baru
    
    for i in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk menyalin id candi yang telah dihancurkan ke temphancur
        temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]

    temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id # Tambahkan id pada list temphancur index terakhir 
    '''-------------------- Update Data Candi Yang Dihancurkan --------------------'''


    '''-------------------- Update Data Global --------------------'''
    tempdata.jumlah_candi_yang_dihancurkan += 1 # Jumlah candi yang telah dihancurkan bertambah 1
    tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<") # Sort id yang telah dihancurkan secara descending
    '''-------------------- Update Data Global --------------------'''

'''-------------------- Hapus ID --------------------'''


'''-------------------- Hancurkan Candi --------------------'''
def hancurkancandi():
    import Visual

    '''-------------------- Input ID --------------------'''
    id = int(input("Masukkan ID candi: ")) # Input id candi yang akan dihancurkan
    '''-------------------- Input ID --------------------'''


    '''-------------------- Hapus ID --------------------'''
    # cek candi apakah ada atau tidak
    if cekid(id):

        '''-------------------- Konfirmasi Hapus --------------------'''
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ") # Konfirmasi untuk hancurkan candi
        '''-------------------- Konfirmasi Hapus --------------------'''


        '''-------------------- Validasi Konfirmasi --------------------'''
        while confirm != 'Y' and confirm != 'N': # Saat input user bukan 'Y' atau 'N'
            Visual.render_screen(["EXIT", "", "", "Silakan masukan input sesuai dengan ketentuan!"],4) # Pesan Kesalahan 
        '''-------------------- Validasi Konfirmasi --------------------'''


        '''-------------------- Menghapus ID Candi --------------------'''
        if confirm == "Y":
            remove_dataid(id) # Menghapus id candi
            # Animasi hancurkan candi
            Visual.printascii("hancur_candi",access)
            Visual.printascii(access,access)
        '''-------------------- Menghapus ID Candi --------------------'''

    else:

        '''-------------------- Tampilan Animasi --------------------'''
        Visual.render_screen(["Tidak ada candi dengan ID tersebut."],1)
        time.sleep(2)
        '''-------------------- Tampilan Animasi --------------------'''

    '''-------------------- Hapus ID --------------------'''

'''-------------------- Hancurkan Candi --------------------'''

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
            "10. undo".ljust(80," "),"   Untuk mengembalikan jin yang telah dihapus".ljust(80," "),
            "11. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")], 24)
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




'''------------------------------------------------------------B04------------------------------------------------------------'''
def undo():
    import Visual, time, tempdata
    '''-------------------- Cek Jumlah Langkah (Stack) --------------------'''
    if tempdata.jumlah_stack == 1: # Ketika tidak ada langkah yang terekam
        
        '''-------------------- Tampilan Kesalahan --------------------'''
        Visual.render_screen(["Tidak ada data yang bisa di undo!", "Silakan melakukan penghapusan jin terlebih dahulu sebelum melakukan undo."],2) # Pesan Kesalahan
        time.sleep(2)
        '''-------------------- Tampilan Kesalahan --------------------'''

    else: # Ketika ada langkah yang terekam

        Visual.render_screen(["Apakah ingin melakukan undo penghapusan jin? (Y/N)"],1)
        
        '''~~~~~~~~~~~~~~~~~~~~    Rekursif     ~~~~~~~~~~~~~~~~~~~~'''
        '''-------------------- Konfirmasi Undo --------------------'''
        def Konfirmasi():
            konfirmasi = input("(Y/N)? ") # Meminta konfirmasi user

            '''-------------------- Validasi Konfirmasi Undo --------------------'''
            if konfirmasi != "Y" and konfirmasi != "N": # Ketika input user tidak sesuai ketentuan
                Visual.render_screen(["Input tidak sesuai!","Silakan masukan (Y/N)!"],2) # Pesan kesalahan
                return Konfirmasi() # memanggil fungsi Konfirmasi 
            else:
                return konfirmasi # Mengembalikan input user
            '''-------------------- Validasi Konfirmasi Undo --------------------'''
            
        konfirmasi = Konfirmasi() # Meminta konfirmasi user
        '''-------------------- Konfirmasi Undo --------------------'''
        '''~~~~~~~~~~~~~~~~~~~~    Rekursif     ~~~~~~~~~~~~~~~~~~~~'''


        if konfirmasi == "Y":
            tempdata.jumlah_stack -= 1

            '''-------------------- Update Data Setelah diUndo --------------------'''
            tempdata.data_candi = tempdata.undo_stack[tempdata.jumlah_stack-1][0] # Update data candi
            tempdata.len_candi = tempdata.undo_stack[tempdata.jumlah_stack-1][1] # Update panjang candi
            tempdata.data_user = tempdata.undo_stack[tempdata.jumlah_stack-1][2] # Update data user
            tempdata.len_user = tempdata.undo_stack[tempdata.jumlah_stack-1][3] # Update panjang user
            tempdata.data_jin_yang_pernah_membangun = tempdata.undo_stack[tempdata.jumlah_stack-1][4] # Update data jin yang pernah membangun
            tempdata.len_pembangun = tempdata.undo_stack[tempdata.jumlah_stack-1][5] # Update panjang data jin yang pernah membangun
            '''-------------------- Update Data Setelah diUndo --------------------'''


            '''-------------------- Update Stack Setelah diUndo --------------------'''
            temp_undo_stack = [[] for i in range(tempdata.jumlah_stack)] # Tempat untuk data stack setelah melakukan undo 
            for i in range(tempdata.jumlah_stack): # Loop untuk mengisi stack data terbaru dengan data yang lama setelah dilakukan undo (panjang berkurang 1)
                temp_undo_stack[i] = tempdata.undo_stack[i] 
            '''-------------------- Update Stack Setelah diUndo --------------------'''


            '''-------------------- Tampilan Animasi --------------------'''
            Visual.printascii("undo",access)
            '''-------------------- Tampilan Animasi --------------------'''

    '''-------------------- Cek Jumlah Langkah (Stack) --------------------'''
                
def update_stack(command: str):
    import tempdata
    if command == "save": # Ketika ingin update data stack setelah melakukan save (Reset data stack)

        '''-------------------- Update Isi Stack --------------------'''
        tempdata.jumlah_stack = 1
        tempdata.undo_stack = [[tempdata.data_candi, tempdata.len_candi, tempdata.data_user, tempdata.len_user, tempdata.data_jin_yang_pernah_membangun, tempdata.len_pembangun]]
        '''-------------------- Update Isi Stack --------------------'''

    elif command == "hapus": # Ketika ingin update stack setelah melakukan hapus jin

        '''-------------------- Update Panjang Stack --------------------'''
        tempdata.jumlah_stack += 1 # banyak langkah yang dijalankan bertambah 1
        '''-------------------- Update Panjang Stack --------------------'''

        '''-------------------- Update Isi Stack --------------------'''
        temp_undo_stack = [[] for i in range(tempdata.jumlah_stack)] # list sebagai tempat untuk data stack terbaru
        for i in range(tempdata.jumlah_stack - 1): # Mengisi list dengan data stack yang lama
            temp_undo_stack[i] = tempdata.undo_stack[i]

        temp_undo_stack[tempdata.jumlah_stack-1] = [tempdata.data_candi, tempdata.len_candi, tempdata.data_user, tempdata.len_user, tempdata.data_jin_yang_pernah_membangun, tempdata.len_pembangun] # Menambahkan data stack terbaru setelah user menghapus jin

        tempdata.undo_stack = temp_undo_stack # Update data stack
        '''-------------------- Update Isi Stack --------------------'''


'''------------------------------------------------------------B04------------------------------------------------------------'''