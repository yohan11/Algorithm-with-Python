N = int(input())
N = 1000 - N
answer_list = [0] * 6
jandon_list = [500, 100, 50, 10, 5, 1]

for i in range(len(jandon_list)):
    if N == 0:
        break
    answer_list[i] = N // jandon_list[i]
    N = N % jandon_list[i]

print(sum(answer_list))
