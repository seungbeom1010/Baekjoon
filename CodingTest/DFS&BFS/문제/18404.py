from collections import deque

n, m = map(int, input().split())
x, y = map(int, input().split())
graph = [[0] * n for _ in range(n)]
enemy_loc = []
for _ in range(m):
    a, b = map(int, input().split())
    enemy_loc.append((a, b))

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph

for a, b in enemy_loc:
    print(bfs(x - 1, y - 1)[a - 1][b - 1] - 1)