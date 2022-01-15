cl = input().split()

print(max([int(cl[0][::-1]), int(cl[1][::-1])]))