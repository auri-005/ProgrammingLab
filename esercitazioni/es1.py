# Aurora Gardisan SM32A00056
class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    def get_data(self, city_name):
        lista = []
        try:
            file = open(self.name, "r") #apro il file
        except:
            raise Exception(f"Errore, il file {self.name} non esiste")
        righe = file.read().split('\n')
        file.close()
        trovata = False
        for riga in righe[1:]:  # salto intestazione
            parti = riga.split(',')
            if len(parti) < 4:
                continue
            city = parti[3]
            if city == city_name:
                trovata = True
                break
        if not trovata:
            raise ExamException("Errore, il nome della città non è presente nel file")
        for riga in righe[1:]:
            parti = riga.split(',') #divido la riga in colonne 
            if len(parti) < 4:
                continue
            
            data = parti[0]
            temp = parti[1]
            city = parti[3]

            if temp == '':
                continue
            #errore se non esiste la città 
            
            #filtro le città
            if city != city_name:
                continue
            #filtro i valori validi della temp
            try:
                temp = float(temp)
            except:
                continue
            lista.append([data, temp])
        return lista
    def compute_slope(self, time_series, first_year, last_year):
        if first_year >= last_year:
            raise ExamException("Errore, intervallo non valido")
        dati_annuali = {}
        for data, temp in time_series:
            anno = int(data[:4])
            if anno < first_year or anno > last_year:
                continue
            if anno not in dati_annuali:
                dati_annuali[anno] = []
            dati_annuali[anno].append(temp)
        
        #anni che hanno almeno 6 misurazioni mensili valide
        anni_validi = []
        medie_annuali = []
        for anno, temps in dati_annuali.items():
            temps = dati_annuali[anno] #lista di temperature
            if len(temps) >= 6:
                anni_validi.append(anno)

                #media annuale per ogni anno valido nell'intervallo dato
                medie_annuali.append(sum(temps)/len(temps))
        
        n = len(anni_validi)
        if n == 0:
            raise ExamException("Errore, la lunghezza degli anni validi non può essere uguale a zero")
        
        x_media = sum(anni_validi)/n
        y_media = sum(medie_annuali)/n
        
        #coefficiente angolare
        numeratore = 0
        for i in range(len(anni_validi)):
            numeratore += (anni_validi[i]-x_media)*(medie_annuali[i]-y_media)
        denominatore = sum((xi -x_media)**2 for xi in anni_validi)
        if denominatore == 0:
            raise ExamException("Errore, il denominatore non può essere uguale a zero")

        coefficiente_angolare = numeratore/denominatore
        return coefficiente_angolare

time_series_file = CSVTimeSeriesFile(r"C:/Users/auror/Desktop/UNIVERSITA/git/ProgrammingLab1/esercitazioni/1.csv")
time_series_italy = time_series_file.get_data("Rome")
print(time_series_italy)
coeff = time_series_file.compute_slope(time_series_italy, 1890, 1895)
print(coeff)