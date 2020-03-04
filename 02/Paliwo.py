#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km
#wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

l_per_100 =float(input("Podaj spalanie na 100km: "))
distance = int(input("Jak daleko jedziemy? "))
price_per_l = 5.04

total = price_per_l * distance/100 * l_per_100
print(round(total, 2))

