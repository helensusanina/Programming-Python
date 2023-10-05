string = str(input())
result = ""
count = 0
while count < len(string):
    if string[count] == " ":
        result += string[count - 1]
    count += 1
print(result + string[-1])


