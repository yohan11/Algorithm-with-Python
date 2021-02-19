#시각 

T = int(input())

for TC in range(1, T+1):
    hour1, min1, hour2, min2 = map(int, input().split())
    hour = (hour1+hour2) % 12
    min = min1+min2
    if min >= 60:
        hour += min//60
        min = min % 60

    print(f"#{TC} {hour} {min}")
