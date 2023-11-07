## 시간초과가 뜬 답안.
## 해결법
# x축을 0부터 이동하며 현재 x에서 점이 몇 개 찍히는 지를 구해주면 된다.
# 전체 거리 d의 제곱 = x 좌표 제곱 + y 좌표 제곱 이므로
# d에서 현재 x좌표 제곱만큼을 먼저 빼준다면 y좌표 제곱의 최대 크기가 나온다.
# 이걸 k로 나눠준 후(최종 좌표는 b*k이므로) +1 (0을 생각해서) 해주면 된다.
import math

def solution(k, d):
    answer = 0
    ground = []
    x,y = 0,0

    for i in range((d//k)+1):
        x= i*k
        for j in range((d//k)+1):
            y = j*k
            if math.sqrt(x**2+y**2)<=d:
                ground.append((x,y))
    answer = len(set(ground))

    return answer

## 최종 답안
# import math
# def solution(k, d):
#     answer = 0
#     # x 기준으로 세기
#     for x in range(0, d + 1, k):
#         res_d = math.floor(math.sqrt(d*d - x*x))
#         answer += (res_d // k) + 1
#     return answer 