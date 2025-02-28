#Вычисление квадратного корня после задержки

import time
import math

num = int(input())
delay = int(input())

time.sleep(delay / 1000)  # Переводим миллисекунды в секунды
sqrt_result = math.sqrt(num)

print(f"Square root of {num} after {delay} miliseconds is {sqrt_result}")
