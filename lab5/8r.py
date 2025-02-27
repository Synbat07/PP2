import re

s = input()
print(re.split(r'(?=[A-Z])', s))


"""
Ввод:  "SplitThisString"
Вывод: ['Split', 'This', 'String']
"""
