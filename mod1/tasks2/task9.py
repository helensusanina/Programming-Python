string = str(input())
alphabetVowel = "ауоыиэяюёе"
alphabetConsonant = "йцкнгшщхзфвпрлджчсмтб"
countVow, countConsonant = 0, 0
for i in string:
    if i in alphabetVowel:
        countVow += 1
    if i in alphabetConsonant:
        countConsonant += 1
print(countVow, countConsonant)
