s = input()
p = input()

answer = 0
idx = 0

while idx < len(p):
    new_p = ""

    if p[idx:] in s:
        answer += 1
        break
    for i in range(idx, len(p)):
        new_p += p[i]

        if new_p not in s:
            answer += 1
            idx = i
            break
print(answer)
