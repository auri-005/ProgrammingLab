def conta_parola_file(file, parola):
    count = 0
    f = open(file, "r")
    for riga in f:
        parole = riga.split() #divide la riga in parole
        for p in parole:
            if p == parola:
                count += 1
    f.close()
    return count

parola = input("Scegli la parola da cercare nel file : ") 
file = input("Scegli il nome del file : ")

print(conta_parola_file(file, parola))