class CSVFile:
    def __init__(self, name):
        self.name = name
    def get_data(self):
        with open (self.name, "r") as file:
            lista = []

            for righe in file:
                lista.append(righe.strip().split(',')) # ogni riga viene divisa dalla virgola
            return lista

file = CSVFile('shampoo_sales.csv')
print(file.get_data())