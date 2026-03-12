def conteggio(file):
    f = open(file, "r")
    diz = {}
    for riga in f:
        parole = riga.split()
        for p in parole: #p è la mia chiave
            if p in diz:
                diz[p] += 1
            else:
                diz[p] = 1
    f.close()
    return diz

print(conteggio("testo.txt"))
