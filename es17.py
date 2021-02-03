nazioni = ["Italia", "Francia", "Germania", "Spagna", "Inghilterra", "Grecia", "Turchia", "Portogallo"]
capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Atene", "Ankara", "Lisbona"]
diz = {}
numero = len(nazioni)
for num in range(0, numero):
    diz[nazioni[num]] = capitali[num]
diz2 = dict(zip(diz.values(), diz.keys()))
print("scrivi il nome di una delle seguenti capitali: Roma, Parigi, Berlino, Madrid, Londra, Atene, Ankara, Lisbona per sapere il paese") 
while True:
    scelta = input("scrivi la capitale qui:").capitalize()
    if scelta in diz2.keys():
        print("il paese è", diz2[scelta])
        scelta2 = int(input("premi 0 per sapere un altro paese o 1 abbandonare"))
        if scelta2 == 1:
            break
        elif scelta2 == 0:
            print("inseriscine un'altra")
        else:
            print("questo comando non fa niente, riprova")
            break
    elif scelta not in diz2.keys():
        print("scrivine un'altra che questa non è nell'elenco precedente")
    else:
        pass
