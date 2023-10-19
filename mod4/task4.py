def is_palindrome_possible(word):
    letter_count = {}
    odd_count = 0

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for count in letter_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True

def generate_palindrome(word):
    if not is_palindrome_possible(word):
        return "Невозможно составить палиндром"

    palindrome = []
    middle_letter = ""

    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter, count in letter_count.items():
        if count % 2 == 0:
            palindrome.extend([letter] * (count // 2))
        else:
            middle_letter = letter * count

    return "".join(palindrome) + middle_letter + "".join(palindrome[::-1])


word = input("Введите слово: ")
palindrome = generate_palindrome(word)
print("Палиндром:", palindrome)