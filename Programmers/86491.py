# 코딩테스트 고득점 Kit - 완전탐색
# 최소직사각형

def solution(sizes):
    max_width = 0
    max_height = 0

    for size in sizes:
        size.sort()

    for i in range(len(sizes)):
        if sizes[i][0] > max_width:
            max_width = sizes[i][0]
        if sizes[i][1] > max_height:
            max_height = sizes[i][1]
    
    return max_width * max_height