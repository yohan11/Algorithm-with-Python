# '-' 이후에 '+'가 나오면 '-' 뒤에 괄호를 쳤을 때 뒤에 값들의 합이 음수로 변하기 때문에 값이 작아지게 된다.
# '-'를 기준으로 전체 식을 나눠서 괄호를 친다.

original_exp = input()
exp_list = original_exp.split("-")
sum_list = []
for i in exp_list:
    n_lst = i.split("+")
    sum = 0
    for n in n_lst:
        sum += int(n)
    sum_list.append(sum)

res = sum_list[0]

for n in range(1, len(sum_list)):
    res -= sum_list[n]

print(res)
