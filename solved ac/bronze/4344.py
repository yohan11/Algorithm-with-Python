#평균은 넘겠지
T = int(input())

for TC in range(T):
    data = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for i in range(1, data[0]+1):
        sum += data[i]
    avg = sum/data[0]
    for i in range(1, data[0]+1):
        if data[i] > avg:
            cnt += 1
    p = cnt/data[0]*100
    print(f"{round(p,3)}%")
