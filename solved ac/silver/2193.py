# n = int(input())

# dp = [1] * (n + 1)

# if n >= 3:
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n])

## 아래가 정석적인 풀이방법임
# 이전의 0, 1 개수를 사용
n = int(input())

dp = [[0] * 2 for _ in range(n + 1)]

dp[1] = [0, 1]

for i in range(2, n + 1):
    dp[i][0] += dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] += dp[i - 1][0]

print(sum(dp[n]))
