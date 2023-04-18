

def read_csv(name_file: str):
    fo = open(f"Template File CSV/{name_file}", 'r')
    data = fo.readlines()
    fo.close()   
    return(data)

def lengtharr(n:list) -> int:
    count = 0
    i = 1
    cek = True
    while cek:
        if n[i] == 'EOP':
            cek = False
        else:
            count +=1
            # print('i',i)
            # print('count',count)
        i+=1
    return count

def length(n: str,EOP: str):
    count = 0
    i = 0
    cek = True
    while cek:
        if n[i] == EOP:
            cek = False
        else:
            count +=1
            # print('i',i)
            # print('count',count)
        i+=1
    return count

def splitkoma (line: str,row: int):
    split_value = ["" for i in range(row)]
    temp = ''
    index1 = 0
    index2 = 0
    char = line[index2]
    while char != '.':
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
    return split_value

# splitkoma('username;password;role.\n',3)




datacandi = read_csv("candi.csv")
datauser = read_csv("user.csv")
databahanbangunan = read_csv("bahan_bangunan.csv")

lencandi = lengtharr(datacandi)
lenuser = lengtharr(datauser)
lenbahan = 1


datauser2 = [[] for i in range(lenuser)]
for i in range(0,lenuser):
    datauser2[i] = splitkoma(datauser[i+1],3)
datacandi2 = [[] for i in range(lencandi)]
for i in range(0,lencandi):
    datacandi2[i] = splitkoma(datacandi[i+1],6)
databahanbangunan2 = [[]]
databahanbangunan2[0] = splitkoma(databahanbangunan[1],3) 

total_candi_dihancurkan = 0
id_candi_dihancurkan = []



# # print(datacandi)
# print()
# print(datacandi2)
# print(lencandi)
# print()

# # print(datauser)
# print()
# print(datauser2)
# print(lenuser)
# print()

# # print(databahanbangunan)
# print(databahanbangunan2)
