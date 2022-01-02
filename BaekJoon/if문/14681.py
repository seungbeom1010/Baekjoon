xy_v = []

for i in range(2):
    xy_v.append(int(input()))

if xy_v[0] > 0 and xy_v[1] > 0:
    print(1)
elif xy_v[0] < 0 and xy_v[1] > 0:
    print(2)
elif xy_v[0] < 0 and xy_v[1] < 0:
    print(3)
else:
    print(4)
