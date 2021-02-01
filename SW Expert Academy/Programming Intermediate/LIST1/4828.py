#최댓값과 최솟값의 차 
T = int(input())

LISTN = []
for test_case in range(1, T + 1):
    N = int(input())
    LISTN = list(map(int, input().split()))
    answer = max(LISTN)-min(LISTN)
    print("#%d %d" % (test_case, answer))
    LISTN.clear()
#문제 풀면서 익힌것: 여백있는 입력값을 숫자 리스트로 저장 list(map(int, input().split()))
