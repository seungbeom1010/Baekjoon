import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
visited1 = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
graph1 = []
for _ in range(n):
    graph1.append(list(input().rstrip()))

graph2 = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph1[i][j] == 'G':
            graph2[i].append('R')
        else:
            graph2[i].append(graph1[i][j])


def dfs(x, y, sign, graph, visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if visited[x][y] == 0 and graph[x][y] == sign:
        visited[x][y] = 1
        dfs(x - 1, y, sign, graph, visited)
        dfs(x + 1, y, sign, graph, visited)
        dfs(x, y - 1, sign, graph, visited)
        dfs(x, y + 1, sign, graph, visited)
        return True
    return False

count1 = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, graph1[i][j], graph1, visited1):
            count1 += 1
        if dfs(i, j, graph2[i][j], graph2, visited2):
            count2 += 1

print(count1, count2)