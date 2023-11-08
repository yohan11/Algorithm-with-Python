# from collections import deque

# N = int(input())
# X = deque(sorted(list(map(int, input().split()))))
# answer = []

# while True:
#     if len(X) < X[-1]:
#         break

#     group = []
#     for j in range(X[0]):
#         group.append(X.popleft())
#     answer.append(group)

# print(len(answer))


N = int(input())
X = sorted(list(map(int, input().split())))

answer = 0
member = 0

for i in X:
    member += 1
    if member >= i:
        answer += 1
        member = 0
print(answer)
