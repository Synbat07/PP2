def reverse_words(s):
    words = s.split()  # Разбиваем строку на список слов
    if len(words) == 1:
        return words[0]
    return words[-1] + " " + reverse_words(" ".join(words[:-1]))

s = input("Введите строку: ")
print(reverse_words(s))
