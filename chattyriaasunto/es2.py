class Cliente:
    def __init__(self, nome, cognome, lista_acq):
        self.nome = nome
        self.cognome = cognome
        self.lista_acq = lista_acq

    def saluta(self):
        print(f"Il cliente {self.nome} {self.cognome} ha acquistato:")
        for prodotto in self.lista_acq:
            print(prodotto)


class Commesso:
    def __init__(self, nome, cognome, lista_vend):
        self.nome = nome
        self.cognome = cognome
        self.lista_vend = lista_vend

    def saluta(self):
        print(f"Il commesso {self.nome} {self.cognome} ha venduto:")
        for prodotto in self.lista_vend:
            print(prodotto)

    def check(self, cliente):
        for prodotto in cliente.lista_acq:
            if prodotto not in self.lista_vend:
                return False
        return True


def check_cl_com(lista_clienti, lista_commessi):
    for cliente in lista_clienti:
        trovato = False

        for commesso in lista_commessi:
            if commesso.check(cliente) == True:
                trovato = True
                break

        if trovato == False:
            return False

    return True


# --- CREAZIONE OGGETTI ---
prodotti_cliente1 = ["Pane", "Latte", "Farina", "Uova"]
c1 = Cliente("Aurora", "Gardisan", prodotti_cliente1)

prodotti_cliente2 = ["Acqua", "Uova"]
c2 = Cliente("Marco", "Bianchi", prodotti_cliente2)

prodotti_commesso1 = ["Pane", "Latte", "Farina", "Uova", "Acqua"]
co1 = Commesso("Simone", "Rossi", prodotti_commesso1)

prodotti_commesso2 = ["Ciliege", "Uova", "Acqua"]
co2 = Commesso("Luca", "Verdi", prodotti_commesso2)

# --- LISTE ---
lista_clienti = [c1, c2]
lista_commessi = [co1, co2]

# --- TEST ---
co1.saluta()
c1.saluta()

print("Il commesso co2 può soddisfare c1?", co2.check(c1))
print("Tutti i clienti possono essere soddisfatti da almeno un commesso?",
    check_cl_com(lista_clienti, lista_commessi))