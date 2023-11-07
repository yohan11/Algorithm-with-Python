num_list = sorted(list(map(int, input().split())))
while True:
    if -1 in num_list:
        break
    cnt = 0
    for num in num_list:
        if num * 2 in num_list:
            cnt += 1
    print(cnt - 1)
    num_list = sorted(list(map(int, input().split())))
