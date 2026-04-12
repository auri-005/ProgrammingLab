class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, "r")
            file.close()
        except:
            raise ExamException("Errore: impossibile aprire il file")
    def get_data(self, country_name):
        file = open(self.name, "r")
        data = []

        first_line = True
        for line in file:
            line = line.strip()

            #salto l'intestazione, la prima riga
            if first_line:
                first_line= False
                continue
            #se c'è una riga vuota la salto 
            if not line :
                continue
            #divido la riga in 'colonne'
            elem = line.split(";")
            #controllo che ci siano almeno 4 colonne di elem:
            if len(elem) < 4:
                continue
            #seleziono come se fosse un array i dati che mi servono
            date = elem[0]
            temp = elem[1]
            incert = elem[2]
            country = elem[3]
            #i miei dati se non soddisfano le condizioni vengono saltati e si prova con la riga seguente 
            if temp == "" or incert == "" or country == "" or temp == "":
                continue
            try:
                temp = float(temp)
                incert = float(incert)
            except:
                continue
            
            if incert >= 5:
                continue
            #se country è la stessa che mi viene data in input la aggiungo alla mia lista 
            if country == country_name:
                data.append([date, temp, incert])
        #se la mia lista è vuota, quindi non ho nessun paese nei dati uguale a quello dato in input alzo un eccezione 
        if data == []:
            raise ExamException("Errore: il paese richiesto non è presente nel file")
        #chiudo il file e ritorno la mia lista 
        file.close()
        return data
    def compute_cons_variation_compare(self, time_series1, time_series2, year):
        if not isinstance(year, int):
            raise ExamException("Errore: anno non valido, deve essere intero")
        #raggruppo temperatura e incertezza per anno e mese nei dizionari relativi alle due time_series
        rag_anno1 = {}
        #estrapolo tutti i dati che mi servono da time_series1
        for elem1 in time_series1:
            data1 = elem1[0]
            temp1 = elem1[1]
            inc1 = elem1[2]
            year1 = int(data1[3:7])
            month1 = int(data1[0:2])

            #se l'anno è lo stesso richiesto in input aggiungo nel dizionario la chiave mese e i valori richiesti
            if year1 == year:
                rag_anno1[month1] = [temp1, inc1]
        rag_anno2 = {}
        #eseguo gli stessi identici passsaggi anche per time_series2
        for elem2 in time_series2:
            data2 = elem2[0]
            temp2 = elem2[1]
            inc2 = elem2[2]
            year2 = int(data2[3:7])
            month2 = int(data2[0:2])

            if year2 == year:
                rag_anno2[month2] = [temp2, inc2]
        if rag_anno1 == {} or rag_anno2=={}:
            raise ExamException("Errore: l'anno indicato non rientra nella copertura del dataset")
        #variazioni tra mesi consecutivi, entrambi i mesi sono presenti in entrambi gli anni
        result = {}
        for m in range(1,12):
            if m in rag_anno1 and m in rag_anno2:
                if m+1 in rag_anno1 and m+1 in rag_anno2:
                    #calcolo per time_series1
                    var1 = rag_anno1[m+1][0] - rag_anno1[m][0]
                    max_inc1 = rag_anno1[m][1] + rag_anno1[m+1][1]
                    #calcolo per time_series2
                    var2 = rag_anno2[m+1][0] - rag_anno2[m][0]
                    max_inc2 = rag_anno2[m][1] + rag_anno2[m+1][1]

                    #confrontare le variazioni 
                    var = var2 - var1
                    max_inc = max_inc2 + max_inc1
                    #salvare ii dati in un dizionario
                    result[m] = (float(var), float(max_inc))
        if result == {}:
            raise ExamException("Errore: nessuna coppia di mesi valida per il confronto tra gli anni indicati")
        return result


ts_file = CSVTimeSeriesFile(r"esercitazioni/4.csv")
t1 = ts_file.get_data("Zambia")
t2 = ts_file.get_data("Sudan")
print(ts_file.compute_cons_variation_compare(t1, t2, 1990))