def contarighe(nomefile):
    conta = 0
    for riga in open(nomefile):
        conta += 1
    return conta
print(contarighe('ProgrammingLab/lezione2/shampoo_sales.csv'))