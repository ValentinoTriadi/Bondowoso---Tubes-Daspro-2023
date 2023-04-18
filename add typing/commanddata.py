''' ------------------------------Command Data------------------------------ '''
# TODO: Read CSV file and convert it to array
def splitkoma (line: str):
    import command
    split_value = []
    temp = ''
    for i in range(command.length(line)):
        if i == command.length(line)-1:
            break
        if line[i] == ';':
            split_value.append(temp)
            temp = ''
        else:
            temp += line[i]
    if temp:
        split_value.append(temp)
    return split_value

def read_csv(name_file: str):
    import command
    fo = open(f"Template File CSV/{name_file}", 'r')
    data = fo.readlines()
    fo.close()   

    data1=[]
    for i in range(command.length(data)):
        if i != command.length(data)-1:
            data1.append(splitkoma(data[i]))
        else:
            text = data[i] + "\n"
            data1.append(splitkoma(text))
    return data1


# TODO: Remove Specific line of data from CSV file
def remove_data(name_file: str, user):
    import command
    datauser = read_csv(name_file)
    tempdata = []

    for i in range(command.length(datauser)):
        if datauser[i][0] != user:
            tempdata.append(datauser[i])
    
    rewrite_data(name_file, tempdata)


# TODO: Rewrite CSV File with array of array
def rewrite_data(name_file: str,data):
    #data ?
    import command, commanddata
    fo = open(f"Template File CSV/{name_file}", 'w')
    fo.close()

    for i in range(command.length(data)):
        templine = ""
        if i != command.length(data) -1:
            for j in range(command.length(data[i])):
                if j != command.length(data[i]) -1:
                    templine += str(data[i][j]) + ";"
                else:
                    templine += str(data[i][j]) + "\n"
        else:
            for j in range(command.length(data[i])):
                if j != command.length(data[i]) -1:
                    templine += str(data[i][j]) + ";"
                else:
                    templine += str(data[i][j])

        datas = [templine]
        commanddata.save_csv(name_file, datas)


def save_csv(name_file: str, data):
    import command
    fo = open(f"Template File CSV/{name_file}", 'a')

    tempdata = []
    for i in range(command.length(data)):
        tempdata.append(data[i])

    fo.writelines(tempdata)
    fo.close()

     



     



            

    

