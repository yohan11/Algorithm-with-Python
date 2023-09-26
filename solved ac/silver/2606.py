def dfs(idx):
    global graph, visited, answer
    visited[idx] = True
    answer += 1

    for i in range(1, n + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


n = int(input())
m = int(input())

visited = [False] * (n + 1)
graph = [[False] * (n + 1) for _ in range(n + 1)]
answer = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 1번 컴퓨터에 연결되어있는 컴퓨터 갯수만 구함 -> 1번에 대한 dfs를 한 번 돌때 마다 answer += 1
dfs(1)

print(answer - 1)
