string = str(input()).replace(" ", "")
count = 0
for i in range(len(string)):
    for j in range(len(string)-1):
        if string[i] == string[j+1]:
            count += 1
            break

if count > 0:
    print(True)
else:
    print(False)