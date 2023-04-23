import util_function, function_jin, time, function_candi, os.path, typing
logins = False
access = ""
user = "asdf"
path_folder = ""
username_jin_summon = ""

'''-------------------------------F01------------------------------'''
def login():
    import tempdata, Visual
    global logins, access, user
    Visual.render_screen(["Login"],1)
    time.sleep(0.5)
    datapass = tempdata.data_user
    username = input("Username: ")
    password = input("Password: ")

    index = 0
    cekuser = False
    cekpass = ""
    for i in range(tempdata.len_user):
        if datapass[i][0] == username: # datapass[i](akun pada baris ke brp pada data)[0](username)
            cekuser = True
            index = i
            cekpass = datapass[i][1]
    if not cekuser:
        Visual.render_screen(["Username tidak terdaftar!"],1)
        time.sleep(2.5)
        login()
    else:
        if password == cekpass:
            access = datapass[index][2]
            user = datapass[index][0]
            logins = True
            Visual.printascii(access,access)
            
        else:
            Visual.render_screen(["Password salah!"],1)
            time.sleep(2.5)
            login()

'''-------------------------------F02------------------------------'''
def logout():
    import Visual
    global logins, access, user
    logins = False
    access = ""
    user = ""
    
    Visual.printascii("logout",None)
    login()


''' ------------------------------F03------------------------------ '''
def summonJin():
    global username_jin_summon # Username dari jin yang akan disummon
    import tempdata, Visual
    Visual.render_screen(["Summon Jin"],1) # Menampilkan animasi summon jin
    time.sleep(0.5)
    if tempdata.len_user < 102: # Jika total jin masih di bawah 100
        Visual.render_screen(["Jenis jin yang dapat dipanggil: ", # Animasi opsi jenis jin
        "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
        "(2) Pembangun - Bertugas membangun candi"], 3)

        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ")) # Menerima input jenis jin yang akan dipanggil
        while jin != 2 and jin != 1:
            Visual.render_screen([f'Tidak ada jenis jin bernomor "{jin}"!'], 1) # Jika input di luar dari opsi
            time.sleep(2.5)
            Visual.render_screen(["Jenis jin yang dapat dipanggil: ",
            "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
            "(2) Pembangun - Bertugas membangun candi"], 3)
            jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ")) # Looping meminta input jenis jin

        if jin == 1: # Ketika user menginput opsi 1
            role = "Pengumpul"
            Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
            username = input("Masukkan username jin: ") # Memasukkan username jin yang akan dipanggil
            while function_jin.Cek_User(username): # Jika username sudah terdaftar akan looping meminta input
                Visual.render_screen([f'Username "{username}" sudah diambil!'],1) 
                time.sleep(2)
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
                username = input("Masukkan username jin: ")
        else: # Ketika user menginput opsi 2
            role = "Pembangun"
            Visual.render_screen(['Memilih jin "Pembangun".'], 1)
            username = input("Masukkan username jin: ") # Memasukkan username jin yang akan dipanggil
            while function_jin.Cek_User(username): # Jika username sudah terdaftar akan looping meminta input
                Visual.render_screen([f'Username "{username}" sudah diambil!'],1)  
                time.sleep(2)
                Visual.render_screen(['Memilih jin "Pembangun".'], 1)
                username = input("Masukkan username jin: ")
        username_jin_summon = username # Username akan disave sesuai dengan variabel username

        password = input("Masukkan password jin: ") # Meminta data password untuk username jin yang akan disummon
        while not 5 <= util_function.length(password + '.', '.') <= 25: # Jika password panjangnya tidak dari 5 sampai 25 huruf
            Visual.render_screen(["Password panjangnya harus 5-25 karakter!"],1)
            time.sleep(2.5)
            if role == "Pengumpul": # Sesuai opsi jenis jin yang dipilih di atas
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1) 
            elif role == "Pembangun": # Sesuai opsi jenis jin yang dipilih di atas
                Visual.render_screen(['Memilih jin "Pembangun".'], 1)
            password = input("Masukkan password jin: ")

        datas = [username,password,role] # Mengubah inputan data menjadi bentuk list bernama datas
        # commanddata.save_csv("user.csv", datas)

        tempdatas = [[] for i in range(tempdata.len_user + 1)] # Menambahkan list datas ke ke datas temporary untuk disave sementara
        for i in range(tempdata.len_user):
            tempdatas[i] = tempdata.data_user[i]
        tempdatas[tempdata.len_user] = datas        
        tempdata.len_user += 1

        tempdata.data_user = tempdatas # Memasukkan tempdatas ke data user

        time.sleep(1)
        if role == "Pengumpul":
            Visual.printascii("summon_pengumpul",access) # Menampilkan animasi summon jin pengumpul
        elif role == "Pembangun":
            Visual.printascii("summon_pembangun",access) # Menampilkan animasi summon jin pembangun

        
    else: # Jika jin yang terdaftar sudah 100
        Visual.render_screen(["Jumlah Jin telah maksimal! (100 jin).",f"{user} tidak dapat men-summon lebih dari itu."],2)
        time.sleep(2)
    

