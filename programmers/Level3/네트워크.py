answer = 0


def dfs(idx, visited, graph, n):
    global answer
    visited[idx] = True

    for i in range(n):
        if not visited[i] and graph[idx][i]:
            dfs(i, visited, graph, n)


def solution(n, computers):
    global answer
    MAX = 200
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [False] * MAX

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i][j] = True

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph, n)
            answer += 1

    return answer
