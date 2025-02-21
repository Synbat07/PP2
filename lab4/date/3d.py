from datetime import datetime

now = datetime.now()

# Убираем микросекунды, устанавливая их в 0
new_datetime = now.replace(microsecond=0)

print("Оригинальное время:", now)
print("Без микросекунд:", new_datetime)
