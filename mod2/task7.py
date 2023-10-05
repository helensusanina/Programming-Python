string = str(input())
count1 = 0
count0 = 0
for i in string:
    if i == "1":
        count1 += 1
    if i == "0":
        count0 += 1
if count0 == count1:
    print("yes")
else:
    print("no")
