def conta_numeri():
    n = input("Scegli un numero : ")
    n = int(n)
    num_numeri = 0
    print("Se scegli zero la conta si fermerà")
    somma = 0
    
    while(n != 0):
        somma += n
        num_numeri +=1
        n = input("Scegli un numero : ")
        n = int(n)
    print(f"La somma dei {num_numeri} numeri scelti dall'utente è di : {somma}")

conta_numeri()

