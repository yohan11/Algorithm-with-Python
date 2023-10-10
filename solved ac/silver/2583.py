# 보류

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global visited, graph, cnt, M, N
    # 편의상 기본 값을 True로 놓고 시작하기 때문에 주어진 영역을 벗어날 경우 탈출해야한다.
    # 주어진 영역을 벗어나서도 모두 True이기 때문에 인덱스 에러 발생
    if y <= 0 or x <= 0 or y > M or x > N:
        return
    visited[y][x] = True
    cnt += 1
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


M, N, K = map(int, input().split())
max = 100 + 10

graph = [[True] * (max) for _ in range(max)]
visited = [[False] * (max) for _ in range(max)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i + 1][j + 1] = False
answer = 0
count_list = []
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if graph[i][j] and not visited[i][j]:
            answer += 1
            cnt = 0
            dfs(i, j)
            count_list.append(cnt)

print(answer)
count_list = sorted(count_list)
for c in count_list:
    print(c, end=" ")
