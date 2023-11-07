N, M = map(int, input().split())
tree_list = sorted(list(map(int, input().split())))

start, end = 1, max(tree_list)

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for tree in tree_list:
        if tree >= mid:
            sum += tree - mid

    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
