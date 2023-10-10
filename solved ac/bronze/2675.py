T=int(input())

for _ in range(T):
    num, word=map(str,input().split())
    num=int(num)
    result=''
    for w in word:
        result+=w*num
    print(result)