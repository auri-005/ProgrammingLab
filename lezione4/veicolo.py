class Veicolo():
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__(self):
        stringa = "Veicolo -> Marca : {}, Modello: {}, Anno: {}, Velocità: {} "
        return stringa.format(self.marca, self.modello, self.anno, self.speed)
#oppure return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Velocità: {self.speed}"
    def accellerare(self):
        self.speed += 5
    def frenare(self):
        self.speed -= 5
    def get_speed(self):
        return self.speed

