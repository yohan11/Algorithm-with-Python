import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, lst):
    global visited, num_list, answer_list
    if n == M:
        answer_list.append(lst)
        return
    prev = 0
    for j in range(N):
        if not visited[j] and prev != num_list[j]:
            # 예를 들어 이전 단계에서 7 9 라는 수열을 만들었으면 다음 단계의 7로 시작하는 수열에서 9를 다시 사용하지 않도록
            prev = num_list[j]
            visited[j] = True
            dfs(n + 1, lst + [num_list[j]])
            visited[j] = False


N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

MAX = 10000 + 10
visited = [False] * MAX

answer_list = []

dfs(0, [])

for lst in answer_list:
    print(*lst)
