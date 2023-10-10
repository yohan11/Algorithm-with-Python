import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())


def dfs(n, lst):
    global answer_list
    if n == M:
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return
        answer_list.append(lst)
        return

    for j in range(1, N + 1):
        dfs(n + 1, lst + [j])


answer_list = []
dfs(0, [])

for lst in answer_list:
    print(*lst)
