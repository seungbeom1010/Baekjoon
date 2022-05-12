# n, m = map(int, input().split())
# L = list(map(int, input().split()))

# result = 0

# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             temp = L[i] + L[j] + L[k]
#             if temp <= m and temp > result:
#                 result = temp

# print(result)


from itertools import *

n, m = map(int, input().split())

cards = list(map(int, input().split()))

comb = combinations(cards, 3)

result = 0
for i in comb:
    if sum(i) <= m and sum(i) > result:
        result = sum(i)
print(result)