''' ------------------------------F04------------------------------ '''
def hapusJin():
    import tempdata, Visual
    Visual.render_screen(["Hapus Jin"],1) # Menampilkan animasi tampilan opsi penghapusan jin
    time.sleep(0.5)
    username = input("Masukkan username jin : ") # Meminta input username jin yang akan dihapus

    if not function_jin.Cek_User(username): # Jika username yang diinput tidak memiliki kesamaan dengan data yang ada
        Visual.render_screen(["Tidak ada jin dengan username tersebut."],1)
        time.sleep(2)
        Visual.printascii(access, access)
    elif function_jin.Cek_User(username): # Jika username terdaftar di dalam data
        option = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ") # Input user terkait konfirmasi penghapusan jin

        if option == "Y": # Jika input user adalah Ya
            data_user = tempdata.data_user # Mengambil data user
            datacandi = tempdata.data_candi # Mengambil data candi
            for i in range(tempdata.len_user):
                if data_user[i][0] == username: # Mencari indeks data yang usernamenya sesuai dengan input user
                    index = i
            for i in range(index,tempdata.len_user-1): 
                tempdata.data_user[i] = tempdata.data_user[i+1] # Menghapus data jin lalu menaikkan semua data di bawahnya 1 indeks ke atas
            tempdata.len_user -= 1 # panjang tempdata berkurang 1
            tempdatas = [[] for i in range(tempdata.len_user)] # Membuat ulang tempdata yang baru
            for i in range(tempdata.len_user):
                tempdatas[i] = tempdata.data_user[i]
            tempdata.data_user = tempdatas # Meng-assign kembali tempdatas untuk data user

            count = 0 
            for i in range(tempdata.len_candi): # Menghitung banyak candi yang dibangun oleh jin yang akan dihapus
                if datacandi[i][1] == username:
                    count+=1

            tempdatas = [[] for i in range(tempdata.len_candi - count)] # Membuat list tempdatas baru
            j = 0
            for i in range(tempdata.len_candi):
                if datacandi[i][1] != username: # Jika candi tidak dibangun oleh jin yang akan dihapus
                    tempdatas[j] = datacandi[i] # Candi tersebut akan di-assign ke tempdatas
                    j+=1
                else: # Jika candi dibuat oleh jin yang akan dihapus
                    tempdata.len_candi-=1 # Panjang data candi berkurang 1
                    id = datacandi[i][0] # ID Candi akan masuk ke variabel id
                    temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan + 1)] # List sementara candi yang dihancurkan
                    for i in range(tempdata.jumlah_candi_yang_dihancurkan):
                        temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]
                    temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id # Meng-assign id candi yang dohancurkan
                    tempdata.jumlah_candi_yang_dihancurkan += 1 # Jumlah candi yang dihancurkan bertambah 1
                    tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<")
            tempdata.data_candi = tempdatas # Data candi terbaru dari tempdatas
            if data_user[index][2] == "Pembangun": # Jika role jin yang dihapus adalah pembangun
                Visual.printascii("hapus_jin_bangun",access) # Menampilkan animasi jin dihapus
            elif data_user[index][2] == "Pengumpul": # Jika role jin yang dihapus adalah pembangun
                Visual.printascii("hapus_jin_kumpul",access) # Menampilkan animasi jin dihapus



