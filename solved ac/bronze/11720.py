T = int(input()) #  받을숫자 개수

num=list(input()) #받아올 숫자 문자열 54321

sum=0 #합

for i in range(T):
    sum += int(num[i])

print(sum)