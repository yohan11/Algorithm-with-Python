#반복문자 지우기
T = int(input())

for TC in range(1, T+1):
    data = list(input())
    stack = []
    for i in range(len(data)):
        if not len(stack) or data[i] != stack[-1]:
            stack.append(data[i])
        elif data[i] == stack[-1]:
            stack.pop()

    print("#%d %d" % (TC, len(stack)))
