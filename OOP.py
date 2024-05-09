class Szoba:
    def __init__(self, szobaszam: int, ar: int):
        self.szobaszam=szobaszam
        self.ar=ar

class EgyagyasSzoba:
    def __init__(self, szobaszam: int, ar: int):
        super().__init__(szobaszam, ar)

class KetagyasSzoba:
    def __init__(self, szobaszam: int, ar: int):
        super().__init__(szobaszam, ar)

class Szalloda:
    def __init__(self, nev):
        self.szobak=[]

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba=szoba
        self.datum=datum

class FoglalasKezeles:
    def __init__(self, szalloda):
        self.szalloda=szalloda
        self.foglalasok=[]

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam==szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                return szoba.ar
        return None

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam==szobaszam and foglalas.datum==datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def listazas(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")