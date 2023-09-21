n = int(input())

dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n] % 10007)


## 재귀함수로 풀었을 때 -> 런타임에러

# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)


# n = int(input())

# print(fibo(n) % 10007)
