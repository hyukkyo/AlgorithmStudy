x = int(input())

# num = 1
# count = 0
# while num != x:
#     if x >= num * 5:
#         num *= 5
#         count += 1
#         continue

#     elif x >= num * 3:
#         num *= 3
#         count += 1
#         continue

#     elif x >= num * 2:
#         num *= 2
#         count += 1
#         continue

#     else:
#         num += 1
#         count += 1
#         continue

# print(count)

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1 # 2는 1만드는 방법에 +1하는거다.

    if i % 2 == 0: # 2곱해서 만들기
        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
