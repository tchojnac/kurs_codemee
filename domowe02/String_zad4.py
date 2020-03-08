#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
#Połącz dane w jeden ciąg book za pomocą spacji
#Policz liczbę wszystkich znaków w napisie boo

tytul = input("Podaj tytuł książki:")
print(tytul.title())
autor = input("Podaj nazwisko autora: ")
print(autor.title())
liczba_stron = input("Podaj ilość stron:")
print(int(liczba_stron))
book = (tytul.title() + ' ' + autor.title() + ' ' + (liczba_stron))
print(book)

print(len(book))
