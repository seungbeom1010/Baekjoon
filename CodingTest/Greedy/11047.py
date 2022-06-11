n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data = sorted(data, reverse=True)
result = 0
for i in data:
    if k // i > 0:
        result += k // i
        k = k % i 


print(result)
