T = int(input())
for i in range(1, T+1):
    N, C = map(int, input().split())
    data = list(map(int, input().split()))
    sumData = []
    for a in range(0, N-C+1):
        sumData.append(sum(data[a:a+C])) #data의 a부터 a+C-1까지의 요소끼리 더함
    maxSum = max(sumData)
    minSum = min(sumData)
    answer = maxSum-minSum
    print("#%d %d" % (i, answer))
    data.clear()
