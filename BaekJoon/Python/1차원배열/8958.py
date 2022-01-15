for _ in range(int(input())):
    ox_list = [x for x in input()]
    sum = 0
    strike = 0
    for i in ox_list:
        if i == 'O':
            strike += 1
            sum += strike
        else:
            strike = 0
    
    print(sum)