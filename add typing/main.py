import commanddata, command, commandjin, time, commandcandi, tempdata
logins = False
access = ""
user = ""
start = False

'''-------------------------------F01------------------------------'''
def login():
    global logins, access, user
    datapass = tempdata.datauser2
    username = input("Username: ")
    password = input("Password: ")

    index = 0
    cekuser = False
    cekpass = ""
    for i in range(tempdata.lenuser):
        if datapass[i][0] == username: # datapass[i](akun pada baris ke brp pada data)[0](username)
            cekuser = True
            index = i
            cekpass = datapass[i][1]
    if not cekuser:
        print("\nUsername tidak terdaftar!")
        login()
    else:
        if password == cekpass:
            access = datapass[index][2]
            user = datapass[index][0]
            logins = True
            print(f"\nSelamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
            
        else:
            print("\nPassword salah!")
            login()


'''-------------------------------F02------------------------------'''
def logout():
    global logins, access, user
    logins = False
    access = ""
    user = ""
    print()
    login()


''' ------------------------------F03------------------------------ '''
def summonJin():
    if tempdata.lenuser < 102:
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi\n")

        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while jin != 2 and jin != 1:
            print(f'\nTidak ada jenis jin bernomor "{jin}"!')
            jin = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))

        if jin == 1:
            role = "Pengumpul"
            print('\nMemilih jin "Pengumpul".')
        else:
            role = "Pembangun"
            print('\nMemilih jin "Pembangun".')

        username = input("\nMasukkan username jin: ")
        while commandjin.cekUser(username):
            print(f'\nUsername "{username}" sudah diambil!\n')
            username = input("Masukkan username jin: ")
        # tempuser = username + '.'
        password = input("Masukkan password jin: ")
        while not 5 <= tempdata.length(password + '.', '.') <= 25:
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin: ")

        datas = [username,password,role]
        # commanddata.save_csv("user.csv", datas)

        tempdatas = [[] for i in range(tempdata.lenuser + 1)]
        for i in range(tempdata.lenuser):
            tempdatas[i] = tempdata.datauser2[i]
        tempdatas[tempdata.lenuser] = datas        
        tempdata.lenuser += 1

        tempdata.datauser2 = tempdatas

        time.sleep(1)
        print("\nMengumpulkan sesajen...") ; time.sleep(1)
        print("Menyerahkan sesajen...") ; time.sleep(1)
        print("Membacakan mantra...\n") ; time.sleep(1)

        print(f"Jin {username} berhasil dipanggil!")
    else:
        print(f"Jumlah Jin telah maksimal! (100 jin). {user} tidak dapat men-summon lebih dari itu")
    

''' ------------------------------F04------------------------------ '''
def hapusJin():
    username = input("Masukkan username jin : ")

    if not commandjin.cekUser(username):
        print("\nTidak ada jin dengan username tersebut.")
    elif commandjin.cekUser(username):
        option = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")

        if option == "Y":
            datauser = tempdata.datauser2
            datacandi = tempdata.datacandi2
            for i in range(tempdata.lenuser):
                if datauser[i][0] == username:
                    index = i
            for i in range(index,tempdata.lenuser-1):
                tempdata.datauser2[i] = tempdata.datauser2[i+1]
            tempdata.lenuser -= 1
            tempdatas = [[] for i in range(tempdata.lenuser)]
            for i in range(tempdata.lenuser):
                tempdatas[i] = tempdata.datauser2[i]
            tempdata.datauser2 = tempdatas

            count = 0
            for i in range(tempdata.lencandi):
                if datacandi[i][1] == username:
                    count+=1

            tempdatas = [[] for i in range(tempdata.lencandi - count)]
            j = 0
            for i in range(tempdata.lencandi):
                if datacandi[i][1] != username:
                    tempdatas[j] = datacandi[i]
                    j+=1
                else:
                    tempdata.lencandi-=1
                    id = datacandi[i][0]
                    temphancur = [0 for i in range(tempdata.total_candi_dihancurkan+1)]
                    for i in range(tempdata.total_candi_dihancurkan):
                        temphancur[i] = tempdata.id_candi_dihancurkan[i]
                    temphancur[tempdata.total_candi_dihancurkan] = id
                    tempdata.total_candi_dihancurkan += 1
                    tempdata.id_candi_dihancurkan = command.sort(temphancur,tempdata.total_candi_dihancurkan, "<")
            tempdata.datacandi2 = tempdatas


''' ------------------------------F05------------------------------ '''
def ubahJin():
    username = input("Masukkan username jin : ")

    if not commandjin.cekUser(username):
        print("\nTidak ada jin dengan username tersebut.")
    else:
        datauser = tempdata.datauser2
        for i in range(tempdata.lenuser):
            if datauser[i][0] == username:
                index = i
        tempdata.datauser2[index][2] = commandjin.ubahrole(tempdata.datauser2[index][2])

        # print(tempdata.datauser2, tempdata.lenuser)


