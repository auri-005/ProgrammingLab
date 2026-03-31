class Canguro():
    def __init__(self, contenuto_tasca= None): # def __init__(self, contenuto_tasca=[]): errore!! si inserisocno gli oggetti sia in can sia un guro
        if contenuto_tasca is None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)
    def __str__(self):
        return f"Il canguro ha : {self.contenuto_tasca}"
    

can = Canguro()
guro = Canguro()
can.intasca('wallet')
print(can)
print(guro)