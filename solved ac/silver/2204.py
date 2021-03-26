T = int(input())
data = []
max = 0
for i in range(T):
    d = list(input())
    data.append(d)
for a in range(0, T):
    for b in range(a+1, T):
        if str(data[a]).lower() < str(data[b]).lower():
            max = a
        elif str(data[a]).lower() > str(data[b]).lower():
            max = b
print(''.join(data[max]))
