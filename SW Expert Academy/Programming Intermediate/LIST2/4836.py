#색칠하기
T = int(input())
whiteboard = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1,T+1):
    N=int(input())
    for area in range(1,N+1):
        x1,y1,x2,y2,color=map(int,input().split())
