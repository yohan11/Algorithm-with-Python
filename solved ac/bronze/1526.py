N = int(input())
num_list = [1, 2, 3, 5, 6, 8, 9, 0]
answer_list = []

for i in range(1, N + 1):
    flag = True
    for num in num_list:
        if str(num) in str(i):
            flag = False
    if flag:
        answer_list.append(i)

print(max(answer_list))
