#색칠하기
T = int(input())

for TC in range(1, T+1):
    red = []
    blue = []
    N = int(input())
    for area in range(1, N+1):
        x1, y1, x2, y2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if color == 1:
                    red.append((x, y))
                elif color == 2:
                    blue.append((x, y))
    red = set(red)
    blue = set(blue)
    purple = red.intersection(blue)
    print("#%d %d" % (TC, len(purple)))
