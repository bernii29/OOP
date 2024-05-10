from datetime import datetime

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

    def szobahozzaad(self, szoba):
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

def interfesz(foglalaskezelo):
    while True:
        print("Mit szeretne csinálni?")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas=int(input("Adja meg a művelet számát!"))

        if valasztas==1:
            szobaszam=int(input("Adja meg a szoba számát!"))
            datum=input("Adja meg a foglalás dátumát!")
            foglalaskezelo.foglalas(szobaszam, datum)
        elif  valasztas==2:
            szobaszam = int(input("Adja meg a szoba számát!"))
            datum = input("Adja meg a lemondás dátumát!")
            foglalaskezelo.lemondas(szobaszam, datum)
        elif valasztas==3:
            foglalaskezelo.listazas()
        elif valasztas==4:
            break
