# 탐색의 대상을 "거리"로 설정해야한다.
import sys

input = sys.stdin.readline


def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]  # 현재 집의 좌표
        count = 1  # 공유기 갯수

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]
        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


N, C = map(int, input().split())

home = []

for _ in range(N):
    home.append(int(input()))

home = sorted(home)

start, end = 1, home[-1] - home[0]  # 거리의 최소, 최대값

answer = 0

binary_search(home, start, end)

print(answer)
