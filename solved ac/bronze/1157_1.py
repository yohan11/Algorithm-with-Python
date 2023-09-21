word=list(input().lower())

alphabet_dict={}
max_alpha_list=[]

for alpha in word:
    if alpha in alphabet_dict:
        alphabet_dict[alpha] += 1
    else:
        alphabet_dict[alpha] = 1

for alpha in alphabet_dict:
    if alphabet_dict[alpha] == max(alphabet_dict.values()):
        max_alpha_list.append(alpha)

if len(max_alpha_list) == 1 :
    print(max_alpha_list[0].upper())
else:
    print('?')

