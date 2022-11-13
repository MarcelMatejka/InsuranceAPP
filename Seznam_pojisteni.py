import datetime

class Pojisteni:

    Nazev = ""
    Castka = int()
    Predmet = ""
    Platnost_od = datetime.datetime.now()
    Platnost_do = datetime.datetime.now()

    def __init__(self,Nazev,Castka,Predmet,Platnost_od,Platnost_do):
        self.nazev = Nazev
        self.castka = Castka
        self.predmet = Predmet
        self.platnost_od = Platnost_od
        self.platnost_do = Platnost_do

        # Vrátí textovou reprezentaci pojisteni
    def __str__(self,Nazev,Castka,Predmet,Platnost_od,Platnost_do):
        return f"Název: {0}, Častka {1}, Předmět {2}, Platnost od: {3}, Platnost do {4}" .format(self.nazev, self.castka, self.predmet, self.platnost_od, self.platnost_do)

print(pojisteni)