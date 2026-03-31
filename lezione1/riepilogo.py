"""
ESERCIZI PRIME SLIDE
#es1
convertire = int(538)
ore = int(convertire/60)
minuti = convertire - ore*60

print(f"{ore}h:{minuti}min.")

#es2
numero = int(input('Inserisci un numero: '))
print(f"Il quadrato del numero è :{numero**2}")
print(f"Il cubo del numero è: {numero**3}")

#es3
numero = int(input("inserisci un numero: "))
if(numero%2 == 0):
    print("Il numero inserito è pari")
else:
    print("Il numero inserito è dispari")

#es4
def conta_lettera(parola, lettera):
    count = 0
    for carattere in parola:
        if carattere==lettera:
            count += 1
    return count

parola = input("Scegli una parola: ")
lettera = input("scegli una lettera: ")
conteggio = conta_lettera(parola, lettera)
print(f"Il numero di volte che la lettera {lettera} è contenuta in {parola} è: {conteggio}")

#es5
x = int(input("inserisci un numero: "))
count = 0
def is_prime(x):
    for i in range(2, x):
        if(x%i == 0):
            print("Il numero non è primo")
            return
    print("Il numero è primo")
    return

is_prime(x)

#es6
x = int(input("Inserisci dei numeri, se inserisci zero si ferma: "))
somma = 0
while(x != 0):
    somma += x
    x = int(input())
print(f"La somma dei tuoi numeri è: {somma}")

#es7
def fattoriale():
    x = int(input("Scegli un valore di cui fare il fattoriale: "))
    fattoriale = 1
    for i in range (2,x+1):
        fattoriale *= i
    print(f"Il fattoriale di {x} è {fattoriale}")

fattoriale()

#es8
def is_triangle(lato1,lato2,lato3):
    if(lato1 == 0 or lato2==0 or lato3==0):
        print("Non può essere un triangolo")
    elif(lato1==lato2 and lato3 !=lato1 or lato2==lato3 and lato1 !=lato1 or lato1==lato3 and lato2 !=lato1):
        print("E' un triangolo isoscele")
    elif(lato1 != lato2 and lato2 !=lato3 and lato3 != lato1):
        print("Il triangolo è scaleno")
    elif(lato1 == lato2 and lato2 == lato3):
        print("Il triangolo è rettangolo")

lato1 = int(input("Scegli la lunghezza del primo lato: "))
lato2 = int(input("Scegli la lunghezza del secondo lato: "))
lato3 = int(input("Scegli la lunghezza del terzo lato: "))

is_triangle(lato1, lato2, lato3)

#es9

def conta_vocali(parola):
    count = 0
    for carattere in parola:
        if carattere in vocals:
            count +=1
    print(f"La parola {parola} contiene {count} vocali.")

vocals = {"a", "e", "i", "o", "u"}
x = str(input("Scegli una parola: "))
conta_vocali(x)
"""