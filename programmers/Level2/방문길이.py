def solution(dirs):
    sets = set()
    y, x = 0, 0
    moving = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}

    for dir in dirs:
        dy, dx = moving[dir]
        newY = y + dy
        newX = x + dx
        if newY <= 5 and newY >= -5 and newX <= 5 and newX >= -5:
            sets.add(((y, x), (newY, newX)))
            sets.add(((newY, newX), (y, x)))
            y = newY
            x = newX
    answer = len(sets) // 2
    print(answer)


solution("ULURRDLLU")
