# n은 행
def dfs(n):
    global answer
    if n == N:
        answer += 1
        return
    for j in range(N):
        if v1[j] == v2[n + j] == v3[n - j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j] = 0


N = int(input())

answer = 0
v1 = [0] * N  # 열 정보(퀸이 놓인 세로줄에 오지 않도록)
v2 = [0] * (2 * N)  # i+j 정보 (퀸이 놓인 오른쪽 아래 대각선 줄에 오지 않도록), 2n - 1 개 (마지막 좌표가 n,n이므로 n+n)
v3 = [0] * (2 * N)  # i-j 정보 (퀸이 놓인 왼쪽 아래 대각선 줄에 오지 않도록),                      "
dfs(0)
print(answer)
