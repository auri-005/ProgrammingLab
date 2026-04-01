class Dispositivo():
    def __init__(self, marca, modello):
        self.marca = marca 
        self.modello = modello 
    def __str__(self):
        return (f"Dispositivo: marca= {self.marca}, modello= {self.modello}")
    
class Smartphone(Dispositivo):
    def __init__(self, marca, modello, memoria_gb):
        super().__init__(marca, modello)
        self.memoria_gb = memoria_gb
    def __str__(self):
        return(f"Smartphone: marca= {self.marca}, modello={self.modello}, memoria gb={self.memoria_gb}")
class Laptop(Dispositivo):
    def __init__(self, marca, modello, dimensione_schermo):
        super().__init__(marca, modello)
        self.dimensione_schermo = dimensione_schermo
    def __str__(self):
        return(f"Laptop: marca={self.marca}, modello={self.modello}, dimensione schermo={self.dimensione_schermo}")

d = Dispositivo("Apple", 13)
S = Smartphone("Samsung", "Galaxy 10", 256)
L = Laptop("Samsung","Tab 4", "13 pollici")

print(d)
print(L)
print(S)