
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

osztalyzat = int(input("Osztályzatod: "))

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

def korEll():
    eletkor = float(input("Hány éves vagy?"))
    if eletkor >= 18:
        print("Nagykorú vagy!")
    else:
        print("Még nem vagy nagykorú")

def belepes():
    jelszo = input("Jelszo ")
    if jelszo == "python123":
        print("Sikeres belépés!")
    else:
        print("Hibás jelszó")

belepes()

def paros_vizsgalat():
    numb = float(input("Írj be megint egy számot"))
    if numb % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")



def vizsgal(szam:float):
    if szam > 0:
        print("Pozitív szám")
    elif szam < 0:
        print("Negatív szám")
    else:
        print("Nulla")

def belepes():
    felhasznalo = input("Felhasználó név:")
    if felhasznalo == "attila":
        jelszo = input("Jelszó:")
        if jelszo == "python":
            print("Sikeres belépés")
        else:
            print("Hibás jellszó")

    else:
        print("Ismeretlen felhasznló")

def jegy(szazalek):
    if szazalek < 0 or szazalek > 100:
        print("Hibás százalék!")
    elif szazalek < 40:
        print("Elégtelen")
    elif szazalek < 55:
        print("Elégésges")
    elif szazalek < 70:
        print("Közepes")
    elif szazalek < 85:
        print("Jó")
    else:
        print("Jeles")


koszones()

korEll()

paros_vizsgalat()

szam = float(input("Adj meg egy számot: "))
vizsgal(szam)

belepes()

szazalek = float(input("Add meg a százalékot"))
jegy(szazalek)

