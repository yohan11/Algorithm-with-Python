#글자수

T = int(input())

for TC in range(1, T+1):
    str1 = input()
    str2 = input()
    alphabet = {}
    for a in range(len(str1)):  # makeDictionary
        word = str1[a]
        if str1[a] not in alphabet:
            alphabet[word] = 0
    for b in range(len(str2)):  # test
        if str2[b] in alphabet:
            alphabet[str2[b]] += 1

    print("#%d %d" % (TC, max(alphabet.values())))
