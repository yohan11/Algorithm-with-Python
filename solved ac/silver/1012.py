import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# [상, 하, 좌, 우]
dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global visited, graph
    visited[y][x] = True

    # 주어진 위치의 상하좌우를 탐색해야함
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        # 다음 위치(현재의 상,하,좌,우)에 대한 탐색
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


T = int(input())
max = 50 + 10

for tc in range(T):
    M, N, K = map(int, input().split())

    visited = [[False] * max for _ in range(max)]
    graph = [[False] * max for _ in range(max)]

    for _ in range(K):
        x, y = map(int, input().split())
        # 이러한 문제 유형은 노드가 서로 연결되어 있는 것이 아니라 그래프의 어떤 위치(y,x)에 존재한다는 것 뿐이다.
        # newY, newX 값을 사용할 경우 인덱스 에러를 막기 위함이다.
        graph[y + 1][x + 1] = True
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if not visited[i][j] and graph[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)

## visited 배열을 사용하지 않는 방법

# T = int(input())

# dirY = [-1, 1, 0, 0]
# dirX = [0, 0, -1, 1]
# max = 50 + 10

# def dfs(y, x):
#     global graph
#     graph[y][x] = False

#     for i in range(4):
#         newY = y + dirY[i]
#         newX = x + dirX[i]
#         if graph[newX][newX]:
#             dfs(newY, newX)


# for tc in range(T):
#     M, N, K = map(int, input().split())


#     graph = [[False] * max for _ in range(max)]

#     answer = 0

#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[y + 1][x + 1] = True

#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             if graph[i][j]:
#                 dfs(i, j)
#                 answer += 1

#     print(answer)
