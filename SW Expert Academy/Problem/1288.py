#새로운 불면증 

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    count = {}
    c = 1
    sheep = 0
    for i in range(0, 10):
        count[f"{i}"] = 0
    while True:
        sheep = N*c
        num = list(map(int, str(sheep)))
        for i in num:
            count[f"{i}"] += 1
        c += 1
        if count["0"] > 0 and count['1'] > 0 and count['2'] > 0 and count['3'] > 0 and count['4'] > 0 and count['5'] > 0 and count['6'] > 0 and count['7'] > 0 and count['8'] > 0 and count['9'] > 0:
            break
    print(f"#{TC} {N*(c-1)}")
