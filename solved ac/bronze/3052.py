res_list = []

for _ in range(10):
    N = int(input())
    res = N % 42
    if res not in res_list:
        res_list.append(res)

print(len(res_list))
