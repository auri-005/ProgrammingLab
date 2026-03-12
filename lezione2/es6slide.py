def conta_parole(lista):
    diz = {}

    for parola in lista:
        if parola in diz:
            diz[parola] += 1
        else:
            diz[parola] = 1
    return diz

parole = ["cane", "gatto", "cane", "topo", "gatto", "cane"]
print(conta_parole(parole))