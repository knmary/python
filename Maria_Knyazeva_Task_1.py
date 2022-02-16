DICT_MAIN = {'zero':'ноль','one':'один','two':'два','three':'три','four':'четыре','five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять'}
word_main = str(input('Введите числительное от 0 до 10 на английском языке:'))

def num_translate(word):
    for word in DICT_MAIN.keys():
        word = DICT_MAIN.get(word_main, None)
    return word

print(num_translate(word_main))
