def Ouick_Exponentiation(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return Ouick_Exponentiation(a ** 2, n / 2)
    if n % 2 != 0:
        return a * Ouick_Exponentiation(a, (n - 1))


degreeBase = int(input('Основание:'))
degree = int(input('Степень:'))
print(Ouick_Exponentiation(degreeBase, degree))
