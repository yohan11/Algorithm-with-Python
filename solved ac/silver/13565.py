import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global visited, graph, answer, N
    visited[y][x] = True

    # 현재 도달한 y축(세로 층)이 마지막 줄(층)일 경우 answer을 True로 변경
    if y == N:
        answer = True
        return

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)


N, M = map(int, input().split())
MAX = 1000 + 10
visited = [[False] * MAX for _ in range(MAX)]
graph = [[False] * MAX for _ in range(MAX)]

for i in range(1, N + 1):
    row = input()
    for j in range(1, M + 1):
        # 문제풀이의 편의성을 위해 중요한 부분(전류가 흐르는 부분)을 1로 변환하여 저장해준다.
        graph[i][j] = int(row[j - 1]) == 0

answer = False

for j in range(1, M + 1):
    # 첫번째 줄에서 시작한 탐색이 마지막 줄까지 도달할 수 있는 지를 보는 것이기 때문에 [1][j]에 대한 탐색을 한다.
    if graph[1][j]:
        dfs(1, j)

print("YES" if answer else "NO")
