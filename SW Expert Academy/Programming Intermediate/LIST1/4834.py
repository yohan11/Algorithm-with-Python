T = int(input())
for test in range(1, T+1):
    N = int(input())
    data = list(map(int, list(input())))
    dataKey = set(data)  # 중복되지 않는 집합형으로 바꿔준다
    dataD = {}
    count = 0
    for i in dataKey:
        dataD[i] = 0
    for number in data:
        if number in dataD.keys():
            dataD[number] += 1
    count = max(dataD.values())
    for key, value in dataD.items():
        if value == count:
            maxK = key
    print("#%d %d %d" % (test, maxK, count))
    data.clear()
