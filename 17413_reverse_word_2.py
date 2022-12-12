S = input()

spell = []
word = []

tag = 0
for i in S:
    if i == '<':
        if(len(spell) != 0):
            spell.reverse()
            word.append(''.join(spell))
            spell.clear()
        tag = 1

    if tag == 0:
        if i != ' ':
            spell.append(i)
        else:
            if(len(spell) != 0):
                spell.reverse()
                spell.append(' ')
                word.append(''.join(spell))
                spell.clear()
    elif tag == 1:
        spell.append(i)

    if i == '>':
        if(len(spell) != 0):
            word.append(''.join(spell))
            spell.clear()
        tag = 0

if(len(spell) != 0):
    spell.reverse()
    word.append(''.join(spell))
    spell.clear()

print(''.join(word))