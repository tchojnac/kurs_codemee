#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku:
#niedowaga / waga normalna / nadwaga / otyłość.
#if 18 < bmi < 25:

waga = int(input("Podaj wage w kg: "))
wzrost = float(input("Podaj wsrost w m: "))
bmi = waga / wzrost **2
print("Moje BMI to: ", round(bmi, 2))

if bmi < 18:
    print("niedowaga")
elif bmi < 25:
    print("norma")
elif bmi < 30:
    print("nadwaga")
else:
    print("otylosc")