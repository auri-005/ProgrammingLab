"""
#esercizio 
class Canguro():
    def __init__(self, contenuto_tasca = None):
        if contenuto_tasca is None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)
    def __str__(self):
        return (f"L'oggetto contenuto nella tasca è: {self.contenuto_tasca}")

can = Canguro()
guro = Canguro()
can.intasca("portafoglio")
can.intasca("borraccia")


print(can)
print(guro)

#es1
import random
#classi originali
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str(self):
        return f'Person {self.name}, {self.surname}'
    def saluta(self):
        random_number = random.randint(0,2)
        if random_number == 0:
            print(f"Hello, I am {self.name}, {self.surname}")
        elif random_number == 1:
            print(f"Hi, I am {self.name}!")
        elif random_number == 2:
            print(f"Yo bro! {self.name} here!")

class Studente(Person):
    def __init__(self, nome, cognome, corso):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = corso
    def saluta(self):
        Person.saluta(self)
        print(f"Frequento il corso: {self.corso}")

class Docente(Person):
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente units", nome, cognome)
        self.corso = corso
    def saluta(self):
        Person.saluta(self)
        print(f"Insegno i corsi: {self.corso}")

#classi modificate 
class Studente(Person):
    def __init__(self, name, surname, corso):
        super().__init__(name, surname)
        self.corso = corso
    def saluta(self):
        Person.saluta(self)
        print(f"I corsi frequentati di {self.name} {self.surname}:")
        for corso in self.corso :
            print (corso)
class Docente(Person):
    def __init__(self, name, surname, corso):
        super().__init__(name, surname)
        self.corso = corso
    def saluta(self):
        Person.saluta(self)
        print(f"I corsi insegnati dal docente {self.name} {self.surname} sono :")
        for corso in self.corso:
            print(corso)

corsiS = ['Programmazione', 'Scienze', 'Storia', 'Informatica']
corsiD = ['Algebra lineare', 'Matematica 1']
s = Studente("Enrico", "Rossi", corsiS)
s.saluta()
d = Docente("Matteo", "Gallet", corsiD)
d.saluta()

#es2
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
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
    def __str__(self):
        return(f"Modello: {self.modello}, marca: {self.marca}, anno:{self.anno}, velocità: {self.speed}, numero di porte: {self.numero_porte}")

class Moto(Veicolo):
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo 
    def __str__(self):
        return(f"Modello: {self.modello}, marca: {self.marca}, anno:{self.anno}, velocità: {self.speed}, tipo: {self.tipo}")

a = Auto("Panda", "Fiat", 2010, 5)
m = Moto("Ninja", "Kawasaki", 2022, "sportiva")

print(a)
print(m)

#es3
import random
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str(self):
        return f'Person {self.name}, {self.surname}'
    def saluta(self):
        random_number = random.randint(0,2)
        if random_number == 0:
            print(f"Hello, I am {self.name}, {self.surname}")
        elif random_number == 1:
            print(f"Hi, I am {self.name}!")
        elif random_number == 2:
            print(f"Yo bro! {self.name} here!")
class Studente(Person):
    def __init__(self, name, surname, corso):
        super().__init__(name, surname)
        self.corso = corso
    def saluta(self):
        Person.saluta(self)
        print(f"I corsi frequentati di {self.name} {self.surname}:")
        for corso in self.corso :
            print (corso)
class Docente(Person):
    def __init__(self, name, surname, materie_doc):
        super().__init__(name, surname)
        self.materie_doc = materie_doc
    def saluta(self):
        Person.saluta(self)
        print(f"I corsi insegnati dal docente {self.name} {self.surname} sono :")
        for materie_doc in self.materie_doc:
            print(materie_doc)
    def controllo(self, Studente):
        check = 1
        for elemento in Studente.corso:
            if elemento not in self.materie_doc:
                check = 0
        if check == 0:
            print("Il docente non insegna tutti i corsi frequentati dallo studente")
        else:
            print("Il doce insegna tutti i corsi frequentati dallo studente")
def verifica_copertura(studenti, docenti):
    for studente in studenti:
        coperto = False
    for docente in docenti:
        if all(corso in docente.materie_doc for corso in studente.corso):
            coperto = True
            break
        if not coperto:
            print(f"Nessun docente copre tutti i corsi di {studente.name} {studente.surname}")
            return False
    print("Tutti gli studenti hanno almeno un docente che copre i loro corsi")
    return True

studenti = [
    Studente("Enrico", "Rossi", ['Programmazione', 'Scienze']),
    Studente("Luca", "Bianchi", ['Matematica 1'])
]

docenti = [
    Docente("Matteo", "Gallet", ['Algebra lineare', 'Matematica 1']),
    Docente("Sara", "Verdi", ['Programmazione', 'Scienze'])
]

verifica_copertura(studenti, docenti)


corsiS = ['Programmazione', 'Scienze', 'Storia', 'Informatica']
corsiD = ['Algebra lineare', 'Matematica 1']
s = Studente("Enrico", "Rossi", corsiS)
s.saluta()
d = Docente("Matteo", "Gallet", corsiD)
d.saluta()
d.controllo(s)
"""