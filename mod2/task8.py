strInput = str(input())
sign = strInput.find(",")
str = strInput[:sign] + " "
symbol = strInput[sign + 1:]
count = 0
for i in range(len(str)):
    if str[i] == symbol:
        count += 1
    if count > 0 and str[i+1] != symbol:
        break
print(count)
