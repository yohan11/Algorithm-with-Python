# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline


# def dfs(n, lst):
#     global visited, height_list, answer_list

#     if n == 7:
#         answer_list.append(lst)
#         return
#     for j in height_list:
#         if not visited[j]:
#             visited[j] = True
#             dfs(n + 1, lst + [j])
#             visited[j] = False


# height_list = []
# for _ in range(9):
#     height = int(input())
#     height_list.append(height)

# height_list = sorted(height_list)

# answer_list = []
# visited = [False] * (100 + 10)

# dfs(0, [])

# for lst in answer_list:
#     if sum(lst) == 100:
#         for n in lst:
#             print(n)
#         break


## 진정한 브루트포스 방법으로 푸는 방법은 아래인 것 같다.
## 전체 합 중 2개를 골라 뺐을 때 100이 되면 정답.

height_list = []
for _ in range(9):
    height = int(input())
    height_list.append(height)

height_list = sorted(height_list)
targetA, targetB = 0, 0
for i in range(9):
    for j in range(i + 1, 9):
        if sum(height_list) - (height_list[i] + height_list[j]) == 100:
            targetA = height_list[i]
            targetB = height_list[j]

height_list.remove(targetA)
height_list.remove(targetB)

for n in height_list:
    print(n)
