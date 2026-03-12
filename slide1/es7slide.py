def fattoriale():
    x = input("Scegli un numero : ")
    x = int(x)
    fatt = 1
    for i in range (1, x+1):
        fatt *= i
    print(f"Il fattoriale di {x} è {fatt}")

fattoriale()