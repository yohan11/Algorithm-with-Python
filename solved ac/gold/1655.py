## 시간초과 -> copy를 하는 부분에서 시간초과가 남
# import sys
# import heapq

# input = sys.stdin.readline

# original_list = []
# num_list = []

# N = int(input())

# for i in range(N):
#     num = int(input())
#     heapq.heappush(num_list, num)
#     heapq.heappush(original_list, num)

#     if i == 0:
#         print(num)
#     else:
#         for _ in range(i // 2):
#             heapq.heappop(num_list)
#         print(heapq.heappop(num_list))
#     num_list = original_list.copy()

## 정답 코드
# heap 2개를 만들고, 중앙값을 기준으로 작은 수, 큰 수를 나눠서 저장한다.
# 작은 수를 담는 힙은 최대힙(내림차순)으로 구현해야하는데, 이는 원래 수에 -1을 곱해서 구현할 수 있다. -1을 곱하면 절닷값이 클수록 작으므로
# 두 힙의 길이를 비교해서, 같을 경우 왼쪽 힙에 넣고 다를 경우 오른쪽 힙에 넣어서 균형을 맞춘다,
# 작은 수 힙의 첫번째 자리에 큰 수 힙의 가장 작은 요소(첫번째 요소)보다 큰 수가 들어가있다면 서로의 첫번째 요소를 바꾼다. 단 서로의 힙에 넣을때는 -1을 곱해서!
import sys
import heapq

input = sys.stdin.readline

leftheap = []
rightheap = []

N = int(input())
for i in range(N):
    num = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)
    if len(leftheap) >= 1 and len(rightheap) >= 1:
        if (leftheap[0]) * (-1) > rightheap[0]:
            temp = leftheap[0] * (-1)
            heapq.heappop(leftheap)
            heapq.heappush(leftheap, rightheap[0] * (-1))
            heapq.heappop(rightheap)
            heapq.heappush(rightheap, temp)

    print(leftheap[0] * (-1))
