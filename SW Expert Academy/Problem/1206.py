T = int(input())

for t in range(1, T + 1):
    W = int(input())
    H = list(map(int,input().split()))
    answer = 0 
    for i in range(2, len(H)-2):
        if H[i] > H[i-1] and H[i] > H[i-2] and H[i] > H[i+1] and H[i] > H[i+2]:
            print("Im high ", H[i])
            answer += H[i] - H[i-1] 
            if answer < H[i] - H[i-2] :
                answer -= H[i-2] - H[i-1] 
            answer += H[i] - H[i+1]
            if answer < H[i] - H[i+2] :
                answer -= H[i+2] - H[i+1]
    print(answer)