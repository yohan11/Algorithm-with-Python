# 백트래킹 문제로 접근해서 모든 경우의 수 중 최소를 구하는 거라고 생각했는데, 아니었다.
# 그리디 알고리즘을 쓰는 문제로, 적은시간부터 오름차순으로 정렬하면 되는 문제였다.
N = int(input())
P = list(map(int, input().split()))

P = sorted(P)

answer = 0

for i in range(N):
    answer += sum(P[: i + 1])

print(answer)
