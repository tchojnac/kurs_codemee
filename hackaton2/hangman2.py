import turtle, random
def startUp():

    t = turtle.Turtle()  # rozpoczyna moduł turtle
    t.pu()  # w górę
    t.setx(-250)
    t.sety(80)
    t.pd()  # w dół
    t.speed(50)
    t.fd(100)
    t.rt(180)
    t.fd(50)
    t.rt(90)
    t.fd(170)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie
    # powyższy kod rysuje szubienicę dla wisielca

    print("-" * 26)
    print("Witamy w grze Wisielec!")
    print("-" * 26)
    print("Tylko słowa angielskie!")
    print("-" * 26)
    print("Kategorie...")
    print("")
    print("(1) Technology")
    print("(2) Food")
    print("(3) Sports")
    print("(4) Animals")
    print("")
    # powyższy kod to instrukcja dla użytkownika

    main(t)


def main(t):
    '''
    Główne funkcje dla gry.
    '''
    # Kategorie zawierające różne słowa dla gry
    technology = ["headset", "computer", "phone", "processor", "memory", "storage", "keyboard"]
    food = ["banana", "mango", "steak", "apple", "carrot", "rice", "soup", "pasta"]
    sports = ["skijumping", "hockey", "football", "baseball", "basketball", "volleyball", "boxing"]
    animals = ["cat", "dog", "lion", "chicken", "mouse", "bird", "shark", "dolphin", "duck"]
    categories = [technology, food, sports, animals]  # lista z listą kategorii
    categoryStrings = ["Technology", "Food", "Sports", "Animals"]  # użyta później do wyboru kategorii
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]  # użyte aby zapewnić że dana użytkownika jest literą
    guessedLetters = []  # lista odgadywanych liter użytkownika
    while True:
        userCategory = input("Którą kategorię chcesz zgadywać? (ex: 1):")
        if userCategory == "1" or userCategory == "2" or userCategory == "3" or userCategory == "4":  # zapewnia, że użytkownik wprowadził poprawne dane
            userCategory = int(userCategory)  # konwertuje dane użytkownika na cyfrę
            userCategory -= 1  # musi być podniesiona o jeden ponieważ lista zaczyna się od zera
            break  # koniec pętli z pytaniem o dane wejściowe
        else:  # jeśli użytkownik błędnie wprowadził dane
            print("Zła wartość!")  # użytkownik błędnie wprowadził dane
    categoryWord = random.choice(categories[userCategory])  # losowe słowo z kategorii wybranej przez użytkownika
    word = []  # inicjowanie listy dla słowa jakie będzie zgadywane
    for i in range(len(categoryWord)):
        word.append(categoryWord[i])  # każda litera jest dołączona do listy, która może być indywidualnie zmieniana później (w gwiazdkach)
    hiddenWord = []  # lista ze słowem pokazanym użytkownikowi
    for i in range(0, len(word)):
        hiddenWord.append("*")  # ukryte słowo podane jest jako odowiednia ilość gwiazdek
    totalCorrect = 0  # śledzi poprawnie podane litery
    incorrect = 0  # śledzi błędnie podane litery
    print("")
    print("Kategorie:", categoryStrings[userCategory])  # nwyświetla użytkownikowi wybraną kategorię
    print("Gra się rozpoczęła!")
    print("Pamiętaj o drugim oknie pokazującym rysunek Wisielca!")
    print("")
    print("Możesz odgadnąć moje słowo?")
    print("".join(hiddenWord))  # wyświetla słowo, które jest bieżąco wybrane i pokazane jako lista  w formacie string
    print("")
    # powyższy kod jest instrukcją dla użytkownika
    while True:
        correct = 0  # użyte aby sprawdzić czy bieżąca litera jest odgadnięta (nie całość)
        while True:
            newLetter = True  # użyte do określenia czy litera była już podana
            found = False  # sprawdza, czy wybrana litera była podana w źle podanych literach
            outputStatement = False  # zapobiega duplikowaniu instrukcji błędów
            print("")
            guess = input("Wprowadź literę:")
            for i in guessedLetters:  # sprawdza czy litera już była odgadywana
                if guess == i:
                    print("Już podałeś tą literę!")
                    print("".join(hiddenWord))  # słowo jest pokazane jako string
                    outputStatement = True  # zapobiega duplikowaniu instrukcji błędów
                    newLetter = False  # leitera już była odgadywana
            if newLetter == True:  # ten kod tylko działa jeśli odgadywana litera nie jest powtórzona później
                for i in alphabet:
                    if guess == i:  # sprawdza, czy litera jest w alfabecie
                        # del alphabet[alphabet.index(i)]
                        guessedLetters.append(guess)  # odgadywana litera jest w liście już podanych liter
                        found = True  # litera znaleziona w słowie
                    elif len(guess) > 1:  # sprawdza czy podana litera jest tylko jedna
                        print("Zła dana. Musi być litera!")
                        print("".join(hiddenWord))  # słowo jest pokazane jako string
                        outputStatement = True  # zapobiega duplikowaniu instrukcji błędów
                        break  # wyjście aby pozwolić użytkownikowy na nowy wybór
            if found == True:  # jeśli litera jest znaleziona, pętla pozwala użytkownikowi odgadywać
                break
            elif found == False:  # jeśli litera nie jest pojedynczą zgadywaną literą, pętla jest kontynuowana
                if outputStatement == False:  # zapobiega duplikowaniu instrukcji błędów
                    print("Not a valid input!")
                    print("".join(hiddenWord))  # słowo jest pokazane jako string
        for i in range(0, len(word)):
            if guess == word[i]:
                correct = 1  # odświeżenie tak, aby odgadnięta litera była zidentyfikowana
                totalCorrect += 1  # liczba poprawnych liter jest zwiększona
                hiddenWord[i] = guess  # bieżące słowo jest zaktualizowane tak aby wyświetlić odgadniętą literę użytkownikowi
                word[i] = "*"  # bieżące słowo jest zaktualizowane tak aby ukruć odgadywane litery gwiazdkami
                print("You guessed a letter!")
                print("".join(hiddenWord))  # słowo jest pokazane jako string
        if correct == 0:  # sprawdza, czy użytkownik nie odgadł żadnej litery
            incorrect += 1  # zwiększenie o jeden liczby niepoprawnych odgadnięć
            print("Tej litery nie ma w słowie!")
            print("".join(hiddenWord))  # słowo jest pokazane jako string
            drawHangman(t, incorrect)  # funkcja do wywołania narysowania części wisielca
        stringWord = "".join(word)  # słowo jest dołączone jako string
        check = len(stringWord) * "*"  # stworzony string równa liczba gwiazdek i liter słowa
        if stringWord == check:  # sprawdza czy odgadywane słowo jest w gwiazdkach (odkąd każda litera jest zmieniona w słowie z gwiazdkami gdy jezt zgadnięta)
            print("")
            print("Wygrałeś!")
            print("")
            print("Wynik:", incorrect, "(# niepoprawnych odgadnięć - niższy rezultat jest lepszy!)")
            break
        elif incorrect == 6:  # koniec gry jeżeli użytkownik 6 razy błędnie podał literę
            print("")
            print("Podałeś błędnie 6 liter! KONIEC GRY")
            break

    endGame(t)


