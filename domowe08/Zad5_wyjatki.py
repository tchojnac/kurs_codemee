#W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
#Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

import bmi

def fix_string(user_imput, unit):
    if unit in user_imput:
        container = ''
        for char in user_imput:
            if char.isnumeric() or char == '.':
                container += char
                return float(container)
            else:
                return -1
while True:
    weight = input("Podaj wage kg: ")

    try:
        float(weight)
    except ValueError:
        print('value error')
    #breakpoint() #co sie dzieje w kodzie blad
        w = fix_units(weight, 'kg')

        if w == -1:
            print('wartosc nieprawidlowa')
    else:
        break

else:
    w = float(weight)
    break
print(w)

height = input("Podaj wzrost w m: ")
try:
    float(height)
except ValueError as e:
    h = fix_units(height, 'm')
    if h == -1:
        print('wartosc nieprawidlowa')
        else:
        h = float(height)
print(h)

result_bmi = bmi.calculate_bmi(w, h)
state = bmi.get_state(result_bmi)
print(state)
filename = state.lower() + '.txt'
with open(filename) as fopen:
    tip = fopen.read()

    print(tip)

