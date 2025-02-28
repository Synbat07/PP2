file_path = "example.txt"

try:
    print("Количество строк:", sum(1 for _ in open(file_path, encoding="utf-8")))
except FileNotFoundError:
    print("Файл не найден!")

