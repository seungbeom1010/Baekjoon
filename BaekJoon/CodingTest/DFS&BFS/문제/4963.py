import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
graph.sort()
if n == 1:
    print(graph[-1] * graph[-1])
else:
    print(graph[0] * graph[-1])