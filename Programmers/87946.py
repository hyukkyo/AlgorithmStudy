# 코딩테스트 고득점 Kit - 완전탐색
# 피로도
from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0

    for case in permutations(dungeons):
        current_cost = k
        count = 0
        for need_cost, cost in case:
            if need_cost > current_cost:
                break
            else:
                count += 1
                current_cost -= cost

        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons