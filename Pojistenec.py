
class Pojistenec:

    def __init__(self,jmeno,prijmeni,vek,telefon,email,ulice,mesto,psc):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        self.email=email
        self.ulice=ulice
        self.mesto=mesto
        self.psc=psc

    def __str__(self):
        return f"{self.jmeno}\t {self.prijmeni}\t {self.vek}\t {self.telefon}\t {self.email}\t {self.ulice}\t {self.mesto}\t {self.psc}"


