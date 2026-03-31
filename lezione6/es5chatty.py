class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        file = open(self.name, "r")
        data = []
        for riga in file:
            elements = riga.strip().split(",") #divido le righe del file con una virgola
            data.append(elements) #aggiungo gli elementi in data
        file.close()
        return data

class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data() #uso le stesse funzioni della classe padre sopra
        numerical_data = []
        for row in data:
            try:
                giorno = row[0] #la colonna 1 è il giorno
                numero = float(row[1]) #la colonna 2 è quella dei numeri che vengono convertiti in float

                numerical_data.append([giorno, numero])
            except:
                print("Errore nella riga :", row )
                print("La riga viene saltata")
        return numerical_data
    

'''
questo è il mio file di partenza come idea
giorno,10
lunedi,5
martedi,7
mercoledi,ciao
giovedi,12
'''