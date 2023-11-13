from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            newX = x + dirX[i]
            newY = y + dirY[i]
            if newX < 0 or newX >= n or newY < 0 or newY >= m:
                continue
            if graph[newX][newY] == 0:
                continue
            if graph[newX][newY] == 1:
                graph[newX][newY] = graph[x][y] + 1
                queue.append((newX, newY))
    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dirX = [-1, 1, 0, 0]
dirY = [0, 0, -1, 1]

print(bfs(0, 0))
