import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, sum, count):
    global answer, lst, N, S

    # 종료조건
    if n == N:
        if sum == S and count > 0:
            answer += 1
        return

    # 하부함수 호출
    # 배열에 포함시킬때
    dfs(n + 1, sum + lst[n], count + 1)
    # 배열에 포함시키지 않을때
    dfs(n + 1, sum, count)


N, S = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
dfs(0, 0, 0)
print(answer)
