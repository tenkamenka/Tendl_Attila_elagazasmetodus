
# szam = float(input("Adj meg egy számot: "))
#
# if szam > 0:
#     print("Pozitív szám")
# elif szam < 0:
#     print("Negatív szám")
# else:
#     print("Nulla")
#
# if szam % 2 == 0:
#     print ("Páros")
# else:
#     print("Páratlan")
#
# osztalyzat = float(input("Osztályzatod: "))
#
# if osztalyzat == 1:
#     print("elégtelen")
# elif osztalyzat == 2:
#     print("elégséges")
# elif osztalyzat == 3:
#     print("közepes")
# elif osztalyzat == 4:
#     print("jó")
# elif osztalyzat == 5:
#     print("jeles")
# else:
#     print("Hibás osztályzat")
#
# def koszones():
#     print("Szia! Örülök, hogy itt vagy!")
#
# koszones()
#
# def korEll():
#     eletkor = float(input("Hány éves vagy?"))
#     if eletkor >= 18:
#         print("Nagykorú vagy!")
#     else:
#         print("Még nem vagy nagykorú")
#
# korEll()
#
# def belepes():
#     jelszo = input("Jelszo ")
#     if jelszo == "python123":
#         print("Sikeres belépés!")
#     else:
#         print("Hibás jelszó")
#
# belepes()
#
# def paros_vizsgalat():
#     numb = float(input("Írj be megint egy számot"))
#     if numb % 2 == 0:
#         print("Páros")
#     else:
#         print("Páratlan")
#
# paros_vizsgalat()

def vizsgal(szam:float):
    if szam > 0:
        print("Pozitív szám")
    elif szam < 0:
        print("Negatív szám")
    else:
        print("Nulla")

szam = float(input("Adj meg egy számot: "))
vizsgal(szam)

def belepes():
    felhasznalo = input("Felhasználó név:")
    jelszo = input("Jelszó:")
    if felhasznalo == "attila" and jelszo == "python":
        print("Sikeres belépés")
    else:
        print("Helytelen adatok")

belepes()

