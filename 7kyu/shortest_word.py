# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def shortest(word):
    print(len(min([w for w in list(word.split(' '))], key=len)))


shortest("bitcoin take over the world maybe who knows perhaps")
