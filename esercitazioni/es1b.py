class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    def get_data(self, name_city):
        try:
            file = open(self.name, "r")
        except:
            raise ExamException("Errore, impossibile aprire il file")
        lista = []
        first_line = True
        for line in file:
            line = line.strip()

            #salto intestazione
            if first_line:
                first_line = False
                continue

            #se è una riga vuota, continua
            if not line:
                continue

            elem = line.split(",")
            if len(elem)<4:
                continue
            
            data = elem[0]
            temp = elem[1]
            city = elem[3]
            if temp == "" or data == "":
                continue
            try:
                temp = float(temp)
            except:
                continue
            if city == name_city:
                lista.append([data, temp])
        if lista == []:
            raise ExamException("Errore: il nome della città non è presente nel file")
        file.close()
        return lista
    def compute_slope(self, time_series, first_year, last_year):
        if first_year >= last_year:
            raise ExamException("Errore: intervallo di anni non valido")
        #raggruppare le temp per anno 
        temp_anno = {}
        for data, temp in time_series:
            data = int(data[0:4]) #considero solo l'anno
            if data < first_year or data > last_year:
                continue
            if data not in temp_anno:
                temp_anno[data] = []
            temp_anno[data].append(temp)
        #calcolo quali solo gli anni validi che hanno almeno 6 misurazioni mensili 
        anni_validi = []
        media_annuale = []
        for anno, temps in temp_anno.items():
            temps = temp_anno[anno]
            if len(temps) >= 6 :
                anni_validi.append(temps)
            else:
                print("Attenzione: riga non valida per misurazioni non sufficienti")
            #calcolo la media annuale per ogni anno 
                media_annuale.append(sum(temps)/len(temps))
        #calcolo media di tutti gli anni validi
        #calcolo di tutte temperature medie
        n = len(anni_validi)
        if n == 0:
            raise ExamException("Errore: n non può essere zero")
        x_media = sum(anni_validi)/n
        y_media = sum(media_annuale)/n

        #calcolare coefficiente angolare
        numeratore = 0
        denominatore = 0
        for i in range(len(anni_validi)):
            numeratore += (anni_validi[i]-x_media)*(media_annuale[i]-y_media)
            denominatore += (anni_validi[i]-x_media)**2
        m = numeratore/denominatore
        if m == 0:
            raise ExamException("Errore: il denominatore non può essere zero")
        return m

time_series_file = CSVTimeSeriesFile(r"C:/Users/auror/Desktop/UNIVERSITA/git/ProgrammingLab1/esercitazioni/1.csv")
time_series_italy = time_series_file.get_data("Rome")
print(time_series_italy)



