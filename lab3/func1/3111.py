def is_palindrome(s):
    s = s.lower().replace(" ", "")  #!!! s.replace(" ", "") — удаляет все пробелы из строки
    return s == s[::-1]

print(is_palindrome(input("Enter a word or phrase: ")))
