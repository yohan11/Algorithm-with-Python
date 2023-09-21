def check_password(password):
        return len(password)>=6 and len(password)<=9
    
N = int(input())
for i in range(N):
    password=input()
    if check_password(password):
        print('yes')
    else:
        print('no')