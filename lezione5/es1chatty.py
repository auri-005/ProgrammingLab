class Cliente():
    def __init__(self, nome, cognome, lista_acq):
        self.nome = nome
        self.cognome = cognome
        self.lista_acq = lista_acq
    def saluta(self):
        print(f"Il cliente {self.nome} {self.cognome} ha acquistato:")
        for prodotto in self.lista_acq:
            print(prodotto)
class Commesso():
    def __init__(self, nome, cognome, lista_vend):
        self.nome = nome
        self.cognome = cognome
        self.lista_vend = lista_vend
    def saluta(self):
        print(f"Il commesso {self.nome} {self.cognome} ha venduto:")
        for prodotto in self.lista_vend:
            print(prodotto)
prodotti1 = ["Pane", "Latte", "Farina", "Uova"]
c1 = Cliente("Aurora", "Gardisan", prodotti1)
prodotti2 = ["Ciliege", "Uova", "Acqua"]
c2 = Commesso("Simone", "Rossi", prodotti2)

Commesso.saluta(c2)
Cliente.saluta(c1)