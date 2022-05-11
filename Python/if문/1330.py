# 첫째 줄에 다음 세 가지 중 하나를 출력한다.

# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.

n = list(map(int, input().split()))

if n[0] > n[1]:
    print(">")
elif n[0] < n[1]:
    print("<")
else:
    print("==")