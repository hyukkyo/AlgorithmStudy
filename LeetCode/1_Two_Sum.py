# class Solution(object):
#     def twoSum(self, nums, target):
#         memo = {} # 딕셔너리 선언
#         for v in nums:
#             memo[v] = 1
        
#         for v in nums:
#             needed_number = target - v
#             if needed_number in memo: # O(1)의 시간복잡도로 바로 탐색해버림
#                 return True
        
#         return False
    
# 하지만 위 풀이는 같은 수를 두번 체크할 때도 있기 때문에, 오류가 발생함.
    
class Solution(object):
    def twoSum(self, nums, target):

        memo = {}
        for v in nums:
            memo[v] = 1
        for v in nums:
            del memo[v] # 딕셔너리에서 잠시 삭제
            needed_number = target - v
            if needed_number in memo:
                
                return True
            
            memo[v] = 1 # 다시 입력
        
        return False
            

print(Solution.twoSum(self=Solution, nums=[4,1,9,7,8,2], target=14))
