#오름차순 

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = sorted(data)
    print(f"#{TC}", end=" ")
    for i in result:
        print(i, end=" ")
    print("")
