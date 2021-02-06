T = int(input())

for TC in range(1, T+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    else:
        result = 0
    print("#%d %d" % (TC, result))
