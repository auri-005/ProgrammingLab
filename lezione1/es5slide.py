x = input("Scegli un numero")
x = int(x)
def is_prime(x):
    for i in range(2, x):
        if(x%(i) == 0):
            print(f"{x} non è primo")
            return
    print(f"{x} è primo")

is_prime(x)