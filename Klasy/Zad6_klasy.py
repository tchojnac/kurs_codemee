#Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
#Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków
# #oraz minimalną składkę zdrowotną.
#Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
# Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#Wszyscy pracownicy mają wspólną nazwę firmy.
# Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
#Adam Kowalski Love Python Company
#email -> smkwlsk@lovepythoncompany.com

class Employee:

    def __init__(self, name, lastname, position, salary, exp):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.salary = salary
        self.exp = exp
    def show(self):
        print(f"{self.lastname} | {self.position}")
        print(f"{self.salary} | PLN - exp: {self.exp} years")
    def salary_bump(self):
        self.salary = self.salary * 1.11
        print('New salary: ', self.salary)

p1 = Employee('Jan', 'Kowalski', 'QA', '4500', 1.5)
p1.show()
print("-------bump------")
p1.salary_bump()
p1.show()