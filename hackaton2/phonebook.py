import json

wpis = {'imie': 'Zbigniew', 'numer': 5140,
        'imie': 'Aneta', 'numer': 5246,
        'imie': 'Gosia', 'numer': 5900,
        'imie': 'Gerard', 'numer': 5487,
        'imie': 'Jacek', 'numer': 5151,
        'imie': 'Mariusz', 'numer': 5082,
        'imie': 'Kasia', 'numer': 5026
        }

lista_numerow = []

lista_numerow.append(wpis)

with open('ksiazka_numerow.json', mode='w') as plik:
    json.dump(lista_numerow, plik)


    def wczytaj_nowy_wpis(lista):
            imie = input('Podaj imie: ')
            numer = int(input('Podaj numer: '))
            wpis = {'imie': imie, 'numer': numer}
            lista.append(wpis)


    lista_numerow = []

    wpis = {'imie': 'Jimi', 'numer': 1234}
    lista_numerow.append(wpis)

    wczytaj_nowy_wpis(lista_numerow)

    with open('ksiazka_numerow.json', mode='w') as plik:
            json.dump(lista_numerow, plik)


    def wczytaj_nowy_wpis(lista):
            imie = input('Podaj imie: ')
            numer = input('Podaj numer: ')

            try:
                    numer = int(numer)
            except ValueError:
                    print('Podano niepoprawny numer.')
            else:
                    wpis = {'imie': imie, 'numer': numer}
                    lista.append(wpis)


    def wczytaj_liste_wpisow():
            try:
                    with open('ksiazka_numerow.json', mode='r') as plik:
                            lista_numerow = json.load(plik)
                            print(f'Wczytano {len(lista_numerow)} wpisów.')
                            return lista_numerow
            except FileNotFoundError:
                    return []


    if __name__ == '__main__':
            lista_numerow = wczytaj_liste_wpisow()
            while True:
                    odpowiedz = input('Czy wczytać nowy wpis? [t/n]')
                    if odpowiedz == 't':
                            wczytaj_nowy_wpis(lista_numerow)
                    elif odpowiedz == 'n':
                            break

            with open('ksiazka_numerow.json', mode='w') as plik:
                    json.dump(lista_numerow, plik)


