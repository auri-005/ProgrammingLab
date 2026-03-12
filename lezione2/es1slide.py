new_list = [1,2,3,4,5]

def somma_my_list(lista):
    sum = 0
    for item in lista:  #for elem in lista 
        sum = sum + item
    return sum

print(somma_my_list(new_list))

#devo definire la variabile sum dentro la funzione altrimenti non la trova.

