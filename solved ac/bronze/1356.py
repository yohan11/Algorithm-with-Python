def find_multiple(lst):
    result = 1
    for n in lst:
        result *= int(n)
    return result


N = int(input())
answer_list = []
flag = False

for i in range(1, len(str(N))):
    front = str(N)[:i]
    back = str(N)[i:]
    front_res = find_multiple(front)
    back_res = find_multiple(back)
    if front_res == back_res:
        flag = True
        break

print("YES" if flag else "NO")
