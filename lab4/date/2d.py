from datetime import datetime, timedelta
now = datetime.now().date()

yest = now - timedelta(days=1)
tom = now + timedelta(days=1)

print("Yesterday: ", yest)
print("Today: ", now)
print("Tomorrow: ", tom)
