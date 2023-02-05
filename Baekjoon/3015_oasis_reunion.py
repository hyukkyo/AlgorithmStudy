n = int(input())

count = 0
arr = []
max_between = 1

for i in range(n):
    height = int(input())
    
    if len(arr) > 0: # 비어있지 않으면
        max_between = 1

        for j in arr[::-1]: # 뒤에서부터
            if j < max_between or height < max_between:
                continue
            count += 1
            if j > max_between:
                max_between = j
            

    arr.append(height)

print(count)

#timeout