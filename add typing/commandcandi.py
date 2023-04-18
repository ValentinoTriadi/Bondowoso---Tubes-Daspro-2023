import commanddata, command, tempdata

def saveCandi(material: list, username: str):
    dataCandi = tempdata.datacandi2
    if tempdata.total_candi_dihancurkan == 0:
        id = tempdata.lencandi
    else:
        pass # Kondisi saat ada yg diancurinn tapi bikinnya nanti dulu

    harga = int(material[0]) * 10000 + int(material[1]) * 15000 + int(material[2]) * 7500
    datas = [id,username,material[0],material[1],material[2],harga]
    return datas


def countBahan(bahan: str):
    data = tempdata.datacandi2

    if bahan == "pasir":
        index = 2
    elif bahan == "batu":
        index = 3
    elif bahan == "air":
        index = 4

    count = 0
    for i in range(tempdata.lencandi):
        count += int(data[i][index])
    
    return count


def canditer(mahal: bool):
    data = tempdata.datacandi2
    lendata = tempdata.lencandi
    tempid = ['' for i in range(lendata)]
    tempharga = [0 for i in range(lendata)]

    for i in range(lendata):
        tempid[i] = data[i][0]
        tempharga[i] = int(data[i][5])

    if mahal:
        harga = command.maksimum(tempharga,lendata)
        for i in range(lendata):
            if tempharga[i] == harga:
                return tempid[i],harga
    else:
        harga = command.minimum(tempharga,lendata)
        for i in range(lendata):
            if tempharga[i] == harga:
                return tempid[i],harga