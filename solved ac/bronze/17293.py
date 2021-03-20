#맥주
beer = int(input())
res = beer
while res >= 0:
    if res == 2:
        print('''2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.\n''')
        res -= 1
    elif res == 1:
        print('''1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.\n''')
        res -= 1
    elif res == 0:
        print(f'''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {beer} bottles of beer on the wall.''')
        break
    else:
        print(f'''{res} bottles of beer on the wall, {res} bottles of beer.
Take one down and pass it around, {res-1} bottles of beer on the wall.\n''')
        res -= 1
