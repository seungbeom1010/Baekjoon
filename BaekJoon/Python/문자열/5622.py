croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()

for i in croa:
    a = a.replace(i, '*')

print(len(a))