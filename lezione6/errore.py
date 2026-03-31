my_var = 'ciao'

try:
    my_var = float(my_var)
except:
    print('Non posso convertire "my_var" a valore numerico!')

print('ma il codice continua!!!')
#------------------------------------------------------------------------------------------------------------------------------
my_var = 'ciao'

try:
    my_var = float(my_var)
except Exception as e:
    print('Non posso convertire "my_var" a valore numerico!')
    print('La variabile "my_var" valeva : "{}"'.format(my_var))
    print('Ed ho ottenuto questo errore: "{}"'.format(e)) #per stampare il tipo di errore