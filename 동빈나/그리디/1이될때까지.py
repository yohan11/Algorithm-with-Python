# n, k = map(int, input().split())

# answer = 0

# while True:
#     if n == 1:
#         break
#     if n % k == 0:
#         n = n // k
#         answer += 1
#     else:
#         n = n - 1
#         answer += 1

# print(answer)


n, k = map(int, input().split())

answer = 0

while True:
    target = (n // k) * k
    answer += n - target
    n = target

    if n < k:
        break

    answer += 1
    n = n // k

print(answer)
