import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph
    visited[idx] = True
    print(idx, end=" ")

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


def bfs():
    global graph, visited
    queue = []

    queue.append(v)
    visited[v] = True

    while queue:
        # 큐의 맨 앞에 있는 노드 뺴옴, 해당 노드에 연결되어 있는 모든 (방문하지 않은) 노드들을 큐에 추가함
        idx = queue.pop(0)
        print(idx, end=" ")
        for i in graph[idx]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
max = 1000 + 10
visited = [False] * max
graph = [[] for _ in range(max)]


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

dfs(v)
print()
visited = [False] * max
bfs()
