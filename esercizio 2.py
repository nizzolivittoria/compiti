print("lunghezza parole")

N = int(input ("quante parole ci sono?"))
A = []
B = []
n = 1
while True:
    p = input ("inserisci la parola:")
    A.append(p)
    B.append(len(p))
    if N == n:
        print("le lettere sono:", B)
        break
    n = n + 1
