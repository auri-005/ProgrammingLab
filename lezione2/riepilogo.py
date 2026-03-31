""""
#es1
my_list = [1,2,3,4,5]

def somma_lista(my_list):
    somma = 0
    for element in my_list:
        somma += element
    return somma

print(somma_lista(my_list))

#es2
my_stringa = str(input("Inserisci una stringa da verificare se è palindromo: "))

def is_palindromo(x):
    n = len(x)
    metà = int(len(x)/2)
    for i in range(metà):
        if x[i] != x[n-1-i]:
            return False
    return True


print(is_palindromo(my_stringa))

#es3
my_list = [1,2,3,4,5,6]
print(my_list)

def scambio_indici(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    print(A)

scambio_indici(my_list, 2, 4)

#es4

def check(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

my_list1 = [1,5,2,7,3,99]
my_list2 = [4,8,43,54,23,99]
print(check(my_list1,my_list2))

#es5

def numeri_corrisp(A):
    my_dict = {0 : "zero", 1: "uno", 2: "due", 3:"tre", 4: "quattro", 5:"cinque", 6: "sei", 7:"sette", 8:"otto", 9:"nove"}
    nuova_lista = []
    for elemento in A:
        num_lettere = my_dict[elemento]
        nuova_lista.append(num_lettere)
    return nuova_lista

my_list = [1,0,7,9,8]
print(numeri_corrisp(my_list))

#es6
def cont_occ(A):
    my_dict = {}
    for parola in my_list:
        if parola not in my_dict:
            my_dict[parola] = 1
        else :
            my_dict[parola] += 1
    return my_dict

my_list = ["cane", "oggi", "gatto", "ieri", "cane", "gatto", "ieri"]
print(cont_occ(my_list))

#es7
def sum_value(file):
    totale = 0
    mio_file = open(file, "r")
    next(mio_file)
    for line in mio_file:
        data, sales = line.split(',')
        totale += float(sales)
    mio_file.close()
    return totale

my_file = "C:/Users/auror/Desktop/UNIVERSITA/git/ProgrammingLab1/lezione2/shampoo_sales.csv"
print(sum_value(my_file))

#es8
def conteggio(file, x):
    count = 0
    my_file = open(file, 'r')
    for line in my_file:
        parola = line.split(',')
        for parola in line:
            if parola == x:
                count += 1
    return count

parol_cercar = input("Inserisci una parola da cercare: ")
files = input("Inserisci il nome del file in cui cercare la parola: ")
print(conteggio(files, parol_cercar))

#es9
def  conteggio(file):
    dict = {}
    mio_file = open(file, "r")
    next(mio_file)
    next(mio_file)
    for line in mio_file:
        parola = line.split(",")
        if parola not in dict:
            dict[parola] = 1
        else:
            dict[parola] += 1
    mio_file.close()

    return dict

print(conteggio("testo.txt"))

#es10

def remove_dupl(file):
    mio_file = open(file, "r")
    new_file = open("unique.txt", "w")
    righe = set()

    for line in mio_file:
        if line not in righe:
            righe.add(line)
            new_file.write(line)
    mio_file.close()
    new_file.close()

file1 = input("Inserisci il nome del file: ")
remove_dupl(file1)
"""
