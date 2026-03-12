def remove_righe_dupl(file):
    my_file = open(file, "r")
    u = open("unique.txt", "w")
    righe = set()

    for riga in my_file:
        if riga not in righe:
            righe.add(riga)
            u.write(riga)
    my_file.close()
    u.close()

file1 = input("scegli il file da leggere : ")
remove_righe_dupl(file1)
