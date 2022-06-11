import sys

n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
cnt = 0

def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]

for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1
        if A == B:
            break
    if A == B:
        break

if A == B:
    print(cnt)
else:
    print(-1)