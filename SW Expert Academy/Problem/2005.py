#파스칼의 삼각형

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    for i in range(1, N+1):
        Tri = [[1]*a for a in range(1, i+1)]
    print(f"#{TC}")
    for i in range(N):
        if len(Tri[i]) > 2:
            for j in range(1, len(Tri[i])-1):
                Tri[i][j] = Tri[i-1][j]+Tri[i-1][j-1]

        for x in Tri[i]:
            print(x, end=" ")
        print("")
