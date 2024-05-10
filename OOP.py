from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam=szobaszam
        self.ar=ar

    def tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def tipus(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev=nev
        self.szobak=[]

    def szobahozzaad(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba=szoba
        self.datum=datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda=szalloda
        self.foglalasok=[]

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam==szobaszam:
                foglalas_datum=datetime.strptime(datum, '%Y-%m-%d')
                if foglalas_datum < datetime.now():
                    print("A foglalás dátuma már elmúlt.")
                    return None
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam==szobaszam and foglalas.datum==foglalas_datum:
                        print("A szoba ekkor már foglalt.")
                        return None
                self.foglalasok.append(Foglalas(szoba, foglalas_datum))
                return szoba.ar
        print("Nincs ilyen szoba.")
        return None

    def lemondas(self, szobaszam, datum):
        lemondas_datum=datetime.strptime(datum, '%Y-%m-%d')
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam==szobaszam and foglalas.datum==lemondas_datum:
                self.foglalasok.remove(foglalas)
                print("A foglalás sikeresen lemondva.")
                return
        print("Nincs ilyen foglalás.")

    def listaz(self):
        if self.foglalasok:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")
        else:
            print("Nincs foglalás.")

def felhasznaloi_interfesz(foglalaskezelo):
    while True:
        print("Válasszon egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Adja meg a kívánt művelet számát: ")

        if valasztas=="1":
            szobaszam=input("Adja meg a foglalandó szoba számát: ")
            datum=input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            foglalaskezelo.foglalas(szobaszam, datum)
        elif valasztas=="2":
            szobaszam=input("Adja meg a lemondandó foglalás szoba számát: ")
            datum=input("Adja meg a lemondás dátumát (ÉÉÉÉ-HH-NN): ")
            foglalaskezelo.lemondas(szobaszam, datum)
        elif valasztas=="3":
            foglalaskezelo.listaz()
        elif valasztas=="4":
            break
        else:
            print("Érvénytelen választás. Kérjük, válasszon újra.")

def main():
    szoba1=EgyagyasSzoba("101", 1000)
    szoba2=EgyagyasSzoba("102", 1500)
    szoba3=KetagyasSzoba("103", 2000)

    szalloda = Szalloda("GDE Szálloda")

    szalloda.szobahozzaad(szoba1)
    szalloda.szobahozzaad(szoba2)
    szalloda.szobahozzaad(szoba3)

    foglalaskezelo=FoglalasKezelo(szalloda)

    foglalaskezelo.foglalas("101", "2024-06-03")
    foglalaskezelo.foglalas("102", "2024-07-03")
    foglalaskezelo.foglalas("103", "2024-08-05")
    foglalaskezelo.foglalas("101", "2024-07-07")
    foglalaskezelo.foglalas("102", "2024-08-09")

    felhasznaloi_interfesz(foglalaskezelo)

if __name__=="__main__":
    main()
