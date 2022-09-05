from turtle import distance


def solution(numbers, hand):
    answer=''
    distance={'L':0, 'R':0}
    L=[1,4,7]
    R=[3,6,9]
    M=[2,5,8,0]
    if numbers[0] in M:
        if hand=='right':
            answer+='R'
        else:
            answer+='L'
    for i in range(len(numbers)):
        number=numbers[i]
        if number in L:
            answer+='L'
        elif number in R:
            answer+='R'
        elif number in M:
            if number==2:






numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand='right'
print(solution(numbers,hand))