''' ------------------------------F05------------------------------ '''
def ubahJin():
    import tempdata, Visual
    username = input("Masukkan username jin : ")

    if not function_jin.Cek_User(username):
        Visual.render_screen(["Tidak ada jin dengan username tersebut."],1)
        time.sleep(2)
        Visual.printascii(access,access)
    else:
        data_user = tempdata.data_user
        for i in range(tempdata.len_user):
            if data_user[i][0] == username:
                index = i
        tempdata.data_user[index][2] = function_jin.ubah_role(tempdata.data_user[index][2])

        if tempdata.data_user[index][2] == "Pembangun":
            Visual.printascii("ubah_kumpul_bangun",access)
        elif tempdata.data_user[index][2] == "Pengumpul":
            Visual.printascii("ubah_bangun_kumpul",access)
    

''' -------------------------------F06------------------------------ '''
def bangun(username: str):
    import tempdata, Visual
    # candi = commanddata.read_csv("candi.csv")
    candi = tempdata.data_candi
    # bahan = commanddata.read_csv(f"bahan_bangunan.csv")
    bahan = tempdata.data_bahan_bangunan
    pasir = util_function.randint(1,5) ; batu = util_function.randint(1,5) ; air = util_function.randint(1,5)

        
    if pasir <= int(bahan[0][0]) and batu <= int(bahan[0][1]) and air <= int(bahan[0][2]):
        bahan[0][0] = str(int(bahan[0][0]) - pasir) ; bahan[0][1] = str(int(bahan[0][1]) - batu) ; bahan[0][2] = str(int(bahan[0][2]) - air )
        material = [str(pasir),str(batu),str(air)]
        tempdata.data_bahan_bangunan = bahan
        if tempdata.len_candi < 100:
            if tempdata.jumlah_candi_yang_dihancurkan == 0:
                tempdatacandi = [[] for i in range(tempdata.len_candi + 1)]
                for i in range(tempdata.len_candi):
                    tempdatacandi[i] = candi[i]

                tempdatacandi[tempdata.len_candi-1] = function_candi.saveCandi(material, username)
                tempdata.data_candi = tempdatacandi
            else:
                tempdatacandi = [[] for i in range(tempdata.len_candi)]
                cek = True
                for i in range(tempdata.len_candi):
                    if tempdatacandi[i] == [] and cek:
                        tempdatacandi[i] = function_candi.saveCandi(material, username)
                        cek = False
                    else:
                        tempdatacandi[i] = candi[i]
                tempdata.data_candi = tempdatacandi
            
            '''---------- Cek apakah username ada di list jin_yang_pernah_membangun atau tidak ----------'''
            # Kalau ada, maka list jin_yang_pernah_membangun tidak ditambahkan username
            # Kalau tidak ada, maka list jin_yang_pernah_membangun ditambahkan username
            cek = True  # Kondisi awal apabila user tidak ditemukan dalam list jin_yang_pernah_membangun
            for j in range(tempdata.len_pembangun): # Loop untuk mengecek apakah user ada didalam list jin_yang_pernah_membangun atau tidak
                if tempdata.data_jin_yang_pernah_membangun[j] == username:   # Kondisi saat user ditemukan ada didalam list jin_yang_pernah_membangun
                    cek = False
            if cek: # Kondisi saat user tidak ditemukan dalam list jin_yang_pernah_membangun
                tempdata.len_pembangun += 1 # Panjang list jin_yang_pernah_membangun bertambah 1
                temp_jin_pembangun = ["" for i in range(tempdata.len_pembangun)]    # Inisialisasi awal list baru untuk menyimpan list jin_yang_pernah_membangun yang akan ditambah user baru
                for j in range(tempdata.len_pembangun): # Loop untuk mengisi list baru dengan list jin_yang_pernah_membangun dan user baru
                    if i != tempdata.len_pembangun - 1:
                        temp_jin_pembangun[i] = tempdata.data_jin_yang_pernah_membangun
                    else:
                        temp_jin_pembangun[i] = username


            Visual.printascii("bangun_candi",access)
            Visual.render_screen([f"Sisa candi yang perlu dibangun: {100-tempdata.len_candi}."],1)
            time.sleep(2.5)

        else:
            Visual.printascii("bangun_candi",access)
            Visual.render_screen(["Sisa candi yang perlu dibangun: 0."],1)
            time.sleep(2.5)
    else:
        Visual.render_screen(["Bahan bangunan tidak mencukupi","Candi tidak bisa dibangun!"],2)
        time.sleep(2.5)
    
