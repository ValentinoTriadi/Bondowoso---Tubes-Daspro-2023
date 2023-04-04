def length(n):
    cek = True
    i = 0
    lengths = 0
    while cek == True:
        try:
            n[i]
            lengths += 1
            i+=1
        except IndexError:
            cek = False
    return lengths


        