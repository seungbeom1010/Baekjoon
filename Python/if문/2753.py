a, b = map(int, input().split())

if b - 45 >= 0:
    a = a
    b = b - 45
else:
    if a - 1 == -1:
        a = 23
        b = 60 - 45 + b
    else:

        a = a - 1
        b = 60 - 45 + b
        
print(a, end=' ') 
print(b)