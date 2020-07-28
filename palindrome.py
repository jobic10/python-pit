def check(string):
    string = list(string)
    pal = []
    for i in range(len(string)-1,-1,-1):
        print(i)
        pal.append(string[i])
    if pal == string:
        return True
    else:
        return False
