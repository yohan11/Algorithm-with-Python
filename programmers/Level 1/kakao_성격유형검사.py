# 같은 유형의 검사지(q)가 나왔을 때 제대로 동작하지 않음, index 값 찾기와 누적합 이슈
#
# result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
# survey=["CF", "RT", "AN"]
# choices=[7, 1, 3]
# answer=''
# for q in survey:
#     score=choices[survey.index(q)]
#     if score >= 1 and score <=3:
#         key=result[q[0]]
#         if score==1:
#             key+=3
#         elif score==2:
#             key+=2
#         elif score==3:
#             key+=1
#         result[q[0]]=key
#     elif score>=5 and score<=7:
#         key=result[q[1]]
#         if score==5:
#             key+=1
#         elif score==6:
#             key+=2
#         elif score==7:
#             key+=3
#         result[q[1]]=key

# answer += 'R' if result['R']>=result['T'] else 'T'
# answer += 'C' if result['C']>=result['F'] else 'F'
# answer += 'J' if result['J']>=result['M'] else 'M'
# answer += 'A' if result['A']>=result['N'] else 'N'


# print(answer)


#수정 후 최종 답안

def solution(survey, choices):
    answer = ''
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for i in range(len(survey)):
        q=survey[i]
        score=choices[i]
        if score >= 1 and score <=3:
            if score==1:
                result[q[0]]+=3
            elif score==2:
                result[q[0]]+=2
            elif score==3:
                result[q[0]]+=1
        elif score>=5 and score<=7:
            if score==5:
                result[q[1]]+=1
            elif score==6:
                result[q[1]]+=2
            elif score==7:
                result[q[1]]+=3

    answer += 'R' if result['R']>=result['T'] else 'T'
    answer += 'C' if result['C']>=result['F'] else 'F'
    answer += 'J' if result['J']>=result['M'] else 'M'
    answer += 'A' if result['A']>=result['N'] else 'N'

    return answer


