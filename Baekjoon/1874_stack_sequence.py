t = int(input())

st = []
result = []
j = 1
valid = 1

for i in range(t):
    num = int(input())
    
    
    while j<=num:
        st.append(j)
        result.append('+')
        j = j+1

    if st[-1] == num:
        st.pop()
        result.append('-')
    else:
        valid = 0

if valid == 1:
    for k in result:
        print(k)
else:
    print('NO')