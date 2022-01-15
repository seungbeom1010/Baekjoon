

def hanoi(n, start, sub, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, sub)
        print(start, end)
        hanoi(n-1, sub, start, end)

n = int(input())

print(2**n - 1)

hanoi(n, 1, 2, 3)