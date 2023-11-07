from collections import deque

N = int(input())
X = deque(sorted(list(map(int, input().split()))))
answer = []

while True:
    if len(X) < X[-1]:
        break

    group = []
    for j in range(X[0]):
        group.append(X.popleft())
    answer.append(group)

print(len(answer))
