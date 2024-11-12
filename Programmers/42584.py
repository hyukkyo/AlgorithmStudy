def solution(prices):
    n = len(prices)
    answer = [0]*n
    
    for i in range(n-1):
        for j in range(i+1, n):
            answer[i] += 1

            if prices[i] > prices[j]:
                break

    answer[-2] = 1

    return answer