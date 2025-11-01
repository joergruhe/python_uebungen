from typing import String
from math import sqrt
from calendar import calendar

def Begruessung():
    return "Hallo, willkommen zu meinen Funktionen!"

def berechne_qudrat(zahl : int) -> int:
    return zahl ** 2

def addiere(a : int, b : int) -> int:
    return a + b

def ist_gerade(zahl : int) -> bool:
    return zahl % 2 == 0

def celsius_zu_fahrenheit(celsius : float) -> String:
    Fahreninheit = (celsius * 9/5) + 32
    return f"{Fahreninheit} °F"

def max_in_Liste(liste : list[int]) -> int:
    return max(liste)

def berechneQuadratwurzel(zahl : float) -> float:
    if zahl < 0:
        raise ValueError("Die Zahl darf nicht negativ sein.")
    return sqrt(zahl)

def zeige_Kalender(jahr : int, monat : int) -> String:
    return calendar.month(jahr, monat)
