# 내가품
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            city = city.lower()

            if city not in cache:
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                elif len(cache) >= cacheSize:
                    if len(cache) > 0:
                        cache.popleft()
                        cache.append(city)
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1
    return answer
