# Площадь правильного многоугольника
"""
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""

import math

n = 4  # количество сторон
s = 25  # длина стороны

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("Площадь многоугольника: ", area)
