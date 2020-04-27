import os
import random
import sys


def show_quote(text):
    sentence = random.choice(text)
    sentence = sentence.split('.')
    print('*' * 70)
    print(sentence[0].center(70))
    print(sentence[1].strip().center(70))
    print('*' * 70)


filename = input("Podaj nazwę pliku")
#filename = "quotes.txt"

if os.path.exists(filename) and os.stat(filename).st_size > 0:
    with open(filename, encoding='utf-8') as fopen:
        quotes = fopen.readlines()

    show_quote(quotes)
try:
    quotes = True
except Exception as e:
    print(sys.exc_info()[0].__name__)



