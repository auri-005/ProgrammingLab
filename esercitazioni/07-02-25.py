class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, "r")
            file.read()
            file.close()
        except:
            raise ExamException("Errore: impossibile aprire o leggere il file")
    def get_data(self):
        file = open(self.name, "r")

        data = []
        first_line = True
        for line in file:
            line = line.strip()

            if first_line:
                first_line = False
                continue
            if not line:
                continue
            
            elem = line.split(",")
            #controllo che ci siano almeno due colonne(quelle che servono a me)
            if len(elem)<2:
                continue

            date = elem[0]
            temp = elem[1]

            if date == "" or temp == "":
                continue
            try:
                temp = float(temp)
            except:
                continue
            if temp < 0:
                continue
            data.append([date, temp])
        file.close()
        return data
def compute_variations(time_series, first_year, last_year, N):
    if first_year > last_year:
        raise ExamException("Errore, intervallo non definito")
    if N > (last_year - first_year):
        raise ExamException("Errore: intervallo considerato errato")
    #raggruppo i dati per anno:
    rag_anni = {}
    for elem in time_series:
        date = elem[0]
        temp = elem[1]

        year= int(date[0:4])
        if year >= first_year and year <= last_year:
            if year not in rag_anni:
                rag_anni[year] = []
            rag_anni[year].append(temp)
    #calcolare la media annuale per ciascun anno
    medie_annuali = {}
    for anno in rag_anni:
        lista_temp = rag_anni[anno]
        media = sum(lista_temp)/len(lista_temp) 
        medie_annuali[anno] = media

    #calcolare media basata sui 3 anni precedenti
    media_mobile = {}
    result = {}
    for year in range(first_year+N, last_year+1):
        if year not in medie_annuali:
            continue

        #calcolo la media degli N anni precedenti
        somma = 0
        valid = True
        for i in range(1,N+1):
            anno_prec = year-i
            if anno_prec in medie_annuali:
                somma += medie_annuali[anno_prec]
            #se manca anche solo uno degli N anni precedenti non posso calcolare
            else:
                valid = False
                break
        if valid:
            media_mobile = somma/ N
            #calcolare variazione
            result[str(year)] = medie_annuali[year] - media_mobile
    return result

time_series_file = CSVTimeSeriesFile(r"esercitazioni/GlobalTemperatures.csv")
time_series = time_series_file.get_data()
print(time_series)
print(compute_variations(time_series, 1900, 1904, 3))