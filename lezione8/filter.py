lista =[1,2,3,4,5,6,7,8,9]
list_comp = [n for n in lista if n%2==0]
list_con_filter = list(filter(lambda n :n%2==0, lista))
print(list_comp, list_con_filter)