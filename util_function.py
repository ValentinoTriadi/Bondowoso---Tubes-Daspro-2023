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
import time
# Aspek randomisasi dari RNG kami adalah
# 1. Random Seed dari waktu saat fungsi dipanggil
# 2. LCG
# 3. Index yang terus bergerak

j = 0 # Variabel untuk mengambil index sebuah array hasil randomisasi
'''-------------------- Generate Seed --------------------'''
def generate_random_seed(min_value: int, max_value:int) -> int: 
    current_time = int(time.time() * 1000) # Mengambil waktu saat fungsi ini dijalankan
    return (current_time % (max_value - min_value + 1)) + min_value # Mengembalikan sisa bagi waktu saat ini dengan range yang diinginkan
'''-------------------- Generate Seed --------------------'''


'''-------------------- Linear congruential generator --------------------'''
def lcg(x:int) -> tuple:
    # Source: Numerical Recipes from the "quick and dirty generators" list, Chapter 7.1, Eq. 7.1.6 parameters from Knuth and H. W. Lewis
    a = 1664525 # Multiplier
    c = 1013904223 # Increment
    m = 2**32 # Modulus
    x1 = ((a * x) + c) % m # Formula
    r = x1/m # 0 <= r <= 1
    return x1, r
'''-------------------- Linear congruential generator --------------------'''


'''-------------------- Custom Round --------------------'''
def rounds(batas_bawah: int, batas_atas: int, nilai: int) -> int:
    if batas_bawah <= nilai < batas_bawah + 0.73: # Ketika nilai mendekati batas bawah, pembulatan diatur sedemikian rupa agar rasio (chance) keluarnya sebuah angka yang mendekati batas bawah bertipe integer mendekati rasio (chance) keluarnya angka yang berada pada pertengahan batas
        return batas_bawah
    elif  batas_atas - 0.78 < nilai <= batas_atas: # Ketika nilai mendekati batas atas, pembulatan diatur sedemikian rupa agar rasio (chance) keluarnya sebuah angka yang mendekati batas atas bertipe integer mendekati rasio (chance) keluarnya angka yang berada pada pertengahan batas
        return batas_atas
    else:
        return round(nilai) # Mengembalikan nilai pembulatan apabila nilai tidak mendekati batas bawah maupun batas atas
'''-------------------- Custom Round --------------------'''


'''-------------------- Random Number Generator --------------------'''
def rng(x: int, size: int, ranges: int, batas_bawah: int) -> int:
    global j 
    arr = [0 for i in range(size)] # Membuat array berisi elemen sebanyak size 
    for i in range (size): # Loop untuk mengisi array dengan integer hasil randomisasi
        x,r = lcg(x) # Melakukan randomisasi integer
        arr[i] = (rounds(batas_bawah, batas_bawah + ranges, (r * ranges) + batas_bawah)) # Membulatkan dan memasukan ke array

    if j != size-1: # Ketika index belum mencapai index terakhir dari array
        j +=1 # Index bertambah 1
    else: # Ketika index dari array mencapai index terakhir dari array
        j = 0 # Index mengulang dari Index awal

    return arr[j] # Mengembalikan elemen dari array sesuai index 

def randint(min: int, maks: int) -> int:
    return rng(generate_random_seed(min,maks), 1000, maks - min, min) # Melakukan randomisasi dan mengembalikan hasil randomisasi berupa integer
'''-------------------- Random Number Generator --------------------'''

'''---------------------------------------------------------- RNG ----------------------------------------------------------'''




'''---------------------------------------------------------- Process Data ----------------------------------------------------------'''

'''-------------------- Read CSV --------------------'''
def read_csv(name_file: str, name_folder: str) -> tuple:
    fo = open(f"./save/{name_folder}/{name_file}", 'r') # Membaca file CSV
    
    '''-------------------- Inisialisasi Awal --------------------'''
    length = 0 # Variabel yang menyimpan panjang data 
    data = ["" for i in range(1000)] # List tertentu untuk menyimpan data yang dibaca
    '''-------------------- Inisialisasi Awal --------------------'''


    '''-------------------- Proses Membaca Data --------------------'''
    for line in fo: # Loop untuk membaca seluruh baris pada file yang di open
        data[length] = line # Memasukan baris ke list
        length += 1 # Menambahkan panjang data
    '''-------------------- Proses Membaca Data --------------------'''

    fo.close() # Menutup file CSV   
    length -= 1 # Mengurangi panjang data sebanyak 1, karena pada data yang kami proses, kami tidak menginginkan header file masuk ke dalam data kami (Kami hanya mengambil isi dari datanya, tidak dengan headernya)

    '''-------------------- Proses Mengupdate Tempat Data --------------------'''
    tempdata = ["" for i in range(length)] # Inisialisasi tempat menyimpan data yang panjangnya sesuai dengan data yang ada
    for i in range(length): # Loop untuk mengisi list tempat menyimpan data
        tempdata[i] = data[i+1] # Mengisi list dengan data, dimulai dari line 1 hingga akhir ( line 1 merupakan awal dari data yang bukan merupakan header )
    '''-------------------- Proses Mengupdate Tempat Data --------------------'''

    return tempdata, length # Mengembalikan data dan panjang data

