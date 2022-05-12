for _ in range(int(input())):

    A = list(map(int, input().split()))

    avg_A = sum(A[1:]) / A[0]

    cnt = 0

    for i in A[1:]:
        if i > avg_A:
            cnt += 1
    
    rate = cnt / A[0] * 100 
    
    print(f'{rate:.3f}%')