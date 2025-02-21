from datetime import datetime, timedelta
now = datetime.now().date()

# Вычитаем 5 дней
new = now - timedelta(days=5)

print("Текущая дата: ", now)
print("Дата 5 дней назад: ", new)
