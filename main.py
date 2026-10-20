#szam = 5 (eredetileg csak számot írtam, így is működött, de megnéztem a bekérést neten)
szam = float(input("Adj meg egy számot: "))

if szam > 0:
    print("Pozitív szám")
elif szam < 0:
    print("Negatív szám")
else:
    print("Nulla")

if szam % 2 == 0:
    print ("Páros")
else:
    print("Páratlan")

osztalyzat = float(input("Osztályzatod: "))

if osztalyzat == 1:
    print("elégtelen")
elif osztalyzat == 2:
    print("elégséges")
elif osztalyzat == 3:
    print("közepes")
elif osztalyzat == 4:
    print("jó")
elif osztalyzat == 5:
    print("jeles")
else:
    print("Hibás osztályzat")

def koszones():
    print("Szia! Örülök, hogy itt vagy!")

koszones()

def korEll():
    eletkor = float(input("Hány éves vagy?"))
    if eletkor >= 18:
        print("Nagykorú vagy!")
    else:
        print("Még nem vagy nagykorú")

korEll()