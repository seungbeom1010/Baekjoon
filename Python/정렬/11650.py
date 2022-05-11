
array = []

for _ in range(int(input())):
    array.append(list(map(int, input().split())))

array = sorted(array, key = lambda x : [x[0], x[1]])

for x in array:
    print(x[0], x[1])