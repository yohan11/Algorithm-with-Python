#조교의 점수매기기

T = int(input())

for TC in range(1, T+1):
    N, studentCode = map(int, input().split())
    Score = [[]*3 for _ in range(N)]
    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    FinalScore = [0]*N
    for i in range(N):
        middle, final, report = map(int, input().split())
        Score[i].append(middle)
        Score[i].append(final)
        Score[i].append(report)
        FinalScore[i] = middle*0.35+final*0.45+report*0.2
    # 처음 상태의 점수리스트에서 원하는 학생을 점수 정렬 하기 전에 인덱스로 뽑아내놓기! -> 이것을 딕셔너리로 해결하려다가 엄청 헤맸다..-
    score_of_k = FinalScore[studentCode-1]
    FinalScore.sort(reverse=True)
    # 미리 뽑아놓은 학생의 점수를 이용하여 index로 학생을 찾아내기, 평점을 매기는 식?? 이것때매 엄청 헤맸다..
    grade_of_k = int(FinalScore.index(score_of_k) / (N // 10))
    print(f"#{TC} {grades[grade_of_k]}")
