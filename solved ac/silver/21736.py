import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global visited, graph, cnt

    # visited 처리해주는 부분, 순서 유의, 감이 안잡힐때는 print로 찍어서 확인해보기
    if graph[y][x] == "P" and not visited[y][x]:
        cnt += 1

    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)


N, M = map(int, input().split())
MAX = 600 + 10
visited = [[False] * MAX for _ in range(MAX)]
graph = [[False] * MAX for _ in range(MAX)]

for i in range(1, N + 1):
    row = input()
    for j in range(1, M + 1):
        if row[j - 1] == "X":
            graph[i][j] = False
        elif row[j - 1] == "O":
            graph[i][j] = True
        else:
            graph[i][j] = row[j - 1]
cnt = 0
targetY, targetX = 0, 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if graph[i][j] == "I":
            targetY = i
            targetX = j


dfs(targetY, targetX)

print("TT" if cnt == 0 else cnt)
