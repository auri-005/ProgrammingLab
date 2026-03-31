class Poligono():
    def lati(self, lati):
        self.lati = lati
    def descrizione(self):
        return(f'Sono un poligono con {self.lati} lati')

class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    def descrizione(self):
        return('Sono un quadrilatero')

class Rettangolo(Quadrilatero):
    def parametri(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    def descrizione(self):
        return(f'Sono un rettangolo di {self.lato} lato e {self.altezza} altezza')
    def perimetro(self):
        return 2 * (self.base + self.altezza)
    def area(self):
        return self.base * self.altezza

class Triangolo(Poligono):
    def parametri(self, lato1, lato2, lato3):
        super().__init__()
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
    def descrizione(self):
        return (f'Sono un triangolo con lato1 {self.lato1}, lato2 {self.lato2}, e lato3 {self.lato3}')
    def perimetro(self):
        return (self.lato1 + self.lato2 + self.lato3)
    def is_equilatero(self):
        if self.lato1 == self.lato2 and self.lato3 == self.lato1:
            return True
        else:
            return False

#ESEMPIO UTILIZZO:
p = Poligono(5)
print(p.descrizione())

q = Quadrilatero()
print(q.descrizione())

r = Rettangolo(4, 6)
print(r.descrizione())
print("Perimetro:", r.perimetro())
print("Area:", r.area())

t = Triangolo(3, 3, 3)
print(t.descrizione())
print("Perimetro:", t.perimetro())
print("Equilatero:", t.is_equilatero())