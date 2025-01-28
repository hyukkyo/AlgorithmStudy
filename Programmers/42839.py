# 코딩테스트 고득점 Kit - 완전탐색
# 소수 찾기
from itertools import permutations

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = []
    for i in range(1, len(numbers)+1):
        for t in list(permutations(numbers, i)): # 순열한 문자열 조합을
            nums.append(int(''.join(t))) # 숫자로 join해서 넣어준다
    
    nums = set(nums) # 중복제거

    answer = len(nums)
    for num in nums:
        if num == 0 or num == 1:
            answer -= 1
        else:
            if is_prime(num) == False:
                answer -= 1
    
    return answer