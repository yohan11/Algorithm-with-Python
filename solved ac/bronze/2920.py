melody = list(map(int, input().split()))

up = 1
down = 1

for i in range(1, len(melody)):
    if melody[i] > melody[i - 1]:
        up += 1
    elif melody[i] < melody[i - 1]:
        down += 1

if up == len(melody):
    print("ascending")
elif down == len(melody):
    print("descending")
else:
    print("mixed")
