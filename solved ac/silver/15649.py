import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, lst):
    if n == M:  # M개로 이루어진 수열을 완성했을때, n단계 == M단계가 됐을 떄
        ans.append(lst)
        return

    for j in range(1, N + 1):
        if not visited[j]:
            visited[j] = True
            dfs(
                n + 1, lst + [j]
            )  # 1차원 배열끼리 연결한다. 예를들어 이전 lst에 [1]이 있었다면 다음 [2]를 추가해줄 경우 [1,2]가 된다.
            visited[j] = False


N, M = map(int, input().split())
ans = []
visited = [False] * (N + 1)

dfs(0, [])

for lst in ans:
    print(*lst)
