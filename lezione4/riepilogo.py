"""
#esempio1
import random
class Coin():

    def __init__(self, faccia):
        self.faccia = faccia
    def lancio(self):
        if random.randint(0,1) == 0:
            self.faccia = 'Croce'
        else:
            self.faccia = 'Testa'
    def ritorno(self):
        return self.faccia
moneta = Coin('croce')
moneta.lancio()
print(moneta.ritorno())

#es1
class Veicolo():
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca 
        self.speed = 0
    def __str__(self):
        return (f"Marca : {self.marca}, modello: {self.modello}, anno: {self.anno}, velocità: {self.speed}")
    def accellerare(self):
        self.speed += 5
    def frenare(self):
        self.speed -= 5
    def get_speed(self):
        return (f"velocità corrente: {self.speed}")

#es2
class CSVFile():

    def __init__(self, name_file):
        self.name_file = name_file
    def get_data(self):
        lista = []
        my_file = open(self.name_file, "r")
        for line in my_file:
            element = line.split(",")
            lista.append(element)
        my_file.close()
        return lista
"""
