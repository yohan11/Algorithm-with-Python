#내가 짠 코드 (틀림)
def is_right(a, b):
    global honest
    for ques in range(a, b):
        if Olie[ques] > answer_list[game]:
            if Stan[ques] != "too high":
                honest = False
        elif Olie[ques] < answer_list[game]:
            if Stan[ques] != "too low":
                honest = False
    return honest


Olie = []
Stan = []
answer_list = []
ques_list = []
i = 0
while True:
    Olie.append(int(input()))
    if Olie[-1] == 0:
        Olie.remove(Olie[-1])
        break
    Stan.append(input())
    if Stan[-1] == 'right on':
        answer_list.append(Olie[-1])
        if len(ques_list) >= 1:
            ques_list.append(len(Olie)-ques_list[i-1])
        else:
            ques_list.append(len(Olie))
        i += 1
for game in range(0, len(answer_list)):
    honest = True
    if game == 0:
        honest = is_right(0, ques_list[game])
    else:
        honest = is_right(ques_list[game]+1, ques_list[game]+ques_list[game-1])
    if honest == True:
        print("Stan may be honest")
    else:
        print("Stan is dishonest")

#구글에 나와있는 코드(정답)
def _4335():
    Check = [True] * 11
    while 1:
        T = int(input())
        if T == 0:
            return
        S = str(input())
        if S == 'too high':
            for i in range(T, 11):
                Check[i] = False
        elif S == 'too low':
            for i in range(0, T+1):
                Check[i] = False
        else:
            if Check[T]:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')
            Check = [True] * 11

_4335()
