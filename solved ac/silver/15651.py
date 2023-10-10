import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, lst):
    global answer
    if n == M:
        answer.append(lst)
        return

    for j in range(1, N + 1):
        dfs(n + 1, lst + [j])


N, M = map(int, input().split())
answer = []
dfs(0, [])

for lst in answer:
    for num in lst:
        print(num, end=" ")
    print()
