# 한자리 숫자가 arr에 들어있는데 연속으로 나오면 하나 빼고 다 날림

def solution(arr):
    answer = [arr[0]]

    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    
    return answer