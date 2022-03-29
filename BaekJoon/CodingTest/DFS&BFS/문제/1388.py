import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(input().rstrip())

def dfs(x, y, sign):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if visited[y][x] == 0 and graph[y][x] == sign:
        visited[y][x] = 1
        if graph[y][x] == '-':
            dfs(x + 1, y, sign)
        elif graph[y][x] == '|':
            dfs(x, y + 1, sign)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(j, i, graph[i][j]) == True:
            # print(visited)
            count += 1

print(count)