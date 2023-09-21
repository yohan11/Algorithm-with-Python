enter_log_dict={}

N=int(input())

for i in range(N):
    enter_log_input=input().split()
    if enter_log_input[1] == 'enter':
        enter_log_dict[enter_log_input[0]] = enter_log_input[1]
    elif enter_log_input[1] == 'leave':
        del enter_log_dict[enter_log_input[0]]

enter_person=sorted(enter_log_dict.keys(),reverse=True)

for person in enter_person:
    print(person)