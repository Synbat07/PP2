import os

path = "example.txt"  # Укажи свой путь

if os.path.exists(path):
    print(f"Путь {path} существует")
    print("Читаемый?", os.access(path, os.R_OK))
    print("Записываемый?", os.access(path, os.W_OK))
    print("Исполняемый?", os.access(path, os.X_OK))
else:
    print(f"Путь {path} НЕ существует")
