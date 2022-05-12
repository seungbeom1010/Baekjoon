for i in range(1, int(input()) + 1):

    A = [int(x) for x in input().split()]

    print('Case #' + str(i) + ': ' + str(A[0]) + ' + ' + str(A[1]) + ' = ' + str(sum(A)))