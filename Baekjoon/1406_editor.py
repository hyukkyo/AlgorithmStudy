# s = input()
# m = int(input())
# n = len(s)
# i=0
# while i < m:
#     c = input()
#     if c == 'L':
#         n -= 1
#     elif c == 'D':
#         if len(s) > n:
#             n += 1

#     elif c == 'B':
#             s = s[:n-1] + s[n:]
#     else:
#         s = s[:n] + c[2] + s[n:]
#         n += 1
    
#     if n < 0:
#         n = 0    
#     i += 1
# print(s)
#timeout

#스택 두개로 나눠서 커서를 다루는 풀이가 있었음.
import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()
            
    else:
        st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))