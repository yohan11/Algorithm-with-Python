#간단한 369 게임

N = int(input())
arr = []
for i in range(1, N+1):
    arr.append(i)
for i in arr:
    i = str(i)
    c = 0
    if '3' in i or '6' in i or '9' in i:
        c = i.count("3")+i.count("6")+i.count("9")
        i = "-"*c

    print(i, end=" ")
