N = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
previous = 0
for i in data:
    previous += i
    result += previous

print(result)

