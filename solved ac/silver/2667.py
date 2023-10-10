import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):
    global visited, graph, count
    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)
            count += 1


dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]

n = int(input())
max = 25 + 10
visited = [[False] * max for _ in range(max)]
graph = [[False] * max for _ in range(max)]

for i in range(1, n + 1):
    row = input()
    for j in range(1, n + 1):
        graph[i][j] = int(row[j - 1]) == 1

answer = 0
count_list = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not visited[i][j] and graph[i][j]:
            count = 1
            dfs(i, j)
            count_list.append(count)
            answer += 1
print(answer)
count_list = sorted(count_list)
for i in count_list:
    print(i)
