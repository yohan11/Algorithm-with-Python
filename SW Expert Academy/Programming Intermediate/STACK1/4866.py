#괄호검사
T = int(input())

for TC in range(1, T+1):
    data = input()
    stack = []
    for i in range(len(data)):
        if data[i] == "(" or data[i] == "{" or data[i] == "[":
            stack.append(data[i])
        elif data[i] == ")" or data[i] == "}" or data[i] == "]":
            if len(stack) == 0:
                stack = [data[i]]
                break
            elif data[i] == ")" and stack[-1] != "(" or data[i] == "}" and stack[-1] != "{" or data[i] == "]" and stack[-1] != "[":
                stack = [data[i]]
                break
            else:
                stack.pop()
    if not len(stack):
        print("#%d 1" % (TC))
    else:
        print("#%d 0" % (TC))
