#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
#utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = input("Podaj dowolne dwa wyrazy: ")
s2 = input("Podaj dowolny wyraz: ")
middle = len(s1)//2

print(s1[0:middle] + ' ' + s2 + ' ' + s1[middle::])


