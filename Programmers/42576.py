# 참여자 participant
# 완주자 completion
# 완주 못한사람을 리턴

def solution(participant, completion):
    count = {}
    for p in participant:
        if p in count:
            count[p] += 1
        else:
            count[p] = 1
    
    for c in completion:
        if c in count:
            count[c] -= 1

            # 0이되면 그냥 삭제
            if count[c] == 0:
                del count[c]
    
    return list(count.keys())[0]
    # return next(iter(count))