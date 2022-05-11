import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x not in graph[y]:
        graph[y].append(x)
    if y not in graph[x]:
        graph[x].append(y)

result = 0

def dfs(graph, v, visited):
    visited[v] = True
    global result
    result += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(result - 1)

