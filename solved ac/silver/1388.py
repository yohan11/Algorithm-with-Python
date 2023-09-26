import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):
    global visited, graph
    visited[y][x] = True

    # 나도 세로/가로 장식이고, 나와 인접한 다음도 세로/가로 장식일 경우에만 dfs를 돌리겠다.
    if graph[y][x] == "-" and graph[y][x + 1] == "-":
        dfs(y, x + 1)
    if graph[y][x] == "|" and graph[y + 1][x] == "|":
        dfs(y + 1, x)


n, m = map(int, input().split())
max = 50 + 10
visited = [[False] * max for _ in range(max)]
# 그래프에 존재하는지가 아니라 모양이 -, | 인지가 중요하므로
graph = [[""] * max for _ in range(max)]

for i in range(1, n + 1):
    row = input()
    for j in range(1, m + 1):
        graph[i][j] = row[j - 1]

answer = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not visited[i][j]:
            dfs(i, j)
            answer += 1

print(answer)
