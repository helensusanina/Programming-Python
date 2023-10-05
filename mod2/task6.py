stringSite = str(input())
firstSym = stringSite.find(".")
domen1 = stringSite[:firstSym]
secondSym = stringSite.find(".", firstSym + 1)
domen2 = stringSite[firstSym + 1:secondSym]
domen3 = stringSite[secondSym + 1:]

print(domen3)
print(domen2)
print(domen1)