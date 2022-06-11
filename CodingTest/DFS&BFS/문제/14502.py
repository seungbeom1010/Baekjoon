n, m = map(int, input().split())
src = []
for _ in range(n):
	src.append(list(map(int, input())))
answer = 0


# def wall_map(x, y):


def virus_map(x, y, sign):
	if x < 0 or x > n:
		return 0
	if y < 0 or y > m:
		return 0

	if map[x][y] == '2':
		sign = 1
	if map[x][y] == '0' and sign == 1:
		map[x][y] = 2
		virus_map(x - 1, y, sign)
		virus_map(x, y - 1, sign)
		virus_map(x + 1, y, sign)
		virus_map(x, y + 1, sign)

def count_zero(map):
	count = 0

	for i in range(n):
		for j in range(m):
			if map[n][m] == '0':
				count += 1
	
	return count




print(count_zero())
