import re

s = input()
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower())


"""
Ввод:  "helloWorld"
Вывод: "hello_world"
"""
