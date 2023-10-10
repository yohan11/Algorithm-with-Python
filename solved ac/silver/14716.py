import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0, -1, -1, 1, 1]
dirX = [0, 0, -1, 1, 1, -1, -1, 1]


def dfs(y, x):
    global visited, graph
    visited[y][x] = True

    for i in range(8):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


M, N = map(int, input().split())
MAX = 250 + 10

visited = [[False] * MAX for _ in range(MAX)]
graph = [[False] * MAX for _ in range(MAX)]

for i in range(1, M + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        graph[i][j] = row[j - 1] == 1

answer = 0

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if graph[i][j] and not visited[i][j]:
            dfs(i, j)
            answer += 1

print(answer)
