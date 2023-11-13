def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            # idx가 5가 되었는데도 target넘버가 아니다 => 이전 인덱스 차례로 돌아감
            return
        else:
            # 다음 원소를 더해서 result를 만드는 경우
            dfs(idx + 1, result + numbers[idx])
            # 다음 원소를 빼서 result를 만드는 경우
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer
