

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):


    result = []
    for i in range(num):
        result.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return result

print(get_jokes(5))
#['город сегодня яркий', 'автомобиль вчера утопичный', 'дом завтра яркий', 'город завтра яркий', 'город сегодня зеленый']
