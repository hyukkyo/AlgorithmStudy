n, m = map(int, input().split())

height_list = list(map(int, input().split()))

# height_list.sort(reverse=True) # 내림차순으로 정렬 19 17 15 10
# print(height_list)

# cut_height = height_list[0] - 1 # 18부터 시작
# while True:
#     pieces = 0 # 남은 떡의 길이
#     for height in height_list:
#         if height - cut_height > 0:
#             pieces = pieces + (height - cut_height)
#     # print(pieces)
#     if pieces >= m: # 남은 떡의 길이가 m이상이면 그만 반복
#         break

#     cut_height = cut_height - 1 # 17 16 15 순으로 내림

# print(cut_height)

# 이진탐색으로 풀어야함. 입력값 범위가 20억이라서.

start = 0
end = max(height_list)
# start, end 설정

result = 0 # 조건을 만족하는 커트라인
while start <= end:
    total = 0 # 자른 떡의 길이
    mid = (start + end) // 2 # 중간값 설정
    for height in height_list:
        if height > mid: # 자를수있으면
            total += (height - mid) # 더한다
    
    if total < m: # 모자라면 더 많이 잘라야 함
        end = mid - 1 # end를 mid보다 작게 땡겨옴. 그러면 mid가 줄어들어서 더 많이 자를 수 있음

    else: # 더 많으면 
        result = mid # 일단 결과값에 기록. mid의 최댓값을 담는거니까.
        start = mid + 1 # start를 mid보다 크게 가져옴. 그러면 mid가 커짐.

print(result)