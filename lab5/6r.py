import re

s = input()
print(re.sub(r"[ ,.]", ":", s))

"""
Ввод:  "Hello. How are you?"  
Вывод: "Hello::How:are:you?"  
"""