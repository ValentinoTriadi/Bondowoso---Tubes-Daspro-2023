import util_function, load_only

name_folders = load_only.nama_folder
# name_folders = "asdfasdfasdf"

datacandi, len_candi = util_function.read_csv("candi.csv", name_folders)
datauser, len_user = util_function.read_csv("user.csv", name_folders)
databahanbangunan = util_function.read_csv("bahan_bangunan.csv", name_folders)[0]

data_user = [[] for i in range(len_user)]
for i in range(len_user):
    data_user[i] = util_function.split_koma(datauser[i],3)

data_candi = [[] for i in range(len_candi)]
for i in range(len_candi):
    data_candi[i] = util_function.split_koma(datacandi[i],6)

temp_data_candi = [["" for j in range(6)] for i in range(len_candi)]
for i in range(len_candi):
    if data_candi[i] != []:
        for j in range(6):
            if j != 5:
                temp_data_candi[i][j] = data_candi[i][j]
            else:
                temp_data_candi[i][j] = 10000 * int(data_candi[i][2]) + 15000 * int(data_candi[i][3]) + 7500 * int(data_candi[i][4])
for i in range(len_candi):
    if temp_data_candi[i][0] != '':
        data_candi[i] = temp_data_candi[i]
    else:
        data_candi[i] = []

data_bahan_bangunan = [[]]
data_bahan_bangunan[0] = util_function.split_koma(databahanbangunan[0],3) 

jumlah_candi_yang_dihancurkan = 0
for i in range(len_candi):
    if data_candi[i] == []:
        jumlah_candi_yang_dihancurkan += 1

index = 0
id_candi_yang_dihancurkan = [0 for i in range(jumlah_candi_yang_dihancurkan)]
for i in range(len_candi):
    if data_candi[i] == []:
        id_candi_yang_dihancurkan[index] = i + 1
        index += 1


len_pembangun = 0
for i in range(len_user):
    if data_user[i][2] == "Pembangun":
        len_pembangun += 1
data_jin_yang_pernah_membangun = ["" for i in range(len_pembangun)]
j = 0
for i in range(len_user):
    if data_user[i][2] == "Pembangun":
        data_jin_yang_pernah_membangun[j] = data_user[i][0]
        j += 1

for i in range(len_candi):
    if data_candi[i] != []:
        cek = True
        for j in range(len_pembangun):
            if data_candi[i][1] == data_jin_yang_pernah_membangun[j]:
                cek = False
        
        if cek:
            len_pembangun += 1
            temp_data_jin_yang_pernah_membangun = ["" for k in range(len_pembangun)]
            for k in range(len_pembangun-1):
                temp_data_jin_yang_pernah_membangun[k] = data_jin_yang_pernah_membangun[k]
            temp_data_jin_yang_pernah_membangun[len_pembangun-1] = data_candi[i][1]
            data_jin_yang_pernah_membangun = temp_data_jin_yang_pernah_membangun