import os

path = "example.txt"

if os.path.exists(path):
    print(f"Путь {path} существует")
    print("Имя файла:", os.path.basename(path))
    print("Директория:", os.path.dirname(path))
else:
    print(f"Путь {path} НЕ существует")
