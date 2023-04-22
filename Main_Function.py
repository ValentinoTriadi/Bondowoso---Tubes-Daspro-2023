import util_function, function_jin, time, function_candi, os.path
logins = False
access = ""
user = ""
path_folder = ""

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
        time.sleep(1)
        login()
    else:
        if password == cekpass:
            access = datapass[index][2]
            user = datapass[index][0]
            logins = True
            Visual.printascii(access,access)
            
        else:
            Visual.render_screen(["Password salah!"],1)
            time.sleep(1)
            login()

'''-------------------------------F02------------------------------'''
def logout():
    import Visual
    global logins, access, user
    logins = False
    access = ""
    user = ""
    
    Visual.printascii("logout",None)
    Visual.printascii(access,None)
    login()


''' ------------------------------F03------------------------------ '''
def summonJin():
    import tempdata, Visual
    Visual.render_screen(["Summon Jin"],1)
    time.sleep(0.5)
    if tempdata.len_user < 102:
        Visual.render_screen(["Jenis jin yang dapat dipanggil: ",
        "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
        "(2) Pembangun - Bertugas membangun candi"], 3)

        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while jin != 2 and jin != 1:
            Visual.render_screen([f'Tidak ada jenis jin bernomor "{jin}"!'], 1)
            time.sleep(1)
            Visual.render_screen(["Jenis jin yang dapat dipanggil: ",
            "(1) Pengumpul - Bertugas mengumpulkan bahan bangunan",
            "(2) Pembangun - Bertugas membangun candi"], 3)
            jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        if jin == 1:
            role = "Pengumpul"
            Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
            username = input("Masukkan username jin: ")
            while function_jin.Cek_User(username):
                Visual.render_screen([f'Username "{username}" sudah diambil!'],1)
                time.sleep(1.5)
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
                username = input("Masukkan username jin: ")
        else:
            role = "Pembangun"
            Visual.render_screen(['Memilih jin "Pembangun".'], 1)
            username = input("Masukkan username jin: ")
            while function_jin.Cek_User(username):
                Visual.render_screen([f'Username "{username}" sudah diambil!'],1)
                time.sleep(1.5)
                Visual.render_screen(['Memilih jin "Pembangun".'], 1)
                username = input("Masukkan username jin: ")

        password = input("Masukkan password jin: ")
        while not 5 <= util_function.length(password + '.', '.') <= 25:
            Visual.render_screen(["Password panjangnya harus 5-25 karakter!"],1)
            time.sleep(1.5)
            if role == "Pengumpul":
                Visual.render_screen(['Memilih jin "Pengumpul".'], 1)
            elif role == "Pembangun":
                Visual.render_screen(['Memilih jin "Pembangun".'], 1)
            password = input("Masukkan password jin: ")

        datas = [username,password,role]
        # commanddata.save_csv("user.csv", datas)

        tempdatas = [[] for i in range(tempdata.len_user + 1)]
        for i in range(tempdata.len_user):
            tempdatas[i] = tempdata.data_user[i]
        tempdatas[tempdata.len_user] = datas        
        tempdata.len_user += 1

        tempdata.data_user = tempdatas

        time.sleep(1)
        if role == "Pengumpul":
            Visual.printascii("summon_pengumpul",access)
        elif role == "Pembangun":
            Visual.printascii("summon_pembangun",access)

        Visual.printascii(access,access)
    else:
        Visual.render_screen(["Jumlah Jin telah maksimal! (100 jin).",f"{user} tidak dapat men-summon lebih dari itu."],2)
        time.sleep(1)
        Visual.printascii(access,access)
    

''' ------------------------------F04------------------------------ '''
def hapusJin():
    import tempdata, Visual
    Visual.render_screen(["Hapus Jin"],1)
    time.sleep(0.5)
    username = input("Masukkan username jin : ")

    if not function_jin.Cek_User(username):
        Visual.render_screen(["Tidak ada jin dengan username tersebut."],1)
        time.sleep(1)
        Visual.printascii(access, access)
    elif function_jin.Cek_User(username):
        option = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")

        if option == "Y":
            data_user = tempdata.data_user
            datacandi = tempdata.data_candi
            for i in range(tempdata.len_user):
                if data_user[i][0] == username:
                    index = i
            for i in range(index,tempdata.len_user-1):
                tempdata.data_user[i] = tempdata.data_user[i+1]
            tempdata.len_user -= 1
            tempdatas = [[] for i in range(tempdata.len_user)]
            for i in range(tempdata.len_user):
                tempdatas[i] = tempdata.data_user[i]
            tempdata.data_user = tempdatas

            count = 0
            for i in range(tempdata.len_candi):
                if datacandi[i][1] == username:
                    count+=1

            tempdatas = [[] for i in range(tempdata.len_candi - count)]
            j = 0
            for i in range(tempdata.len_candi):
                if datacandi[i][1] != username:
                    tempdatas[j] = datacandi[i]
                    j+=1
                else:
                    tempdata.len_candi-=1
                    id = datacandi[i][0]
                    temphancur = [0 for i in range(tempdata.jumlah_candi_yang_dihancurkan + 1)]
                    for i in range(tempdata.jumlah_candi_yang_dihancurkan):
                        temphancur[i] = tempdata.id_candi_yang_dihancurkan[i]
                    temphancur[tempdata.jumlah_candi_yang_dihancurkan] = id
                    tempdata.jumlah_candi_yang_dihancurkan += 1
                    tempdata.id_candi_yang_dihancurkan = util_function.sort(temphancur,tempdata.jumlah_candi_yang_dihancurkan, "<")
            tempdata.data_candi = tempdatas
            if data_user[index][3] == "Pembangun":
                Visual.printascii("hapus_jin_bangun",access)
            elif data_user[index][3] == "Pengumpul":
                Visual.printascii("hapus_jin_kumpul",access)
            Visual.printascii(access,access)
        else:
            Visual.printascii(access,access)


