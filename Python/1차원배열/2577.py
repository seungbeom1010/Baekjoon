A = 1

for _ in range(3):
    A *= int(input())

B = [int(x) for x in str(A)]

for i in range(10):
    print(B.count(i))