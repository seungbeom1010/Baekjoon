from sys import stdin
import copy

N = int(stdin.readline())
A = list(map(int, stdin.readline().rstrip()))
B = list(map(int, stdin.readline().rstrip()))

r1 = copy.deepcopy(A)
r2 = copy.deepcopy(A)

def switch(i):
    if i == 0:
        A[i] = 1 - A[i]
        A[i + 1] = 1 - A[i + 1]
    elif i == N - 1:
        A[i - 1] = 1 - A[i - 1]
        A[i] = 1 - A[i]
    else:
        A[i - 1] = 1 - A[i - 1]
        A[i] = 1 - A[i]
        A[i + 1] = 1 - A[i + 1]

for i in range(2):
    A = r1 if i == 0 else r2

    cnt = 0
    for j in range(N):
        if j == 0:
            if i == 0 and A != B:
                cnt += 1
                switch(j)
        else:
            if A[j - 1] != B[j - 1]:
                cnt += 1
                switch(j)
    if A == B:
        print(cnt)
        break

if A != B:
    print(-1)
    
