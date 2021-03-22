#명령 프롬프트
TC = int(input())
file_name1 = list(input())
for i in range(TC-1):
    file_name2 = list(input()) #첫번째 문자열과 따로받기, 리스트로 받기
    for b in range(0, len(file_name1)):
        if file_name1[b] != file_name2[b]:
            file_name1[b] = "?"
print(''.join(file_name1)) #리스트에 있는 문자열 출력
