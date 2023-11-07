L, P, V = map(int, input().split())
cnt = 0
while True:
    if L == 0 and P == 0 and V == 0:
        break
    cnt += 1
    a = V // P  # 휴가 중 연속되는 날짜 로테이션 수
    V = V % P
    if V > L:
        res = a * L + L
    else:
        res = a * L + V
    print(f"Case {cnt}: {res}")
    L, P, V = map(int, input().split())

# 반례: 5 15 40
# 40의 경우 15로 두번 나누고 10이 남는데, 이때 10을 그대로 더해주면 틀린 답, 10일 중에서도 5일만 사용
