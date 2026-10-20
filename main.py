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