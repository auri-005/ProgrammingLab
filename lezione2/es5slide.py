def lista_stringa(A):
    new_list = []
    number = ["zero","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    for elem in A:
        new_list.append(number[elem])

    return new_list

lista = [1,0,7,9,8]
lista_stringa(lista)