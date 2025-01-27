# 코딩테스트 고득점 Kit - 완전탐색
# 모의고사

def solution(answers):
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]

    count_1, count_2, count_3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == answer_1[i%len(answer_1)]:
            count_1 += 1
        if answers[i] == answer_2[i%len(answer_2)]:
            count_2 += 1
        if answers[i] == answer_3[i%len(answer_3)]:
            count_3 += 1

    count_max = max(max(count_1, count_2), count_3)
    result = []
    if count_max == count_1:
        result.append(1)
    if count_max == count_2:
        result.append(2)
    if count_max == count_3:
        result.append(3)
    
    return result
