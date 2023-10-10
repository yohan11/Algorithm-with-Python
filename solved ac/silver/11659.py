# 누적 합 문제
# 배열의 [ A ~ B ] 범위의 구간 합을 구하고자 할 때, 누적합 배열을 구한 후 B 까지의 누적합에서 A-1까지의 누적합을 빼주면 [ A ~ B] 범위의 구간의 합을 구할 수 있습니다.
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0] * N
sum_list[0] = num_list[0]
for i in range(1, N):
    sum_list[i] = sum_list[i - 1] + num_list[i]


for _ in range(M):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    if x == 0:
        answer = sum_list[y]
    else:
        answer = sum_list[y] - sum_list[x - 1]
    print(answer)
