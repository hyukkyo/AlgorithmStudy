sentence = input()
m = int(input())

cursor = len(sentence)

for i in range(m):
    command = input()
    
    if command == 'L':
        if cursor > 0:
            cursor -= 1
    elif command == 'D':
        if len(sentence) > cursor:
            cursor += 1

    elif command == 'B':
        if cursor > 0:
            sentence = sentence[:cursor-1] + sentence[cursor:]
            cursor -= 1
    else:
        sentence = sentence[:cursor] + command.split(' ')[1] + sentence[cursor:]
        cursor += 1

print(sentence)

# timeout