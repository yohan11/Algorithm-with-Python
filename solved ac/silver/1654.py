import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lan_list = []

for _ in range(K):
    lan = int(input())
    lan_list.append(lan)

lan_list = sorted(lan_list)
start, end = 1, max(lan_list)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for lan in lan_list:
        if mid <= lan:
            sum += lan // mid
    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
