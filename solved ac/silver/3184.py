import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global visited, graph, wolf, sheep
    visited[y][x] = True
    if graph[y][x] == "o":
        sheep += 1
    elif graph[y][x] == "v":
        wolf += 1

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX] != False and not visited[newY][newX]:
            dfs(newY, newX)


R, C = map(int, input().split())
max = 250 + 10
graph = [[False] * max for _ in range(max)]
visited = [[False] * max for _ in range(max)]

for i in range(1, R + 1):
    row = input()
    for j in range(1, C + 1):
        if row[j - 1] == ".":
            graph[i][j] = True
        elif row[j - 1] == "#":
            graph[i][j] = False
        else:
            graph[i][j] = row[j - 1]

answer = 0

wolf_result = 0
sheep_result = 0

for i in range(1, R + 1):
    for j in range(1, C + 1):
        if graph[i][j] != False and not visited[i][j]:
            wolf = 0
            sheep = 0
            dfs(i, j)
            if wolf >= sheep:
                wolf_result += wolf
            else:
                sheep_result += sheep

print(sheep_result, wolf_result)
