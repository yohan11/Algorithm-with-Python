N, K = map(int, input().split())

num_list = list(map(int, input().split()))
sum_list = [0] * N
# res_list = [0] * N --> max 처리해줄 때 빈 공간의 0을 인식해버림
res_list = [0] * (N - K + 1)
sum_list[0] = num_list[0]
for i in range(1, N):
    sum_list[i] = sum_list[i - 1] + num_list[i]

for i in range(N - K + 1):
    if i == 0:
        res_list[i] = sum_list[i + (K - 1)]
    else:
        res_list[i] = sum_list[i + (K - 1)] - sum_list[i - 1]


print(max(res_list))

# 2개의합
# 1,2 -> sum_list[1]
# 2,3->sum_list[2]-sum_list[0]
# 3,4->sum_list[3]-sum_list[1]
# 4,5

# 3개의합
# 1,2,3 -> sum_list[2]
# 2,3,4 -> sum_list[3]-sum_list[0]
# 3,4,5 -> sum_list[4]-sum_list[1]
