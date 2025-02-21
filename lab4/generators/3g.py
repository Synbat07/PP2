# числа которые деляться на 3 и 4

def num (n):
    for i in range (0, n):
        if i%3==0 and i%4==0:
            yield i
    
n = int(input ("Enter n: "))

for j in num(n):
    print (j)