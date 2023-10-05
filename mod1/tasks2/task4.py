number = int(input())
def convert(num, base):
    num_bin = ''
    while num > 0:
        num_bin = str(num % base) + num_bin
        num = num // base
    return (num_bin)


print(convert(number, 2), convert(number, 8), convert(number, 16))
