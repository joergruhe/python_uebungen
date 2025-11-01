print("Hello World")
a = 5
b = 10
print("Summe:", a + b)
s  = input("Geben Sie etwas ein: ")
print("Sie haben eingegeben:", s)
Laenge = input("Geben Sie die Länge ein: ")
Breite = input("Geben Sie die Breite ein: ")
Flaeche = float(Laenge) * float(Breite)
print("Die Fläche beträgt:", Flaeche)
TestType = type(Flaeche)
print("Der Typ der Fläche ist:", TestType)
qua = input("Zu quadrierende Zahl eingeben: ")
quadriert = float(qua) ** 2
print("Das Quadrat der Zahl ist:", quadriert)
celsius = input("Geben Sie die Temperatur in Celsius ein: ")
fahrenheit = (float(celsius) * 9/5) + 32
print("Die Temperatur in Fahrenheit ist:", fahrenheit)
zahl1 = input("Geben Sie die erste Zahl ein: ")
zahl2 = input("Geben Sie die zweite Zahl ein: ")
c = zahl1
zahl1 = zahl2
zahl2 = c
print("Nach dem Tausch: Zahl 1 =", zahl1, ", Zahl 2 =", zahl2)
Laufzeit = float(input("Geben Sie die Laufzeit in Jahren ein: "))
Zinsrate = float(input("Geben Sie die jährliche Zinsrate in Prozent ein: "))
Kapital = float(input("Geben Sie das Anfangskapital ein: "))
Endkapital = Kapital * (1 + Zinsrate / 100) ** Laufzeit
print("Das Endkapital nach", Laufzeit, "Jahren beträgt:", Endkapital