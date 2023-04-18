import command, tempdata

''' ------------------------------Command Jin------------------------------ '''
def cekUser(username: str):
    fo = tempdata.datauser2
    sama = False

    for i in range(tempdata.lenuser):
        if fo[i][0] == username:
            sama = True

    return sama


def ubahrole(role: str):
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

def countJin(jenis: str) -> int:
    data = tempdata.datauser2
    count = 0
    for i in range(tempdata.lenuser):
        if data[i][2] == jenis:
            count += 1

    return count


def jinter(rajin: bool):
    datacandi = tempdata.datacandi2
    datauser = tempdata.datauser2
    listpembangun = ['' for i in range(countJin('Pembangun'))]
    j = 0
    for i in range(tempdata.lenuser): # List para pembangun
        # while j<countJin('Pembangun'):
        if datauser[i][2] == 'Pembangun':
            listpembangun[j] = datauser[i][0]
            j+=1

    jumlah_yg_dibangun_jin = [0 for i in range(countJin("Pembangun"))]
    for i in range(tempdata.lencandi): # List user yg bangun candi
        for j in range(countJin('Pembangun')):
            if datacandi[i][1] == listpembangun[j]:
                jumlah_yg_dibangun_jin[j]+=1

    if rajin:
        maks = command.maksimum(jumlah_yg_dibangun_jin, countJin('Pembangun'))
        jumlah_jin_terajin = 0
        for i in range(countJin('Pembangun')):
            if jumlah_yg_dibangun_jin[i] == maks:
                jumlah_jin_terajin +=1

        if jumlah_jin_terajin == 0:
            return '-'

        listterajin = ['' for i in range(jumlah_jin_terajin)]
        index = 0
        for i in range(countJin('Pembangun')):
            if jumlah_yg_dibangun_jin[i] == maks:
                listterajin[index] = listpembangun[i]
                index += 1

        if jumlah_jin_terajin == 1:
            return listterajin[0]
        else:
            return command.leksikal(listterajin,jumlah_jin_terajin, False) # Belum dikerjain
    else:
        mins = command.minimum(jumlah_yg_dibangun_jin, countJin('Pembangun'))
        jumlah_jin_termalas = 0
        for i in range(countJin('Pembangun')):
            if jumlah_yg_dibangun_jin[i] == mins:
                jumlah_jin_termalas +=1

        if jumlah_jin_termalas == 0:
            return '-'

        listtermalas = ['' for i in range(jumlah_jin_termalas)]
        index = 0
        for i in range(countJin('Pembangun')):
            if jumlah_yg_dibangun_jin[i] == mins:
                listtermalas[index] = listpembangun[i]
                index += 1

        if jumlah_jin_termalas == 1:
            return listtermalas[0]
        else:
            return command.leksikal(listterajin,jumlah_jin_termalas,True) # Belum dikerjain
    