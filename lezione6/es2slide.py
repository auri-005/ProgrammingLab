class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            file = open(self.name, "r")
        except FileNotFoundError:
            print("Errore: il file non esiste")
            return None
        
        data = []
        for righe in file:
            elements = righe.strip().split(",")
            data.append(elements)
        
        file.close()
        return data

class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        numerical_data = []
        for row in data:
            new_row = [row[0]] #la prima colonna (data) resta stringa
            try:
                for element in row[1:]:
                    new_row.append(float(element))
                numerical_data.append(new_row)
            except:
                print("errore nella riga :", row)
                print("La riga viene saltata")
        return numerical_data
    
file = NumericalCSVFile("shampoo_sales.csv")
data = file.get_data()
print(data)