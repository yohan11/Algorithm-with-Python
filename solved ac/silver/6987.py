def answer():    
    global answer_list
    for _ in range(4):
        row=list(map(int,input().split()))
        A = row[:3]
        B = row[3:6]
        C = row[6:9]
        D = row[9:12]
        E = row[12:15]
        F = row[15:18]
        every_team=[A,B,C,D,E,F]

        # 승리 합 != 패배 합
        victory_sum=0
        lose_sum=0
        for team in every_team:
            victory_sum+=team[0]
            lose_sum+=team[-1]
        if victory_sum != lose_sum:
            answer_list.append(0)
            continue
        
        # 무승부 게임 수
        moo_list=[]
        for team in every_team:
            if team[1]!=0:
                moo_list.append(team[1])
        if len(moo_list)%2==1:
            answer_list.append(0)
            continue
        # 무승부 갯수가 맞지 않을 때
        moo_list2=[]
        for moo in moo_list:
            if moo!=0:
                if moo not in moo_list:
                    moo_list2.append(moo)
        if len(moo_list2) >1:
            answer_list.append(0)
            continue
        
        # 승+무+패 수가 모든 팀에서 같아야함
        result_sum = sum(A)
        for team in every_team:
            if sum(team) != result_sum:
                answer_list.append(0)
                continue
            
        answer_list.append(1)

answer_list=[]
answer()
for a in answer_list:
    print(a,end=" ")
