n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        # 예를 들어 n=3인 경우 00x ~ 09x 까지 모두 고려해야한다.
        # 규칙성 찾는 과정에서 생략하지말고 모든 케이스를 정확하게 세워보자.
        dp[i][j] = sum(dp[i - 1][j:])

print(sum(dp[n]) % 10007)
