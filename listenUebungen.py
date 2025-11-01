import math
import random

ListeDef = [ 1, 2, 3, 4, 5 ]
for zahl in ListeDef:
    print("Die Zahl ist:", zahl)

namenslISTE = ["Anna", "Bernd", "Clara"]
namenslISTE.append("David")

listeLoeschen = [10, 20, 30, 40, 50]
listeLoeschen.remove(30)
print("Aktualisierte Liste:", listeLoeschen)
print("Länge der Liste", len(namenslISTE))
if 10 in listeLoeschen:
    print("10 ist in der Liste enthalten.")
else:
    print("10 ist nicht in der Liste enthalten.")

Wochentage = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")
for tag in Wochentage:
    print("Wochentag:", tag)

listeZUfalligerZahlen = []
for i in range(5):
    random_zahl = random.randint(1, 100)
    print("Zufällige Zahl zwischen 1 und 100:", random_zahl)
    listeZUfalligerZahlen.append(random_zahl)
listeZUfalligerZahlen.sort()
print("Sortierte Liste zufälliger Zahlen:", listeZUfalligerZahlen)

tupleBeispiel = (1,2,3,4,5)
print("Element bei Index 2 im Tuple:", tupleBeispiel[2])
listeTuple = list (tupleBeispiel)
listeTuple.append(6)
print("Aktualisierte Liste aus Tuple:", listeTuple)
