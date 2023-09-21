n = int(input())

dp = [1] * (n + 1)

# n==1일 경우 dp[2]의 초기값을 설정해줄 경우 에러

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + (dp[i - 2] * 2)

print(dp[n] % 10007)
