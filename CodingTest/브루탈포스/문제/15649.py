n, m = map(int, input().split())

temp_list = []
def get_number(n, m, temp_n, temp_list):
	if temp_n == m:
		for i in temp_list:
			print(i, end=" ")
		print()
	else:
		for i in range(1, n + 1):
			if i not in temp_list:
				temp_list_l = list(temp_list)
				temp_list_l.append(i)
				get_number(n, m, temp_n + 1, temp_list_l)


get_number(n, m, 0, temp_list)
