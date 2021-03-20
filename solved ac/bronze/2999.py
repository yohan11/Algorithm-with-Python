#비밀 
enc = input()
N = len(enc)
RC_list = {}
for R in range(1, N+1):
    for C in range(1, N+1):
        if R*C == N:
            if R <= C:
                RC_list[R] = C
R = int(max(RC_list.keys()))
C = RC_list.get(R)
dec = [[0 for _ in range(C)] for _ in range(R)]
res = 0
while res < N:
    for a in range(R):
        for b in range(C):
            dec[a][b] = enc[res]
            res += 1
decrypt = ''
for a in range(C):
    for b in range(R):
        decrypt += dec[b][a]
print(decrypt)
