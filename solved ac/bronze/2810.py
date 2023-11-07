N = int(input())
row = input()

seat = []


i = 0
while i < N:
    if row[i] == "S":
        seat.append(row[i])
    elif row[i] == "L":
        seat.append(row[i : i + 2])
        i += 1
    i += 1
holder = ["*"] * (len(seat) + 1)

print(N if N < len(holder) else len(holder))
