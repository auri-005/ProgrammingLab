class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        risultato = []
        try:
            file = open(self.name, "r")
        except:
            raise ExamException(f"Errore, impossibile aprire il file {self.name}")
        first_line = True
        for line in file:
            line = line.strip() #tolgo gli spazi 
            if first_line:
                first_line = False
                continue
            if not line: #riga vuota
                continue
            parts = line.split(",")
            if len(parts) < 2: #se non ci sono gli elementi che mi servono
                continue
            date_str = parts[0].strip()
            passenger_str = parts[1].strip()

            #controllo sui passeggeri
            try:
                passengers = int(passenger_str)
                if passengers < 0:
                    print("Errore, valore numero passeggeri non valido")
                    continue
            except:
                print("Attenzione, valore noon numerico")
                continue
            risultato.append([date_str, passengers])
        file.close()
        return risultato

time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()

def compute_variations(time_series, first_year, last_year):
    risultato = {}
    if not isinstance(first_year, str) or not isinstance(last_year, str):
        raise ExamException("Errore, tipo non valido, non è formato stringa")
    if first_year > last_year:
        raise ExamException("Errore, intervallo non valido")
    
    #raggruppo i passeggeri per anno in un dizionario
    year_pass = {}
    for item in time_series:
        data = item[0]
        passeg = item[1]

        try:
            passeg = int(passeg)
        except:
            print("Riga ignorata: passeggeri non numerici")
            continue
        if passeg < 0:
            print("Riga ignorata: passeggeri negativi")
            continue
        year = int(data[:4])
        first_year_int = int(first_year)
        last_year_int = int(last_year)
        if year < first_year_int or year > last_year_int:
            print(f"L'anno {year} non si trova all'interno dell'intervallo accettato")
            continue
        if year not in year_pass:
            year_pass[year] = []
        year_pass[year].append(passeg)

    #controllo se first year e last year sono presenti nei dati
    if first_year_int not in year_pass or last_year_int not in year_pass:
        raise ExamException("Errore, gli anni di first year e last year non sono presenti nei dati")
    
    #calcolo medie annuali
    medie = {}
    for y in year_pass:
        values = year_pass[y] #valore associato all'anno
        medie[y] = sum(values)/len(values)
    #metto in lista e la ordino
    valid_years = []
    for y in medie:
        valid_years.append(y)
    valid_years.sort()
    #calcolare le differenze per ogni coppia di anni nell'intervallo
    result = {}
    for i in range(1,len(year_pass)):
        y1 = year_pass[i-1]
        y2 = year_pass[i]
        
        key = f"{y1}-{y2}"
        result[key]= medie[y2]-medie[y1]
    return result
print(compute_variations(time_series, "1880", "1958"))