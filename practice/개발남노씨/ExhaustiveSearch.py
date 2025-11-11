# brute force

# nums = [1,2,3,4]로 만들수있는 모든 순열을 반환하시오.

nums = [1,2,3,4]

def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        
        for num in nums:
            if num in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans

print(permute(nums))