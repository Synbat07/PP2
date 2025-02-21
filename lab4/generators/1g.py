def squares(N):
    """Генерирует квадраты чисел от 0 до N (включительно)."""
    for i in range(N + 1):
        yield i ** 2

N = int(input("Введите число N: "))

for square in squares(N):
    print(square)
