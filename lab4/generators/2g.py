#четные

def even (n):
    for i in range (0, n+1, 2):
        yield str(i)
    
n = int(input ("Enter n: "))

print (", ".join(even(n)))