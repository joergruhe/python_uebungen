note = int(input("Bitte geben Sie eine Zahl von 1 bis 100 ein: "))
if 90 <= note <= 100:
    print("Ihre Note ist: Sehr Gut")
elif 80 <= note < 90:
    print("Ihre Note ist: Gut")
elif 70 <= note < 80:
    print("Ihre Note ist: Befriedigend")
elif 60 <= note < 70:
    print("Ihre Note ist: Ausreichend")
elif 50 <= note < 60:
    print("Ihre Note ist: Mangelhaft")
elif 0 <= note < 50:
    print("Ihre Note ist: Ungenügend")
else:
    print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 100 ein.")

zahlnullen = int(input("Geben Sie eine Zahl ein, um die Anzahl der Nullen zu bestimmen: "))
if zahlnullen < 0:
    print ("Zahl ist negativ", zahlnullen)
elif zahlnullen == 0:
    print ("Zahl ist null", zahlnullen)
else:
    print ("Zahl ist positiv", zahlnullen)

summe = 0
for i in range(1, 101):
    summe += i
print("Die Summe der Zahlen von 1 bis 100 ist:", summe)

for i in range(1, 21):
    if i % 2 == 0:
        print(i, "ist eine gerade Zahl.")
    else:
        print(i, "ist eine ungerade Zahl.")

RichtigeZahl = 44
Benutzereingabe = input("Geben sie ihre Zahl ein: ")
while Benutzereingabe != RichtigeZahl:
    if int(Benutzereingabe) < RichtigeZahl:
        print("Die eingegebene Zahl ist zu klein. Bitte erneut versuchen.")
    else:
        print("Die eingegebene Zahl ist zu groß. Bitte erneut versuchen.")
    Benutzereingabe = int(input("Geben sie ihre Zahl ein: "))
print("Herzlichen Glückwunsch! Sie haben die richtige Zahl erraten.")