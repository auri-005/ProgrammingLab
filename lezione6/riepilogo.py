"""
#es1a 
class CsvFile:
    def __init__(self, name_file):
        self.name = name_file
    
    def get_data(self):
        try:
            my_file = open(self.name, "r")
        except:
            print("Errore: il file non esiste")

        lista = []
        my_file = open(self.name,"r") #apre il file contenuto nella variabile self.name e lo legge

        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        
        my_file.close()
        return lista

#es1b
class CsvFile:
    def __init__(self, name_file):
        self.name = name_file

        try:
            my_file = open(self.name, "r")
            my_file.readline()
            my_file.close()
        except:
            print("Errore: il file non esiste")
    
    def get_data(self):
        lista = []
        my_file = open(self.name,"r") #apre il file contenuto nella variabile self.name e lo legge

        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        
        my_file.close()
        return lista

#es2
class NumericalCSVFile(CsvFile):
    def __init__(self, name_file):
        super().__init__(name_file)
    def get_data(self):
        data = super().get_data()
        if data is None:
            return None
        numerical_data = []
        for row in data:
            new_row = [row[0]] #la prima resta stringa, quella della data
            try: 
                for element in row[1:]:
                    new_row.append(float(element))
                    numerical_data.append(new_row)
            except:
                print("errore nella riga:", row)
                print("La riga viene saltata")
        return numerical_data
    
file = NumericalCSVFile(r"lezione2/shampoo_sales.csv")
data = file.get_data()
print(data)

#es3
class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        my_file = open(self.name, "r")
        data = []
        for line in my_file:
            elements = line.split(",")
            data.append(elements)
        my_file.close()
        return data
file = CSVFile("lezione2/shampoo_sales.csv")
data = file.get_data()
print(data)

#es4
class CSVFile():
    def __init__(self, name):
        self.name = name
        if not isinstance(name, str):
            raise TypeError("Il nome del file deve essere una stringa")
        
    def get_data(self, start = None, end = None):
        try:
            my_file = open(self.name, "r")
        except:
            print("Errore, file non trovato")
            return None
        
        data = []
        line_number = 0
        for line in my_file:
            line_number +=1
            if line_number < start:
                continue
            if line_number > end:
                break
            elements = line.split(",")
            data.append(elements)
        my_file.close()
        return data

file = CSVFile("lezione2/shampoo_sales.csv")
print(file.get_data(start = 1, end = 5))

#es6
from datetime import datetime
birth_str=(input("Inserisci la tua data di nascita (YYYY-MM-DD): "))
birth_date=datetime.strptime(birth_str, "%Y-%m-%d")

today = datetime.now()

#calcolo età
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
#prossimo compleanno
next_birthday = datetime(today.year, birth_date.month, birth_date.day)
if next_birthday < today:
    next_birthday = datetime(today.year +1, birth_date.month, birth_date.day)
#tempo rimanente
time_left = next_birthday - today
total_seconds = int(time_left.total_seconds())

days = total_seconds // (24 * 3600)
total_seconds %= (24 * 3600)

hours = total_seconds // 3600
total_seconds %= 3600

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Età:", age)
print("Tempo al prossimo compleanno:")
print(days, "giorni", hours, "ore", minutes, "minuti", seconds, "secondi")

#es7
while True:
    user_input = input("Inserisci un numero intero: ")
    try:
        num = int(user_input)
        print("Il quadrato del numero è: ", num**2)
        break
    except:
        print("Errore, valore non valido. Riprovare")

#es8
scelta = 0
print("Il programma seguente si ripeterà finchè non digiterà il numero 3.\n")
while scelta != 3:
    try:
        scelta = int(input("Scegli una tra le tre proposte e digita il numero corrispondente:\n1) calcolare la somma di due numeri.\n2) calcolare la differenza tra due numeri.\n3) uscire.\nIl programma si ripeterà finchè non digiterà il numero 3.\n"))
    except:
        print("Errore, valore non valido")
        continue #importante!!! senza il ciclo continua col valore vecchio di scelta, dunque si creerebbe un errore
    if scelta == 1:
        try:
            num1 = int(input("Scegli un valore per la somma:"))
            num2 = int(input("Scegli il secondo valore per la somma: "))
            print("La somma dei due numeri è: ", num1 + num2)
        except:
            print("Errore, tipo non valido")
    elif scelta == 2:
        try:
            num1 = int(input("Scegli un valore per la differenza:"))
            num2 = int(input("Scegli il secondo valore per la differenza: "))
            print("La differenza dei due valori è:", num1 - num2)
        except:
            print("Errore, tipo non valido")
    elif scelta == 3:
        print("Hai scelto la terza opzione, il programma si interrompe.\n")
        break
"""