mush_list = []

for _ in range(10):
    mush = int(input())
    mush_list.append(mush)

answer_list = []
sum = 0
for m in range(len(mush_list)):
    sum += mush_list[m]
    answer_list.append(sum)
    if sum > 100:
        break

if abs(100 - answer_list[-1]) < abs(100 - answer_list[-2]):
    print(answer_list[-1])
elif abs(100 - answer_list[-1]) > abs(100 - answer_list[-2]):
    print(answer_list[-2])
elif abs(100 - answer_list[-1]) == abs(100 - answer_list[-2]):
    print(answer_list[-1] if answer_list[-1] > answer_list[-2] else answer_list[-2])
