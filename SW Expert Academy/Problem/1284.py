#수도요금 경쟁

T=int(input())

for TC in range(1,T+1):
    P, Q, R, S, W=map(int,input().split())
    A=P*W    
    if W<=R:
       B=Q 
    else:
        B=Q+S*(W-R)
    
    if A>B:
        print(f"#{TC} {B}")
    else:
        print(f"#{TC} {A}")
