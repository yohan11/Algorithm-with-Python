## 메모리 초과
# import sys

# input = sys.stdin.readline

# from queue import PriorityQueue

# hq = PriorityQueue()
# N = int(input())

# for i in range(N):
#     row = list(map(int, input().split()))
#     for j in range(N):
#         hq.put(row[j])

# for _ in range((N**2) - N):
#     hq.get()

# print(hq.get())

## heapq 자료구조를 사용한 코드
# 메모리 초과를 해결해주려면 heap 리스트의 길이를 조절해주어야 한다.
# 리스트에 수를 다넣는 것이 아니라 가장 큰 수 N개만 넣어서 그중에 가장 작은 수를 찾기
import heapq

heap = []
N = int(input())

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if len(heap) < N:
            heapq.heappush(heap, row[j])
        else:
            if row[j] < heap[0]:
                pass
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, row[j])

print(heap[0])
