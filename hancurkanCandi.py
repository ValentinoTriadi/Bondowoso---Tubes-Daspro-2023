#import read

#data = read.read_csv("candi.csv")

def hancurkancandi ():
    found = False
    confirm = None
    idx = 0

    idCandi = input("Masukkan ID candi: ")
    for i in range(count_list(data)):
        if (data[i][0]) == (str(idCandi)):
            found = True
            idx = i
            break

    if found == True:
        confirm = str(input(f"Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)?"))
        if confirm == 'Y':
            removeCandi(idx)
    else:
        print("Tidak ada candi dengan ID tersebut.")
    
def removeCandi (baris):
    fo = open("Template File CSV/candi.csv", 'r')
    lines = fo.readlines()
    fo.close()

    del lines[baris]
 
    fo = open("Template File CSV/candi.csv", 'w')
    fo.writelines(lines)
    fo.close()

def count_list(data):
    count = 0
    for x in data:
        count += 1
    return count

#hancurkancandi() 
#Abis ancurin candi harus load data kembali
