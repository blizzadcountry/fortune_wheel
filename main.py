# Что изготавливают из сахарной свёклы?
# * * * * *
# Назовите букву: а
# Есть такая буква

# * а * a *
# Назовите букву: e
# Нет такой буквы!

import time

def get_letter():
    letter = input('Назовите букву: ')
    
    return letter

answer = "сахар"
print("Что изготавливают из сахарной свёклы?")

table = ['*' for i in range(len(answer))]

while True:
    time.sleep(1)
    print(*table)
    time.sleep(1)
    if letter in answer:
        time.sleep(1)
        print('Есть такая буква!')
        for i in range(len(answer)):
            if answer[i] == letter:
               table[i] = letter
        if '*' not in table:
            time.sleep(1)
            print('Победа!')
            print('Было загадано слово:',answer)
            break
    else:
        time.sleep(1)
        print('Такой буквы нет!')