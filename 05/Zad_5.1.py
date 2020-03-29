#def mood():
#    print("How are you")

# reszta kodu
#mood()
#Napisz funkcję, która pyta użytkownika o pary książka + ocena i zapisuje ją w programie.
#Napisz funkcję, która zapyta o numer książki i wyświetli książkę wraz z oceną
#W prosty sposób obsłuż błąd użytkownika - użytkownik zapyta o numer w bazie, który nie istnieje

def add_books_to_library(counter):
counter =int(input("Ile książek chcesz dodać?"))
books = []
for k in range(counter):
    title = input("Podaj tytuł książki: ")
    grade = int(input("Podaj ocenę książki 1-10: "))
    books.append((title, grade))
    print('---------------')
return books

def show_book():
    nr  = int(input("Podaj nr książki do wyświetlenia: "))
    index = nr - 1
    if index >= len(books):
        print("Nie mam tyle książek")
    else:
        print(f"Twoja książka to {books[indeks]}")









