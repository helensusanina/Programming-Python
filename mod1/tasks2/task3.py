abc= input()
ind1 = abc.find(" ")
a = int(abc[:ind1])
ind2 = abc.find(" ", ind1 + 1)
b = int(abc[ind1+1:ind2])
c = int(abc[ind2 + 1:])
if a < b:
    if b < c:
        print(b)
    else:
        if a < c:
            print(c)
        else:
            print(a)
else:
    if c < b:
        print(b)
    else:
        if c < a:
            print(c)
        else:
            print(a)

