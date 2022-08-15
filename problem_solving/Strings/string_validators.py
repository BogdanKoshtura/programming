if __name__ == '__main__':
    s = input()

    for inx, i in enumerate(s):
        if True == i.isalnum():
            print(True)
            break
        elif inx == (len(s) - 1):
            print(False)
    
    for inx, i in enumerate(s):
        if True == i.isalpha():
            print(i.isalpha())
            break
        elif inx == (len(s) - 1):
            print(False)

    for inx, i in enumerate(s):
        if True == i.isdigit():
            print(i.isdigit())
            break
        elif inx == (len(s) - 1):
            print(False)
    
    for inx, i in enumerate(s):
        if True == i.islower():
            print(i.islower())
            break
        elif inx == (len(s) - 1):
            print(False)

    for inx, i in enumerate(s):
        if True == i.isupper():
            print(i.isupper())
            break
        elif inx == (len(s) - 1):
            print(False)



    