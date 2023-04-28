'''----------------------------- Maks/Min -----------------------------'''
def maksimum(arr,len_arr):
    maks = arr[0]
    for i in range(len_arr):
        if maks < arr[i]:
            maks = arr[i]
    return maks

def minimum(arr, len_arr):
    min = arr[0]
    for i in range(len_arr):
        if min > arr[i]:
            min = arr[i]
    return min


'''----------------------------- Leksikografi -----------------------------'''
def sort(arr, length, operator):
    for i in range(1,length):
        for j in range(i, 0, -1):
            if operator == '>':
                if arr[j]>arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                else:
                    break
            elif operator == '<':
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                else:
                    break
    return arr

def leksikal(arr,length, highest):
    if highest:
        arr = sort(arr,length, '>')
    else:
        arr = sort(arr,length, '<')
    return arr


'''----------------------------- RNG -----------------------------'''
j = 0

def lcg(x):
    a = 1664525
    c = 1013904223
    m = 2**32
    x1 = ((a * x) + c) % m
    r = x1/m
    return x1, r

def buletin(batas_bawah, batas_atas, nilai):
    if batas_bawah <= nilai < batas_bawah + 0.73:
        return batas_bawah
    elif  batas_atas - 0.78 < nilai <= batas_atas:
        return batas_atas
    else:
        return round(nilai)

def rng(x, size, ranges, batas_bawah):
    global j
    arr = [0 for i in range(size)]
    for i in range (size):
        x,r = lcg(x)
        arr[i] = (buletin(batas_bawah, batas_bawah + ranges, (r * ranges) + batas_bawah))
    j +=1
    return arr[j]

def randint(min, maks):
    return rng(1, 1000, maks - min, min)


'''----------------------------- Process Data -----------------------------'''
def read_csv(name_file, name_folder):
    fo = open(f"./save/{name_folder}/{name_file}", 'r')
    length = 0
    data = ["" for i in range(1000)]
    # datas = 
    for line in fo:
        data[length] = line
        length += 1
    fo.close()   
    length -= 1
    tempdata = ["" for i in range(length)]
    for i in range(length):
        tempdata[i] = data[i+1]
    return tempdata, length

def length(arr,EOP):
    count = 0
    i = 0
    cek = True
    while cek:
        if arr[i] == EOP:
            cek = False
        else:
            count +=1
        i+=1
    return count

def split_koma (line,row):
    split_value = ["" for i in range(row)]
    temp = ''
    index1 = 0
    index2 = 0
    char = line[index2]
    while char != '\n':
        if char == ';':
            split_value[index1] = temp
            temp = ''
            index1 +=1
            index2 +=1
        else:
            temp += char
            index2 +=1
        char = line[index2]
    split_value[index1] = temp
    if split_value[0] != "":
        return split_value
    else:
        return []


'''----------------------------- Save Data -----------------------------'''
def write_csv(file_name, path_name):
    import tempdata
    file = open(f"./{path_name}/{file_name}","w")
    if file_name == "candi.csv":
        data = tempdata.data_candi
        tempdatas = ["" for i in range(tempdata.len_candi + 1)]
        tempdatas[0] = f"id;pembuat;pasir;batu;air\n"
        for i in range(tempdata.len_candi):
            if data[i] == []:
                tempdatas[i+1] = "\n"
            else:
                tempdatas[i+1] = f"{data[i][0]};{data[i][1]};{data[i][2]};{data[i][3]};{data[i][4]}\n"
    elif file_name == "user.csv":
        data = tempdata.data_user
        tempdatas = ["" for i in range(tempdata.len_user + 1)]
        tempdatas[0] = f"username;password;role.\n"
        for i in range(tempdata.len_user):
            tempdatas[i+1] = f"{data[i][0]};{data[i][1]};{data[i][2]}\n"

    elif file_name == "bahan_bangunan.csv":
        data = tempdata.data_bahan_bangunan
        tempdatas = ["" for i in range(2)]
        tempdatas[0] = f"pasir;batu;air.\n"
        tempdatas[1] = f"{data[0][0]};{data[0][1]};{data[0][2]}\n"

    file.writelines(tempdatas)
    file.close()
