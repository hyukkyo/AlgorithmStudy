T = int(input())

for i in range(T):
    nums = list(map(int, input().split()))
    sum_odd = 0
    # print(nums)
    for num in nums:
        if num % 2 != 0:
            sum_odd += num
    
    result = '#' + str(i+1) + ' ' + str(sum_odd)
    print(result)