''' -------------------------------F07------------------------------ '''
def kumpul(batch: bool):
    import tempdata, Visual
    pasir = util_function.randint(0,5) ; batu = util_function.randint(0,5) ; air = util_function.randint(0,5)
    bahan = tempdata.data_bahan_bangunan
    bahan[0][0] = str(int(bahan[0][0]) + pasir) ; bahan[0][1] = str(int(bahan[0][1]) + batu) ; bahan[0][2] = str(int(bahan[0][2]) + air )
    if batch :
        return [pasir,batu,air]
    else:
        Visual.printascii("kumpul", access)
        Visual.render_screen([f"Jin menemukan {pasir} pasir, {batu} batu, {air} air."],1)
        time.sleep(2.5)

    
''' -------------------------------F08------------------------------ '''
def batchkumpul():
    import Visual
    jinPengumpul = function_jin.count_jin("Pengumpul")

    if jinPengumpul == 0:
        Visual.render_screen(["Kumpul gagal","Anda tidak punya jin pengumpul","Silahkan summon terlebih dahulu."],3)
        time.sleep(2)
        Visual.printascii(access,access)
    else:
        pasir = 0 ; batu = 0 ; air = 0
        for i in range(jinPengumpul):
            PBA = kumpul(True)
            pasir += PBA[0] ; batu += PBA[1] ; air += PBA[2]

        Visual.render_screen([f"Mengerahkan {jinPengumpul} jin untuk mengumpulkan bahan."],1)
        time.sleep(2.5)
        Visual.printascii("kumpul",access)
        Visual.render_screen([f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air."],1)
        time.sleep(2.5)

    
def batchbangun():  
    import tempdata, Visual
    Jumlah_jin_Pembangun = function_jin.count_jin("Pembangun")

    if Jumlah_jin_Pembangun == 0:
        Visual.render_screen(["Bangun gagal","Anda tidak punya jin pembangun","Silahkan summon terlebih dahulu."],3)
        time.sleep(2)
        Visual.printascii(access,access)
    else:
        data_user = tempdata.data_user 
        if Jumlah_jin_Pembangun - tempdata.jumlah_candi_yang_dihancurkan > 0:
            lendata = tempdata.len_candi + Jumlah_jin_Pembangun - tempdata.jumlah_candi_yang_dihancurkan
        else:
            lendata = tempdata.len_candi
        temp_candi = [[] for i in range(lendata)]
        for i in range(tempdata.len_candi):
            temp_candi[i] = tempdata.data_candi[i]
        total_Material = [0,0,0]
        bahan = tempdata.data_bahan_bangunan
        jin = ["" for i in range(Jumlah_jin_Pembangun)]

        j = 0
        for i in range(tempdata.len_user):
            if data_user[i][2] == "Pembangun":
                jin[j] = data_user[i][0]
                j += 1

        temp_id_candi_yang_dihancurkan = tempdata.id_candi_yang_dihancurkan
        temp_jumlah_candi_yang_dihancurkan = tempdata.jumlah_candi_yang_dihancurkan

        j = 0
        for i in range(lendata):
            if temp_candi[i] == []:
                pasir = util_function.randint(1,5) ; batu = util_function.randint(1,5) ; air = util_function.randint(1,5)
                material = [str(pasir),str(batu),str(air)]
                
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

                harga = int(material[0]) * 10000 + int(material[1]) * 15000 + int(material[2]) * 7500
                temp_candi[i] = [index,jin[j],material[0],material[1],material[2],harga]
                j += 1
                total_Material[0] += pasir ; total_Material[1] += batu ; total_Material[2] += air

        Visual.render_screen([f"Mengerahkan {Jumlah_jin_Pembangun} jin untuk membangun candi dengan total bahan",
                              f"{total_Material[0]} pasir, {total_Material[1]} batu, dan {total_Material[2]} air."],2)
        time.sleep(2.5)


        if total_Material[0] <= int(bahan[0][0]) and total_Material[1] <= int(bahan[0][1]) and total_Material[2] <= int(bahan[0][2]):
            bahan[0][0] = str(int(bahan[0][0]) - total_Material[0]) ; bahan[0][1] = str(int(bahan[0][1]) - total_Material[1]) ; bahan[0][2] = str(int(bahan[0][2]) - total_Material[2] )


            '''---------- Cek apakah username ada di list jin_yang_pernah_membangun atau tidak ----------'''
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
                        temp_jin_pembangun = ["" for i in range(tempdata.len_pembangun)]    # Inisialisasi awal list baru untuk menyimpan list jin_yang_pernah_membangun yang akan ditambah user baru
                        for j in range(tempdata.len_pembangun): # Loop untuk mengisi list baru dengan list jin_yang_pernah_membangun dan user baru
                            if j != tempdata.len_pembangun - 1:
                                temp_jin_pembangun[j] = tempdata.data_jin_yang_pernah_membangun
                            else:
                                temp_jin_pembangun[j] = data_user[i][2]

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
            Visual.printascii("batch_bangun",access)
            Visual.render_screen([f"Jin berhasil membangun total {Jumlah_jin_Pembangun} candi."],1)
            time.sleep(2.5)

        else:
            sisa_pasir = total_Material[0] - int(bahan[0][0])
            sisa_batu = total_Material[1] - int(bahan[0][1])
            sisa_air = total_Material[2] - int(bahan[0][2])
            if sisa_pasir < 0:
                sisa_pasir = 0
            if sisa_batu < 0:
                sisa_batu = 0
            if sisa_air < 0:
                sisa_air = 0
            Visual.render_screen([f"Bangun gagal. Kurang {sisa_pasir} pasir, {sisa_batu} batu, dan {sisa_air} air."],1)
            time.sleep(2.5)


''' -------------------------------F09------------------------------ '''
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

''' -------------------------------F10------------------------------ '''
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

''' -------------------------------F11------------------------------ '''
def cekid(id: int) -> bool:
    import tempdata
    data_candi = tempdata.data_candi
    for i in range (tempdata.len_candi):
        cek = True
        for j in range(tempdata.jumlah_candi_yang_dihancurkan): # Loop untuk cek apakah id yang akan dihancurkan ada pada list id_candi_yang_dihancurkan
            if i + 1 == tempdata.id_candi_yang_dihancurkan[j]:
                cek = False
        if cek: # Saat id yang akan dihancurkan tidak ada pada list id_candi_yang_dihancurkan 
            if data_candi[i] != [] and id == int(data_candi[i][0]):
                return True
    return False

# TODO: Remove Specific line of data from array
def remove_dataid(id: int):
    import tempdata
    for i in range(tempdata.len_candi):
        cek = True
        for j in range(tempdata.jumlah_candi_yang_dihancurkan):
            if i + 1 == tempdata.id_candi_yang_dihancurkan[j]:
                cek = False
        if cek: 
            if int(tempdata.data_candi[i][0]) == id: # Asumsi id candi tidak ada yang sama
                tempdata.data_candi[i] =  []


    temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan+1)]
    for i in range(tempdata.jumlah_candi_yang_dihancurkan):
        temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]
    temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id
    tempdata.jumlah_candi_yang_dihancurkan += 1
    tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<")


