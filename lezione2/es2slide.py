stringa = input("Dammi una stringa : \n")

def is_palindrome(x):
    contr = 0
    for i,c in enumerate(x):
        if x[i] != x[-i-1]:
            contr += 1
    if contr == 0:
        print("la stringa è palindroma")
        return True
    else:
        print("la stringa non è palindroma")
        return False

is_palindrome(stringa)

#a[-1::-1] potenza di python per le stringhe