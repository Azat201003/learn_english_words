from random import randint, shuffle
from sys import argv

words_ru = []
words_en = []

with open('words_ru', 'r') as file:
    for line in file.readlines():
        words_ru.append(line[:-1])

with open('words_en', 'r') as file:
    for line in file.readlines():
        words_en.append(line[:-1])

words = list(zip(words_ru, words_en))

def get_random_word() -> tuple:
    return words[randint(0, len(words)-1)]

is_from_english = False

n = 4

if '-en' in argv:
    is_from_english = True

for arg in argv:
    if arg.startswith('--n='):
        n = int(arg.split('--n=')[1])

if is_from_english:
    while True:
        translate, word = get_random_word()
        print(f"{word} is ")
        print()
        vars = [translate] + list([get_random_word()[0] for j in range(n-1)])
        shuffle(vars)
        print(*[f"{i+1}). {trans}" for i, trans in enumerate(vars)], sep='\n')
        print()
        if vars[int(input("your answer is "))-1] == translate:
            print("right!")
            print()
            continue
        print(f"right is {translate}")
        print()
else:
    while True:
        word, translate = get_random_word()
        print(f"{word} это ")
        print()
        vars = [translate] + list([get_random_word()[1] for j in range(n-1)])
        shuffle(vars)
        print(*[f"{i+1}). {trans}" for i, trans in enumerate(vars)], sep='\n')
        print()
        if vars[int(input("твой ответ "))-1] == translate:
            print("правильно!")
            print()
            continue
        print(f"правильный ответ {translate}")
        print()
