A = int(input())
B = int(input())
C = int(input())

result = A*B*C

num_list=[0]*10

result = str(result)

for num in result:
    num_list[int(num)] += 1

for n in num_list:
    print(n)