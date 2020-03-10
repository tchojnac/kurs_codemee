#Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę
#i mieć długość conajmniej 8 znaków.
#Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
#Wyświetl różne komunikaty w zależności od rodzaju błędu.

def validate():
    while True:
        password = input("Podaj hasło z liter i cyfr, zwierające conajmniej 1 dużą literę "
                         "i mające długość conajmniej 8 znaków: ")
        if len(password) < 8:
            print("Sprawdź czy jest conajmniej 8 znaków")
        elif not password.isdigit():
            print("Sprawdź czy jest cyfra: ")
        elif not password.isupper():
            print("Sprawdź czy jest duża litera")
        else:
            print("Hasło jest poprawne")
            break

validate()