def hancurkancandi():
    import Visual
    id = int(input("Masukkan ID candi: "))
    if cekid(id):
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        if confirm == "Y":
            remove_dataid(id)
            Visual.printascii("hancur_candi",access)
            Visual.printascii(access,access)

    else:
        Visual.render_screen(["Tidak ada candi dengan ID tersebut."],1)
        time.sleep(2)

''' -------------------------------F12------------------------------ '''
def ayamberkokok():
    import tempdata, Visual

    if tempdata.len_candi<100:
        Visual.printascii("roro_menang",access)
        time.sleep(10)
    else:
        Visual.printascii("bondo_menang",access)
        time.sleep(10)


''' ------------------------------F13------------------------------ '''

# Ada pada module load_only


''' ------------------------------F14------------------------------ '''
def save():
    global path_folder
    import Visual
    Visual.render_screen(["Save"],1)
    time.sleep(0.5)
    name_folder = input("Masukkan nama folder: ")
    path_folder = f"save/{name_folder}"
    
    

    if not os.path.isdir(f"./{path_folder}"):
        os.mkdir(f"./{path_folder}")

        util_function.write_csv("candi.csv", path_folder)
        util_function.write_csv("user.csv", path_folder)
        util_function.write_csv("bahan_bangunan.csv", path_folder)

        Visual.printascii("save1", access)
    elif not os.path.isdir("./save"):
        os.mkdir(f"./save")
        os.mkdir(f"./{path_folder}")

        util_function.write_csv("candi.csv", path_folder)
        util_function.write_csv("user.csv", path_folder)
        util_function.write_csv("bahan_bangunan.csv", path_folder)

        Visual.printascii("save2",access)        
    elif os.path.isdir(f"./{path_folder}"):
        util_function.write_csv("candi.csv", path_folder)
        util_function.write_csv("user.csv", path_folder)
        util_function.write_csv("bahan_bangunan.csv", path_folder)

        Visual.printascii("save3",access)
    

