import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"{self.a}*x^2+{self.b}*x+{self.c}")

    def oblicz_wartosc(self, x):
        return self.a * x * x + self.b * x + self.c

    def rozwiaz(self):
        if self.a == 0 and self.b == 0:
            if self.c == 0:
                return float("inf"), float("inf")
            else:
                return float("nan"), float("nan")
        if self.a == 0:
            return -self.c/self.b, -self.c/self.b
        delta = self.b**2 - 4*self.a*self.c
        if delta < 0:
            return float("nan"), float("nan")
        return (-self.b-math.sqrt(delta))/(2*self.a), (-self.b+math.sqrt(delta))/(2*self.a)

def main():
    f1 = FunkcjaKwadratowa(2, 3, 1)
    f1.wypisz()
    print(f1.oblicz_wartosc(0))
    print(f1.oblicz_wartosc(1))

    print(FunkcjaKwadratowa(0, 0, 0).rozwiaz())
    print(FunkcjaKwadratowa(0, 0, 1).rozwiaz())
    print(FunkcjaKwadratowa(0, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, -5, 6).rozwiaz())
    print(FunkcjaKwadratowa(1, 4, 4).rozwiaz())

if __name__ == "__main__":
    main()