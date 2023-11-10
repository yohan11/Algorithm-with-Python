def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 남은 k가 있다면 뒤에서부터 제거
    stack = stack[:-k] if k > 0 else stack

    answer = "".join(stack)
    return answer


# def solution(number, k):
#     answer = ''
#     num_list = []
#     answer_list = []
#     for n in number:
#         num_list.append(int(n))

#     remove_count = 0
#     MAX = max(num_list)
#     MAX_idx = num_list.index(MAX)
#     while remove_count<k:

#         if len(num_list[:MAX_idx]) > k-remove_count:
#             MAX -= 1
#             if MAX in num_list:
#                 MAX_idx = num_list.index(MAX)
#         else:
#                 remove_count+=len(num_list[:MAX_idx])
#                 num_list = num_list[MAX_idx:]
#                 for num in num_list:
#                     if num==MAX:
#                         answer_list.append(str(num))
#                         num_list.remove(num)
#                         break
#                 if num_list:
#                     MAX = max(num_list)
#                     MAX_idx = num_list.index(MAX)
#     if num_list:
#         for num in num_list:
#             answer_list.append(str(num))
#     answer = "".join(answer_list)
#     return answer
