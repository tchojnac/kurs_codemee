#text = input("Podaj tekst o dług. nieparzystej >7:")
#center = len(text)//2
#new_text = text[center-1] + text[center] + text[center + 1]
#print(new_text)

#quote = 'Honesty is the first chapter in the book of wisdom.'
#print(len(quote))
#print(quote[-7:-1])
#middle = len(quote)//2
#print(quote[0:middle])
#print(quote[-1])
#print(quote[middle::3])
#print(quote[::2])
#print(quote[::-1])
#print(quote.replace('wisdom', 'friendship'))


palindrom = "Kobyła ma mały bok"
palindrom = palindrom.replace(" ", "")
palindrom = palindrom.lower()
print(palindrom)
print(palindrom == palindrom[::-1])

