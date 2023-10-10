import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dirY=[-1,1,0,0]
dirX=[0,0,-1,1]

def dfs(y,x):
    global visited, graph, cnt
    visited[y][x]=True
    cnt+=1

    for i in range(4):
        newY=y+dirY[i]
        newX=x+dirX[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY,newX)


n,m,k=map(int,input().split())
MAX=100+10

graph=[[False]*MAX for _ in range(MAX)]
visited=[[False]*MAX for _ in range(MAX)]

for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b]=True

count_list=[]    

for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j] and not visited[i][j]:
            cnt=0
            dfs(i,j)
            count_list.append(cnt)
            
print(max(count_list))