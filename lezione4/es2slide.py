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
    

class Auto(Veicolo):
    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno) #li prende dalla classe madre(veicolo)
        self.numero_porte = numero_porte
    def __str__(self):
        return ('veicolo "{}", "{}", "{}", "{}", "{}"'.format(self.modello, self.marca, self.anno, self.speed, self.numero_porte))

class Moto(Veicolo):
    def __init__(self, modello, marca, anno,tipo):
        super().__init__(modello,marca,anno)
        self.tipo = tipo
    def __str__(self):
        return ('veicolo "{}", "{}", "{}", "{}", "{}"'.format(self.modello, self.marca, self.anno, self.speed, self.tipo))
    
macchina = Auto('500', 'Fiat', '2006', '3')
print(macchina)
 
 
bike = Moto('ducati', 'rossa', '2980', 'sportiva')
print (bike)