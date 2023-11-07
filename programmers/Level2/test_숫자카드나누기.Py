# 처음에 시간 초과가 나서 math 라이브러리를 사용하였더니 시간초과는 해결되었다.
# 몇가지 테스트케이스에서 실패가 나서 블로그 참조해서 아래와 같이 수정 후 최종 답안이다.
# 그래도 한개의 테케에서 계속 오류가 났었는데, 사실 잘 이유를 모르겠다
import math
def allImpossible(arr,n):
    for num in arr:
        if num % n == 0:
            return 0
        return n
def allPossible(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        temp = math.gcd(temp,arr[i])
    return temp
def solution(arrayA, arrayB):
    answer = 0

    # 조건 A
    possible_A = allPossible(arrayA)
    for num in arrayB:
        if num%possible_A == 0 :
            break
        else:
            answer = max(answer,possible_A)
    # 조건 B
    possible_B = allPossible(arrayB)
    for num in arrayA:
        if num%possible_B == 0 :
            break
        else:
            answer = max(answer,possible_B)

    return answer

# 아래가 정답인 답안인데, 내가 생각한 코드랑 로직은 비슷한 것 같은데 더 코드가 단순하다는 것 빼고는 어디에서 다른지 잘 감이 잡히지 않는다,
import math

def solution(arrayA, arrayB):
    answer = 0
    a=arrayA[0]
    b=arrayB[0]

    for i in range(len(arrayA)):
        a=math.gcd(a,arrayA[i])
        b=math.gcd(b,arrayB[i])
    
        
    cheA=1
    cheB=1
    for i in range(len(arrayA)):
        if arrayA[i] % b==0:
            cheA=0
        if arrayB[i] % a==0:
            cheB=0

    if cheA==0 and cheB==0:
        return cheA
    else:
        return max(a,b)



