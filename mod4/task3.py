def euclidean_algorithm(a, b):
    if b == 0:
        return a
    else:
        return euclidean_algorithm(b, a % b)


number1 = int(input())
number2 = int(input())
print(euclidean_algorithm(number1, number2))
