from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



