import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, lst):
    global num_list, answer_list, visited

    if n == M:
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return
        answer_list.append(lst)
        return

    for j in num_list:
        if not visited[j]:
            visited[j] = True
            dfs(n + 1, lst + [j])
            visited[j] = False


N, M = map(int, input().split())
num_list = list(map(int, input().split()))

MAX = 10000 + 10
visited = [False] * MAX

answer_list = []

dfs(0, [])
answer_list = sorted(answer_list)

for lst in answer_list:
    print(*lst)
