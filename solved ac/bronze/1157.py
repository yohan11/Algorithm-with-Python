data = list(input())
n = len(data)
res = {}
for i in range(0, n):
    if data[i].upper() not in res.keys():
        res[data[i].upper()] = 1
    else:
        res[data[i].upper()] += 1
max = max(res.values())
count = 0
maxValue = 0
for key, value in res.items():
    if value == max:
        maxValue = value
        count += 1
if count > 1:
    print("?")
elif count == 1:
    for key, value in res.items():
        if value == maxValue:
            print(key)
