import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [1, -1, 0, 0]
dirX = [0, 0, 1, -1]


def dfs(y, x):
    global visited, graph

    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


MAX = 1000 + 10
visited = [[False] * MAX for _ in range(MAX)]
graph = [[False] * MAX for _ in range(MAX)]

answer = 0
N, M = map(int, input().split())

for i in range(1, N + 1):
    row = input()
    for j in range(1, M + 1):
        graph[i][j] = True if row[j - 1] == "0" else False

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if graph[i][j] and not visited[i][j]:
            dfs(i, j)
            answer += 1

print(answer)
