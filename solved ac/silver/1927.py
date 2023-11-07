from queue import PriorityQueue
import sys

input = sys.stdin.readline
N = int(input())
hq = PriorityQueue()

for _ in range(N):
    x = int(input())
    if x == 0:
        if hq.empty():
            print(0)
        else:
            print(hq.get())
    else:
        hq.put(x)
