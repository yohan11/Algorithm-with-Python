import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]


def dfs(y, x):
    global visited, graph
    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)


n = int(input())
MAX = 100 + 10
answer_list = []

map_ = [[0] * MAX for _ in range(MAX)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        map_[i][j] = row[j - 1]

# 2 / 1 1 / 1 1 이라는 값을 주었을 때 정답은 1이지만 출력은 0인 반례가 발생한다.
# 높이가 0일 때 부터 순회해주어야 한다.
for rain_height in range(0, 101):
    answer = 0
    visited = [[False] * MAX for _ in range(MAX)]
    graph = [[False] * MAX for _ in range(MAX)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = map_[i][j] > rain_height

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not visited[i][j] and graph[i][j]:
                dfs(i, j)
                answer += 1
    answer_list.append(answer)

# 입력값의 최대를 저장해놓은 max 변수와 겹쳐서 문제 발생, 다른 이름으로 변수명을 지어줄 것
print(max(answer_list))
