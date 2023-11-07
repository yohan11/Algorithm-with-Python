
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    N = int(input())
    farm = [[0]*N for _ in range(N)]
    for i in range(N):
        row = input()
        for j in range(N):
             farm[i][j] = int(row[j])
              
    for i in range(N//2):
        new_farm = farm[i][(N//2)-i:N-((N//2)-i)]
        for money in new_farm:
            answer += money
    for i in range(N-1, N//2,-1):
        new_farm = farm[i][(N//2)-i:N-((N//2)-i)]
        for money in new_farm:
            answer += money
    new_farm = new_farm[N//2][:]
    for money in new_farm:
            answer += money
         
    print(answer)
        