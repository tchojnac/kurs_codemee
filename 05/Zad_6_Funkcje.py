zawodnik_1 = input("Jak masz na imię 1: ")
zawodnik_2 = input("Jak masz na imię 2: ")

zawodnik_1_odpowiedz = input(" %s: Wybiez kamien papier lub nozyce: " % zawodnik_1)
zawodnik_2_odpowiedz = input(" %s: Wybiez kamien papier lub nozyce: " % zawodnik_2)

def porownaj(odp_1, odp_2):
    if odp_1 == odp_2:
        return("remis")
    elif odp_1 == "kamien":
         if odp_2 == "nozyce":
             return("kamien wygrywa")
         else:
             return("papier wygrywa")
    elif odp_1 == "nozyce":
         if odp_2 == "papier":
             return("nozyce wygrywaja")
         else:
             return("kamien wygrywa")
    elif odp_1 == "kamien":
        if odp_2 == "papier":
            return("papier wygrywa")
        else:
            return("nozyce wygrywaja")
    else:
        print("To nie jest prawidłowy wybór")
        sys.exit()


