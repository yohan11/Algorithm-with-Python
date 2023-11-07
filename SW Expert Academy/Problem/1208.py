
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, 10 + 1):
    answer = 0
    n = int(input())
    h_list = list(map(int,input().split()))
    
    for i in range(n):
        if max(h_list) - min(h_list) <= 1:
            break
        else:
            MAX = max(h_list)
            MIN = min(h_list)
            max_idx = h_list.index(MAX)
            min_idx = h_list.index(MIN)
            h_list[max_idx] -= 1
            h_list[min_idx] += 1
    answer = max(h_list) - min(h_list)