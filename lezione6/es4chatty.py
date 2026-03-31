try:
    file = open("dati.txt", "r")
    print("File aperto correttamente")
    file.close()
except:
    print("Errore: il file non esiste")