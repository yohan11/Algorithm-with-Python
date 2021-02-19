#연월일 달력

T = int(input())

for TC in range(1, T+1):
    data = input()
    year =  data[0:4]
    month = int(data[4:6])
    day = int(data[6:8])
    isTrue = True
    if month > 12 or month < 1:
        isTrue = False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            isTrue = False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            isTrue = False
    else:
        if day > 28:
            isTrue = False
    if isTrue == True:
        print(f"#{TC} {year}/{data[4:6]}/{data[6:8]}")
    else:
        print(f"#{TC} -1")
