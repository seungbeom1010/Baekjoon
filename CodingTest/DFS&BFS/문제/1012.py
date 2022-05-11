import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    return False

def print_worms(n, m):
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    print(result)

for _ in range(int(input())):
    n, m, p = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for _ in range(p):
        x, y = map(int, input().split())
        graph[y][x] = 1
    print_worms(n, m)