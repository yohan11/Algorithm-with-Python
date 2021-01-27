T = int(input())

LISTN = []
for test_case in range(1, T + 1):
    N = int(input())
    LISTN = list(map(int, input().split()))
    answer = max(LISTN)-min(LISTN)
    print("#%d %d" % (test_case, answer))
    LISTN.clear()
