# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)

# print(fibo(4))

# d = [0] * 100 # 메모이제이션을 위해 리스트 초기화

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
    
#     if d[x] != 0: # 이미 값이 채워져있으면 그냥 반환
#         return d[x]
    
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99))

# 위는 탑다운 방식인거고, 아래는 바텀업 방식임

d = [0] * 100 # dp 테이블

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])