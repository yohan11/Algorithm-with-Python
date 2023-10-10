import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs_B(y, x):
    global graph_B, visited, cnt_B
    visited[y][x] = True
    cnt_B += 1

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph_B[newY][newX] and not visited[newY][newX]:
            dfs_B(newY, newX)


def dfs_W(y, x):
    global graph_W, visited, cnt_W
    visited[y][x] = True
    cnt_W += 1

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph_W[newY][newX] and not visited[newY][newX]:
            dfs_W(newY, newX)


N, M = map(int, input().split())
MAX = 100 + 10

graph_B = [[False] * MAX for _ in range(MAX)]
graph_W = [[False] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]


for i in range(1, M + 1):
    row = input()
    for j in range(1, N + 1):
        graph_B[i][j] = row[j - 1] == "B"
        graph_W[i][j] = row[j - 1] == "W"

B_result = 0
W_result = 0
# B편의 위력 구하기
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if graph_B[i][j] and not visited[i][j]:
            cnt_B = 0
            dfs_B(i, j)
            B_result += cnt_B**2

# W편의 위력 구하기
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if graph_W[i][j] and not visited[i][j]:
            cnt_W = 0
            dfs_W(i, j)
            W_result += cnt_W**2

print(W_result, B_result)
