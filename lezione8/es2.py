"""
lista1 = [1,2,3]
lista2 = [4,5]
lista3 = [6,7,8,1]
liste = lista1 + lista2 + lista3
new = [n for n in liste]
print(new)
"""
input = [[1,2,3], [4,5], [6,7,8,1]]
new = [elemento for sotto_lista in input for elemento in sotto_lista]
print(new)