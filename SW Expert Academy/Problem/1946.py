#간단한 압축 풀기

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    Original = ''
    c = 0
    for i in range(N):
        alphabet, num = map(str, input().split())
        num = int(num)
        Original += alphabet*num
    print(f"#{TC}")
    for s in Original:
        print(s, end="")
        c += 1
        if c % 10 == 0:
            print("")
    print("")
