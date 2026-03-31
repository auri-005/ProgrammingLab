class CsvFile:
    def __init__(self, name_file):
        self.name = name_file
    
    def get_data(self):
        lista = []
        my_file = open(self.name,"r") #apre il file contenuto nella variabile self.name e lo legge

        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        
        my_file.close()
        return lista