''' ------------------------------F05------------------------------ '''
def ubahJin():
    import tempdata, Visual
    username = input("Masukkan username jin : ")

    if not function_jin.Cek_User(username):
        Visual.render_screen(["Tidak ada jin dengan username tersebut."],1)
        time.sleep(1)
        Visual.printascii(access,access)
    else:
        data_user = tempdata.data_user
        for i in range(tempdata.len_user):
            if data_user[i][0] == username:
                index = i
        tempdata.data_user[index][2] = function_jin.ubah_role(tempdata.data_user[index][2])

        if tempdata.data_user[index][2] == "Pembangun":
            Visual.printascii("ubah_kumpul_bangun",access)
            Visual.printascii(access,access)
        elif tempdata.data_user[index][2] == "Pengumpul":
            Visual.printascii("ubah_bangun_kumpul",access)
            Visual.printascii(access,access)
    

''' -------------------------------F06------------------------------ '''
def bangun(username):
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
            Visual.printascii(access,access)

        else:
            Visual.printascii("bangun_candi",access)
            Visual.render_screen(["Sisa candi yang perlu dibangun: 0."],1)
            time.sleep(2.5)
            Visual.printascii(access,access)
    else:
        Visual.render_screen(["Bahan bangunan tidak mencukupi","Candi tidak bisa dibangun!"],2)
        time.sleep(2.5)
        Visual.printascii(access,access)
    
''' -------------------------------F07------------------------------ '''
def kumpul(batch):
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
        Visual.printascii(access,access)

    
''' -------------------------------F08------------------------------ '''
def batchkumpul():
    import Visual
    jinPengumpul = function_jin.count_jin("Pengumpul")

    if jinPengumpul == 0:
        Visual.render_screen(["Kumpul gagal","Anda tidak punya jin pengumpul","Silahkan summon terlebih dahulu."],3)
        time.sleep(1)
        Visual.printascii(access,access)
    else:
        pasir = 0 ; batu = 0 ; air = 0
        for i in range(jinPengumpul):
            PBA = kumpul(True)
            pasir += PBA[0] ; batu += PBA[1] ; air += PBA[2]

        Visual.render_screen([f"Mengerahkan {jinPengumpul} jin untuk mengumpulkan bahan."],1)
        time.sleep(1)
        Visual.printascii("kumpul",access)
        Visual.render_screen([f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air."],1)
        time.sleep(1)
        Visual.printascii(access,access)

    
def batchbangun():  
    import tempdata, Visual
    Jumlah_jin_Pembangun = function_jin.count_jin("Pembangun")

    if Jumlah_jin_Pembangun == 0:
        Visual.render_screen(["Bangun gagal","Anda tidak punya jin pembangun","Silahkan summon terlebih dahulu."],3)
        time.sleep(1)
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
                    for i in range(1,temp_jumlah_candi_yang_dihancurkan): # mengisi list baru dengan list temp_id_candi_yang_dihancurkan setelah diambil 1 id terkecil
                        tempdatas[i-1] = temp_id_candi_yang_dihancurkan[i]
                    
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
            Visual.printascii(access,access)

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
            Visual.printascii(access,access)


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
    Visual.printascii(access,access)

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
    Visual.printascii(access,access)

''' -------------------------------F11------------------------------ '''
def cekid(id):
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
def remove_dataid(id):
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
        time.sleep(1)
        Visual.printascii(access,access)

''' -------------------------------F12------------------------------ '''
def ayamberkokok():
    global start
    import tempdata, Visual

    start = False 
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
    time.sleep(2)
    Visual.printascii("home",access)

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
    
    
