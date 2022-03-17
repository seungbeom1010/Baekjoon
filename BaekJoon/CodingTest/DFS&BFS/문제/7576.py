from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))

queue = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[nx][ny] == -1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

result = 0
print_minus = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] > result:
            result = graph[i][j]
        elif graph[i][j] == 0:
            print_minus = 1
if print_minus != 0:
    print(-1)
else:
    print(result - 1)

        


