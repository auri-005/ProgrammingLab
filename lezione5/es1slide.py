class Persona:
 
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
 
    def saluta(self):
#        print('Ciao sono: ', self.ruolo + "," , self.nome, self.cognome)
        print (f"Ciao sono: {self.ruolo} {self.nome} {self.cognome}")
 
class Studente(Persona):
 
    def __init__(self, nome, cognome, corso):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = corso
 
    def saluta(self):
        Persona.saluta(self)
        print(f"Frequento il corso: {self.corso}")
 
class Docente(Persona):
 
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso
 
    def saluta(self):
        Persona.saluta(self)
        print(f"Docente del corso: {self.corso}")
 
class Studente(Persona):
 
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi
 
    def saluta(self):
        Persona.saluta(self)
        print(f"I corsi di {self.nome} {self.cognome} sono: ")
        for corso in self.corsi:
            print(corso)
 
class Docente(Persona):
 
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi
 
    def saluta(self):
        Persona.saluta(self)
        print(f"I corsi insegnati da {self.nome} {self.cognome} sono: ")
        for corso in self.corsi:
            print(corso)
 
corsiS = ['Programmazione', 'Laboratorio', 'Analisi', 'Algebra']
s = Studente('Enrico', 'Rossi', corsiS)
s.saluta()
corsiD = ['Laboratorio', 'Algebra']
d = Docente('Gino', 'Grassi', corsiD)
d.saluta()
 