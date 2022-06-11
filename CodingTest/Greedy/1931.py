N = int(input())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = sorted(data, key = lambda x : (x[1], x[0]))
end_time = data[0][1]
cnt = 1
for i in range(1, N):
    if data[i][0] >= end_time:
        cnt += 1
        end_time = data[i][1]

print(cnt)