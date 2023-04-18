import tempdata

def read_csv(name_file: str):
    fo = open(f"Template File CSV/{name_file}", 'r')
    data = fo.readlines()
    fo.close()   
    return(data)

# def length(n: str) -> int:
def length(n: str) -> int:
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


def maksimum(arr: list,lenarr: int):
    maks = arr[0]
    for i in range(lenarr):
        if maks < arr[i]:
            maks = arr[i]
    return maks

def minimum(arr: list, lenarr: int):
    min = arr[0]
    for i in range(lenarr):
        if min > arr[i]:
            min = arr[i]
    return min


'''----------------------------- Leksikografi -----------------------------'''
def sort(arr: list, length: int, operator: str):
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

def leksikal(arr: list,length: int, highest: bool):
    if highest:
        arr = sort(arr,length, '>')
    else:
        arr = sort(arr,length, '<')
    print(arr)
    return arr

# leksikal(['aasdf','ggsdf','dadu','duda','dadui','dadi','jasdf','tgsa','hsg'],9,False)

'''----------------------------- RNG -----------------------------'''
# def generate_random_number(min_value, max_value): 
#     current_time = int(time.time() * 1000)
#     return (current_time % (max_value - min_value + 1)) + min_value

def varj():
    f = open("Template File CSV/rng.csv",'r')
    data = f.readlines()
    temp = ""
    for i in range(tempdata.length(str(data[0])+'.','.')):
        temp += (data[0][i])
    f.close()
    f = open("Template File CSV/rng.csv",'w')
    temp = int(temp)
    if temp <999:
        f.writelines([str(temp+1)])
    else:
        f.writelines([str(0)])
    f.close()

    return temp

def lcg(x: int):
    multiplier = 1664525
    increment = 1013904223
    modulus = 2**32
    x1 = ((multiplier * x) + increment) % modulus
    r = x1/modulus
    return x1, r

def buletin(batasbawah: int, batasatas: int, n: float):
    if batasbawah<=n<batasbawah+0.73:
        return batasbawah
    elif  batasatas - 0.78 < n <= batasatas:
        return batasatas
    else:
        return round(n)

def rng(x : int,size: int,ranges: int,batasbawah: int):
    arr = [0 for i in range(size)]
    for i in range (size):
        x,r = lcg(x)
        arr[i] = (buletin(batasbawah, batasbawah+ranges,r*ranges+batasbawah))
    j = varj()
    # print(arr)
    # temp = []
    # for i in range(batasbawah,batasbawah+ranges+1):
    #     temp.append(arr.count(i))
    # print(temp)
    return arr[j]

def randint(min: int,maks: int):
    return rng(1,1000,maks-min,min)

randint(0,5)
# randint(1,5)
# import time
# for i in range(1000):
#     print(randint(1,5))
#     time.sleep(0.1)
