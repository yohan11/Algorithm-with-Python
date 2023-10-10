# 시간제한이 있는 문제로, index() 보다는 딕셔너리 자료구조를 활용하면 O(1)의 시간으로 풀 수 있다.
# sys도 활용할것

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_list = {}
for i in range(1, N + 1):
    pokemon = input().rstrip()
    # 이름:번호로 , 번호:이름으로 모두 저장
    pokemon_list[i] = pokemon
    pokemon_list[pokemon] = i
for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(pokemon_list[int(question)])
    else:
        print(pokemon_list[question])
