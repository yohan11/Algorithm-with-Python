#돼지
T = int(input())
for TC in range(T):
    food = int(input())
    firstDay = list(map(int, input().split()))
    count = 0
    lastDay = [0]*6
    a = True
    sum = 0
    for pig in range(0, len(firstDay)):
        if pig >= 0 and pig <= 2:
            lastDay[pig] = firstDay[pig+1] + \
                firstDay[pig-1]+firstDay[pig+3]+firstDay[pig]
        elif pig >= 3 and pig <= 4:
            lastDay[pig] = firstDay[pig+1] + \
                firstDay[pig-1]+firstDay[pig-3]+firstDay[pig]
        elif pig == 5:
            lastDay[pig] = firstDay[0]+firstDay[4]+firstDay[2]+firstDay[pig]
    while food > 0:
        for i in range(0, 6):
            if lastDay[i] > food:
                a = False
        if a == True:
            count += 1
            break
        else:
            break

    print(count+1)
