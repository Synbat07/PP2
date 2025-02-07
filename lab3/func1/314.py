numbers = [int(x) for x in input().split()]

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
