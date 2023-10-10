# 모든 리프노드(마지막 노드)에서 부터 루트노드까지의 거리를 합산한 것이 홀수면 성원이가 이긴다.

import sys

sys.setrecursionlimit(600000)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            # 노드에서 루트노드까지의 거리를 구하는 공식
            depth[i] = depth[idx] + 1
            dfs(i)


N = int(input())
MAX = 500000 + 10

visited = [False] * MAX
graph = [[] for _ in range(N + 1)]
depth = [0] * (MAX)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

# 이 노드가 리프노드인 경우에만 count
for i in range(2, N + 1):
    if len(graph[i]) != 1:
        depth[i] = 0

# print(depth)
print("No" if sum(depth) % 2 == 0 else "Yes")
