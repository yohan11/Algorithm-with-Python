T = int(input())

for _ in range(T):
    row = input()
    answer = 0
    if row[0] == "O":
        answer += 1
    part_answer = answer
    for i in range(1, len(row)):
        if row[i] == "O" and row[i - 1] == "O":
            part_answer = part_answer + 1
        if row[i] == "X":
            part_answer = 0
        if row[i] == "O" and row[i - 1] == "X":
            part_answer = 1
        answer += part_answer

    print(answer)


# n = int(input())

# for _ in range(n):
#     ox_list = list(input())
#     score = 0
#     sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
#     for ox in ox_list:
#         if ox == "O":
#             score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
#             sum_score += score  # sum_score = sum_score + score
#         else:
#             score = 0
#     print(sum_score)
