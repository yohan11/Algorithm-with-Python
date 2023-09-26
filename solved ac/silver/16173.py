import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [0, 1]
dirX = [1, 0]


def dfs(y, x):
    global visited, graph, n
    visited[y][x] = True

    # 맨 끝칸(n,n)에 도당하면, 즉 visited가 True가 되면 성공
    if y == n and x == n:
        return

    # 아래, 오른쪽으로만 이동하므로 2번 반복
    for i in range(2):
        newY = y + dirY[i] * graph[y][x]
        newX = x + dirX[i] * graph[y][x]
        if not visited[newY][newX]:
            dfs(newY, newX)


n = int(input())
# 최대 몇칸 이동할 수 있는지도 고려해주어야한다.
max = 3 + 100 + 10

visited = [[False] * (max) for _ in range(max)]
graph = [[0] * (max) for _ in range(max)]


for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        graph[i][j] = row[j - 1]


# 맨 첫번째 칸에서 출발하므로
dfs(1, 1)

print("HaruHaru" if visited[n][n] else "Hing")
