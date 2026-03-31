def triangolo(n1, n2, n3):
    if(n1 == 0 or n2 == 0 or n3 == 0):
        print("Non è un triangolo")
    elif(n1 == n2 and n2 == n3):
        print("Il triangolo è equilatero")
    elif(n1 != n2 and n2 != n3 and n3 != n1):
        print("Il triangolo è scaleno")
    elif((n1 == n2 and n3 != n2) or (n2 == n3 and n1 != n2) or (n3 == n1 and n2 != n3)):
        print("Il triangolo è isoscele")

num1 = input("Scegli un numero : ")
num2 = input("Scegli un numero : ")
num3 = input("Scegli un numero : ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

triangolo(num1, num2, num3)