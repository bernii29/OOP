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