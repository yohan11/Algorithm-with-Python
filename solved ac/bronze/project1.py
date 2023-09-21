my_list=[12,65,54,39,102,339,221]

result=[]

for i in filter(lambda a : a% 13 ==0, my_list):
    result.append(i)

print(f'Multiples of 13 are {result}')
