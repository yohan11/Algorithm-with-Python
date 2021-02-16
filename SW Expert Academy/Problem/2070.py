#큰 놈, 작은 놈, 같은 놈

T=int(input())

for TC in range(1,T+1):
    a,b=map(int,input().split())
    if a>b:
        print(f"#{TC} >")
    elif a<b:
        print(f"#{TC} <")
    else:
        print(f"#{TC} =")

