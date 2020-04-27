students = {"Tomek": 25, "Marek": 20, "Leszek":23, "Mirek": 21, "Zenek": 22}


def print_student_age():
    while True:
        try:
            name = input("Podaj imię studenta: ")
            print(students[name])
            break
        except:
            print("Imię nie jest zarejestrowane")


print_student_age()