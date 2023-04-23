import util_function

''' ------------------------------ Cek User ------------------------------ '''
def Cek_User(username: str) -> bool:
    import tempdata
    fo = tempdata.data_user
    sama = False

    for i in range(2,tempdata.len_user):
        if fo[i][0] == username:
            sama = True

    return sama


''' ------------------------------ Ubah Role ------------------------------ '''
def ubah_role(role: str) -> str:
    if role == "Pengumpul":
            option = input(f'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ')
            while option != "Y" and option != "N":
                print("Input salah! Masukan hanya Y/N\n")
                option = input(f'Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ')
            
            if option == "Y":
                return 'Pembangun'
            else:
                return 'Pengumpul'
    else:
            option = input(f'Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ')
            while option != "Y" and option != "N":
                print("Input salah! Masukan hanya Y/N\n")
                option = input(f'Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ')

            if option == "Y":
                return 'Pengumpul'
            else:
                return 'Pembangun'


''' ------------------------------ Hitung Jin ------------------------------ '''
def count_jin(jenis: str) -> int:
    import tempdata
    data = tempdata.data_user
    count = 0
    for i in range(tempdata.len_user):
        if data[i][2] == jenis:
            count += 1

    return count


''' ------------------------------ Cari Jin Terajin/Termalas ------------------------------ '''
def jinter(rajin: bool) -> str:
    import tempdata
    datacandi = tempdata.data_candi
    listpembangun = tempdata.data_jin_yang_pernah_membangun

    jumlah_yg_dibangun_jin = [0 for i in range(tempdata.len_pembangun)]
    for i in range(tempdata.len_candi): # List user yg bangun candi
        for j in range(tempdata.len_pembangun):
            if datacandi[i] != []:
                if datacandi[i][1] == listpembangun[j]:
                    jumlah_yg_dibangun_jin[j]+=1

    if rajin:
        maks = util_function.maksimum(jumlah_yg_dibangun_jin, tempdata.len_pembangun)
        jumlah_jin_terajin = 0
        for i in range(tempdata.len_pembangun):
            if jumlah_yg_dibangun_jin[i] == maks:
                jumlah_jin_terajin +=1

        if jumlah_jin_terajin == 0:
            return '-'

        listterajin = ['' for i in range(jumlah_jin_terajin)]
        index = 0
        for i in range(tempdata.len_pembangun):
            if jumlah_yg_dibangun_jin[i] == maks:
                listterajin[index] = listpembangun[i]
                index += 1

        if jumlah_jin_terajin == 1:
            return listterajin[0]
        else:
            return util_function.leksikal(listterajin,jumlah_jin_terajin, False)[0]
    else:
        mins = util_function.minimum(jumlah_yg_dibangun_jin, tempdata.len_pembangun)
        jumlah_jin_termalas = 0
        for i in range(tempdata.len_pembangun):
            if jumlah_yg_dibangun_jin[i] == mins:
                jumlah_jin_termalas +=1

        if jumlah_jin_termalas == 0:
            return '-'

        listtermalas = ['' for i in range(jumlah_jin_termalas)]
        index = 0
        for i in range(tempdata.len_pembangun):
            if jumlah_yg_dibangun_jin[i] == mins:
                listtermalas[index] = listpembangun[i]
                index += 1

        if jumlah_jin_termalas == 1:
            return listtermalas[0]
        else:
            return util_function.leksikal(listtermalas,jumlah_jin_termalas,True)[0]