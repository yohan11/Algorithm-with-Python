# from collections import deque


# def solution(people, limit):
#     answer = 0
#     people.sort()

#     people = deque(people)

#     while people:
#         if len(people) == 1:
#             answer += 1
#             people.pop()
#         else:
#             weight = people[0] + people[-1]

#             if weight > limit:
#                 answer += 1
#                 people.pop()
#             else:
#                 people.pop()
#                 people.popleft()
#                 answer += 1

#     return answer


def solution(people, limit):
    answer = 0
    people.sort()

    light, heavy = 0, len(people) - 1

    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
            answer += 1
        else:
            heavy -= 1
            answer += 1

    return answer
