import sys

input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return arr[start : end + 1].count(target)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


# 딕셔너리 형태로 정답들을 저장해야 시간초과가 나지 않는다.
n_dic = {}
for n in N_list:
    start = 0
    end = len(N_list) - 1
    if n not in n_dic:
        n_dic[n] = binary_search(N_list, n, start, end)

print(" ".join(str(n_dic[x]) if x in n_dic else "0" for x in M_list))
