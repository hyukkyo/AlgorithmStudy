t = int(input())

for i in range(t):
    sentence = input()
    words = sentence.split(' ')
    for j in words:
        print(j[::-1], end=' ')
    print()