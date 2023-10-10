import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global graph, visited, cnt
    visited[y][x] = True
    # 한 덩이에 몇개 있는지 셀 때
    cnt += 1
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


n, m = map(int, input().split())

MAX = 500 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, m + 1):
        graph[i][j] = row[j - 1] == 1
answer = 0
count_list = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            answer += 1
            count_list.append(cnt)


print(answer)
print(max(count_list) if count_list else 0)
