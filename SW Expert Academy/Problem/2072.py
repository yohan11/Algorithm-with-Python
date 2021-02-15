#홀수만 더하기

T = int(input())

for TC in range(1, T+1):
    num = list(map(int, input().split()))
    sumNum = []
    sum = 0
    for i in range(10):
        if num[i] % 2 == 1:
            sumNum.append(num[i])
    for i in sumNum:
        sum += i
    print(f"#{TC} {sum}")
