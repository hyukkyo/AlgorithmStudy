def longestConsecutive(nums):
    longest = 0
    num_dict = {}

    for num in nums:
        num_dict[num] = True
        # 딕셔너리에 전부 넣어줌. 중복은 제외

    for num in num_dict:
        if num - 1 not in num_dict: # 6앞에 5가 있는가?
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

# O(n)으로 내려가면서 보다가 특정 파트에서만 O(n)을 돌기 때문에, 그냥 O(n)이 된다.

longestConsecutive([6, 7, 100, 5, 4, 4])