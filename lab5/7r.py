import re

s = input()
print(re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s))

"""
Ввод:  "hello_world"
Вывод: "helloWorld"
"""