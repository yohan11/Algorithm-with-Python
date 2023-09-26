import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph, answer
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            answer[i] = idx
            dfs(i)


n = int(input())
max = 100000 + 10
visited = [False] * max
graph = [[] for _ in range(max)]
answer = [0] * max

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

dfs(1)

for i in range(2, n + 1):
    print(answer[i])
