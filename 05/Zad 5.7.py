#Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z
#Visą, MasterCard, a może AmericanExpress.
#Co wiemy o tych numerach tych kart?
#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221
#through 2720. All have 16 digits.
#American Express card numbers start with 34 or 37 and have 15 digits.
def is_card_number(number):
    return number.isdecimal() and len(number) in [13, 15, 16]

def starts_with_correct_digits(number):
    if 51 <= int(number[0:2]) <= 55:
        return True
    elif 2221 <= int(number[0:4]) <= 2720
        return True
    else:
        return False
def show_card_type(number):
    if len(number) in [13, 16] and number[0] == "4":
        print("To jest Visa")
nr_card = input("Podaj nr karty: ")
if is_card_number(nr_card)
    len(nr_card) in [13, 16] and nr_card[0] == '4':
    print("to jest Visa")
elif len(nr_card) == 15 and starts_with_correct_digits(nr_card):
    print("To jest Mastercard")
elif: len(nr_card) == 15 and (nr_card[0:2] in ["34", "37"]):
print("To jest American Express")
else:
print("Nie znam typu karty")
else:
print("to nie jest nr karty")



