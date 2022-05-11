
def drawingStars(n):

    if n == 1:
        return '*'
    
    else:
        Stars = drawingStars(n // 3)
        R = []

        for S in Stars:
            R.append(S * 3)
        
        for S in Stars:
            R.append(S + ' ' * (n // 3) + S)
        
        for S in Stars:
            R.append(S * 3)
        
        return R
    
print('\n'.join(drawingStars(int(input()))))
