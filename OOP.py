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
    def __init__(self, szoba, datum, nev):
        self.szoba=szoba
        self.datum=datum
        self.nev=nev

class FoglalasKezeles:
    def __init__(self, szalloda):
        self.szalloda=szalloda
        self.foglalasok=[]

    def foglalas(self, szobaszam, datum, nev):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam==szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum, nev))
                return szoba.ar
        return None

    def lemondas(self, szobaszam, datum, nev):
