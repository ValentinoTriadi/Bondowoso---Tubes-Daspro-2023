import command
# datas = ["\nuser1,pass1,role1"]

def save_csv(name_file, data):
    fo = open(f"Template File CSV/{name_file}", 'a')

    tempdata = []
    for i in range(command.length(data)):
        tempdata.append(data[i])

    fo.writelines(tempdata)
    fo.close()


# save_csv("user.csv")