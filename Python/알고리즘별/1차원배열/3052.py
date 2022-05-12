cnt = 0

left_list = []

for _ in range(10):
    A = int(input()) % 42
    if A not in left_list:
        cnt += 1
    left_list. append(A)

print(cnt)