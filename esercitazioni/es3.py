class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, "r")
            file.close()
        except:
            raise ExamException("Errore, impossibile aprire o leggere il file")
    def get_data(self):
        file = open(self.name, "r")
        data = []
        first_line = True
        for line in file:
            line = line.strip()

            #salto la prima riga, l'intestazione
            if first_line:
                first_line = False
                continue
            #salto le righe vuote
            if not line:
                continue

            elem = line.split(";")
            #controllo che abbiano tutti e tre i dati che mi servono
            if len(elem)<3:
                continue
            
            data_str = elem[0]
            t_max = elem[1]
            t_min = elem[2]

            if data_str == "" or t_min == "" or t_max == "":
                continue
            try:
                t_min = float(t_min)
                t_max = float(t_max)
            except:
                continue
            if t_min < -50 or t_max > 50:
                continue
            if t_min > t_max:
                print(f"I valori scartati per l'anno {data_str} sono {t_min} temperatura minima e {t_max} la temperatura massima.")
                continue
            data.append([data_str, t_min, t_max])
        file.close()
        return data
    def compute_monthly_spread_diff(self, time_series, first_year, second_year):
        if not isinstance(first_year, int) or not isinstance(second_year, int):
            raise ExamException("Errore, gli anni devono essere interi")
        if first_year > second_year:
            raise ExamException("Errore, gli anni devono essere in ordine crescente")
        #i due dizionari in cui inserirò lo spread per ciascun mese diviso nei due anni 
        year1 = {}
        year2 = {}
        for elem in time_series:
            date = elem[0]
            val1 = elem[1]
            val2 = elem[2]

            spread = val2-val1

            year = int(date[0:4])
            month = int(date[5:7])
            if year == first_year:
                    year1[month] = spread
            if year == second_year:
                    year2[month] = spread
        
        spread_year1_year2 = {}
        for m in year1:
            if m in year2:
                spread_years = year2[m]-year1[m]
                spread_year1_year2[m] = spread_years
            else:
                print(f"La variazione per il mese di {m} non può essere calcolata")
        if spread_year1_year2 == {}:
            raise ExamException("Errore, nessun mese confontabile tra gli anni indicati")
        return spread_year1_year2

esempio = CSVTimeSeriesFile(r"C:/Users/auror/Desktop/UNIVERSITA/git/ProgrammingLab1/esercitazioni/3.csv")
data = esempio.get_data()
print(data)
result = esempio.compute_monthly_spread_diff(data, 1970, 2000)
print(result)