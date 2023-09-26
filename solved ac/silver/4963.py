import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상,하,좌,우,대각선을 모두 탐색하기 위한 좌표 세트 설정
dirY = [-1, -1, 0, 1, 1, 1, 0, -1]
dirX = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(y, x):
    global visited, graph
    visited[y][x] = True

    for i in range(8):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)


while True:
    w, h = map(int, input().split())
    max = 50 + 10
    if w == 0 and h == 0:
        break

    visited = [[False] * max for _ in range(max)]
    graph = [[False] * max for _ in range(max)]

    answer = 0

    for i in range(1, h + 1):
        row = list(map(int, input().split()))
        for j in range(1, w + 1):
            graph[i][j] = row[j - 1] == 1

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if not visited[i][j] and graph[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)
