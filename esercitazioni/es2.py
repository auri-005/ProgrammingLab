class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, "r")
            file.close()
        except:
            raise ExamException("Errore, impossibile aprire il file")
    def get_data(self):
        file = open(self.name, "r")
        
        lista = []
        first_line = True
        for line in file:
            line = line.strip() #tolgo gli spazi

            #salto l'intestazione
            if first_line:
                first_line = False
                continue
            #se una riga è vuota
            if not line:
                continue

            parts = line.split(",")
            #mi servono almeno 3 colonne utili, se non c'è salto la riga
            if len(parts) < 3:
                continue

            data = parts[0] #.strip()??
            temp = parts[1] #.strip()??
            var = parts[2] #.strip()??

            if temp == "" or var == "":
                continue
            #tolgo valori non numerici, vuoti o nulli
            try:
                temp = float(temp)
                var = float(var)
            except:
                print("Attenzione, valori non accettati, li salto")
                continue
            if var < 5:
                lista.append([data, temp])
            else:
                print(f"La data {data} viene saltata perchè valore troppo incerto")
        file.close()
        return lista
    def compute_month_variation(self, time_series, first_year, second_year):
        if not isinstance(first_year, int) or not isinstance(second_year, int):
            raise ExamException("Errore: gli anni inseriti devono essere di tipo intero.")
        if second_year <= first_year:
            raise ExamException("Errore: il secondo anno deve essere maggiore del primo")
        
        #raggruppare le temperature per anno, per i due considerati
        raggrup = {}
        for item in time_series:
            data = item[0]
            temp = item[1]

            year = int(data[6:10]) #considero solo l'anno
            month = data[3:5]
            if year == first_year or year == second_year:
                if year not in raggrup:
                    raggrup[year] = {}
                raggrup[year][month] = temp
        if second_year not in raggrup:
            raise ExamException(f"Anno {second_year} non presente nei dati")

        if first_year not in raggrup:
            raise ExamException(f"Anno {first_year} non presente nei dati")
        year1 = raggrup[first_year]
        year2 = raggrup[second_year]
        #considerare i mesi presenti in entrambi gli anni 
        common_month = []
        for y in year1:
            if y in year2:
                common_month.append(y)
        print(common_month)
        
        #differenze mensili
        result = {}
        for m in common_month:
            result[m] = year2[m] - year1[m]
        return result

    
time_series_file = CSVTimeSeriesFile(r"C:/Users/auror/Desktop/UNIVERSITA/git/ProgrammingLab1/esercitazioni/2.csv")
data = time_series_file.get_data()
print(data)
print(time_series_file.compute_month_variation(data, 1900, 2000))
