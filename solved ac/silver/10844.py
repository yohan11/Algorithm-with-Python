n = int(input())

# 2차원 배열로 만들어서 각 계단 수 별 자릿수의 갯수가 몇개인지 저장한다.
dp = [[0] * 12 for _ in range(n + 1)]
dp[1][2:11] = [1] * 9

# i는 계단 수, j는 자릿수
# 숫자 m의 갯수를 알려면 이전 계단의 m+1, m-1의 갯수를 세면 된다.
# 가지치기 그림 형식으로 이해할 것
for i in range(2, n + 1):
    for j in range(1, 11):
        dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]

print(sum(dp[n]) % 1000000000)
