N = int(input())
students = sorted(list(map(int, input().split())))
groups = []
answer_list = []
start, end = 0, len(students) - 1

while start <= end:
    group = [students[start], students[end]]
    groups.append(group)
    start += 1
    end -= 1

for group in groups:
    sum = 0
    for s in group:
        sum += s
    answer_list.append(sum)

print(min(answer_list))
