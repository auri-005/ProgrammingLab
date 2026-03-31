class CsvFile:
    def __init__(self, name):
        self.name = name

        try:
            file = open(self.name, "r")
            file.readline() #leggiamo la prima riga per verificare se esiste o meno il file
            file.close()
        except FileNotFoundError:
            print("Errore: il file non esiste")
    def get_data(self):
        file = open(self.name,"r")
        data = []

        for riga in file:
            elements = riga.strip().split(",")
            data.append(elements)
        file.close()
        return data

miio_file = CsvFile("dati.csv")