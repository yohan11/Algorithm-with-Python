import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global visited, graph
    visited[idx] = True

    for i in range(1, n + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


# max로 사이즈를 설정하는 이유? -> 괜한 오류나 신경쓸게 줄어든다고함,, 아직 이해는 안됨
max = 1000 + 10
visited = [False] * max
graph = [[False] * max for _ in range(max)]

n, m = map(int, input().split())
answer = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 연결된 덩어리를 찾아야하기 때문에 모든 수의 visited가 1이 될때 까지 반복해봐야함
# 모든 '덩어리'의 개수를 찾는 것이기 때문에 한번의 dfs가 시작될때 마다 answer을 추가해줌. '바이러스'문제와의 차이점
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
