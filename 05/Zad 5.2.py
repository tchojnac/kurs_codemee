#Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi
#na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
#(niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

#funkcja obliczająca bmi ,- waga wzrost
def calculate_bmi(weight, height):
    return weight /height ** 2

#funkcja podająca wartość
def get_state(bmi):
    if bmi < 18:
        print("Niedowaga")
    elif bmi < 25:
        print("Waga normalna")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")

#reszta kodu
#podaj wagę i wzrost
weight = float(input("Podaj wagę[kg]:"))
height = float(input("Podaj wzrost[m]:"))
# wyślij wagę i wzrost do funkcji obliczającej BMI
result_bmi = calculate_bmi(w, h)
get_state(result_bmi)