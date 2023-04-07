#import read

#data = read.read_csv("candi.csv")

def ayamBerkokok():
    nCandi = count_list(data)
    print("Kukuruyuk.. Kukuruyuk..\n")
    print(f"Jumlah Candi : {nCandi}\n")
    if nCandi >= 100 :
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        #Panggil Exit
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        #Panggil Exit
    
def count_list(data):
    count = 0
    for x in data:
        count += 1
    return count

#ayamBerkokok()
