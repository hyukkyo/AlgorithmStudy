from collections import deque

def solution(numbers, target):
    answer = 0

    q = deque()

    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])

    while q:
        number, idx = q.popleft()

        idx += 1
        if idx < len(numbers):
            q.append([number + numbers[idx], idx])
            q.append([number - numbers[idx], idx])
        else:
            if number == target:
                answer += 1

    return answer