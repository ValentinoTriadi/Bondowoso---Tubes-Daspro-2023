import command

def splitkoma (line):
    split_value = []
    temp = ''
    for i in range(command.length(line)):
        if i == command.length(line)-1:
            break
        if line[i] == ',':
            split_value.append(temp)
            temp = ''
        else:
            temp += line[i]
    if temp:
        split_value.append(temp)
    return split_value

def read_csv (name_file):
    fo = open(f"Template File CSV/{name_file}", 'r')
    data = fo.readlines()
    fo.close()   

    data1=[]
    for line in data:
        data1.append(splitkoma(line))
    return data1

# read_csv("user.csv")