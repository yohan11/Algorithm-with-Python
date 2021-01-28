T = int(input())
for test in range(1, T+1):
    N = int(input())
    data = list(map(int, list(input()))) #여백없이 주어진 숫자들을 리스트에 저장하기
    maxN = max(data)
    count = 0
    for number in data:
        if number == maxN:
            count += 1
    print("#%d %d %d" % (test, maxN, count))
    data.clear()
