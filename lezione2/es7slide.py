def somma(file):
    totale = 0
    my_file = open(file, "r")
    next(my_file) #grazie al next non leggo anche il titolo del mio file, altrimenti avrebbe fatto Data, sales: cosi facendo lui comincia dalla riga di indice due dove ho i miei valori che devo salvare
    for line in my_file:
        data, vendite=line.split(",")
        totale += float(vendite)
    my_file.close()
    return totale
print(somma("shampoo_sales.csv"))