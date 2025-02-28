import os

path = "."  # Текущая папка
items = os.listdir(path)

print("Содержимое папки:")
for item in items:
    print("-", item)
