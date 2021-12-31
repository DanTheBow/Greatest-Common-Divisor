# Der größte gemeinsame Teiler (ggT) von zwei Zahlen
# ist die größte Zahl, durch die man beide Zahlen teilen kann.
# Beispiel: Größter gemeinsamer Teiler von 4 und 6 ist 2.
# Die englische Bezeichnung ist greatest common divisor (gcd) für ggT.

def gcd(a, b):
    while a != b:
        if b > a:
            a, b = b, a
        a = a - b
    return a
