import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, lst):
    global num_list, answer_list
    if n == M:
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return
        answer_list.append(lst)
        return

    prev = 0
    for j in range(N):
        if prev != num_list[j]:
            prev = num_list[j]
            dfs(n + 1, lst + [num_list[j]])


N, M = map(int, input().split())
num_list = sorted(map(int, input().split()))

answer_list = []
dfs(0, [])

for lst in answer_list:
    print(*lst)
