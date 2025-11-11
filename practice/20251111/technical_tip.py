import string

# 아스키코드
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)

# 대소문자
# str.isupper()
# str.islower()

s = '가나다라'
n = 7

print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))

# 2차원 배열 1차원으로 만들기
my_list = [[1, 2], [3, 4], [5, 6]]
answer = sum(my_list, [])

# Counter 함수
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # 1이 몇번등장한지