''' ------------------------------F15------------------------------ '''
def help():
    import Visual
    print(" HELP ".center(28,"="))
    if logins:
        if access == "bandung_bondowoso":
            Visual.render_screen(["1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. summonjin".ljust(80," "),"   Untuk memanggil jin dari dunia lain".ljust(80," "),
            "3. hapusjin".ljust(80," "),"   Untuk menghapus jin".ljust(80," "),
            "4. ubahjin".ljust(80," "),"   Untuk mengubah tipe jin".ljust(80," "),
            "5. batchkumpul".ljust(80," "),"   Untuk mengerahkan seluruh jin untuk mengumpulkan bahan".ljust(80," "),
            "6. batchbangun".ljust(80," "),"   Untuk mengerahkan seluruh jin untuk membangun".ljust(80," "),
            "7. laporanjin".ljust(80," "),"   Untuk mengambil laporan jin yang berisi kinerja para jin".ljust(80," "),
            "8. laporancandi".ljust(80," "),"   Untuk mengambil laporan candi yang berisi progress pembangunan candi".ljust(80," "),
            "9. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "10. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")], 20)

        elif access == "roro_jonggrang":
            Visual.render_screen(["1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. hancurkancandi".ljust(80," "),"   Untuk menghancurkan candi yang tersedia".ljust(80," "),
            "3. ayamberkokok".ljust(80," "),"   Untuk menyelesaikan permainan".ljust(80," "),
            "4. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "5. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],10)

        elif access == "Pembangun":
            Visual.render_screen(["1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. bangun".ljust(80," "),"   Untuk membangun candi".ljust(80," "),
            "3. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "4. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],8)

        elif access == "Pengumpul":
            Visual.render_screen(["1. logout".ljust(80," "),"   Untuk keluar dari akun yang digunakan sekarang".ljust(80," "),
            "2. kumpul".ljust(80," "),"   Untuk mengumpulkan resource candi".ljust(80," "),
            "3. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
            "4. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],8)
    else:
        Visual.render_screen(["1. login".ljust(80," "),"   Untuk masuk menggunakan akun".ljust(80," "),
        "2. save".ljust(80," "),"   Untuk menyimpan data yang berada di program".ljust(80," "),
        "3. exit".ljust(80," "),"   Untuk keluar dari permainan".ljust(80," ")],6)

    
''' ------------------------------F16------------------------------ '''
def keluar():
    import Visual
    Visual.render_screen(["EXIT"],1)
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while confirm != 'y' and confirm != 'n':
        Visual.render_screen(["EXIT"],1)
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if confirm == 'y':
        save()
    Visual.printascii("exit",access)
    
    
