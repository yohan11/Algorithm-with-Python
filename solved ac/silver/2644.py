import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx, count):
    global visited, graph, y, answer
    visited[idx] = True

    if idx == y:
        answer = count
        return 0

    for i in graph[idx]:
        if not visited[i]:
            dfs(i, count + 1)  # 전달받은 이전 단계의 촌수에 1을 더해서 넘겨준다


n = int(input())
x, y = map(int, input().split())
m = int(input())
max = 100 + 10
answer = -1

visited = [False] * max
graph = [[] for _ in range(max)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

# dfs 함수에 촌수를 세주는 count를 함께 매개변수로 전달해준다.
dfs(x, 0)

print(answer)
