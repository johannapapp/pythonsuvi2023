m = int(input())
n = int(input())
x = input("kas sa soovid liita?")
if x == "jah":
    print(m + n)
elif x == "ei":
    y = input("aga lahutada?")
    if y == "jah":
        print(m-n)
    elif  y == "ei":
        z = input("aga astendada?")
        if z == "jah":
            print(m ** n)
        elif z == "ei":
            s = input("aga jääki leida?")
            if s  == "jah":
                print(m % n)
            elif s == "ei":
                l = input("aga ümardada teatud komakohani")
            if l == "jah":
                k = int(input("mis komakohani?"))
                print(round(m, k))
                print(round(n, k))
