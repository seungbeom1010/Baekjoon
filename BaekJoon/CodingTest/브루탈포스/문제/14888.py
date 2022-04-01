from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
sign_num = list(map(int, input().split()))
signs = ['+', '-', '*', '/']
sign_list = ''
for i in range(4):
	sign_list += sign_num[i] * signs[i]

max_num = -1000000000
min_num = 1000000000
current_value = num_list[0]
for temp in list(set(permutations(sign_list))):
	for i in range(1, n):
		if temp[i - 1] == '+':
			current_value += num_list[i]
		elif temp[i - 1] == '-':
			current_value -= num_list[i]
		elif temp[i - 1] == '*':
			current_value *= num_list[i]
		elif temp[i - 1] == '/':
			current_value = int(current_value / num_list[i])
	if max_num < current_value:
		max_num = current_value
	if min_num > current_value:
		min_num = current_value
	current_value = num_list[0]

print(max_num, min_num, sep="\n")