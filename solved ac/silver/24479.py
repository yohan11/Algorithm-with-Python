import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph, answer, order
    order += 1
    visited[idx] = True
    answer[idx] = order

    for i in graph[idx]:  # 간선에 포함되는 애들만 동적으로 배열을 만들어주었기 때문에 그래프 안에 있는 애들을 꺼내와서 씀
        if not visited[i]:
            dfs(i)


n, m, r = map(int, input().split())
max = 100000 + 10

# 정적으로 배열을 만들기에는 Max가 10만개이므로 공간낭비이다.
# 동적으로 배열을 만들어주는 것이 필요하다.
visited = [False] * (max)
graph = [[] for _ in range(n + 1)]  # 그래프 정보를 동적으로 채워주기 위함
answer = [0] * max
order = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)  # 그래프 정보를 동적으로 채워줌
    graph[y].append(x)

# 그래프가 오름차순으로 탐색하기 때문에 동적으로 채운 배열을 정렬해준다.
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

dfs(r)

for i in range(1, n + 1):
    print(answer[i])
