from tokenize import String


String1 = "Joerg Ruhe"
print(String1," Länge von Name1:", len(String1))
AnzahlBuchstaben = String1.count("r")
print("Anzahl der Buchstaben 'r' in Name1:", AnzahlBuchstaben)
String1_upper = String1.upper()
print("Name1 in Großbuchstaben:", String1_upper)
String1_lower = String1.lower()
print("Name1 in Kleinbuchstaben:", String1_lower)
String1 = String1.swapcase()
print("Name1 mit vertauschten Groß-/Kleinbuchstaben:", String1)
Satz ="Das ist ein Beispielsatz."
SatzListe = Satz.split(" ")
print("Satz in Liste von Wörtern aufgeteilt:", SatzListe)
SatzBindestrich = "-".join(SatzListe)
print("Satz mit Bindestrichen verbunden:", SatzBindestrich)
SatzBindestrich_ersetzt = SatzBindestrich.replace("-", " ")
print("Satz mit Bindestrichen durch Leerzeichen ersetzt:", SatzBindestrich_ersetzt)
Test1 = "  Text mit Leerzeichen  "
Test2 = "\tText mit Tabs\t"
TestVariable = " {} nächdstes Wort {} ".format(Test1, Test2)
print(TestVariable)
Test4 = f"format String {Test1} nächstes Wort {Test2} "
if "Text" in TestVariable:
    print("'Text' ist in TestVariable enthalten.")