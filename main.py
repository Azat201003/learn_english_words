from random import randint, shuffle
from sys import argv

words_ru = []
words_en = []

with open('/home/azat/Документы/learn_ew/words_ru', 'r') as file:
    for line in file.readlines():
        words_ru.append(line[:-1])

with open('/home/azat/Документы/learn_ew/words_en', 'r') as file:
    for line in file.readlines():
        words_en.append(line[:-1])

words = list(zip(words_ru, words_en))

def get_random_word() -> tuple:
    return words[randint(0, len(words)-1)]

is_english = False

n = 4

if '-en' in argv:
    is_english = True

for arg in argv:
    if arg.startswith('--n='):
        n = int(arg.split('--n=')[1])


def get_translates(translate_index) -> list:
    translates = []
    for i in range(n-1):
        translate = get_random_word()[translate_index]
        while translate in translates:
            translate = get_random_word()[translate_index]
        translates.append(translate)

    return translates


def main(is_english=False):
    word_index = int(is_english)
    translate_index = 1-int(is_english)
    count_of_rights = 0
    count_of_games  = 0
    while True:
        rand = get_random_word()
        translate, word = rand[translate_index], rand[word_index]
        print(f"{word} " + (" is ..." if is_english else " это ...") + "\n")
        variants = [translate] + get_translates(translate_index)
        shuffle(variants)
        print(*[f"{i+1}). {variant_translate}" for i, variant_translate in enumerate(variants)], sep='\n', end='\n\n')
        count_of_games  += 1
        answer = variants[int(input("Your answer is " if is_english else "твой ответ "))-1]
        print(f"\nRight answer is {variants.index(translate)+1}). {translate}\n")
        if answer == translate:
            count_of_rights += 1
            print(f"Right! {count_of_rights}/{count_of_games}\n")
            print("-"*20)
            continue
        print(f"It isn't {count_of_rights}/{count_of_games}\n")
        print("-"*20)
    

main(is_english)