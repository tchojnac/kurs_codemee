#BMI = (65/1.62)**2
waga = int(input("Podaj wage w kg: "))
wzrost = float(input("Podaj wsrost w m: "))
bmi = waga / wzrost **2
print("Moje BMI to: ", bmi)