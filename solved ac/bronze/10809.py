word = input()
alpha_list = [chr(i) for i in range(97, 123)]
result_list = [0] * len(alpha_list)

for i in range(len(alpha_list)):
    if alpha_list[i] in word:
        result_list[i] = word.index(alpha_list[i])
    else:
        result_list[i] = -1

for n in result_list:
    print(n, end=" ")
