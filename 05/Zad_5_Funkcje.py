print("Zgadnij liczbę pomiedzy 0 a 100. Masz 5 szans.")
user_input = int(input('Zgaduj '))

count = 0
last_distance = -1
while user_input is not 41 and count < 4:
    count = count + 1
    how_close_to_answer = (41 - user_input)
    how_close_to_answer = how_close_to_answer.__abs__()
    if how_close_to_answer <= 5 and last_distance > 5:
        user_input = int(input(f'Goraco. Pozostalo szans {5 - count} '))
    elif last_distance == -1:
        if 5 < how_close_to_answer < 20:
            user_input = int(input(f'Cieplo. Pozostalo szans {5 - count} '))
        elif how_close_to_answer >= 20:
            user_input = int(input(f'Zimno. Pozostalo szans {5 - count} '))
        elif how_close_to_answer <= 5:
            user_input = int(input(f'Goroco. Pozostalo szans {5 - count} '))
    else:
        if how_close_to_answer < last_distance:
            if how_close_to_answer <= 5:
                user_input = int(input(f'Gorecej. Pozostalo szans {5 - count} '))
            else:
                user_input = int(input(f'Cieplej. Pozostalo szans {5 - count} '))
        elif how_close_to_answer > last_distance:
            user_input = int(input(f'Zimniej. Pozostalo szans {5 - count} '))
    last_distance = how_close_to_answer


if user_input is not 41:
    print('Przegrales!')
else:
    print('Wygrales!')
    print(f"Wykorzystales {count + 1} szans aby zgadnac.")