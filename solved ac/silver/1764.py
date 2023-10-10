N, M = map(int, input().split())
person_dict = {}
answer_list = []

for _ in range(N + M):
    name = input()
    if name not in person_dict.keys():
        person_dict[name] = 1
    else:
        person_dict[name] += 1

for name in person_dict.keys():
    if person_dict[name] > 1:
        answer_list.append(name)

answer_list = sorted(answer_list)

print(len(answer_list))
for name in answer_list:
    print(name)
