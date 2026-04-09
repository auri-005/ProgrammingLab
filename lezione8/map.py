lista_numeri = [1,3,6]
dizionario_numeri_stringhe = {0: "zero", 1: "uno", 2: "due", 3: "tre", 4: 
"quattro", 5: "cinque", 6: "sei", 7: "sette", 8: "otto", 9: "nove"}
list_comp =[dizionario_numeri_stringhe[n] for n in lista_numeri]
list_con_map = list(map(lambda n: dizionario_numeri_stringhe[n], lista_numeri))
print(list_comp, list_con_map)