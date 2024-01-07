# nums 배열에서 두 숫자를 뽑은 합이 target 숫자가 되면 True를 반환

# 반복문을 두번써서 짜면 O(n^2)

# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return True
#     return False

# print(twoSum(nums = [4,1,9,7,5,3,16], target=14))

# 투포인터로 짜면