''' -------------------------------F06------------------------------ '''
def bangun(username: str):
    #candi = commanddata.read_csv("candi.csv")
    candi = tempdata.datacandi2
    # bahan = commanddata.read_csv(f"bahan_bangunan.csv")
    bahan = tempdata.databahanbangunan2
    pasir = command.randint(1,5) ; batu = command.randint(1,5) ; air = command.randint(1,5)

        
    if pasir <= int(bahan[0][0]) and batu <= int(bahan[0][1]) and air <= int(bahan[0][2]):
        bahan[0][0] = str(int(bahan[0][0]) - pasir) ; bahan[0][1] = str(int(bahan[0][1]) - batu) ; bahan[0][2] = str(int(bahan[0][2]) - air )
        material = [str(pasir),str(batu),str(air)]
        tempdata.databahanbangunan2 = bahan
        if tempdata.lencandi < 100:
            tempdata.lencandi +=1

            tempdatacandi = [[] for i in range(tempdata.lencandi)]
            for i in range(tempdata.lencandi-1):
                tempdatacandi[i] = candi[i]

            tempdatacandi[tempdata.lencandi-1] = commandcandi.saveCandi(material, username)
            tempdata.datacandi2 = tempdatacandi

            time.sleep(0.5)
            print("Candi berhasil dibangun.")
            time.sleep(0.3)
            print(f"Sisa candi yang perlu dibangun: {100-tempdata.lencandi}.")

        else:
            time.sleep(0.5)
            print("Candi berhasil dibangun.")
            time.sleep(0.3)
            print("Sisa candi yang perlu dibangun: 0.")
    else:
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")
    

    
''' -------------------------------F07------------------------------ '''
def kumpul(batch: bool):
    pasir = command.randint(0,5) ; batu = command.randint(0,5) ; air = command.randint(0,5)
    bahan = tempdata.databahanbangunan2
    bahan[0][0] = str(int(bahan[0][0]) + pasir) ; bahan[0][1] = str(int(bahan[0][1]) + batu) ; bahan[0][2] = str(int(bahan[0][2]) + air )
    if batch :
        return [pasir,batu,air]
    else:
        print(f"Jin menemukan {pasir} pasir, {batu} batu, {air} air.")

    
''' -------------------------------F08------------------------------ '''
def batchKumpul():
    jinPengumpul = commandjin.countJin("Pengumpul")

    if jinPengumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. SIlahkan summon terlebih dahulu.")
    else:
        pasir = 0 ; batu = 0 ; air = 0
        for i in range(jinPengumpul):
            PBA = kumpul(True)
            pasir += PBA[0] ; batu += PBA[1] ; air += PBA[2]

        print(f"Mengerahkan {jinPengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")

    
def batchBangun():
    jinPembangun = commandjin.countJin("Pembangun")
    datacandi = tempdata.datacandi2

    if jinPembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        datauser = tempdata.datauser2 
        temp_candi = [[] for i in range(tempdata.lencandi + jinPembangun)]
        for i in range(tempdata.lencandi):
            temp_candi[i] = tempdata.datacandi2[i]
        totalMaterial = [0,0,0]
        bahan = tempdata.databahanbangunan2
        jin = [[] for i in range(jinPembangun)]

        for i in range(tempdata.lenuser):
            for j in range(jinPembangun):
                if datauser[i][2] == "Pembangun":
                    jin[j] = datauser[i][0]


        for i in range(tempdata.lencandi, jinPembangun + tempdata.lencandi):
            pasir = command.randint(1,5) ; batu = command.randint(1,5) ; air = command.randint(1,5)
            material = [str(pasir),str(batu),str(air)]
            # if candi ada yg diancurin
            if tempdata.total_candi_dihancurkan == 0:
                index = tempdata.lencandi+1
                tempdata.lencandi+=1
            else:
                pass # buat kalo misal ada candi yg dihancurin
                # index = 
            harga = int(material[0]) * 10000 + int(material[1]) * 15000 + int(material[2]) * 7500
            temp_candi[i] = [index,jin[i-tempdata.lencandi],material[0],material[1],material[2],harga]
            totalMaterial[0] += pasir ; totalMaterial[1] += batu ; totalMaterial[2] += air

        print(f"Mengerahkan {jinPembangun} jin untuk membangun candi dengan total bahan")
        print(f"{totalMaterial[0]} pasir, {totalMaterial[1]} batu, dan {totalMaterial[2]} air.") ; time.sleep(1)
        # print(temp_candi)
        # print(bahan)


        if totalMaterial[0] <= int(bahan[0][0]) and totalMaterial[1] <= int(bahan[0][1]) and totalMaterial[2] <= int(bahan[0][2]):
            bahan[0][0] = str(int(bahan[0][0]) - totalMaterial[0]) ; bahan[0][1] = str(int(bahan[0][1]) - totalMaterial[1]) ; bahan[0][2] = str(int(bahan[0][2]) - totalMaterial[2] )

            # commanddata.rewrite_data("bahan_bangunan.csv", bahan)
            tempdata.databahanbangunan2 = bahan
            tempdata.datacandi2 = temp_candi
            # tempid = temp_candi[0][0]
            # for i in range(1,command.length(temp)):
            #     if temp[i][0] == tempid:
            #         for j in range(i,command.length(temp)):
            #             temp[j][0] += 1
            #         tempid +=1
            # print(temp)
            # for i in range(command.length(temp)):
            #     tempdatas = [f"{temp[i][0]};{temp[i][1]};{temp[i][2]};{temp[i][3]};{temp[i][4]};{temp[i][5]}\n"]
            #     commanddata.save_csv("candi.csv", tempdatas)

            print(f"Jin berhasil membangun total {jinPembangun} candi.")

        else:
            sisapasir = totalMaterial[0] - int(bahan[0][0])
            sisabatu = totalMaterial[1] - int(bahan[0][1])
            sisaair = totalMaterial[2] - int(bahan[0][2])
            if sisapasir < 0:
                sisapasir = 0
            if sisabatu < 0:
                sisabatu = 0
            if sisaair < 0:
                sisaair = 0
            print(f"Bangun gagal. Kurang {sisapasir} pasir, {sisabatu} batu, dan {sisaair} air.")