def drawHangman(t, incorrect):
    '''
    Ta funkcja jest uruchamiana gdy gracz nie odgadł słowa.
    Części ciała są rysowane do tąd ąż ciało jest kompletne
    oznacza KONIEC GRY. Ta funkcja rysuje różne części
    dla każdej z sześciu niepoprawnych liter. Główna funkcja kończy grę po sześciu błędnych literach.
    '''
    if incorrect == 1:
        t.pu()
        t.setx(-120)
        t.sety(180)
        t.pd()
        t.circle(20)
        t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie
    elif incorrect == 2:
        t.pu()
        t.setx(-100)
        t.sety(160)
        t.pd()
        t.fd(50)
        t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie
    elif incorrect == 3:
        t.rt(45)
        t.fd(30)
        t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie
    elif incorrect == 4:
        t.pu()
        t.rt(-90)
        t.setx(-100)
        t.sety(110)
        t.pd()
        t.fd(30)
        t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie
    elif incorrect == 5:
        t.pu()
        t.rt(-45)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie
    elif incorrect == 6:
        t.pu()
        t.rt(180)
        t.setx(-100)
        t.sety(135)
        t.pd()
        t.fd(30)
        t.pu()
        t.ht()  # Ukrywa turtle aby usunąć strzałkę wyświetlaną na ekranie


def endGame(t):
    '''
    FFunkcja pyta użytkownika, czy chce zagrać jeszcze raz,
    zaczyna od nowa grę jeśli chce grać lub kończy gdy nie.
    '''
    print("")
    playAgain = input("Chcesz zagrać jeszcze raz? (TAK/NIE):")
    playAgain = playAgain.lower()  # wprowadza małe litery uwzględniając wpisanie przez użytkownika dużych liter
    if playAgain == "TAK":  # od nowa uruchamia grę jeżeli użytkownik chce grać ponownie
        t.clear()  # usuwa okno turtle
        print("")
        print("")
        startUp()  # uruchamia grę od nowa


# Mainline
startUp()


