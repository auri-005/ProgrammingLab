def numeri_parole(my_list):
    my_dict = {0 : "zero", 1: "uno", 2: "due", 3:"tre", 4: "quattro", 5:"cinque", 6: "sei", 7:"sette", 8:"otto", 9:"nove"}
    risultato_nomi = [] #lista dove salvare i nomi
    for numero in my_list:
        nome_corrisp = my_dict[numero]
        risultato_nomi.append(nome_corrisp) #aggiunge il nome alla lista
    return risultato_nomi

my_list = [1, 3, 7, 9]
risultato = numeri_parole(my_list)
print(risultato)