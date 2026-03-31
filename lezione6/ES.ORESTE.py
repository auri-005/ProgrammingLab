class CSVFile:
    def __init__(self, name, contenuto):
        self.name = name + ".csv"
        self.contenuto = contenuto
 
    def write(self, added):
        self.contenuto = added
 
    def get_data(self):
        som = []
        for line in self.contenuto:
            som.append(line.split(','))
        return som
   
class NumericalCSVFile(CSVFile):
    def __init__(self, name, contenuto):
        super().__init__(name, contenuto)
 
    def get_data(self):
        som = super().get_data()
        for line in som:
            for i in range(len(line)):
                if i == 0:
                    line[i]=line[i]
                else:
                    try:
                        line[i] = float(line[i])
                    except ValueError:
                        line[i] = line[i]
                        print("Il numero non è convertibile")
        return som

file = NumericalCSVFile("file", " ")
with open(r"ProgrammingLab\lezione2\shampoo_sales.csv") as f:
    file.write(f)
    a = file.get_data()
    print(a)