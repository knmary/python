from sys import argv

with open('bakery.csv','r',encoding='utf-8') as fl:
    prm = len(argv)
    if prm == 1:
        print(fl.read())
    elif prm == 2:
        for line in fl.readlines()[int(argv[1]) - 1:]:
            print(line, end='')