''' -------------------------------F09------------------------------ '''
def laporanJin ():
    datauser = tempdata.datauser2
    databahan = tempdata.databahanbangunan2

    print("> Total Jin:", tempdata.lenuser-2)
    print("> Total Jin Pengumpul:", commandjin.countJin("Pengumpul"))
    print("> Total Jin Pembangun:", commandjin.countJin("Pembangun"))
    print("> Jin Terajin:", commandjin.jinter(True))
    print("> Jin Termalas:", commandjin.jinter(False))
    print("> Jumlah Pasir:", databahan[0][0], "unit")
    print("> Jumlah Air:", databahan[0][2], "unit")
    print("> Jumlah Batu:", databahan[0][1], "unit")


''' -------------------------------F10------------------------------ '''
def laporanCandi():
    print("> Total Candi:", tempdata.lencandi)
    print("> Total Pasir yang digunakan:", commandcandi.countBahan("pasir"))
    print("> Total Batu yang digunakan:", commandcandi.countBahan("batu"))
    print("> Total Air yang digunakan:", commandcandi.countBahan("air"))
    termahal, hargamahal = commandcandi.canditer(True)
    print("> ID Candi Termahal:", termahal, f"({hargamahal})")
    termurah, hargamurah = commandcandi.canditer(False)
    print("> ID Candi Termurah:", termurah, f"({hargamurah})")

''' -------------------------------F11------------------------------ '''
def cekid(id: int) -> bool:
    data = tempdata.datacandi2
    for i in range (tempdata.lencandi):
        if id == int(data[i][0]):
            return True
    return False

# TODO: Remove Specific line of data from array
def remove_dataid(id: int):
    data = tempdata.datacandi2
    tempdatas = ['' for i in range(tempdata.lencandi - 1)]

    j = 0
    for i in range(tempdata.lencandi):
        if int(data[i][0]) != id:
            tempdatas[j] = data[i]
            j+=1

    temphancur = [0 for i in range(tempdata.total_candi_dihancurkan+1)]
    for i in range(tempdata.total_candi_dihancurkan):
        temphancur[i] = tempdata.id_candi_dihancurkan[i]
    temphancur[tempdata.total_candi_dihancurkan] = id
    tempdata.total_candi_dihancurkan += 1
    tempdata.id_candi_dihancurkan = command.sort(temphancur,tempdata.total_candi_dihancurkan, "<")
    tempdata.datacandi2 = tempdatas
    tempdata.lencandi -=1


def hancurkanCandi():
    id = int(input("Masukkan ID candi: "))
    if cekid(id):
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        if confirm == "Y":
            remove_dataid(id)

    else:
        print("Tidak ada candi dengan ID tersebut.")


''' -------------------------------F12------------------------------ '''
def ayamBerkokok():
    global start
    print("Kukuruyuk..",end=' ')
    time.sleep(0.2)
    print("Kukuruyuk..",end='')
    print("Jumlah Candi:", tempdata.lencandi)
    if tempdata.lencandi<100:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    start = False


