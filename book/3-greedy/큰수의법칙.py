import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort(reverse=True)
max = nums[0]
max2 = nums[1]

sum = 0
while M > 0:
    for i in range(K):
        if M == 0:
            break
        sum += max
        M -= 1
        
    if M == 0:
        break
    sum += max2
    M -= 1

print(sum)