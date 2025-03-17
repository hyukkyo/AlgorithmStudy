n = int(input())
nums_n = list(map(int, input().split()))
m = int(input())
nums_m = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

nums_n.sort()

for i in nums_m:
    result = binary_search(nums_n, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수정렬 array = [0] * 1000001 해서 인덱스로 접근하는 방법
# set() 함수를 사용하는 방법