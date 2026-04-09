class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
        self.window = window
        if self.window < 0:
            raise ExamException('Errore, la lunghezza della finestra è negativa')
    def compute(self, lista):
        if not isinstance(lista, list):
            raise ExamException('Errore, deve essere una lista')
        for x in lista:
            if  not isinstance(x, (int, float)):
                raise ExamException('Errore, gli elementi della lista devono essere interi o float')
        if self.window > len(lista):
            raise ExamException('Errore, la lunghezza della lista è inferiore alla finestra')
        risultato = []
        for i in range(len(lista) - self.window +1):
            finestra = lista[i : i+self.window]
            media = float(sum(finestra)/self.window)
            risultato.append(media)
        return risultato

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result) 