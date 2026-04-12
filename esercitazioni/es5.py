class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, "r")
            file.close()
        except:
            raise ExamException("Errore: impossibile aprire o leggere il file")
    def get_data(self):
        file = open(self.name,"r")
        lista = []

        first_line = True
        for line in file:
            line = line.strip()

            if first_line:
                first_line = False
                continue
            if not line:
                continue
            
            elem = line.split(",")
            if len(elem) < 2:
                continue

            data = elem[0]
            temp = elem[1]

            if data == "" or temp == "":
                continue
            try:
                temp = float(temp)
            except:
                continue
            lista.append([data,temp])
        file.close()
        return lista
    def compute_anomaly(self,time_series, baseline_start, baseline_end, year):
        if not isinstance(baseline_start, int) or not isinstance(baseline_end, int):
            raise ExamException("Errore: intervallo di baseline non valido")
        if not isinstance(year, int) or year < baseline_start or year >baseline_end:
            raise ExamException("Errore: anno non valido")
        
        temp_anno = {}
        for elem in time_series:
            date = elem[0]
            temper = elem[1]
            anno = int(date[0:4])

            if anno not in temp_anno:
                temp_anno[anno] = []
            temp_anno[anno].append(temper)
        #calcolo media annuale degli anni validi compresi nell'intervallo indicato
        medie_annuali = {}
        for chiav, val in temp_anno.items():
            if len(val)>= 9:
                medie_annuali[chiav] = sum(val)/len(val)
        if medie_annuali == {}:
            raise ExamException("Errore: baseline priva di anni validi")
        #calcolo baseline:
        tot = 0
        count = 0
        for i in range(baseline_start, baseline_end+1):
            if i in medie_annuali:
                tot += medie_annuali[i]
                count += 1
        baseline = tot / count
        #calcolo medie mensili dell'anno year
        if year in medie_annuali:
            media = 0
            media = sum(temp_anno[year])/len(temp_anno[year])
        else:
            raise ExamException("Errore: anno richiesto privo di dati sufficienti")
        #calcolo anomalia
        anomalia = float(media) - float(baseline)
        return anomalia
    

time_series_file = CSVTimeSeriesFile(r"esercitazioni/5.csv")
data = time_series_file.get_data()
print(data)
print(time_series_file.compute_anomaly(data,1919,1990,1948))
