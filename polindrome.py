

def Polindrom(str1):

    rev = str1[::-1]
    if rev == str1:
        print("Polindrome")
    else:
        print("non polindrom")


if __name__ == '__main__':
    str1 = "lel"
    Polindrom(str1)

