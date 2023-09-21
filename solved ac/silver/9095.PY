T = int(input())
for c in range(T):
    n = int(input())

    # 어차피 테스트케이스가 11까지이므로 배열 길이를 정해줌 -> 인덱스에러 방지
    dp = [1] * 12

    dp[1], dp[2], dp[3] = 1, 2, 4

    if n >= 4:
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])

# 2, 3을 1+1, 1+2와 같이 쪼개서 더하는 케이스를 고려할 필요가 없다 -> 어차피 중복됨
