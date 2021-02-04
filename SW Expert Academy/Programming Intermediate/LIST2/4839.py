#쪽수 
T = int(input())

for TC in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    result = []
    
    for game in range(0, 2):
        l = 1
        cnt = 0
        start, end = l, P
        if game == 0:
            page = Pa
        else:
            page = Pb
        while l <= P:
            mid = int((start+end)//2)
            if mid == page:
                break
            elif mid > page:
                end = mid
                cnt += 1
            elif mid < page:
                start = mid
                cnt += 1
        result.append(cnt)
    if result[0] < result[1]:
        print("#%d A" % (TC))
    elif result[0] > result[1]:
        print("#%d B" % (TC))
    elif result[0] == result[1]:
        print("0")
