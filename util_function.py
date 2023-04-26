'''---------------------------------------------------------- Maks/Min ----------------------------------------------------------'''

'''-------------------- Maksimum --------------------'''
def maksimum(arr: list,len_arr: int) -> int:
    maks = arr[0] # Mengambil elemen pertama array sebagai nilai maksimum sementara
    for i in range(len_arr): # Mencari nilai pada array yang memiliki nilai lebih besar dari nilai maksimum sementara
        if maks < arr[i]: # Kondisi saat ditemukan nilai pada array yang lebih besar daripada nilai maksimum sementara
            maks = arr[i] # Merubah nilai maksimum sementara menjadi nilai pada array yang lebih besar
    return maks # Mengembalikan nilai maksimum
'''-------------------- Maksimum --------------------'''


'''-------------------- Minimum --------------------'''
def minimum(arr: list, len_arr: int) -> int:
    min = arr[0] # Mengambil elemen pertama array sebagai nilai minimum sementara
    for i in range(len_arr): # Mencari nilai pada array yang memiliki nilai lebih kecil dari nilai minimum sementara
        if min > arr[i]: # Kondisi saat ditemukan nilai pada array yang lebih kecil daripada nilai minimum sementara
            min = arr[i] # Merubah nilai minimum sementara menjadi nilai pada array yang lebih kecil
    return min # Mengembalikan nilai minimum
'''-------------------- Minimum --------------------'''

'''---------------------------------------------------------- Maks/Min ----------------------------------------------------------'''




'''---------------------------------------------------------- Leksikografi ----------------------------------------------------------'''

'''-------------------- Sort List (Insertion List Method) --------------------'''
def sort(arr: list, length: int, operator: str) -> list:
    for i in range(1,length): # Mencacah seluruh elemen array
        for j in range(i, 0, -1): # Mencacah elemen array sekarang (index i) hingga elemen pertama
            if operator == '>': # Ketika hendak diurutkan dari terbesar
                if arr[j]>arr[j-1]: # Ketika elemen yang sedang di cek lebih besar dari elemen sebelumnya
                    arr[j],arr[j-1] = arr[j-1],arr[j] # Menukarkan elemen yang sedang di cek dengan elemen sebelumnya
                else:
                    break # Kondisi untuk memberhentikan pengurutan elemen sekarang (index i) dan lanjut ke elemen selanjutnya
            elif operator == '<': # Ketika hendak diurutkan dari terkecil
                if arr[j] < arr[j-1]: # Ketika elemen yang sedang di cek lebih kecil dari elemen sebelumnya
                    arr[j],arr[j-1] = arr[j-1],arr[j] # Menukarkan elemen yang sedang di cek dengan elemen sebelumnya
                else:
                    break # Kondisi untuk memberhentikan pengurutan elemen sekarang (index i) dan lanjut ke elemen selanjutnya
    return arr # Mengembalikan array yang sudah diurutkan
'''-------------------- Sort List (Insertion List Method) --------------------'''


'''-------------------- Leksikal --------------------'''
def leksikal(arr: list,length: int, highest: bool) -> list:
    if highest: # Saat ingin mengurutkan leksikografi dari yang tinggi ke rendah
        arr = sort(arr,length, '>')
    else: # Saat ingin mengurutkan leksikografi dari yang rendah ke tinggi
        arr = sort(arr,length, '<')
    return arr # Mengembalikan array yang sudah diurutkan leksikografinya
'''-------------------- Leksikal --------------------'''

'''---------------------------------------------------------- Leksikografi ----------------------------------------------------------'''




'''---------------------------------------------------------- RNG ----------------------------------------------------------'''
j = 0
import time
def generate_random_seed(min_value: int, max_value:int) -> int: 
    current_time = int(time.time() * 1000)
    return (current_time % (max_value - min_value + 1)) + min_value

def lcg(x:int) -> tuple:
    a = 1664525
    c = 1013904223
    m = 2**32
    x1 = ((a * x) + c) % m
    r = x1/m
    return x1, r

def buletin(batas_bawah: int, batas_atas: int, nilai: int) -> int:
    if batas_bawah <= nilai < batas_bawah + 0.73:
        return batas_bawah
    elif  batas_atas - 0.78 < nilai <= batas_atas:
        return batas_atas
    else:
        return round(nilai)

def rng(x: int, size: int, ranges: int, batas_bawah: int) -> int:
    global j
    arr = [0 for i in range(size)]
    for i in range (size):
        x,r = lcg(x)
        arr[i] = (buletin(batas_bawah, batas_bawah + ranges, (r * ranges) + batas_bawah))

    if j != 999:
        j +=1
    else:
        j = 0

    return arr[j]

def randint(min: int, maks: int) -> int:
    return rng(generate_random_seed(min,maks), 1000, maks - min, min)
'''---------------------------------------------------------- RNG ----------------------------------------------------------'''




'''---------------------------------------------------------- Process Data ----------------------------------------------------------'''
def read_csv(name_file: str, name_folder: str) -> tuple:
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

def length(arr: list,EOP: str) -> int:
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

def split_koma (line: str,row: int) -> list:
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
'''---------------------------------------------------------- Process Data ----------------------------------------------------------'''




'''---------------------------------------------------------- Save Data ----------------------------------------------------------'''
def write_csv(file_name: str, path_name: str):
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
'''---------------------------------------------------------- Save Data ----------------------------------------------------------'''