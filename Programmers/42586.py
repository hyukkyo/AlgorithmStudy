def mysolution(progresses, speeds):
    day_required = []
    for i in range(len(progresses)):
        day_required.append((100 - progresses[i]) // speeds[i])
    
    answer = []
    count = 1
    for i in range(len(day_required)):
        if i == len(day_required)-1: # 끝에 오면 그냥 넣고 끝내기
            answer.append(count)
            break
        
        if day_required[i] >= day_required[i+1]:
            count += 1
        else:
            answer.append(count)
            count = 1

    return answer

# 뭐야 실패했네?

def solution(progresses, speeds):
    dates = []
    for p, s in zip(progresses, speeds):
        date = -((p-100) // s)
        dates.append(date)

    # print(dates)

    dates.append(float("inf"))
    count_date = dates[0]
    count = 0
    answer = []
    for date in dates:
        if date <= count_date:
            count += 1
        else:
            answer.append(count)
            count_date = date
            count = 1

    return answer