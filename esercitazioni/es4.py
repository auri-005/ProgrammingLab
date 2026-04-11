class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name,"r")
        except:
            raise ExamException("Errore: impossibile aprire il file")
        try:
            file.read()
            file.close()
        except:
            raise ExamException("Errore: il file è vuoto o non continene dati validi")
    def get_data(self, nome_paese):
        dat_temp = []
        file = open(self.name, "r")
        first_line = True
        for line in file:
            line = line.strip()

            #salto solo l'intestazione
            if first_line:
                first_line = False
                continue

            #se c'è una riga vuota la salto
            if not line:
                continue
            #divido la riga in 'colonne'
            elem = line.split(",")
            #se non contiene almeno 4 colonne vado alla prossima
            if len(elem)<5:
                continue

            date = elem[0]
            temp = elem[1]
            country = elem[4]

            if temp == "":
                continue
            try:
                temp = float(temp)
            except:
                continue
            if country == nome_paese:
                dat_temp.append([date,temp])
        if dat_temp == []:
            raise ExamException("Errore: il nome del paese non è presente nel file")
        file.close()
        return dat_temp
    def compute_variations(self, time_series_1, time_series_2, first_year, last_year):
        #estrarre le temperature per ciasciun anno
        if first_year > last_year:
            raise ExamException("Errore: intervallo di anni non valido")
        
        temp_ann1 = {}
        temp_ann2 = {}
        for x in time_series_1:
            data1 = x[0]
            temp1 = x[1]

            data1 = int(data1[0:4])
            if temp1 == "":
                continue
            if data1 not in temp_ann1:
                temp_ann1[data1] = []
            temp_ann1[data1].append(temp1)
        
        for y in time_series_2:
            data2 = y[0]
            temp2 = y[1]
            
            data2 = int(data2[0:4])
            if temp2 == "":
                continue
            if data2 not in temp_ann2:
                temp_ann2[data2] = []
            temp_ann2[data2].append(temp2)
        
        #calcolare la media annuale per ogni anno nell'intervallo dato
        #prima serie temporale
        media_ann1 = {}
        for year1, list_temp in temp_ann1.items():
            if first_year <= year1 <=last_year:
                media = sum(list_temp)/len(list_temp)
                media_ann1[year1] = media
        
        #seconda serie temporale
        media_ann2 = {}
        for year2, list_temp in temp_ann2.items():
            if first_year <= int(year2) <=last_year:
                media = sum(list_temp)/len(list_temp)
                media_ann2[year2] = media
        result = {}
        for x in media_ann1:
            if x in media_ann2:
                result[str(x)] = media_ann2[x] - media_ann1[x]

        """
        oppure per calcolare le medie e le differenze: più veloce e 'corretto', spreco meno tempo:
        for year in range(first_year, last_year + 1):  #eseguo direttamente i cicli sugli anni richiesti senza stare a controllare ogni anno ogni volta
            if year in temp_ann1 and year in temp_ann2:
                media1 = sum(temp_ann1[year]) / len(temp_ann1[year])
                media2 = sum(temp_ann2[year]) / len(temp_ann2[year])
                result[str(year)] = media2 - media1

        """

        return result
        



time_series_file = CSVTimeSeriesFile(r"esercitazioni/1-4.csv")
time_series_italy = time_series_file.get_data("Italy")
#print(time_series_italy)
print(time_series_file.compute_variations(time_series_file.get_data("Italy"), time_series_file.get_data("India"), 1990, 1993))