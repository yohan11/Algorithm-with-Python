CL = int(input())  # 스위치의 갯수
SL = list(map(int, input().split()))  # 스위치의 상태
SL.insert(0, 0)
CS = int(input())  # 학생수
for i in range(CS):
    sex, num = map(int, input().split())
    if sex == 1:
        CN = []  # 바꿀 인덱스 리스트
        for a in range(1, CL+1):
            if a % num == 0:
                CN.append(a)
        for n in CN:
            if SL[n] == 0:
                SL[n] = 1
            else:
                SL[n] = 0
    if sex == 2:
        CN = []
        for a in range(1, CL//2+1):
            if SL[num+a] == SL[num-a]:
                if num+a >= 0 and num - a >= 0:
                    CN.append(num+a)
                    CN.append(num-a)
                    CN.append(num)
            elif SL[num+1] != SL[num-1]:
                CN.append(num)
        CN = set(CN)
        for n in CN:
            if n >= 0:
                if SL[n] == 0:
                    SL[n] = 1
                else:
                    SL[n] = 0
SL.pop(0)
for light in SL:
    print(light, end=" ")

#런타임 에러!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