'''-------------------- Read CSV --------------------'''


'''-------------------- Menghitung Panjang String --------------------'''
# Menggunakan metode sentinel
def length(arr: list,EOP: str) -> int:
    count = 0 # Inisialisasi awal jumlah character
    i = 0 # index string
    cek = True # Kondisi pemberhenti perhitungan

    while cek: # Saat kondisi True (sentinel belum ditemukan)
        if arr[i] == EOP: # Saat sentinel ditemukan
            cek = False # Kondisi berubah menjadi False
        else: # Saat sentinel belum ditemukan
            count +=1 # Panjang atau jumlah character bertambah 1
        i+=1 # index string bertambah 1

    return count # Mengembalikan nilai panjang string

'''-------------------- Menghitung Panjang String --------------------'''


'''-------------------- Memisahkan Data --------------------'''
def split_koma (line: str,row: int) -> list:

    '''-------------------- Inisialisasi Awal --------------------'''
    split_value = ["" for i in range(row)] # List Hasil Pemisahan
    temp = '' # Temporary string yang berisi data 
    index1 = 0 # index list hasil pemisahan
    index2 = 0 # index string
    char = line[index2] # Karakter pada string yang ingin dipisahkan
    '''-------------------- Inisialisasi Awal --------------------'''

    while char != '\n': # Loop untuk memisahkan data dengan indikator ';'

        if char == ';': # Saat karakter yg sedang dicek merupakan ';' maka temp string sebelum ';' akan disimpan pada split_value
            split_value[index1] = temp # Menyimpan data 
            temp = '' # Memulai pengambilan data baru
            index1 +=1 # Index list bertambah 1
            index2 +=1 # Index string bertambah 1
        else: # Saat karakter yang sedang dicek bukan merupakan ';'
            temp += char # Karakter ditambahkan ke temp string sebagai data 
            index2 +=1 # Index string bertambah 1

        char = line[index2] # Melanjutkan pengecekan karakter dengan index2

    split_value[index1] = temp # Memasukan data terakhir kedalam list split_value

    if split_value[0] != "": # Ketika data yang di split tidak kosong
        return split_value # Mengembalikan data yang sudah di pisahkan
    else: # Ketika data yang di split kosong
        return [] # Mengembalikan data kosong

'''-------------------- Memisahkan Data --------------------'''

'''---------------------------------------------------------- Process Data ----------------------------------------------------------'''




'''---------------------------------------------------------- Save Data ----------------------------------------------------------'''
def write_csv(file_name: str, path_name: str):
    import tempdata
    file = open(f"./{path_name}/{file_name}","w") # Membuka file / membuat file (jika file belum ada) 

    if file_name == "candi.csv": # Ketika ingin melakukan penyimpanan file candi.csv
        data = tempdata.data_candi # Mengambil data candi
        tempdatas = ["" for i in range(tempdata.len_candi + 1)] # Menyiapkan tempat untuk menuliskan data ke file csv
        tempdatas[0] = f"id;pembuat;pasir;batu;air\n" # Membuat header file

        for i in range(tempdata.len_candi): # Loop untuk mengisi list
            if data[i] == []: # Ketika data kosong
                tempdatas[i+1] = "\n" # Mengisi list dengan data kosong
            else: # Ketika data tidak kosong
                tempdatas[i+1] = f"{data[i][0]};{data[i][1]};{data[i][2]};{data[i][3]};{data[i][4]}\n" # Mengisi list dengan string formating sesuai struktur data
                
    elif file_name == "user.csv": # Ketika ingin melakukan penyimpanan file user.csv
        data = tempdata.data_user # Mengambil data user
        tempdatas = ["" for i in range(tempdata.len_user + 1)] # Menyiapkan tempat untuk menuliskan data ke file csv
        tempdatas[0] = f"username;password;role.\n" # Membuat header file

        for i in range(tempdata.len_user): # Loop untuk mengisi list
            tempdatas[i+1] = f"{data[i][0]};{data[i][1]};{data[i][2]}\n" # Mengisi list dengan string yang di format sesuai struktur data

    elif file_name == "bahan_bangunan.csv": # Ketika ingin melakukan penyimpanan file bahan_bangunan.csv
        data = tempdata.data_bahan_bangunan # Mengambil data bahan bagunan
        tempdatas = ["" for i in range(2)] # Menyiapkan tempat untuk menuliskan data ke file csv
        tempdatas[0] = f"pasir;batu;air.\n" # Membuat header
        tempdatas[1] = f"{data[0][0]};{data[0][1]};{data[0][2]}\n" # Mengisi list dengn string yang di format sesuai struktur data

    file.writelines(tempdatas) # Menuliskan list kedalam csv
    file.close() # Menutup file
'''---------------------------------------------------------- Save Data ----------------------------------------------------------'''