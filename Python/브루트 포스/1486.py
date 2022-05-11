N = int(input())

start = 666

while True:
    if '666' in str(start):
        N -= 1
        if N == 0:
            break
    
    start += 1

print(start)