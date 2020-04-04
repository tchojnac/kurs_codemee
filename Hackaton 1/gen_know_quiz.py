import time

score=int()
print("Witamy w quizie wiedzy ogólnej")
time.sleep(2)
print("Pytanie 1")
time.sleep(2)
Question1 = input ("Numer rejestracyjny samochodu z jakiego miasta zaczyna się ‘PO’? ")
if Question1 == ("Poznań") or Question1 == ("Polkowice"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to Poznań")
time.sleep(2)
print("Pytanie 2")
time.sleep(2)
Question2 = input("W jakim mieście jest Pałac Namiestnikowski? ")
if Question2 == ("Warszawa") or Question2 == ("Kraków"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to Warszawa")
time.sleep(2)
print("Pytanie 3")
time.sleep(2)
Question3 = input("Ile godzin jest w roku przestępnym? ")
if Question3 == ("8784"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to 8784")
time.sleep(2)
print("Pytanie 4")
time.sleep(2)
Question4 = input("W jakim sporcie można wygrać ligę mistrzów? ")
if Question4 == ("Piłka nożna") or Question4 == ("Tenis"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to Piłka Nożna")
time.sleep(2)
print("Pytanie 5")
time.sleep(2)
Question5 = input("Jakie miasto jest stolicą Francji? ")
if Question5 == ("Paryż") or Question5 == ("Marsylia"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to Paryź")
time.sleep(2)
print("Question 6")
time.sleep(2)
Question6 = input("Ile złotych gwiazdek jest we fladze Unii Europejskiej? ")
if Question6 == ("dwanaście") or Question6 == ("dwadzieścia") or Question6 == ("trzydzieści"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to dwanaście")
time.sleep(2)
print("Pytanie 7")
time.sleep(2)
Question7 = input("Kiedy zaczęła nadawać telewizja Polska? ")
if Question7 == ("1952"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to 1952")
time.sleep(2)
print("Pytanie 8")
time.sleep(2)
Question8=input("W którym roku prezydentem został Andrzej Duda? ")
if Question8 == ("2015"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to 2015")
time.sleep(2)
print("Pytanie 9")
time.sleep(2)
Question9 = input("Ile to jest trzy-czwarte z 112? ")
if Question9 == ("84") or Question9  == ("48"):
    print("Prawidłowa odpowiedź")
    score = score + 1
else:
    print("Nieprawidłowa odpowiedź, prawidłowa to 84")
time.sleep(2)
print("Pytanie 10")
time.sleep(2)
Question10 = input("Który typ kąta jest większy od 90 stopni ale mniejszy od 180 stopni? ")
if Question10 == ("rozwarty") or ("ostry"):
    print("Prawidłowa odpowiedź")
    score = score + 1
time.sleep(2)
print("Koniec quizu")
time.sleep(1)
print("Otrzymałeś",(score),"/ 10")
num1 = (score)
num2 = 10
print('{0:.2f}%'.format((num1 / num2 * 100)))