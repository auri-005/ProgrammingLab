class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            file = open(self.name, "r")
        except:
            print("Errore: il file non esiste")
        
        data = []
        for righe in file:
            elements = righe.strip().split(",")
            data.append(elements)
        
        file.close()
        return data

with open("C:/Users/auror/Desktop/UNIVERSITA/PROGRAMMAZIONE Visual studio code/.vscode/shampoo_sales.csv", "r") as mio_file:
    mio_file = CSVFile("dati.csv")
    print(mio_file.get_data())

#DA CONTROLLARE, SBAGLIATO