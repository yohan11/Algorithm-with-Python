import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, lst):
    global visited, answer

    # 종료조건
    if len(lst) == M:
        for num in range(1, M):
            if lst[num] < lst[num - 1]:
                return
        answer.append(lst)
        return

    # 하부함수 호출
    for j in range(1, N + 1):
        if not visited[j]:
            visited[j] = True
            dfs(j, lst + [j])
            visited[j] = False


N, M = map(int, input().split())
visited = [False] * (N + 1)
answer = []
dfs(1, [])

for i in answer:
    for j in i:
        print(j, end=" ")
    print()
