def solution(s):
    answer = []
    s = list(s)
    

    for i in range(0, len(s)-1):
        count = 0
        for j in range(i+1, len(s)):
            if s[i] <= s[j]:
                count += 1
            elif s[i] > s[j]:
                count += 1 
                #여기에서 append를 또했던게 문제
                break
        answer.append(count) #두번째 for문에서는 count 조절만 해주고, 끝났을 때 append
    
    answer.append(0)

    return answer

s = input()
print(solution(s))