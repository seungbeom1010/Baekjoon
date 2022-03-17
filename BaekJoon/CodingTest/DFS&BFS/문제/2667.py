n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

temp = 0

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global temp
        temp += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(temp)
            temp = 0
print(len(result))
for i in sorted(result):
    print(i)