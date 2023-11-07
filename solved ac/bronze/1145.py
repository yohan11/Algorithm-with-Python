def find_lcm(a, b, c):
    lcm = 0
    while True:
        lcm += 1
        if lcm % a == 0 and lcm % b == 0 and lcm % c == 0:
            return lcm


num_list = sorted(map(int, input().split()))
answer_list = []

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            answer_list.append(find_lcm(num_list[i], num_list[j], num_list[k]))

print(min(answer_list))

## 또다른 방법
# num_list = list(map(int, input().split()))

# lcm = min(num_list)
# cnt = 0
# while True:
#     cnt = 0
#     for i in range(len(num_list)):
#         if lcm % num_list[i] == 0:
#             cnt += 1
#     if cnt >= 3:
#         print(lcm)
#         break
#     lcm += 1
