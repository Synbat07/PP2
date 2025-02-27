import re

s = input()
print(re.sub(r'(?<!^)([A-Z])', r' \1', s))


"""
Ввод:  "HelloWorld"
Вывод: "Hello World"
"""
