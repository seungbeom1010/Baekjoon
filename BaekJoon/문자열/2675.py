for _ in range(int(input())):
    a, b = list(input().split())
    answer = ''
    for i in b:
        answer += i * int(a)
    
    print(answer)
        
        