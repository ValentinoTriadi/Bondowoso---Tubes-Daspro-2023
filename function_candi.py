import util_function

'''----------------------------- Process List -----------------------------'''
def saveCandi(material: list, username: str) -> list:
    import tempdata
    if tempdata.jumlah_candi_yang_dihancurkan == 0:
        tempdata.len_candi +=1
        id = tempdata.len_candi
    else:
        id = tempdata.id_candi_yang_dihancurkan[0]

        tempdatas = [ 0 for i in range(tempdata.jumlah_candi_yang_dihancurkan - 1)]
        for i in range(1,tempdata.jumlah_candi_yang_dihancurkan):
            tempdatas[i-1] = tempdata.id_candi_yang_dihancurkan[i]
        
        tempdata.id_candi_yang_dihancurkan = tempdatas
        tempdata.jumlah_candi_yang_dihancurkan -= 1

    harga = int(material[0]) * 10000 + int(material[1]) * 15000 + int(material[2]) * 7500
    datas = [str(id), username, material[0], material[1], material[2], harga]
    return datas

'''----------------------------- Hitung Jumlah Bahan Yang Terpakai -----------------------------'''
def countbahan(bahan: str) -> int:
    import tempdata
    data = tempdata.data_candi

    if bahan == "pasir":
        index = 2
    elif bahan == "batu":
        index = 3
    elif bahan == "air":
        index = 4

    count = 0
    for i in range(tempdata.len_candi):
        if data[i] != []:
            count += int(data[i][index])
    
    return count

'''----------------------------- Cari Candi Termahal/Termurah -----------------------------'''
def canditer(mahal: bool) -> tuple:
    import tempdata
    data = tempdata.data_candi
    lendata = tempdata.len_candi - tempdata.jumlah_candi_yang_dihancurkan
    tempid = ['' for i in range(lendata)]
    tempharga = [0 for i in range(lendata)]

    index = 0
    for i in range(tempdata.len_candi):
        if data[i] != []:
            tempid[index] = data[i][0]
            tempharga[index] = int(data[i][5])
            index += 1

    if mahal:
        harga = util_function.maksimum(tempharga,lendata)
        for i in range(lendata):
            if tempharga[i] == harga:
                return tempid[i],harga
    else:
        harga = util_function.minimum(tempharga,lendata)
        for i in range(lendata):
            if tempharga[i] == harga:
                return tempid[i],harga