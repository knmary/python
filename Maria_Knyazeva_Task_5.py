from random import choice

NOUNS  = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
    for i in range(n):
        random_index = choice(NOUNS)
        random_index_1 = choice(ADVERBS)
        random_index_2 = choice(ADJECTIVES)
        joke = f'{random_index} {random_index_1} {random_index_2}'
        list_2 = []
        print(joke)
        if flag == True:
            list_2 = joke.split()
            for noun in NOUNS:
                for fun in list_2:
                    if noun == fun:
                        NOUNS.remove(noun)

            for adverb in ADVERBS:
                for fun in list_2:
                    if adverb == fun:
                        ADVERBS.remove(adverb)


            for adjective in ADJECTIVES:
                for fun in list_2:
                    if adjective == fun:
                        ADJECTIVES.remove(adjective)


get_jokes(n=3, flag=True)