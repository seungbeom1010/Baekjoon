
L = []

for _ in range(int(input())):
    L.append(list(map(int, input().split())))

R = []

for i in range(len(L)):
    count = 0
    for j in range(len(L)):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            count += 1
    
    R.append(count + 1)


for A in R:
    print(A, end=" ")