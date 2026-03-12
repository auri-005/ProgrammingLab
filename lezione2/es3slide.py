
def scambia(lista, i, j):
    tmp = lista[i]
    lista[i] = lista [j]
    lista[j] = tmp
    print(lista)


my_list = [1,2,3,4,5,6]
i = int(2)
j = int(4)
scambia(my_list, i, j)