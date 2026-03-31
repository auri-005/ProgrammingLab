def conta_lettera(parola, lettera):
    count = 0
    for carattere in parola:
        if carattere == lettera:
            count+=1
    return count

par = input("Scegli una parola ")
lett = input("Scegli una lettera (contenuta nella parola) ")
x = conta_lettera(par, lett)
print(f"Il numero di volte che compare {lett} in {par} è {x}")
