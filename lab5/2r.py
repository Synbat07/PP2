import re

print(bool(re.fullmatch(r"^a[b]{2,3}$", input())))

"""
Ввод: abb  
Вывод: True  

Ввод: abbb  
Вывод: True  

Ввод: a  
Вывод: False  
"""