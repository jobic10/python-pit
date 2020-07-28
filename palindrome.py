def check(string):
    string = list(string)
    pal = []
    for i in string[::-1]:
        print(i)
        pal.append(i)
    if pal == string:
        return True
    else:
        return False

    # Checks if a string is palindrome 
