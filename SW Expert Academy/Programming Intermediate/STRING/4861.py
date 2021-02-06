#
T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    garo_data = []
    result = []
    sero_data = []
    for a in range(N):  # collectGaroData
        str1 = input()
        garo_data.append(str1)
        for i in range(len(str1)-M+1): #garoTest
                if str1[i:M+i] == str1[i:M+i][::-1]:
                    result.append(str1[i:M+i])

    for b in range(N):  # collectSeroData
        seroDataElement = ''
        for c in range(N):
            seroDataElement += garo_data[c][b]
        sero_data.append(seroDataElement)
    for data in sero_data:
        for i in range(len(data)-M+1): #seroTest
                    if data[i:M+i] == data[i:M+i][::-1]:
                        result.append(data[i:M+i])
    print("#%d %s"%(TC,result[0]))
