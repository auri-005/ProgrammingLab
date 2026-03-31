def conta_vocali(stringa):
    count = 0
    for carattere in stringa: 
        if carattere in vocals:
            count += 1
    print(f"Il numero di vocali in {stringa} è {count}")

vocals = {"a","e","i","o","u"}
parola = input("Scegli una parola : ")
conta_vocali(parola)