''' ------------------------------F13------------------------------ '''
def load():
    global start
    import argparse, os
    parser = argparse.ArgumentParser()
    parser.add_argument("name_folder", help="Nama Folder", nargs='?')

    name_folder = parser.parse_args().name_folder
    if name_folder == "TUBES-DASPRO":
        print("Loading...\n\nSelamat datang di program “Manajerial Candi”\nSilahkan masukkan pilihan Anda")
        start = True
    elif name_folder == None:
        print("Tidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
    elif name_folder != "TUBES-DASPRO":
        print(f"Folder \"{name_folder}\" tidak ditemukan.")

    
''' ------------------------------F14------------------------------ '''
# Belum Kelar
def save():
    name_folder = input("Masukkan nama folder: ")

    return

''' ------------------------------F15------------------------------ '''
def help():
    print(" HELP ".center(28,"="))
    if logins:
        print("1.\tlogout\n\tUntuk keluar dari akun yang digunakan sekarang")
        if access == "bandung_bondowoso":
            print("2.\tsummonjin\n\tUntuk memanggil jin dari dunia lain")
            print("3.\thapusjin\n\tUntuk menghapus jin")
            print("4.\tubahjin\n\tUntuk mengubah tipe jin")
            print("5.\tbatchkumpul\n\tUntuk mengerahkan seluruh jin untuk mengumpulkan bahan")
            print("6.\tbatchbangun\n\tUntuk mengerahkan seluruh jin untuk membangun")
            print("7.\tlaporanjin\n\tUntuk mengambil laporan jin yang berisi kinerja para jin")
            print("8.\tlaporancandi\n\tUntuk mengambil laporan candi yang berisi progress pembangunan candi")
            print("9.\tsave\n\tUntuk menyimpan data yang berada di program")
            print("10.\tload\n\tUntuk memuat file eksternal ke dalam permainan")
            print("11.\texit\n\tUntuk keluar dari permainan")

        elif access == "roro_jonggrang":
            print("2.\thancurkancandi\n\tUntuk menghancurkan candi yang tersedia")
            print("3.\tayamberkokok\n\tUntuk menyelesaikan permainan")
            print("4.\tsave\n\tUntuk menyimpan data yang berada di program")
            print("5.\texit\n\tUntuk keluar dari permainan")
            print("6.\tload\n\tUntuk memuat file eksternal ke dalam permainan")

        elif access == "Pembangun":
            print("2.\tbangun\n\tUntuk membangun candi")
            print("3.\tload\n\tUntuk memuat file eksternal ke dalam permainan")
            print("4.\texit\n\tUntuk keluar dari permainan")
        elif access == "Pengumpul":
            print("2.\tkumpul\n\tUntuk mengumpulkan resource candi")
            print("3.\tload\n\tUntuk memuat file eksternal ke dalam permainan")
            print("4.\texit\n\tUntuk keluar dari permainan")
    else:
        print("1.\tlogin\n\tUntuk masuk menggunakan akun")
        print("2.\tload\n\tUntuk memuat file eksternal ke dalam permainan")
        print("3.\texit\n\tUntuk keluar dari permainan")

    
''' ------------------------------F16------------------------------ '''
def keluar():
    global start
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while confirm != 'y' and confirm != 'n':
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if confirm == 'y':
        save()
    start = False
    
    

load()
while start:
    menu = input(">>> ")
    if menu == "login" and not logins:
        login()
    elif menu == "login" and logins:
        print("Login gagal!")
        time.sleep(0.1)
        print(f"Anda telah login dengan username {user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    elif menu == "logout" and logins:
        logout()
    elif menu == "logout" and not logins:
        print("Logout gagal!")
        time.sleep(0.1)
        print(f"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    elif menu == "summonjin" and access == "bandung_bondowoso":
        summonJin()
    elif menu == "hapusjin" and access == "bandung_bondowoso":
        hapusJin()
    elif menu == "ubahjin" and access == "bandung_bondowoso":
        ubahJin()
    elif menu == "bangun" and access == "Pembangun":
        bangun(user)
    elif menu == "kumpul" and access == "Pengumpul":
        kumpul(False)
    elif menu == "batchkumpul" and access == "bandung_bondowoso":
        batchKumpul()
    elif menu == "batchbangun" and access == "bandung_bondowoso":
        batchBangun()
    elif menu == "laporanjin" and access == "bandung_bondowoso":
        laporanJin()
    elif menu == "laporancandi" and access == "bandung_bondowoso":
        laporanCandi()
    elif menu == "hancurkancandi" and access == "roro_jonggrang":
        hancurkanCandi()
    elif menu == "ayamberkokok" and access == "roro_jonggrang":
        ayamBerkokok()
    elif menu == "exit":
        keluar()
        start = False
    elif menu == "help":
        help()
    elif menu == "save":
        save()
    elif menu == 's':
        print(tempdata.datacandi2)
    elif menu == 'd':
        print(tempdata.datauser2)
    elif menu == 'a':
        print(tempdata.databahanbangunan2)
    else:
        print("Access Denied")