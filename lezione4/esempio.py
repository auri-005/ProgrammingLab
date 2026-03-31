# Creareuna classe coin che ha come attributo il valore della faccia
# due metodi:
#○ uno che simula il lancio della moneta e che salva il valore sull'attributo faccia.
#○ uno che ritorna il valore dell'attributo faccia
import random
class Coin():
    def __init__(self, faccia):
        self.faccia = faccia

    def lanciare(self):
        if random.randint(0,1) == 0:
            self.faccia = 'Testa'
        else:
            self.faccia = 'Croce'
    
    def che_faccia(self):
        return self.faccia

moneta = Coin('Testa')
moneta.lanciare()
print(moneta.che_faccia())
