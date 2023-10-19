def count_letters(filename):
    letter_count = {}
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1])
    return sorted_letter_count

print(count_letters('input.txt'))