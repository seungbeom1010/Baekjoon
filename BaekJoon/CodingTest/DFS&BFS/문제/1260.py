from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    if x not in graph[y]:
        graph[y].append(x)
    if y not in graph[x]:
        graph[x].append(y)

visited_bfs = [False] * (n + 1)
visited_dfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
print("")
bfs(graph, v, visited_bfs)