import argparse

def argparse1():
    parser = argparse.ArgumentParser()
    parser.add_argument("name_folder",type=str, help="Nama Folder")
    try:
        args = parser.parse_args()
    except:
        print("Tidak ada nama folder yang diberikan!")
        return

    name_folder = args.name_folder
    if name_folder != "Template File CSV":
        print("oye")
    else:
        print("asdfasdf")

# python main.py nama_folder


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count", default=0,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)


def splitkoma (line):
    split_value = []
    temp = ''
    for char in line:
        if char == ',':
            split_value.append(temp)
            temp = ''
        else:
            temp += char
    if temp:
        split_value.append(temp)
    return split_value

def read_csv (name_file):
    fo = open(f"Template File CSV/{name_file}", 'r')
    data = fo.read()
    fo.close()   

    data1=[]
    data = data.splitlines()
    for line in data:
        data1.append(splitkoma(line))
        # print("DATA",data)
        # print("line",line)
        # print("data1",data1)
    print(data1)

# read_csv("candi.csv")
# read_csv("user.csv")
# read_csv("bahan_bangunan.csv")

