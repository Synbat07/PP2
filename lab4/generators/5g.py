def countdown(n):
    for i in range(n, -1, -1):  # Начинаем с n, уменьшаем до 0
        yield i

n = int(input("Введите число n: "))

for num in countdown(n):
    print(num)
