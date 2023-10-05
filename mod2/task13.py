barcode = str(input())
countChet = 0
countNechet = 0
for i in range(len(barcode)):
    if i % 2 == 0:
        countNechet += int(barcode[i])
    else:
        countChet += int(barcode[i])
if (3 * countChet + countNechet) % 10 == 0:
    print('yes')
else:
    print("no")
