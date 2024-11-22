# 발상이 진짜 기발하네...

# 원소의 크기가 1000이하인 점을 생각했을때,
# 숫자를 반복 시킨 앞의 4자리만 비교하면 됨
# 332 => 3323
# 32 => 3232
# 34 => 3434
# 343 => 3433

def solution(numbers):
    sorted_numbers = numbers
    sorted_numbers.sort(key = lambda x: (str(x) * 4)[:4], reverse = True)
    # print(sorted_numbers)

    answer = ''.join(map(str, sorted_numbers))

    if int(answer) == 0:
        answer = '0'
        
    return answer