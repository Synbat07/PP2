from datetime import datetime

d1 = datetime.fromisoformat(input("Введите первую дату (YYYY-MM-DD HH:MM:SS): "))
d2 = datetime.fromisoformat(input("Введите вторую дату (YYYY-MM-DD HH:MM:SS): "))

print(abs((d2 - d1).total_seconds()))
